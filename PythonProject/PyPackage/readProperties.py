import configparser
from __builtin__ import staticmethod

config=configparser.RawConfigParser
config.read(".\\Cconfiguration\\config.ini", encoding=None)

class ReadConfig:
    @staticmethod
    def getBaseURL():
        url=config.get('common info', 'baseURL')
        return url
    
    @staticmethod
    def getUserName():
        username=config.get('common info', 'userName')
        return username
        
    @staticmethod
    def getUserPass():
        userpass=config.get('common info', 'userPass')
        return userpass        