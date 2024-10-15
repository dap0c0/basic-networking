import urllib.request
import urllib.error
from http.client import RemoteDisconnected

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

        except UnicodeDecodeError as e:
            print("Could not decode data: %s" % e)
        
        except urllib.error.HTTPError as e:
            print(e)

        except urllib.error.URLError as e:
            print(e)

        except RemoteDisconnected as e:
            print("Encountered error for %s" % host)
            
        return result