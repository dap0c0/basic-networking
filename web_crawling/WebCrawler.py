from cProfile import Profile
from pstats import SortKey, Stats

# TODO:
# rerun the file
from abc import ABC, abstractmethod
from FileOrganizer import FileOrganizer
from PatternExtractor import PatternExtractor
from Queue import LLQueue, Queue

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
        factory = SimpleHTTPFactory(d, url, scheme, host, path)
        from twisted.internet import reactor

        # Initiate a request on the relevant port
        if scheme == "http":
            reactor.connectTCP(host, TwistedWebCrawler.HTTP_PORT, factory)

        elif scheme == "https":
            reactor.connectSSL(host, TwistedWebCrawler.HTTPS_PORT, factory, ssl.ClientContextFactory())

        return d

    def crawl(self, debug: bool):
        assert isinstance(debug, bool)
        ''' Begin asynchronous crawl from the designated seed.'''

        def crawl_driver(debug: bool):
            # While queue is nonempty and no keyboard interrupt, proceed
            assert self.seed != None

            # Define auxiliary methods for event driven processing
            # Callback 1
            def http_success(url_http_pair: tuple):
                ''' Propogate the http_response down the chain
                to allow for further processing. '''
                url, http_response = url_http_pair
                assert isinstance(http_response, bytes)
                # self._http_responses[url] = http_response # May possibly lead to a memory leak
                return url_http_pair

            # Callback 2
            def add_links(url_http_pair: tuple):
                url, http_response = url_http_pair
                assert isinstance(http_response, bytes)
                links = self._extract_links(str(http_response))
                for link in links:
                    self._url_queue.enqueue(link)

                print(f"Enqueued {len(links)} links")
                

                if http_response:
                    return True #
                
            # Errback
            def http_fail(url: str, err):
                assert isinstance(url, str)
                self._errors[url] = err
                
                if debug:
                    print("http failed!!!")

            # Temp method
            def react(mutable: list):
                d = self._promise_http(mutable[0])
                d.addCallbacks(http_success, http_fail)
                d.addCallback(add_links)
                d.addBoth(http_done)
                url = self._url_queue.dequeue()
                mutable[0] = url

            # Stopping condition
            def http_done(http_returned: bool):
                ''' Stop processing when there are no more links to process.'''
                if not http_returned:
                    from twisted.internet import reactor
                    reactor.stop()

                else:
                    # Prompt reactor to promise another http response
                    from twisted.internet import reactor
                    curr_url = self._url_queue.dequeue()
                    curr_url_storage = [curr_url]
                    reactor.callWhenRunning(react, curr_url_storage)

            # Kickoff processing with the seed url
            print(f"Seed is {self.seed}")
            self._url_queue.enqueue(self.seed)

            # while not self._url_queue.is_empty():
            curr_url = self._url_queue.dequeue()
            curr_url_storage = [curr_url]

            from twisted.internet import reactor
            reactor.callWhenRunning(react, curr_url_storage)

        from twisted.internet import reactor
        reactor.callWhenRunning(crawl_driver, debug)
        reactor.run()
