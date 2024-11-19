import socket
import struct
import sys
import argparse
import select

class ChatClient():
    DEFAULT_BUFFSIZE = 1048

    def __init__(self, port: int, host: str, buffsize: int=1048, timeout: float=0.0001, name: str="anon"):
        assert isinstance(name, str)
        assert isinstance(port, int)
        assert isinstance(host, str)
        assert isinstance(buffsize, int)
        assert 0 <= port
        assert 0 < buffsize

        self.name = name
        self.port = port
        self.host = host
        self.timeout = timeout
        self.buffsize = buffsize

        # Manufacture socket for future connection
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.settimeout(self.timeout)

        except socket.error as e:
            print(f"Error creating socket: {e}")
            
    def _connect(self):
        ''' Connect the client to the predesignated host.'''
        addr = (self.host, self.port)

        try:
            self.sock.connect(addr)

        except socket.gaierror as e:
            print(f"Error connecting to {self.host}.")

        else:
            # Send this client's name upon connection
            #            buffer = struct.pack(f"{len(self.name)}s", self.name.encode())
        # self.sock.send(buffer)
            # It might be useful to do a TCP based protocol (hello, syn, etc).
            pass

    def _send_message(self, message: str):
        ''' Send the message to the socket through an established
        "protocol".

        1) Send the origin of the message (IP:PORT)
        2) Send the message.'''
        assert isinstance(message, str)
        og_ip, og_port = self.sock.getsockname()
        
        # Parse the IPv4 address into a set of 4
        assert isinstance(og_ip, str)
        int_seq = [int(i) for i in og_ip.split(".")]

        # Notify the server about the origin of the message.
        # Format is in HHHH-H (ip address, port)
        origin_struct = struct.pack("B B B B H",
                                    int_seq[0],
                                    int_seq[1],
                                    int_seq[2],
                                    int_seq[3],
                                    og_port)
        self.sock.send(origin_struct + bytes(message, "utf-8"))
        
    def _connection_lost(self, addr: tuple):
        ''' Gracefully handle lost connection from server.'''
        pass

    def _recv_data(self, sock: socket.socket) -> bytes:
        ''' Receive a message from the server.'''
        assert isinstance(sock, socket.socket)
        data = b""

        while True:
            try:
                buffer = sock.recv(self.buffsize)

            except TimeoutError:
                return data

            else:
                if len(buffer) == 0:
                    return data

                data += buffer

    def _display_shell_symbol(self, symbol: str):
        assert isinstance(symbol, str)
        sys.stdout.write(symbol)
        sys.stdout.flush()

    def _exit_client(self, msg: str):
        assert isinstance(msg, str)
        sys.stderr.write(msg)
        self.sock.close()
        sys.exit()

    def run(self):
        ''' Connect to the client and run until program exits.

            Allow the client to send data and receive it asynchronously.'''
        try:
            self._connect()
            self._display_shell_symbol("$ ")
            
            while True:
                try:
                    rlist, _, _ = select.select([sys.stdin, self.sock], [], [])
                    
                    for readable in rlist:
                        if readable is sys.stdin:
                            user_input = sys.stdin.readline().strip()
                            self._send_message(user_input)
                            self._display_shell_symbol("$ ")

                        if readable is self.sock:
                            try:
                                data = self._recv_data(readable)

                            except ConnectionResetError:
                                self. _exit_client("\rServer has closed.\nExitting client.\n")

                            if len(data) != 0:
                                sys.stdout.write("\r" + str(data, "utf-8") + "\n")
                                sys.stdout.flush()
                                self._display_shell_symbol("$ ")

                except KeyboardInterrupt:
                    self. _exit_client("\rExitting client.\n")

        except socket.gaierror as e:
            print(e)
            sys.exit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Chat Client")
    parser.add_argument("--host", type=str, action="store",
                        required=True, dest="host")
    parser.add_argument("--port", type=int, action="store",
                        required=True, dest="port")
    parser.add_argument("--buffsize", "-s", action="store", dest="buffsize")
    args = parser.parse_args()
    host = args.host
    port = args.port
    buffsize = args.buffsize

    if buffsize:
        client = ChatClient(port, host, buffsize)

    else:
        client = ChatClient(port, host)

    client.run()
