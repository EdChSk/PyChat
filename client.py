import socket, random, sys, threading, time
from tkinter import *
class Client():
    def __init__(self,addr,port,user):
        print("  Host:",addr)
        print("  Port:",port)
        print("  Attempting Connection To Server...")
        self.server = socket.socket()
        self.server.connect((addr,port))
        print("  ...Connected")
        username = self.connect(user)
        print("  Username: '"+username+"'")
        print(" ------------ Connected -----------")
        self.running = True
        t = threading.Thread(target=self.recv)
        t.start()
        while True:
            data = input("  > ")
            if data != "/exit":
                self.server.send(data.encode())
            else:
                print("Sending disconnection message...")
                self.server.send("".encode())
                print("...Done")
                self.server.close()
                self.running = False
                break
        self.server.close()
    def recv(self):
        while self.running == True:
            try:
                data =self.server.recv(1024).decode()
            except:
                break
            if data and data != "Please enter a name:":
                print("/r"+str(data),end="\n  > ")
            elif data == "  Please enter a username:":
                print("  Name taken! Please enter new name")
    def connect(self,user):
        if user == "":
            username = input("  Please enter a username:\n    >>")
        else:
            username = user
        self.server.send(username.encode())
        data = self.server.recv(1024).decode()
        while data == "TAKEN":
            print("  -! Username Taken !-")
            username = input("  Please enter a different username:\n    >>")
            self.server.send(username.encode())
            data = self.server.recv(1024).decode()
        return username
