from tkinter import *
import socket
import time
import random
import threading

class Host_window():
    def __init__(self,window,master):
        self.root = window
        self.master = master
        self.varz = 0
        self.go = True
        self.var2 = 0
        print("[Creating Host Window.....")
        self.msg = ["1","","","","","","",""]
        t = threading.Thread(target=self.fade)
        t.start()
        self.done = False
        x = threading.Thread(target=self.serv)
        x.start()
        y = threading.Thread(target=self.lp)
        y.start()
        print(".....Host Window Created]")
        self.root.mainloop()
    def maxmin(self):
        if self.varz == 1:
            print("Exiting Fullscreen")
            self.varz = 0
            self.root.attributes('-fullscreen', False)
            if self.var2 == 0:
                self.var2 = 1
                self.root.geometry('{}x{}'.format(200, 210))
                self.master.master.messages.append("?Type /fullscreen to go fullscreen?")
        elif self.varz == 0:
            print("Entering Fullscreen")

            self.varz = 1
            self.root.attributes('-fullscreen',True)        
    def lp(self):
        i = 0
        while self.done == False:
            i += 1
            print("Fail "+str(i)+"/5")
            time.sleep(1)
            if i == 5:
                break
                quit()
        print("\nStarting main server loop...\n  ...Loop started")
        while True:
            try:
                self.l1.configure(text=self.msg[len(self.msg)-1])
            except:
                if self.go == False:
                    break
                else:
                    time.sleep(1)
            self.l2.configure(text=self.msg[len(self.msg)-2])
            self.l3.configure(text=self.msg[len(self.msg)-3])
            self.l4.configure(text=self.msg[len(self.msg)-4])
            self.l5.configure(text=self.msg[len(self.msg)-5])
            self.l6.configure(text=self.msg[len(self.msg)-6])
            self.l7.configure(text=self.msg[len(self.msg)-7])
            self.l8.configure(text=self.msg[len(self.msg)-8])
            time.sleep(0.2)
            if self.go == False:
                break
            
    def serv(self):
        ss = __import__("server")
        self.server = ss.Server("server",self,self.root)
    def sendmsg(self,m):
        if self.done == True:
            self.server.sendmsg(None,self.ent.get())
    def make_widgets(self):
        print("  Creating widgets...")
        self.l = Label(self.root,text="Creating Server...",bg="#000000",fg="#c900ae")
        self.l.place(relx=0,rely=0)
        self.y = Frame(self.root,bg="#000000")
        self.l8 = Label(self.y,text="",bg="#000000",fg="#053500",justify=LEFT,anchor=W)
        self.l8.pack(anchor=W)
        self.l7 = Label(self.y,text="",bg="#000000",fg="#084c00",justify=LEFT,anchor=W)
        self.l7.pack(anchor=W)
        self.l6 = Label(self.y,text="",bg="#000000",fg="#0c7200",justify=LEFT,anchor=W)
        self.l6.pack(anchor=W)
        self.l5 = Label(self.y,text="",bg="#000000",fg="#109100",justify=LEFT,anchor=W)
        self.l5.pack(anchor=W)
        self.l4 = Label(self.y,text="",bg="#000000",fg="#109100",justify=LEFT,anchor=W)
        self.l4.pack(anchor=W)
        self.l3 = Label(self.y,text="",bg="#000000",fg="#109100",justify=LEFT,anchor=W)
        self.l3.pack(anchor=W)
        self.l2 = Label(self.y,text="",bg="#000000",fg="#109100",justify=LEFT,anchor=W)
        self.l2.pack(anchor=W)
        self.l1 = Label(self.y,text="",bg="#000000",fg="#109100",justify=LEFT,anchor=W)
        self.l1.pack(anchor=W)
        self.ent = Entry(self.y,bg="#191919",fg="#ffffff",bd=1,width=30)
        self.ent.pack(pady=10)
        self.y.place(relx=0.5,rely=0.5,anchor="c")
    def fade(self):
        print("\n  Changing host window color...")
        colors = ['#ffffff', '#e1e1e1', '#c8c8c8', '#afafaf', '#969696', '#7d7d7d', '#646464', '#4b4b4b', '#323232', '#191919', '#000000']
        for color in colors:
            self.root.configure(bg=color)
            print("    -"+str(color))
            time.sleep(0.01)
        print("\n  ...Color changed")
        self.make_widgets()
        var = 0
        while True:
            if var == 0:
                self.l.configure(text="Creating Server.")
                var += 1
            elif var == 1:
                self.l.configure(text="Creating Server..")
                var += 1
            elif var == 2:
                self.l.configure(text="Creating Server...")
                var = 0
            time.sleep(0.1)
            if self.done == True:
                break
        print("Server Running")
        self.l.configure(text="Server running",fg="green")
