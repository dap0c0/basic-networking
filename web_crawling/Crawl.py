import argparse
from WebCrawler import TwistedWebCrawler

def main():
    parser = argparse.ArgumentParser(description="Rudimentary web crawler.")
    parser.add_argument("-s", "--seed", action="store", dest="seed", required=True, type=str)
    parser.add_argument("-v", "--verbose", action="store_true", dest="debug")
    parser.add_argument("-o", "--output", action="store", dest="output", required=True, type=str)
    parser.add_argument("--sleep", action="store", dest="sleep_time", type=float)

    args = parser.parse_args()
    seed = args.seed
    debug = args.debug
    output = args.output
    sleep_time = args.sleep_time
    crawler = None

    # Check if crawler should sleep
    if not sleep_time:
        crawler = TwistedWebCrawler(seed, output)
   
    else:
        if sleep_time < 0:
            try: raise argparse.ArgumentTypeError(f"Sleep time must be >= 0") # lol, idk if this is even a practice!
            except argparse.ArgumentTypeError as e:                  # Its just nice that the callstack isn't displayed.
                print("Error: %s" % e)

        crawler = TwistedWebCrawler(seed, output, sleep_time)

    # Unleash the crawler. mwhahaahaahahaha
    if not debug:
            crawler.crawl(debug=False)

    else:
            crawler.crawl(debug=True)

main()
