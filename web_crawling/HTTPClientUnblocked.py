import HTTPClient
import HTTPResponse
import socket

class HTTPClientUnblocked(HTTPClient):
    def fetch(self, **kargs):
    # Connect to new host on port if not previously set
        try:
            connecting_addr = (self._host, self._port)
            self._sock.connect((connecting_addr))
        
        except socket.gaierror as e:
            print("Error connecting to host: %s" % e)
            return
    
        # Send request to host
        request_buffer = self._generate_request("GET", self._path_params, self._http_version, **kargs)
        print("Request: [%s]" % request_buffer)
        self._sock.sendall(request_buffer)
        response = self._recv_data()
        return response

    def _recv_data(self):
        ''' Receive data from the host and return as HTTPResponse'''
        data = b""

        while True:
            received = self._sock.recv(HTTPClient.DEFAULT_BUFFER_SIZE)

            if len(received) == 0:
                return HTTPResponse(data)

            data += received
