from PatternExtractor import PatternExtractor

class HTTPResponse():
    HTML_DELIMITERS = ["<!doctype html>", "<!DOCTYPE html>"]
    CHAR_SET_DEFAULT = "utf-8"
    BUFFSIZE_DEFAULT = 8
    CHARSET_SUBHEADER_CATCHER = r".*[cC]harset=(.*)"

    def __init__(self, data):
        assert isinstance(data, bytes)
        self._data_bytes = data
        self._data_str = self._decode(HTTPResponse.BUFFSIZE_DEFAULT)
        
        # Public instance vars
        self.status_code = self._get_status_code(self._data_str)
        self.headers = self._get_headers(self._data_str)
        self.content = self._get_content(self._data_str)

    def _get_status_code(self, data_str):
        ''' Return the status code of the response.'''
        assert isinstance(data_str, str)
        first_car_ret_ind = data_str.find("\r\n")
        stat_msg = data_str[0:first_car_ret_ind]
        stat_code = int(stat_msg.split(" ")[1]) # HTTP/$version $status $message
        return stat_code
 
    def _get_headers(self, data_str):
        ''' Return the header content (with error code) of the response.'''
        assert data_str != None
        assert isinstance(data_str, str)

        # Headers are always bounded before a double carriage return
        headers_n_status= data_str.split("\r\n\r\n")[0]
        headers = headers_n_status[1:len(headers_n_status)]
        return headers
   
    def _get_content(self, data_str):
        assert data_str != None
        assert isinstance(data_str, str)

        # Content is always past first double carriage return (headers)
        content = data_str.split("\r\n\r\n")[1]
        return content

    def _decode(self, buffsize):
        ''' Decode byte data depending on the encoding.'''
        assert self._data_bytes != None
        assert isinstance(buffsize, int)
        assert buffsize > 0
        charset = HTTPResponse.CHAR_SET_DEFAULT # should be utf-8
        decoded_data = ""
        curr_len = 0
        start = 0
        end = buffsize 
        decode_error = False

        # Try decoding the entire buffer (self._data_bytes).
        while curr_len < len(self._data_bytes) and not decode_error:
            try:
                byte_segment = self._data_bytes[start:end]
                assert len(byte_segment) <= buffsize
                decoded_data += str(byte_segment, charset)
                
                # Move segment focus
                start += len(byte_segment)
                end += len(byte_segment)
                curr_len += len(byte_segment)
            
            except UnicodeDecodeError as e:
                decode_error = True

        # Get the charset in the already decoded data if error found
        if not decode_error:
            assert curr_len == len(self._data_bytes)
        
        else:
            # Start search for charset subheader, located in Content-Type header.
            lines = decoded_data.split("\r\n")
            charset = None
            curr_line = None
            i = 0
            extractor = PatternExtractor()
            extractor.set_pattern(HTTPResponse.CHARSET_SUBHEADER_CATCHER)

            # Keep cycling through lines until exhausted or charset subheader found
            while not charset and i < len(lines):
                curr_line = lines[i]
                matches = extractor.get_matches(curr_line)

                if matches:
                    assert len(matches) == 1
                    charset = matches[0]
                
                else:
                    i += 1

            if charset:
                decoded_data = str(self._data_bytes, charset)
            
            else:
                raise UnicodeDecodeError("Could not find decoding scheme of data.")
            
        return decoded_data
    
    def __repr__(self):
        return self.content