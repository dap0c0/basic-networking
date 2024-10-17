from cProfile import Profile
from pstats import SortKey, Stats

import time
import threading
from abc import ABC, abstractmethod
from HTTPClient import HTTPClient
from FileOrganizer import FileOrganizer
from PatternExtractor import PatternExtractor
from Queue import LLQueue

# def profile(fx):
#     with Profile() as profile:
#         fx
#         Stats(profile).strip_dirs().sort_stats(SortKey.CALLS).print_stats()
#

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
    def __init__(self, seed, results_file, num_threads, sleep=0):
        super().__init__(seed, results_file, sleep=0)
        assert isinstance(num_threads, int)
        self.num_threads = num_threads
        self.threads = [None] * self.num_threads

    def _get_fetch_tasks(self):
        '''Return a queue of num_threads many tasks from the queue. '''
        task_queue = LLQueue()

        for i in range(self.num_threads):
            link_to_fetch = self._queue.dequeue()
            # print("Queue: " + str(self._queue))
            assert link_to_fetch != None
            task_queue.enqueue((self._client.fetch, link_to_fetch)) # might be redundant to keep calling function
        
        assert len(task_queue) == self.num_threads
        return task_queue
    
    def _get_page_sources(self, debug):
        ''' Spawn num_threads worth of threads to fetch from
        pages. Return a queue of page html corresponding to each url.'''
        fetch_tasks = self._get_fetch_tasks()
        assert len(fetch_tasks) == self.num_threads

        # Fetch pages asyncronously. Store page results on parallel array (page_htmls)
        i = 0
        page_htmls_list = [""] * self.num_threads
        page_htmls_queue = LLQueue()

        # Fetch pages per thread
        while i < self.num_threads and not fetch_tasks.is_empty():
            task = fetch_tasks.dequeue()
            fetch_function = task[0]
            url = task[1]

            if debug:
                print("\nRequesting page source from %s" % url)
                print("# In queue: %s" % abs(self._queue))
                print("# Explored: %d" % len(self._explored_links))

            self.threads[i] = threading.Thread(target=self._store_in_list, args=(fetch_function(url), page_htmls_list, i, ))
            self.threads[i].daemon = True
            self.threads[i].start()
            
            # Prevent endless loops
            self._explored_links.append(url)
            
            # Add result to queue if not empty
            page_html = page_htmls_list[i]

            if page_html:
                self._queue.enqueue(page_html)
            
            # Allow next thread to spawn
            i += 1

        assert len(page_htmls_queue) >= 0
        assert len(page_htmls_queue) <= self.num_threads
        return page_htmls_queue

    def _store_in_list(self, fx, result_list, index):
        assert isinstance(fx, object)
        assert isinstance(result_list, list)
        assert isinstance(index, int)
        assert index >= 0
        result_list.insert(index, fx)

    def crawl(self, num_threads, debug=False): # Might be better to have threads defined initially
        assert isinstance(num_threads, int)
        assert num_threads > 0

        link_info_initializer = {
            "links": [
            ],
            "emails": [   
            ],
            "files" : [
            ]
        }
        
        curr_url = self.seed
        print("Starting Crawler from seed [%s]" % curr_url)
        page_source = self._client.fetch(curr_url)
        self._explored_links.append(curr_url)

        if not page_source:
            print("Seed invalid! Halting crawler.")

        else:
            links_found = self._extract_links(page_source)
            for link in links_found: self._queue.enqueue(link)
            
            # Add links to data
            self.data[curr_url] = link_info_initializer
            self.data[curr_url]["links"] = links_found

            # Continue indefinite processing until keyboard interrupt (or other kill sig)
            kill_sig = False

            while not kill_sig:
                try:
                    assert curr_url != None
                    page_htmls_queue = self._get_page_sources(debug)

                    while not page_htmls_queue.is_empty():
                        page_html = page_htmls_queue.dequeue()
                        links_found = self._extract_links(page_html)

                        for link in links_found:
                            self._queue.enqueue(link)

                except KeyboardInterrupt as e:
                    print("Keyboard interrupt caught! Halting crawler.")
                    kill_sig = True


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
                        links_found = self._extract_links(page_source)# Extract links on current url's page source¥
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