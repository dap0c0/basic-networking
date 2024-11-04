import HTTPClientUnblocked
import socket

class HTTPClientAsynchronous(HTTPClientUnblocked):
    async def fetch(self, **kwargs):
        try:
            connecting_addr = (self._host, self._port)
            await self._attempt_connection(connecting_addr)
        
        except socket.gaierror as e:
            print("Error connecting to host: %s" % e)
            return
        
        # Send request to host
        request_buffer = self._generate_request("GET", self._path_params, self._http_version, **kwargs)
        print("Request: [%s]" % request_buffer)
        
        self._sock.sendall(request_buffer)
        response = self._recv_data()
        return response
    
    async def _attempt_connection(self, connecting_addr: tuple) -> bool:
        assert isinstance(connecting_addr, tuple)
        self._sock.connect(connecting_addr)
        return True