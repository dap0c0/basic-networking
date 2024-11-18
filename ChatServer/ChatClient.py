import socket
import struct
import sys
import argparse

class ChatClient():
    DEFAULT_BUFFSIZE = 1048

    def __init__(self, port: int, host: str, buffsize: int=1048, name: str="anon"):
        assert isinstance(name, str)
        assert isinstance(port, int)
        assert isinstance(host, str)
        assert isinstance(buffsize, int)
        assert 0 <= port
        assert 0 < buffsize

        self.name = name
        self.port = port
        self.host = host
        self.buffsize = buffsize

        # Manufacture socket for future connection
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        except socket.error as e:
            print(f"Error creating socket: {e}")
            
    def _connect(self):
        ''' Connect the client to the predesignated host.'''
        addr = (self.host, self.port)

        try:
            self.sock.connect(addr)
            print(f"Peer is {self.sock.getpeername()}")

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
        origin_struct = struct.pack("HHHHH",
                                    int_seq[0],
                                    int_seq[1],
                                    int_seq[2],
                                    int_seq[3],
                                    og_port)
        self.sock.send(origin_struct)

        # Now, send the message
        self.sock.send(bytes(message, "utf-8"))
        print(f"Message sent to {self.sock.getpeername()}.")
        
    def _connection_lost(self, addr: tuple):
        ''' Gracefully handle lost connection from server.'''
        pass

    def _recv_data(self, sock: socket.socket) -> bytes:
        ''' Receive a message from the server.'''
        assert isinstance(sock, socket.socket)
        data = b""

        while True:
            buffer = sock.recvfrom(self.buffsize)

            if len(buffer) == 0:
                return data

            else:
                data += buffer

    def run(self):
        ''' Connect to the client and run until program exits.'''
        try:
            self._connect()
            
            while True:
                try:
                    # Allow the user to type
                    user_input = input("$ ")
                    self._send_message(user_input)

                    # Display the data on the screen
                    # data = self._recv_data(self.sock)
                    # print(str(data, "utf-8") + "\n")
                    

                except KeyboardInterrupt as e:
                    print("Exitting....")
                    sys.exit()

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
