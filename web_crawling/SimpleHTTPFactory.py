from twisted.internet.protocol import ClientFactory
from SimpleHTTP import SimpleHTTP
from twisted.internet import defer

class SimpleHTTPFactory(ClientFactory):
    def __init__(self, deferred: defer.Deferred, url: str, scheme: str, 
                 host: str, path: str):
        self.scheme = scheme
        self.url = url
        self.host = host
        self.path = path
        
        # Allow callbacks and errbacks
        self.deferred = deferred

    def buildProtocol(self, addr):
        return SimpleHTTP(self, self.url, self.scheme, self.host, self.path, True)
        
    def http_finished(self, url: str, http_response: bytes):
        assert isinstance(http_response, bytes)
        assert isinstance(url, str)
        
        if self.deferred:
            d, self.deferred = self. deferred, None
            d.callback((url, http_response))

    def http_failed(self, reason):
        if self.deferred:
            d, self.deferred = self.deferred, None
            d.errback(reason)

