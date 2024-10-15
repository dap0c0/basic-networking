import urllib.request
import urllib.error

class HTTPClient():
    def fetch(self, host):
        ''' Get the sourcecode of the given url. Returns
        none upon error.'''
        result = None

        try:
            response = urllib.request.urlopen(host)
            data = response.read()
            text = data.decode("utf-8")
            result = text
        
        except urllib.error.HTTPError as e:
            print(e)

        except urllib.error.URLError as e:
            print(e)
            
        return result