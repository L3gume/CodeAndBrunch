import json
import datetime
from collections import namedtuple

class Message:
    
    def __init__(self, _date, _author, _content):
        self.date = _date
        self.author = _author
        self.content = _content

    def prettyPrint(self):
        # ... do things
        
class JSONParser:

    def parseJSON(self):
        x = json.loads(data, object_hook=lambda 
                d: namedtuple('X', d.keys())(*d.values()))
        message = Message(x.date, x.author, x.content)
        return message
