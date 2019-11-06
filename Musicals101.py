import re

class ParseTheatreInfo():
    ''' Class to parse datapoints from musicals101.com's information on historical theatres and create an accessible dataset. '''
    
    def __init__(self, text):
        self.text = text
        
        self.address = self.parse_address()
        self.architect = self.parse_architect()
        self.built = self.parse_built()
        self.demolished = self.parse_demolished()
        self.original_name = self.parse_original_name()
        self.later_named = self.parse_later_named()
        self.owners = self.parse_owners()
        self.seats = self.parse_seats()
        self.references = self.parse_references()
        self.history = self.parse_history()
        self.previous_name = self.parse_previous_name()
        self.later_name = self.parse_later_name()
        
        self.data = {
            'address': self.address,
            'architect': self.architect,
            'built': self.built,
            'demolished': self.demolished,
            'original_name': self.original_name,
            'later_named': self.later_named,
            'owners': self.owners,
            'seats': self.seats,
            'references': self.references,
            'history': self.history,
            'previous_name': self.previous_name,
            'later_name': self.later_name,
        }
        
    def parse_address(self):
        g = re.search(r"^(.*)\n", self.text) # first line
        if g is None: return(None)
        else: return(g.groups()[0])
        
    def parse_architect(self):
        g = re.search(r"Architect: ?(.*)\n", self.text, re.I)
        if g is None: return(None)
        else: return(g.groups()[0])
        
    def parse_built(self):
        g = re.search(r"Built: ?(.*)\n", self.text, re.I)
        if g is None: return(None)
        else: return(g.groups()[0])
        
    def parse_demolished(self):
        g = re.search(r"Demolished: ?(.*)\n", self.text, re.I)
        if g is None: return(None)
        else: return(g.groups()[0])
        
    def parse_original_name(self):
        g = re.search(r"Original n|Name: ?(.*)\n", self.text, re.I)
        if g is None: return(None)
        else: return(g.groups()[0])
        
    def parse_later_named(self):
        g = re.search(r"Later named: (.*)\n", self.text, re.I)
        if g is None: return(None)
        else: return(g.groups()[0])
        
    def parse_owners(self):
        g = re.search(r"(Owners|Owners/Managers): ?(.*)\n", self.text, re.I)
        if g is None: return(None)
        else: return(g.groups()[1])
        
    def parse_seats(self):
        g = re.search(r"Seats: ?(.*)\n", self.text, re.I)
        if g is None: return(None)
        else:
            seats = g.groups()[0]
            seats = seats.replace(",","")
            seats = seats.replace(".","")
            try:
                seats = int(seats)
            except ValueError: # seats is not only a number
                pass           # we will then just save the value as is
            return(seats)
        
    def parse_references(self):
        g = re.search(r"- see (.*)", self.text, re.I)
        if g is None: return(None)
        else: return(g.groups()[0])
        
    def parse_history(self):
        g = re.search(r"History: ?(.*)\n", self.text, re.I)
        if g is None: return(None)
        else: return(g.groups()[0])
        
    def parse_previous_name(self):
        g = re.search(r"Previous Names?: ?(.*)\n", self.text, re.I)
        if g is None: return(None)
        else: return(g.groups()[0])
        
    def parse_later_name(self):
        g = re.search(r"Later Names?: ?(.*)\n", self.text, re.I)
        if g is None: return(None)
        else: return(g.groups()[0])