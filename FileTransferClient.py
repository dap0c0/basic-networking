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
        
        def receive_name():
            ''' Receive name from connected socket.'''
            buffer = self.tcp_socket.recv(bufsize)
            return str(buffer, "utf-8")

        def receive_body():
            ''' Receive data from connected socket.'''
            buffer = self.tcp_socket.recv(bufsize)
            return str(buffer, "utf-8")
        
        (name, body) = (receive_name(),
                        receive_body())
        return (name, body)

# TODO
# Need to create a function that calls all functions in order with keyword arguments
        
        