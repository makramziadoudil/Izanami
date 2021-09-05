import requests 
import platform 
import getpass 
import os 


# Read Systeminformations
class ReadSystem:
    def __init__(self):
        self.user = getpass.getuser()
        self.name = platform.node()
        self.os = platform.system()
        self.py = platform.python_version()
        self.ip = requests.get("https://api.ipify.org?format=json").text


    def system_values(self):
        return self.user,self.name,self.os,self.ip,self.py 


