import json
import datetime
from collections import namedtuple

class Message:
    
    def __init__(self, _date, _author, _content):
        self.date = _date
        self.author = _author
        self.content = _content

    def prettyPrint(self):
        print("not implemented")

        
class JSONParser:

    def parseJSON(self, data):
        x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys(), rename = True)(*d.values()))
        message = Message(x.created_at, x.user.screen_name, x.text)
        return message
