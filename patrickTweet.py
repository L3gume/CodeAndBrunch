#!/usr/bin/env python

# PatrickTweet
# A very useful command-line tool that gives you a random tweet with "Patrick" in it.
import twitter
import random

from jsonParser import Message
from jsonParser import JSONParser

def randomTweet(tweet, jsonParser):
    jsonTweet = tweet[random.randint(0, len(tweet) - 1)]
    message = jsonParser.parseJSON(jsonTweet)
    message.prettyPrint()

api = twitter.Api(consumer_key='ghEPZheOTZDGLveQicPtGV39i',
                  consumer_secret='2lTOCuSv4Y1e7Oad7ROP4F8pWTYXaabhIdgBmASh5ygRHA7Dp7',
                  access_token_key='974684154750230528-uHKLAffr0ouHqL7j9WCBT0MgEUFIeUN',
                  access_token_secret='c21kbxb9jRGImDwjWXyOqDdH36OzgfS2eZWy8BcgtnDsH')

tweets = api.GetSearch(term="patrick")
parser = JSONParser()
randomTweet(tweets, parser)
