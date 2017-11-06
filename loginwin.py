from tkinter import *
import socket
import time
import random
import threading

class Log_in_window():
    def __init__(self,window,master):
        print("[Creating Log In Window.....")
        self.master = master
        self.oldip, self.name = self.get_old_ipname()
        self.root = window
        self.create_window()
        print(".....Log In Window Created]")
        self.root.mainloop()
    def get_old_ipname(self):
        try:
            f = open("userInfo.txt","r")
            line = f.readlines()
            f.close()
            name = line[0].strip("\n")
            ip = line[1]
        except: # File does not exist
            name = "Guest"
            ip = "[IP ADDRESS]"

        return ip, name
    def create_window(self):
        print("  Setting Attributes...")
        x = Frame(self.root,bg="#ffffff")
        self.x = x
        photo = PhotoImage(file="logo.gif")
        print("  ...Attributes Set")
        print("  Creating Widgets...")
        l = Label(x, image=photo,bg="#ffffff")
        l.image= photo
        l.grid(column=0,row=0,pady=2.5,columnspan=2)
        l = Label(x,text="",bg="#ffffff").grid(column=0,row=1,pady=2.5,columnspan=2)
        self.User = Entry(x,bg="#ffffff")
        self.User.grid(column=0,columnspan=2,row=2,pady=2.5)
        self.User.insert(0,self.name)
        self.Ip = Entry(x,bg="#ffffff")
        self.Ip.grid(column=0,columnspan=2,row=3,pady=2.5)
        self.Ip.insert(0,self.oldip)
        b = Button(x,text="Login",command=self.login,bg="#ffffff",bd=0.5,width=10).grid(column=1,pady=2.,row=4) # Login Button
        b = Button(x,text="Exit",command=self.master.close,bg="#ffffff",bd=0.5,width=10).grid(column=0,pady=2.,row=4) # Exit Button
        b = Button(x,text="Host",command=self.host,bg="#ffffff",bd=0.5,width=21).grid(column=0,pady=2.,row=5,columnspan=2) # Host Button
        x.place(relx=.5, rely=.5, anchor="c")
        print("  ...Widgets Created")
    def login(self):
        print("[Logging on to existing server.....")
        print("  Getting user information...")
        username = self.User.get()
        ip = self.Ip.get()
        print("  ...Complete")
        print("  Exporting User Information")
        f = open("userInfo.txt","w")
        f.write(username+str("\n")+ip)
        f.close()
        print("  ...Complete")
        print("  Removing old widgets...")
        self.x.destroy()
        print("  ...Widgets removed")
        self.master.client(username,ip)
    def host(self):
        print("  Removing old widgets...")
        self.x.destroy()
        print("  ...Widgets removed")
        self.master.host()
