import json
import datetime
from collections import namedtuple

class Message:
    
    def __init__(self, _date, _author, _content):
        self.date = _date
        self.author = _author
        self.content = _content

    def prettyPrint(self):
        print("Name: " + self.author + "\nDate:" + self.date + "\nTweet: " + self.content)

        
class JSONParser:

    def parseJSON(self, data):
        jsonStr = json.dumps(data._json)
        jsonDict = json.loads(jsonStr, object_hook=lambda d: namedtuple('X', d.keys(), rename = True)(*d.values()))
        message = Message(jsonDict.created_at, jsonDict.user.screen_name, jsonDict.text)
        return message
