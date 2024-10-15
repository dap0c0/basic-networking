from abc import ABC, abstractmethod
from HTTPClient import HTTPClient
from FileOrganizer import FileOrganizer
from PatternExtractor import PatternExtractor
from Queue import LLQueue

class WebCrawler(ABC):
    # Basic hyperlink pattern: scheme://domain.tld/example/path
    # HYPERLINK_REGEX_PATTERN = re.compile(r"(?:\w+://)(?:[\w\d]+\.)+(?:[a-z]*)(?:/\w+)*/?")
    # HYPERLINK_REGEX_PATTERN = re.compile(r"(?:\w+://)(?:[^\s<>().&*^%$#+=]+\.)+(?:[a-z]*)(?:/\w+)*/?")
    HYPERLINK_REGEX_PATTERN = r"(?:\w+://)(?:[a-zA-Z0-9-_]+\.)+(?:[a-z]*)(?:/[a-zA-Z0-9-_]+)*/?"

    def __init__(self, seed, sleep, results_file):
        assert isinstance(seed, str)
        assert (isinstance(sleep, int) or isinstance(sleep, float))
        assert isinstance(results_file, str)
        assert sleep >= 0
        self.seed = seed
        self.sleep = sleep
        self.data = {} # Each url will contain info regarding external links, emails, files

        # Class drivers
        self._results_file = results_file
        self._file_interface = FileOrganizer(self.results_file)
        self._extractor = PatternExtractor()
        self._client = HTTPClient() # Host is set per query

    @abstractmethod
    def crawl(self):
        pass

    def _get_page_source(self, url):
        ''' Get page sourcecode of url.'''
        assert url != None
        assert isinstance(url, str)
        page_source = self._client.fetch(url)
        return page_source

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

class WebCrawlerThreaded(WebCrawler):
    def crawl(self):
        print("crawling....")

# TODO:
# - We have to write to the file
    # - get links
    # - write to file
    # - create a class that can handle all of these operations!
# - write our crawl method
#   - redirect to all links using http client