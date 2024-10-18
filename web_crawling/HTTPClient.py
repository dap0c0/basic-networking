import urllib.request
import urllib.error
from http.client import RemoteDisconnected
import socket

class HTTPClient():
    def fetch(self, host):
        ''' Get the sourcecode of the given url. Returns
        none upon error.'''
        result = None

        try:
            response = urllib.request.urlopen(host)
            data = response.read()
            text = data.decode("utf-8")
            result = text

        except UnicodeDecodeError as e:
            print("Could not decode data: %s" % e)
        
        except urllib.error.HTTPError as e:
            print(e)

        except urllib.error.URLError as e:
            print(e)

        except RemoteDisconnected as e:
            print("Encountered error for %s" % host)
            
        return result

class HTTPClientUnblocked(HTTPClient):
    HTTP_PORT = 80
    COM_GET = "GET"
    COM_POST = "POST"
    COM_PUT = "PUT"
    COM_DELETE = "DELETE"
    DEFAULT_BUFFER_SIZE = 1024

    def __init__(self):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # self._sock.setblocking(0)
        self._curr_host = None
        self._bufsize = HTTPClientUnblocked.DEFAULT_BUFFER_SIZE

    def fetch(self, host, **kargs):
        assert isinstance(host, str)
        
        # Connect to new host if not previously set
        if host != self._curr_host:
            self._curr_host = host
            connecting_addr = (self._curr_host, HTTPClientUnblocked.HTTP_PORT)

            try:
                self._sock.connect((connecting_addr))
            
            except socket.gaierror as e:
                print("Error connecting to host: %s" % e)
                return
            
        # Send request to host
        request_buffer = self._generate_request("GET", "/", 1.1, **kargs)
        print(request_buffer)
        self._sock.sendall(request_buffer)
        data = self._recv_data()
        return data

    def _generate_request(self, command, path, http_vers, **kargs):
        assert isinstance(command, str)
        assert command in (self.COM_DELETE, self.COM_GET, self.COM_POST, self.COM_PUT)
        assert isinstance(path, str)
        assert isinstance(http_vers, float) or isinstance(http_vers, int)
        
        # Generate message in byte format
        message = ""
        request_header = "%s %s HTTP/%s\r\n" % (command, path, http_vers)
        message += request_header

        # Add additional headers as needed
        if kargs:
            for karg in kargs:
                header = karg
                assert isinstance(header, str)
                value = kargs[karg]
                assert isinstance(value, str)
                header_str = "%s: %s\r\n" % (header, value)
                message += header_str

        # Assure that double carriage feed is set to mark end of message
        message += "\r\n"
        return bytes(message, "utf-8")

    def _recv_data(self):
        ''' Receive data from the host'''
        data = b""

        while True:
            received = self._sock.recv(self._bufsize)
            print("Len [%d]" % len(received))
            print(received)

            if len(received) == 0:
                return data

            data += received

# client = HTTPClientUnblocked()
# data = client.fetch("youtube.com", Connection="Close")
# print(data)


        