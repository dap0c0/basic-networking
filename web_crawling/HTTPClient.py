import urllib.request
import urllib.error

class HTTPClient():
    def __init__(self, host):
        assert isinstance(host, str)
        self.host = host
    
    def fetch(self):
        try:
            response = urllib.request.urlopen(self.host)
            data = response.read()
            text = data.decode("utf-8")
            return text
        
        except urllib.error.HTTPError as e:
            print(e)

        except urllib.error.URLError as e:
            print(e)