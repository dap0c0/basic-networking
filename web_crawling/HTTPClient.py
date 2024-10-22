import re
import urllib.parse
import urllib.request
import urllib.error
from http.client import RemoteDisconnected
import http.client
import socket
import ssl
from PatternExtractor import PatternExtractor

# TODO:
# - need to connect to 443 depending on if HTTPS is in url (done)
# - need to organize code
#   - delegate scheme and domain name scanning to pattern extractor (done)
#   - ask urself what are the necessary private vars (url? curr_host?) (done)
# - finish grep extraction for paths
# - finish grep extraction for get queries

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
    HTTPS_PORT = 443
    HTTP_VERSION = 1.1
    HTTPS_VERSION = 2
    COM_GET = "GET"
    COM_POST = "POST"
    COM_PUT = "PUT"
    COM_DELETE = "DELETE"
    DEFAULT_BUFFER_SIZE = 1024
    LINK_CATCHER = r"(\w+)://((?:[a-zA-Z0-9-_]+\.?)+)(.*)" 
    HTML_DELIMITER = "<!DOCTYPE html>"

    def __init__(self):
        try:
            self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # self._sock.setblocking(0)
            self.url = None
            self._host = None
            self._port = None
            self._scheme = None
            self._path_params = None
            self._http_version = None
            self._bufsize = HTTPClientUnblocked.DEFAULT_BUFFER_SIZE
            self._extractor = PatternExtractor()
        
        except socket.gaierror as e:
            print("Error creating socket: %s" % e)

    def _decode(self, response_bytes):
        assert isinstance(response_bytes, bytes)


    def fetch(self, url, **kargs):
        assert isinstance(url, str)
        
        # Connect to new host on port if not previously set
        if url != self.url:
            # Capture all important groups of url
            self._extractor.set_pattern(HTTPClientUnblocked.LINK_CATCHER)
            matches = self._extractor.get_matches(url)[0] # [0] is accessed bc extractor returns a tuple in a list
            self._scheme = matches[0]
            self._host = matches[1]
            self._path_params = matches[2]
            
            # Decide on port depending on scheme, then connect
            self._port = self._decide_port(self._scheme)
            assert self._port != None
            connecting_addr = (self._host, self._port)

            # Change HTTP version and encrypt communication if necesarry
            if self._port == HTTPClientUnblocked.HTTPS_PORT:
                # self._http_version = HTTPClientUnblocked.HTTPS_VERSION
                self._http_version = HTTPClientUnblocked.HTTP_VERSION
                cont = ssl.create_default_context()
                self._sock = cont.wrap_socket(self._sock, do_handshake_on_connect=True, server_hostname=self._host)
            
            else:
                self._http_version = HTTPClientUnblocked.HTTP_VERSION

            try:
                self._sock.connect((connecting_addr))
            
            except socket.gaierror as e:
                print("Error connecting to host: %s" % e)
                return
            
        # Check if url contains path, parameters, or anchors
        url_extras = "/"
        len_bf_path = len(self._scheme) + len("://") + len(self._host)

        if len(url) != len_bf_path:
            url_extras = url[len_bf_path:len(url)]
            self._path = url_extras

        # Send request to host
        request_buffer = self._generate_request("GET", url_extras, self._http_version, **kargs)
        print("Request: [%s]" % request_buffer)
        self._sock.sendall(request_buffer)
        data = self._recv_data()
        return data
    
    def _get_html(self, response):
        ''' Return the html content of the response.'''
        assert isinstance(response, bytes)
        html = None
    
        try:
            response_str = str(response, "utf-8")
            data_split = response_str.split(HTTPClientUnblocked.HTML_DELIMITER)
            assert len(data_split) == 2
            html = data_split[1]
        
        except UnicodeDecodeError as e:
            print("Error decoding data: %s" % e)
        
        except AssertionError as e:
            print("HTML not included in response: %s" % e)
        
        return html
    
    def _get_headers(self, response):
        ''' Return the header content (with error code) of the response.'''
        assert isinstance(response, bytes)
        headers = None
        status_code = self._get_status_code(response)

        try:
            response_str = str(response, "utf")
            data_split = response_str.split(HTTPClientUnblocked.HTML_DELIMITER)
            assert len(data_split) == 2
            headers = data_split[0]

        except UnicodeDecodeError as e:
            print("Error decoding data: %s" % e)
        
        return headers

    def _get_status_code(self, response):
        ''' Return the status code of the response.'''
        assert isinstance(response, str)
        first_car_ret = response.find("\r\n")
        stat_msg = response[0:first_car_ret]
        stat_code = int(stat_msg.split(" ")[1]) # HTTP/$version $status $message
        return stat_code

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

    def _recv_data(self):
        ''' Receive data from the host'''
        data = b""

        while True:
            received = self._sock.recv(self._bufsize)

            if len(received) == 0:
                return data

            data += received