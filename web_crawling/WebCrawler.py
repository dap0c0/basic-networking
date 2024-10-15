import time
from abc import ABC, abstractmethod
from HTTPClient import HTTPClient
from FileOrganizer import FileOrganizer
from PatternExtractor import PatternExtractor
from Queue import LLQueue

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
        self.data = {} # Each url will contain info regarding external links, emails, files

        # Class drivers
        self._results_file = results_file
        self._file_interface = FileOrganizer(self._results_file)
        self._extractor = PatternExtractor()
        self._client = HTTPClient() # Host is set per query
        self._queue = LLQueue()
        self._explored_links = []

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

class WebCrawlerBasic(WebCrawler):
    def crawl(self, debug=False):
        link_info_initializer = {"links": [
            ], 
            "emails": [
            ],
            "files" : [
            ]
            }
        
        def crawl_driver():
            # Start crawling from the seed.
            curr_url = self.seed
            print("Starting Crawler from seed %s....." % curr_url)
            seed_explored = False # One-time switch to prevent false-start

            while True:
                if self.sleep > 0:
                    if debug:
                        print("Sleeping for %ss" % self.sleep)

                    time.sleep(self.sleep)

                if not curr_url in self._explored_links: # Prevent endless loops
                    if debug:
                        print("\nRequesting page source from %s" % curr_url)
                        print("# In queue: %s" % abs(self._queue))
                        print("# Explored: %d" % len(self._explored_links))

                    page_source = self._client.fetch(curr_url)
                    
                    if not seed_explored:
                        seed_explored = True

                        if page_source == None: # Error must have been raised!
                            print("Invalid seed! Exiting...")
                            break

                    self._explored_links.append(curr_url)

                    if page_source: # Check that the url was accessible
                        self.data[curr_url] = link_info_initializer # Initialize data template
                        links_found = self._extract_links(page_source) # Extract links on current url's page source
                        self.data[curr_url]["links"] = links_found # add hyperlink info for current page

                        for link in links_found:
                            self._queue.enqueue(link) # Queue for future crawl
                    
                curr_url = self._queue.dequeue()

        try:
            crawl_driver()
        
        except KeyboardInterrupt as e:
            print("Keyboard interrupt detected. Stopping crawler...")
        
        finally:
            if debug:
                print("%d links explored." % len(self._explored_links))
                print("Writing data in JSON format to %s" % self._results_file)

            self._file_interface.write_file(self.data) 