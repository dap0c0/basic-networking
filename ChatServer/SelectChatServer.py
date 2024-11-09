from ChatServer import ChatServer
import socket
import select
import sys

class SelectChatServer(ChatServer):
    DEFAULT_BUFFER_SIZE = 2048

    def __init__(self, port: int, backlog, buffsize: int):
        super().__init__(port, backlog)
        self.clients = []
        self.buffsize = buffsize

        # Manufacture reusable socket
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

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
        rlist, wlist, _ = select.select(server_in_list, self.clients, [])
        client = None

        for rsock in rlist:
            assert isinstance(rsock, socket.socket)
            
            # The server socket is readable!
            # It must have received a connection from a client.
            if rsock is self.sock:
                client, addr = self.sock.accept()
                print(f"Connection made with {client.getpeername()}")
                self.clients.append(client)
        
            # Display the information to all the clients
            if len(wlist) > 0:
                for client in wlist:
                    assert isinstance(client, socket.socket)
                    msg = bytes(self._make_connection_alert(addr), "utf-8")
                    client.sendall(msg)
                    print(f"Sent {len(msg)} bytes to {client.getpeername()}")

        return client

    def handle_data(self):
        '''Asynchronously receive data from all clients to compose
        their messages.'''
        message_map = {client, b"" for client in self.clients}
        rlist, _, _ = select.select([self.socket], [], [])
        
    def _recv_data(self, sock: socket.socket, buffsize: int) -> bytes:
        data = b""

        while True:
            buffer = sock.recv(buffsize)

            if len(buffer) == 0:
                return data

            else:
                data += buffer

    def data_received(self, data: bytes):
        pass

    def _distribute_message(self, sender: str, data: bytes):
        ''' Upon receiving a message, relay it to all the other 
        clients available. '''
        # Ensure that no client loses any data!
        # Key - value (client - bytes_received)
        msg = bytes(f"<{sender}> ", "utf-8") + data
        self._send_message(self.clients, msg, self.buffsize)

    def _send_message(self, clients: list, data: bytes, buffsize: int):
        ''' Distribute the message asynchronously, ensuring that no
        client loses data.'''
        bytes_expected = len(data)
        
        # Send message to all clients
        _, wlist, _ = select.select([], clients, [])
        client_map = {client: 0 for client in wlist}

        while client_map:
            for client in client_map:
                buffstart = client_map[client]
                buffer = data[buffstart:buffstart + buffsize]
                assert len(buffer) == buffsize
                client.send(buffer)

                # Check if all data was sent successfully
                client_map[client] += len(buffer)

                if client_map[client] == len(data):
                    client_map.pop(client)

    def connection_closed(self):
        pass

    def _make_connection_alert(self, addr: tuple) -> str:
        assert isinstance(addr, tuple)
        return f"Connection made from {addr[0]}\n"

    def run(self):
        ''' Run the server on the port.'''
        while True:
            client = self.handle_connection()

server = SelectChatServer(10000, 5)
server.run()
