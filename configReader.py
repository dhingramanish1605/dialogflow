from configparser import ConfigParser
import os

def readConfig(section,key):
    config=ConfigParser()
    config.read("../dialogflow/config.ini")
    return config.get(section, key)



