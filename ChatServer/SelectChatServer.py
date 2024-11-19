from ChatServer import ChatServer
import socket
import select
import sys
import struct

class SelectChatServer(ChatServer):
    DEFAULT_BUFFER_SIZE = 2048

    def __init__(self, port: int, backlog, buffsize: int=DEFAULT_BUFFER_SIZE, timeout: float=0.001):
        super().__init__(port, backlog)
        self.clients = []
        self.buffsize = buffsize
        self.timeout = timeout

        # Manufacture reusable socket
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.sock.settimeout(self.timeout)

        except socket.error as e:
            print(f"Error creating socket: {e}")
            sys.exit()

        # Start listening on the socket
        try:
            addr = ("localhost", self.port)
            self.sock.bind(addr)
            self.sock.listen(self.backlog)
            print(f"Listening on port {self.port}")

        except socket.error as e:
            print(e)
            sys.exit()

    def handle_connection(self) -> socket.socket | None:
        ''' Allow select to block while awaiting a connection. Display to
            all clients where the connection was made from.
            Return the client socket.'''
        server_in_list = [self.sock]

        # Display connection to clients
        rlist, _, _ = select.select(server_in_list, [], [], self.timeout)

        for rsock in rlist:
            assert isinstance(rsock, socket.socket)
            
            # The server socket is readable!
            # It must have received a connection from a client.
            if rsock is self.sock:
                client, addr = self.sock.accept()
                print(f"Connection made with {client.getpeername()}")

                # Set the timeout of the client to prevent hanging
                client.settimeout(self.timeout)
                self.clients.append(client)
        
                # Display the information to all the clients
                msg = bytes(self._make_connection_alert(addr), "utf-8")
                self._distribute_message(client, "SERVER", msg)

    def handle_data(self):
        '''Asynchronously receive data from all clients to compose
        their messages.

        Each client will send their name in a struct format which
        must be decoded.

        In the event that a client closes their connection,
        notify every other client of their departure.'''
        rlist, _, _ = select.select(self.clients, [], [], 0.001)

        for rsock in rlist:
            # Receive the message
            
            try:
                data = self._recv_data(rsock, self.buffsize)

            except ConnectionResetError:
                host, port = rsock.getsockname()
                print(f"Lost connection with {host}:{port}")
                msg = bytes(f"{host}:{port} has left the server!", "utf-8")
                self._distribute_message(rsock, "SERVER", msg)

                # Prevent writing to the closed socket
                self.clients.remove(rsock)

            else:
                if len(data) != 0:
                    # Capture the origin of the message
                    og_buffer_size = struct.calcsize("B B B B H")
                    og_buffer = struct.unpack("B B B B H", data[:og_buffer_size])
                    a, b, c, d = og_buffer[0:4]
                    ip, port = f"{a}.{b}.{c}.{d}", og_buffer[4]

                    # Distribute the message to all other clients
                    msg = data[og_buffer_size:]
                    self._distribute_message(rsock, f"{ip}:{port}", msg)

    def _recv_data(self, sock: socket.socket, buffsize: int) -> bytes:
        data = b""

        while True:
            try:
                buffer = sock.recv(buffsize)

            except TimeoutError:
                return data

            else:
                if len(buffer) == 0:
                    return data

                data += buffer

    def data_received(self, data: bytes):
        pass

    def _distribute_message(self, excluded_client: socket.socket, sender: str, data: bytes):
        ''' Upon receiving a message, relay it to all the other 
        clients available. '''
        # Ensure that no client loses any data!
        # Key - value (client - bytes_received)
        msg = bytes(f"<{sender}> ", "utf-8") + data
        self.__send_message(excluded_client, self.clients, msg)

    def __send_message(self, excluded_client: socket.socket, clients: list, msg: bytes):
        ''' Send message to all clients except for the sender.'''
        assert isinstance(excluded_client, socket.socket)
        assert isinstance(clients, list)
        assert isinstance(msg, bytes)
        
        # Lists are mutable. Make a copy.
        _, wlist, _ = select.select([], clients, [])

        for writeable in wlist:
            assert isinstance(writeable, socket.socket)

            if writeable != excluded_client:
                writeable.send(msg)
                host, port = writeable.getpeername()
                print(f"Sent {msg} to {host}:{port}")

    def connection_closed(self):
        pass

    def _make_connection_alert(self, addr: tuple) -> str:
        assert isinstance(addr, tuple)
        return f"Connection made from {addr[0]}"

    def run(self):
        ''' Run the server on the port.'''
        while True:
            self.handle_connection()
            self.handle_data()

            
server = SelectChatServer(10000, 5)
server.run()
