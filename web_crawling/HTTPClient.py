import re
import urllib.request
import urllib.error
from http.client import RemoteDisconnected
import socket
import ssl
from PatternExtractor import PatternExtractor

# TODO:
# - need to connect to 443 depending on if HTTPS is in url (done)
# - need to organize code
#   - delegate scheme and domain name scanning to pattern extractor
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
    HTTPS_VERSION = 2.0
    COM_GET = "GET"
    COM_POST = "POST"
    COM_PUT = "PUT"
    COM_DELETE = "DELETE"
    DEFAULT_BUFFER_SIZE = 1024
    HYPERLINK_REGEX_PATTERN = r"(\w+://)([a-zA-Z0-9-_]+\.)+([a-z]*)(/[a-zA-Z0-9-_]+)*/?"
    DOMAIN_NAME_CATCHER = r"\w+://((?:[a-zA-Z0-9-_]+\.?)+)"
    SCHEME_CATCHER = r"(\w+)://"

    def __init__(self):
        try:
            self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # self._sock.setblocking(0)
            self.url = None
            self._host = None
            self._port = None
            self._scheme = None
            self._path = None
            self._http_version = None
            self._bufsize = HTTPClientUnblocked.DEFAULT_BUFFER_SIZE
            self._extractor = PatternExtractor()
        
        except socket.gaierror as e:
            print("Error creating socket: %s" % e)

    def fetch(self, url, **kargs):
        assert isinstance(url, str)
        
        # Connect to new host on port if not previously set
        if url != self.url:
            # Get domain name
            self._extractor.set_pattern(HTTPClientUnblocked.DOMAIN_NAME_CATCHER)
            self._host = self._extractor.get_matches(url)[0]
            self._port = self._decide_port(url)
            assert self._port != None
            connecting_addr = (self._host, self._port)

            # Change HTTP version and encrypt communication if necesarry
            if self._port == HTTPClientUnblocked.HTTPS_PORT:
                self._http_version = HTTPClientUnblocked.HTTPS_VERSION
                cont = ssl.create_default_context()
                print(self._host.__class__)
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

        print(url_extras)
        
        # Send request to host
        request_buffer = self._generate_request("GET", url_extras, self._http_version, **kargs)
        print("Request: [%s]" % request_buffer)
        self._sock.sendall(request_buffer)
        data = self._recv_data()
        return data

    def _decide_port(self, url):
        ''' Decide on the outgoing port to connect to depending
        on the scheme of the url.'''
        assert isinstance(url, str)
        self._extractor.set_pattern(HTTPClientUnblocked.SCHEME_CATCHER)
        scheme = self._extractor.get_matches(url)[0]
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
    
    # def get_scheme(self, url):
    #     assert isinstance(url, str)
    #     scheme = None
    #     matches = re.findall(HTTPClientUnblocked.SCHEME_CATCHER, url)
        
    #     if matches:
    #         scheme = matches[0] # url scheme is the first and only capturing group)
        
    #     return scheme
    
    # def get_domain_name(self, url):
    #     assert isinstance(url, str)
    #     link = None
    #     matches = re.findall(HTTPClientUnblocked.DOMAIN_NAME_CATCHER, url)

    #     if matches:
    #         link = matches[0]
    #         assert isinstance(link, str)
        
    #     return link
    
    # def get_path(self, url):
    #     assert isinstance(url, str)
    #     path = None
    #     matches = re.findall(HTTPClientUnblocked.PATH_CATCHER, url)
    #     print(matches)

    #     if matches:
    #         link = matches[0]
    #         assert isinstance(link, str)
        
    #     return link


# client = HTTPClientUnblocked()
# data = client.fetch("youtube.com", Connection="Close")
# print(data)

# client = HTTPClientUnblocked()
# scheme = client.get_scheme("bruh://youtube.com")
# domain_name = client.get_domain_name("https://natas.labs.overthewire.org/bruh")
# print(scheme)
# print(domain_name)
def print_stats(client, url):
    print("URL: %s\nScheme: %s\nDomain-Name: %s\nPath: %s" % (client.url, client._scheme, client._host, client._path))

def test_vim():
    client = HTTPClientUnblocked()
    url = "https://www.vim.org/"
    data = client.fetch(url, Connection="close", Host="www.vim.org")
    print(str(data, "utf-8"))

def test_pressbooks():
    client = HTTPClientUnblocked()
    url = "https://www.musictheory.net/exercises"
    data = client.fetch(url, Connection="close")
    print_stats(client, url)
    print(data)

test_pressbooks()