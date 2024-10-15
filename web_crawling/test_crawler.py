import WebCrawler

seed = "https://wiki.python.org/moin/HandlingExceptions"
results_file = "results_a.txt"

spider = WebCrawler.WebCrawlerBasic(seed, results_file)
spider.crawl(debug=True)