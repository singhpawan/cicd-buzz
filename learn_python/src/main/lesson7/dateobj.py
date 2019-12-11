# dateobj.py

class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod # cls is "Date" Avoiding the problem of hardcoding
    def from_string(cls, s):
        parts = s.split('-')
        return cls(int(parts[0]), int(parts[1]), int(parts[2]))

    @classmethod
    def today(cls):
        import time
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)



'''
    def date_from_string( s):
        parts = s.split('-')
        return Date(int(parts[0]), int(parts[1]), int(parts[2]))
'''