import socket 
import time 


class Client:
    def __init__(self,host,port):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.host = host
        self.port = port 
        

    # Connect to Server
    def connect_server(self):
        while True:
            if self.sock.connect_ex((self.host,self.port)) != 0:
                time.sleep(3)
                continue 
            break 
    
    # Send Payload 
    def send_payload(self,msg):
        self.sock.send(msg.encode("utf8")) 
