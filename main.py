from tkinter import *
import socket
import time
import random
import threading

class Main_window():
    def __init__(self,master):
        print("[Creating Main Window.....")
        self.master = master
        self.root = Tk()
        print("  Setting Attributes...")
        self.root.title("Python Chat") # Sets window title
        self.root.configure(bg="#ffffff")
        self.root.attributes('-fullscreen', False)# Full screen = True
        self.root.geometry("350x250")
        print("  ...Attributes Set")
        print(".....Main Window Created]")
        cc = __import__("loginwin")
        self.window = cc.Log_in_window(self.root,self)
    def client(self,username,ip):
        self.master.ip = ip
        self.master.username = username
        cc = __import__("client")
        self.window = cc.Client_window(self.root,self)
    def host(self):
        print("Host")
        cc = __import__("host")
        self.window = cc.Host_window(self.root,self)
    def close(self):
        self.root.destroy()
        print(".....Closed all windows")



class User():
    def __init__(self):
        print("Creating User...")
        self.username = ""
        self.ip = "172.19.246.102"
        self.port = 9009
        self.messages = ["1","2","3","4","5","6","7","8"]
        print("...User Created")
        self.window = Main_window(self)
        

User()
