from twisted.internet.protocol import Protocol, ClientFactory

class SimpleHTTP(Protocol):
    HTTP_VERSION = 1.1
    HTTPS_VERSION = 1.1

    def __init__(self, factory, url, scheme, host, path, debug):
        assert isinstance(factory, ClientFactory)
        assert isinstance(url, str)
        assert isinstance(host, str)
        assert isinstance(path, str)
        assert isinstance(debug, bool)
        self.factory = factory
        self.url = url
        self.scheme = scheme
        self.host = host
        self.path = path
        self.debug = debug

        # Get the http version
        self.http_version = None

        if scheme == "http":
            self.http_version = SimpleHTTP.HTTP_VERSION

        elif scheme == "https":
            self.http_version = SimpleHTTP.HTTPS_VERSION

        assert self.http_version != None, "HTTP version not set!"

        # Initialize message for further concatenation
        self.http_response = b""

    def dataReceived(self, data: bytes):
        assert len(data) != None
        self.http_response += data

        if self.debug:
            peer = self.transport.getPeer()
            host, port = peer.host, peer.port
            print(f"Received {len(data)} bytes from {host}:{port}")

    def connectionMade(self):
        ''' Upon connection, send the appropriate GET request
            according to the url given.'''
        main_request = bytes(self._construct_request("GET",
                                                     self.path,
                                                     self.http_version,
                                                     Connection="Close",
                                                     Host=self.host), "utf-8")
        if self.debug:
            peer = self.transport.getPeer()
            host, port = peer.host, peer.port
            print(f"Sending request {main_request} to {host}:{port}")

        self.transport.write(main_request)
        
    def connectionLost(self, reason):
        if self.debug:
            peer = self.transport.getPeer()
            host, port = peer.host, peer.port
            print(f"------------------> Completed response from {host}:{port}")

        self.factory.http_finished(self.url, self.http_response)

    def _construct_request(self, command, path, http_version, **kargs):
        ''' Return string request header.'''
        assert isinstance(command, str)
        assert isinstance(path, str)
        assert isinstance(http_version, int) or isinstance(http_version, float)

        # Make the main request header
        request = ""
        main_header = f"{command} {path} HTTP/{http_version}\r\n"
        request += main_header

        if kargs:
            for karg in kargs:
                assert isinstance(karg, str)
                key = karg
                value = kargs[key]
                header_str = f"{key}: {value}\r\n"

                # Add the header str to the request
                request += header_str

        # Signal the end of the message
        request += "\r\n"
        return request

