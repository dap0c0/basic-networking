from abc import ABC, abstractmethod
from HTTPClient import HTTPClient
from FileOrganizer import FileOrganizer

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
        self.results_file = results_file
        self.file_interface = FileOrganizer(self.results_file)

    @abstractmethod
    def crawl(self):
        pass

    
    def extract_pattern(self, input, pattern):
        ''' Return a list of strings matching the pattern, having
        parsed through input'''
        matched_groups = pattern.findall(input)
        return matched_groups

    def extract_links(self, input):
        return self.extract_pattern(input, WebCrawler.HYPERLINK_REGEX_PATTERN)
    
    def extract_emails(self, input):
        pass

    def write_to_file(self, current_link, links_found):
        pass

    def get_links(self, current_link):
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