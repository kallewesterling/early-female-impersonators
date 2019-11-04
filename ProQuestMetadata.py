import re
from datetime import datetime as dt

class DataPoint():
    
    def __init__(self, csv, headers):
        fields = csv.split("\t")
        _ = {}
        for i, field in enumerate(fields):
            _[headers[i]] = field
        self.data = _
        # self.source = Source(self.data)
    
    def __getitem__(self, item):
        return(self.data.get(item, None))
    
    
class Source():

    def __init__(self, data):
        self.data = data
        
        self._parsed_data, self._title, self._volume, self._issue, self._date, self._page_number = None, None, None, None, None, None
        
    @property
    def title(self):
        self._set_parsed_data()
        return(self._parsed_data['title'])
        
    @property
    def volume(self):
        self._set_parsed_data()
        return(self._parsed_data['volume'])
        
    @property
    def issue(self):
        self._set_parsed_data()
        return(self._parsed_data['issue'])
        
    @property
    def date(self):
        self._set_parsed_data()
        return(self._parsed_data['date'])
        
    @property
    def page_number(self):
        self._set_parsed_data()
        return(self._parsed_data['page_number'])
    
    def _set_parsed_data(self):
        if not self._parsed_data: self._parsed_data = {
            'title': self.parse_title(),
            'volume': self.parse_volume(),
            'issue': self.parse_issue(),
            'date': self.parse_date(),
            'page_number': self.parse_page_number(),
        }
    
    def _get_parsed_data(self):
        if not self._parsed_data: self._set_parsed_data()
        return(self._parsed_data)
        
    def parse_title(self):
        g = re.search("^([A-Za-z\s.-]+) \(.*\); (.*): ", self.data)
        if g:
            return(g.groups()[0])
        else:
            return(None)
        
    def parse_volume(self):
        g = re.search("Vol\. (\d+)", self.data)
        if g:
            return(g.groups()[0])
        else:
            return(None)
    
    def parse_issue(self):
        g = re.search("Iss\. (\d+)", self.data)
        if g:
            return(g.groups()[0])
        else:
            return(None)
        
    def parse_date(self):
        date = None
        
        # Try 1
        g = re.search("((\d{2}) (Jan|Feb|Mar|Apr|May|Jun|June|Jul|July|Aug|Sep|Oct|Nov|Dec) (\d{4}))", self.data)
        if g:
            date_str = g.groups()[0].replace("June", "Jun")
            date_str = date_str.replace("July", "Jul")
            date = dt.strptime(date_str, "%d %b %Y")
        
        # Try 2
        if date is None:
            g2 = re.search("((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (\d+), (\d{4}))", self.data)
            if g2: date = dt.strptime(g2.groups()[0], "%b %d, %Y")
        
        if date is None:
            self._log(f"Warning: Could not find date in the following data.\n\n{self.data}\n\n\n")
        
        return(date)
    
    def parse_page_number(self):
        g = re.search("(.*): (.*)\.", self.data)
        if g:
            return(g.groups()[1])
        else:
            return(None)
    
    def _log(self, msg):
        pass # print(msg)