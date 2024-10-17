import argparse
# from WebCrawler import profile
from WebCrawler import WebCrawlerBasic, WebCrawlerThreaded

def main():
    # def positive(value):
    #     if value < 0:
    #         raise argparse.ArgumentTypeError("Numeric value %s must be >= 0" % value)
    # I don't know how to incorporate error checking for positive values into the argparse module, hehe.
    # I will just resort to if statements

    parser = argparse.ArgumentParser(description="Rudimentary web crawler.")
    parser.add_argument("-s", "--seed", action="store", dest="seed", required=True, type=str)
    parser.add_argument("-v", "--verbose", action="store_true", dest="debug")
    parser.add_argument("-o", "--output", action="store", dest="output", required=True, type=str)
    parser.add_argument("--sleep", action="store", dest="sleep_time", type=float)
    parser.add_argument("-t", "--threads", action="store", dest="threads", type=int)
    args = parser.parse_args()
    seed = args.seed
    debug = args.debug
    output = args.output
    sleep_time = args.sleep_time
    threads = args.threads
    crawler = None

    # Check if crawler should sleep
    if not sleep_time:
        if not threads:
            crawler = WebCrawlerBasic(seed, output)

        else:
            crawler = WebCrawlerThreaded(seed, output, threads)
            print("threaded crawler!!!!")
    
    else:
        if sleep_time < 0:
            try: raise argparse.ArgumentTypeError(f"Sleep time must be >= 0") # lol, idk if this is even a practice!
            except argparse.ArgumentTypeError as e:                  # Its just nice that the callstack isn't displayed.
                print("Error: %s" % e)

        if not threads:
            crawler = WebCrawlerBasic(seed, output, sleep_time)
        
        else:
            crawler = WebCrawlerThreaded(seed, output, sleep_time, threads)

    # Unleash the crawler. mwhahaahaahahaha
    if not debug:
        if not threads:
            crawler.crawl(debug=False)
        
        else:
            crawler.crawl(debug=False, num_threads=threads)
        
    else:
        if not threads:
            crawler.crawl(debug=True)

        else:
            crawler.crawl(debug=True, num_threads=threads)

main()
