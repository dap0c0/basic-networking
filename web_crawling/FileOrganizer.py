import re
import json

class FileOrganizer():
    FILENAME_PATTERN = re.compile(r"\D+\.\w+")

    def __init__(self, filename):
        assert isinstance(filename, str)
        assert self.isvalid(filename)
        self.filename = filename

    def isvalid(self, filename):
        ''' Validate that the string is indeed a valid filename.'''
        assert filename != None
        assert isinstance(filename, str)
        return FileOrganizer.FILENAME_PATTERN.search(filename)
    
    def write_file(self, dictionary, ind):
        ''' Write dictionary in JSON format to file.'''
        assert dictionary != None
        assert ind != None
        assert isinstance(dictionary, dict)
        assert isinstance(ind, int)
        
        with open(self.filename, "w", encoding="utf-8") as write_file:
            json.dump(dictionary, write_file, indent=ind)

    def read_file(self, ind):
        ''' Return the dictionary object from the file.'''
        assert ind != None
        assert isinstance(ind, int)
        
        with open(self.filename, "r", encoding="utf-8") as read_file:
            data = json.load(read_file, indent=ind)

        assert isinstance(data, dict)
        return data

        

