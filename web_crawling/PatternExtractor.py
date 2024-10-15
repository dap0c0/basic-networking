import re

class PatternExtractor():
    ''' Simple regex agent that returns a list of matches
    for any predefined pattern.'''
    def __init__(self):
        self.pattern_cache = {}
        self.pattern = None

    def get_matches(self, string):
        ''' Return a list of matches within the string.'''
        matched_groups = self.pattern.findall(string)
        return matched_groups

    def set_pattern(self, pattern_str):
        ''' Set pattern.'''
        assert pattern_str != None
        assert isinstance(pattern_str, str)

        if self.in_cache(pattern_str):
            self.pattern = self.pattern_cache[pattern_str]

        else:
            self.pattern = re.compile(pattern_str)
            self.pattern_cache[pattern_str] = self.pattern

    def in_cache(self, pattern_str):
        ''' Check if compiled pattern is in cache.'''
        assert pattern_str != None
        assert isinstance(pattern_str, str)
        is_contained = True

        try:
            value = self.pattern_cache[pattern_str]
        
        except KeyError as e:
            is_contained = False

        return is_contained
    
    

    
