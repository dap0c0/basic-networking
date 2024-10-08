import socket
import sys

class FileTransferClient():
    def __init__(self, host, port):
        print(host)
        assert isinstance(host, str)
        assert isinstance(port, int)
        self.host = host
        self.port = port
        self.tcp_socket = None
        self.connected = self.__connect()
    
    def __connect(self):
        try:
            self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        except socket.error as e:
            print("Error creating socket: %s" % e)
            sys.exit(1)

        try:
            print(self.tcp_socket.connect((self.host, self.port)))
            
        except socket.gaierror as e:
            print("Could not resolve address: %s" % e)
            sys.exit(1)
        
        print("Client connected to %s:%s." % (self.host, self.port))
        return True

    def receive_data(self, bufsize=1024):
        ''' Return data in format (body, name).'''
        assert self.connected

        def recv_buffer_len(sock, bufsize):
            '''Convert buffer into integer as anticipated.'''
            assert isinstance(sock, socket.socket)
            assert isinstance(bufsize, int)
            assert bufsize > 0

            buffer = self.tcp_socket.recv(bufsize)
            return int(str(buffer, "utf-8"))

        def recv_all(sock, expected_len):
            ''' Rebuild all packets into one message, then return the str format.'''
            assert isinstance(expected_len, int)
            assert isinstance(sock, socket.socket)
            total_buffer = b""  

            while len(total_buffer) < expected_len:
                total_buffer += sock.recv(bufsize)
            
            if len(total_buffer) != expected_len:
                raise EOFError("Data was not succesfully sent.")
            
            return str(total_buffer)
        
        # Data is received as follows: name, file contents
        data_len = recv_buffer_len(self.tcp_socket, bufsize)
        name = recv_all(self.tcp_socket, data_len)
        data_len = recv_buffer_len(self.tcp_socket, bufsize)
        contents = recv_all(self.tcp_socket, data_len)
        assert name != None
        assert contents != None
        return (name, contents)

    def write_data(self, filename, body):
        assert isinstance(filename, str)
        assert isinstance(body, str)

        try:
            with open(filename, "w") as file:
                file.write(body)

            return True

        except FileNotFoundError as e:
            print("The file %s does not exist: %s" % (filename, e))
            return False
