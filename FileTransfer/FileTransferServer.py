import socket
import time

class FileTransferServer():
    def __init__(self, filepath, backlog=1):
        assert isinstance(filepath, str)
        assert isinstance(backlog, int)
        self.filepath = filepath
        self.backlog = backlog
        self.tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def close(self):
        self.tcp_sock.close()

    def send_file(self):
        def get_file_name(filepath):
            assert isinstance(filepath, str)
            return filepath.split("/")[-1]
        
        def calculate_time(function):
            time_start = time.time()
            function
            time_end = time.time()
            time_total = time_end - time_start
            assert isinstance(time_total, float)
            return time_total

        def send_data(client, data_str):
            ''' Send data_str to client by first sending size of string, then
            the contents of data_str. Returns len(data_str)'''
            assert isinstance(data_str, str)
            assert client != None
            data_len = len(data_str)
             
            def fx(*args):
                for arg in args:
                    arg

            time_total = calculate_time(fx(client.sendall(bytes(str(data_len), "utf-8")),
                              client.sendall(bytes(data_str, "utf-8"))))

            print("Sent client %d bytes in %f seconds." % 
                    (data_len, time_total))

            return data_len

        self.tcp_sock.bind(("localhost", 50500))
        server_port = self.tcp_sock.getsockname()[1]
        print("FT Server listening on port %d" % server_port)

        # Continue listening for connection, then send file data
        try:
            file = open(self.filepath, "r")
            self.tcp_sock.listen(self.backlog)

            # Wait for client connection
            client, address = self.tcp_sock.accept()
            print("Connected by %s:%s" % (address[0], address[1]))
            
            # Send name of file to client
            print("Sending name of file to cilent...")
            filename = get_file_name(file.name)
            send_data(client, filename)
            
            # Send data to client
            print("Sending file data to client...")
            data = file.read()
            send_data(client, data)

            return True

        except FileNotFoundError as e:
            print("Could not open file: %s" % e)
            return False
