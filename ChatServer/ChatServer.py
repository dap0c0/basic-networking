from abc import ABC, abstractmethod

class ChatServer(ABC):
    DEFAULT_BACKLOG = 10000
    MAX_BACKLOG = 1000000

    def __init__(self, port: int, backlog: int=DEFAULT_BACKLOG):
        assert isinstance(port, int)
        assert isinstance(backlog, int)
        assert port >= 0
        assert 0 < backlog and backlog <= ChatServer.MAX_BACKLOG, "Backlog is invalid!"
        self.port = port
        self.backlog = backlog

    @abstractmethod
    def handle_connection(self):
        pass

    @abstractmethod
    def data_received(self, data: bytes):
        pass

    @abstractmethod
    def handle_data(self):
        pass

    @abstractmethod
    def connection_closed(self):
       pass

    @abstractmethod
    def run(self):
        pass
