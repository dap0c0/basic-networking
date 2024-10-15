import argparse
from WebCrawler import WebCrawlerBasic

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
    args = parser.parse_args()
    seed = args.seed
    debug = args.debug
    output = args.output
    sleep_time = args.sleep_time
    crawler = None

    if not sleep_time:
        crawler = WebCrawlerBasic(seed, output)
    
    else:
        if sleep_time < 0:
            try: raise argparse.ArgumentTypeError(f"Sleep time must be >= 0") # lol, idk if this is even a practice!
            except argparse.ArgumentTypeError as e:                  # Its just nice that the callstack isn't displayed.
                print("Error: %s" % e)

        else:
            crawler = WebCrawlerBasic(seed, output, sleep_time)
    
    # Unleash the crawler. mwhahaahaahahaha
    if debug:
        crawler.crawl(debug=True)
    
    else:
        crawler.crawl(debug=False)

main()
