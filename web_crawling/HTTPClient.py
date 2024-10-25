import re
from abc import ABC, abstractmethod
import asyncio
import urllib.parse
import urllib.request
import urllib.error
from http.client import RemoteDisconnected
import socket
import ssl
from PatternExtractor import PatternExtractor
from HTTPResponse import HTTPResponse

class HTTPClient(ABC):
    HTTP_PORT = 80
    HTTPS_PORT = 443
    HTTP_VERSION = 1.1
    HTTPS_VERSION = 2
    COM_GET = "GET"
    COM_POST = "POST"
    COM_PUT = "PUT"
    COM_DELETE = "DELETE"
    DEFAULT_BUFFER_SIZE = 1024
    LINK_CATCHER = r"(\w+)://((?:[a-zA-Z0-9-_]+\.?)+)(.*)" 

    def __init__(self, url):
        self._url = url

        try:
            # Create socket for future communication
            self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            # Capture all important groups of url
            temp_xtr = PatternExtractor()
            temp_xtr.set_pattern(HTTPClient.LINK_CATCHER)
            matches = temp_xtr.get_matches(url)[0] # [0] is accessed bc extractor returns a tuple in a list
            
            # Set scheme, host, path for future query
            self._scheme = matches[0]
            self._host = matches[1]
            self._path_params = matches[2]

            # Decide on port depending on scheme, then connect
            self._port = self._decide_port(self._scheme)
            assert self._port != None
            connecting_addr = (self._host, self._port)

            # Change HTTP version and encrypt communication if necesarry
            if self._port == HTTPClient.HTTPS_PORT:
                self._http_version = HTTPClient.HTTPS_VERSION
                # self._http_version = HTTPClient.HTTP_VERSION
                cont = ssl.create_default_context()
                self._sock = cont.wrap_socket(self._sock, do_handshake_on_connect=True, server_hostname=self._host)

            else:
                self._http_version = HTTPClient.HTTP_VERSION

        except socket.error as e:
            print("Error creating socket: %s" % e)
        
    @abstractmethod
    def fetch(self, **kwargs):
        pass

    def _decide_port(self, scheme):
        ''' Decide on the outgoing port to connect to depending
        on the scheme of the url.'''
        assert isinstance(scheme, str)
        port = None

        if scheme == "http":
            port = HTTPClientUnblocked.HTTP_PORT
            self._scheme = "http"

        elif scheme == "https":
            port = HTTPClientUnblocked.HTTPS_PORT
            self._scheme = "https"

        return port

    def _generate_request(self, command, path, http_vers, **kargs):
        ''' Generate http request for host. Add additional headers
        as needed.'''
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

class HTTPClientBlocked(HTTPClient):
    def fetch(self, **kargs):
        ''' Get the sourcecode of the given url. Returns
        none upon error.'''
        result = None

        try:
            response = urllib.request.urlopen(self._host)
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
            print("Encountered error for %s" % self._host)
            
        return result

class HTTPClientUnblocked(HTTPClient):
    def fetch(self, **kargs):
    # Connect to new host on port if not previously set
        try:
            connecting_addr = (self._host, self._port)
            self._sock.connect((connecting_addr))
        
        except socket.gaierror as e:
            print("Error connecting to host: %s" % e)
            return
    
        # Send request to host
        request_buffer = self._generate_request("GET", self._path_params, self._http_version, **kargs)
        print("Request: [%s]" % request_buffer)
        self._sock.sendall(request_buffer)
        response = self._recv_data()
        return response

    def _recv_data(self):
        ''' Receive data from the host and return as HTTPResponse'''
        data = b""

        while True:
            received = self._sock.recv(self._bufsize)

            if len(received) == 0:
                return HTTPResponse(data)

            data += received

class HTTPClientAsynchronous(HTTPClientUnblocked):
    async def fetch(self, **kwargs):
        try:
            connecting_addr = (self._host, self._port)
            await self._sock.connect((connecting_addr))
        
        except socket.gaierror as e:
            print("Error connecting to host: %s" % e)
            return
        
        # Send request to host
        request_buffer = self._generate_request("GET", self._path_params, self._http_version, **kwargs)
        print("Request: [%s]" % request_buffer)
        await self._sock.sendall(request_buffer)
        response = self._recv_data()
        return response