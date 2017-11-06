from tkinter import *
import socket
import time
import random
import threading


class Client_window():
    def __init__(self,window,master):
        self.fail = 0
        print("[Creating Client Window.....")
        self.root = window
        self.var = 1
        self.var2 = 0
        self.master = master
        ss = __import__("server")
        self.server = ss.Server("client",self)
        #self.server = Server("client",self)
        self.make_window()
        if self.fail > 0:
            ee = __import__("error")
            e = ee.ErrorWindow("Failed to connect")
            pass
        else:
            print(".....Client Window Created]")
            x = "%%u "+self.master.master.username
            self.server.send("",x)
            t = threading.Thread(target=self.server.client_loop)
            t.start()
            x = threading.Thread(target=self.server.client_loop2)
            x.start()
            self.root.mainloop()
    def maxmin(self):
        if self.var == 1:
            print("Exiting Fullscreen")
            self.var = 0
            self.root.attributes('-fullscreen', False)
            if self.var2 == 0:
                self.var2 = 1
                self.root.geometry('{}x{}'.format(200, 210))
                self.master.master.messages.append("?Type /fullscreen to go fullscreen?")
        elif self.var == 0:
            print("Entering Fullscreen")

            self.var = 1
            self.root.attributes('-fullscreen',True)
    def make_window(self):
        try:
            self.l = Label(self.root,text="Connection Established",fg="#25cc00",bg="#ffffff").place(relx=0,rely=0)
            self.l = Button(self.root,text="><",fg="#e8e8e8",bg="#ffffff",bd=0,command=self.maxmin).place(relx=0.985,rely=0)
            print("  Creating Widgets...")
            self.y = Frame(self.root,bg="#ffffff")
            self.root.bind("<Return>",self.server.send)
            self.l8 = Label(self.y,text="",bg="#ffffff",fg="#e8e8e8",justify=LEFT,anchor=W)
            self.l8.pack(anchor=W)
            self.l7 = Label(self.y,text="",bg="#ffffff",fg="#c6c6c6",justify=LEFT,anchor=W)
            self.l7.pack(anchor=W)
            self.l6 = Label(self.y,text="",bg="#ffffff",fg="#9b9b9b",justify=LEFT,anchor=W)
            self.l6.pack(anchor=W)
            self.l5 = Label(self.y,text="",bg="#ffffff",fg="#7a7a7a",justify=LEFT,anchor=W)
            self.l5.pack(anchor=W)
            self.l4 = Label(self.y,text="",bg="#ffffff",fg="#7a7a7a",justify=LEFT,anchor=W)
            self.l4.pack(anchor=W)
            self.l3 = Label(self.y,text="",bg="#ffffff",fg="#7a7a7a",justify=LEFT,anchor=W)
            self.l3.pack(anchor=W)
            self.l2 = Label(self.y,text="",bg="#ffffff",fg="#7a7a7a",justify=LEFT,anchor=W)
            self.l2.pack(anchor=W)
            self.l1 = Label(self.y,text="",bg="#ffffff",fg="#7a7a7a",justify=LEFT,anchor=W)
            self.l1.pack(anchor=W)
            self.ent = Entry(self.y,bg="#ffffff",bd=1,width=30)
            self.ent.pack(pady=10)
            self.y.place(relx=0.5,rely=0.5,anchor="c")
            print("  ...Widgets Created")
        except:
            self.fail += 1
