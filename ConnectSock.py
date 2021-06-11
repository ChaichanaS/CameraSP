import socket
import time
class ConnectRobot:
    def __init__(self,IP,Port):
        self.IP = IP
        self.Port = Port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.IP,self.Port))
        print("Connect....")
    def send_data(self,data):
        self.sock.sendall((data.encode()))
        time.sleep(0.1)
    def get_data(self):
        data = self.sock.recv(1024)
        data = data.decode("ascii")
        return data
    def close_socket(self):
        self.sock.close()

class SeverSockt:
    def __init__(self,Port):
        self.IP = socket.gethostname()
        self.IP = socket.gethostbyname(self.IP)
       
        self.Port = Port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.IP,self.Port))
        self.sock.listen(5)
        self.sever = "ON"
        print("IP is  {}  Port is {}".format(self.IP,self.Port))

    def On_socket(self):
        while True:
            if self.sever == "OFF":
                break
            self.client,self.addr = self.sock.accept()
            if self.addr != None:
                msg = self.client.recv(1024).decode("ascii")
                self.client.send("Hello Client!".encode("ascii"));
                print(str(self.addr) , "mesage " + msg)      

    def send_data(self,data):
        self.client.sendall(data)
    def get_data(self):
        return str(self.addr)
    def off_socket(self):
        self.sever = "OFF"
        self.sock.close()



