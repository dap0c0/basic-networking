from cProfile import Profile
from pstats import SortKey, Stats

from abc import ABC, abstractmethod
from FileOrganizer import FileOrganizer
from PatternExtractor import PatternExtractor
from Queue import LLQueue

from twisted.internet.defer import Deferred
from twisted.internet import ssl
from SimpleHTTPFactory import SimpleHTTPFactory
from SimpleHTTP import SimpleHTTP

import urllib.parse

class WebCrawler(ABC):
    # Basic hyperlink pattern: scheme://domain.tld/example/path
    HYPERLINK_REGEX_PATTERN = r"(?:\w+://)(?:[a-zA-Z0-9-_]+\.)+(?:[a-z]*)(?:/[a-zA-Z0-9-_]+)*/?"

    def __init__(self, seed, results_file, sleep=0):
        assert isinstance(seed, str)
        assert (isinstance(sleep, int) or isinstance(sleep, float))
        assert isinstance(results_file, str)
        assert sleep >= 0
        self.seed = seed
        self.sleep = sleep
        self.http_responses = {} # Each url will contain info regarding external links, emails, files

        # Class drivers
        self._results_file = results_file
        self._file_interface = FileOrganizer(self._results_file)
        self._extractor = PatternExtractor()
        self._url_queue= LLQueue()
        self._explored_links = []
        self._info_initializer = {
            "links": {},
            "emails": {},
            "files": {}
        }

    @abstractmethod
    def crawl(self):
        pass

    def _extract_links(self, input):
        ''' Return the hyperlinks present within the input string.'''
        assert input != None
        assert isinstance(input, str)
        self._extractor.set_pattern(WebCrawler.HYPERLINK_REGEX_PATTERN)
        return self._extractor.get_matches(input)
    
    def _extract_emails(self, input):
        pass

    def _write_to_file(self, current_link, links_found):
        pass

class TwistedWebCrawler(WebCrawler):
    HTTP_PORT = 40
    HTTPS_PORT = 443

    def __init__(self, seed: str, results_file: str, sleep=0):
        assert isinstance(seed, str)
        assert isinstance(results_file, str)
        assert isinstance(sleep, int) or isinstance(sleep, float)
        super().__init__(seed, results_file, sleep)
        
        self._http_responses = {}
        self._errors = {}

    def _promise_http(self, url: str):
        ''' Promise an http request and return the deferred result. '''
        d = Deferred()
        
        # Get the relevant url info
        parsed = urllib.parse.urlparse(url)
        scheme = parsed.scheme
        host = parsed.netloc
        path = parsed.path

        if len(path) == 0:
            path = "/"
        
        # Allow factory to bridge between our code and the reactor loop
        factory = SimpleHTTPFactory(d, scheme, host, path)
        from twisted.internet import reactor

        # Initiate a request on the relevant port
        if scheme == "http":
            reactor.connectTCP(host, TwistedWebCrawler.HTTP_PORT, factory)

        elif scheme == "https":
            reactor.connectSSL(host, TwistedWebCrawler.HTTPS_PORT, factory, ssl.ClientContextFactory())

        return d

    def crawl(self):
        ''' Begin asynchronous crawl with the initial seed.'''
        # While queue is nonempty and no keyboard interrupt, proceed
        assert self.seed != None

        # Define auxiliary methods for event driven processing
        # Callback 1
        def http_success(url: str, http_response: bytes):
            ''' Propogate the http_response down the chain
            to allow for further processing. '''
            assert isinstance(url, str)
            assert isinstance(http_response, bytes)
            # self._http_responses[url] = http_response # May possibly lead to a memory leak
            return http_response
        
        # Callback 2
        def add_links(http_response: bytes):
            assert isinstance(http_response, bytes)
            links = self._extract_links(http_response)
            print(f"{len(links)} links found!")

            for link in links:
                self._url_queue.enqueue(link)
            
        # Errback
        def http_fail(url: str, err):
            assert isinstance(url, str)
            self._errors[url] = err

        # Stopping condition
        def http_done(_):
            ''' Stop processing when there are no more links to process.'''
            if self._url_queue.is_empty():
                from twisted.internet import reactor
                reactor.stop()

        # Kickoff processing with the seed url
        self._url_queue.enqueue(self.seed)

        # while not self._url_queue.is_empty():
        while True:
            curr_url = self._url_queue.dequeue()
            assert curr_url != None
            assert isinstance(curr_url, str)

            # Request from seed for http
            d = self._promise_http(curr_url)
            d.addCallbacks(http_success, http_fail)
            d.addCallback(add_links)
            d.addBoth(http_done)
