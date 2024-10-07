import socket
import time

class FileTransferer():
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
            filename = get_file_name(file.name)
            print("Sending name of file to cilent...")
            buffer = bytes(filename, "utf-8")
            time_total = calculate_time(client.send(buffer))
            print("Sent %s:%s %d bytes in %f seconds." % 
                    (address[0], address[1], len(buffer), time_total))
            
            # Send data to client
            print("Sending file data to client...")
            data = file.read()
            buffer = bytes(data, "utf-8")     
            time_total = calculate_time(client.send(buffer))
            print("Sent %s:%s %d bytes in %f seconds." % 
                    (address[0], address[1], len(buffer), time_total))
            
            return True

        except FileNotFoundError as e:
            print("Could not open file: %s" % e)
            return False
