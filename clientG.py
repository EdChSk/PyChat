from tkinter import *
import time
import sys
import socket
import threading
## --------------- Login Win --------------- ##
class LoginWindow():
    def __init__(self,master,host,port,username):
        self.master = master
        # --- Create  Window --- #
        self.root = Tk()
        self.root.title("Login")
        self.data = ""
        self.root.configure(bg="#ffffff")
        # --- Create Widgets --- #
        photo = PhotoImage(file="logo.gif")
        l = Label(self.root, image=photo,bg="#ffffff")
        l.pack(pady=15,padx=100) # Photo
        l.image= photo
        # Entry Box Width
        y = 30
        # Username
        l = Label(self.root,text="Username:",bg="#ffffff").pack(pady=0) # Username Text
        self.e1 = Entry(self.root,width=y)
        self.e1.insert(END,username)
        self.e1.pack(pady=1) # Username Entry
        # IP address
        l = Label(self.root,text="Host:",bg="#ffffff").pack(pady=0) # Host Text
        self.e2 = Entry(self.root,width=y)
        self.e2.insert(END,host)
        self.e2.pack(pady=1) # Host Entry
        # Port
        l = Label(self.root,text="Port:",bg="#ffffff").pack(pady=0)#  Port Text
        self.e3 = Entry(self.root,width=y)
        self.e3.insert(END,port)
        self.e3.pack(pady=1) # Port Entry
        b = Button(self.root,text="Login",command=self.done,padx=y,bg="#ffffff")
        b.pack(pady=0)# Login Button
        self.l = Label(self.root,text="")
        # ---- Pack Widgets ---- #

        self.l.pack(pady=0)
    def done(self):
        if self.data == "":
            port = self.e3.get()
            try:
                port = int(port)
            except ValueError:
                print("!! Invalid port, using 9009")
                port = 9009
            print("Connecting...")
            self.master.username = self.e1.get()
            self.master.host = self.e2.get()
            self.master.port = port
            self.master.server.connect((self.master.host,self.master.port))
            print("...Connected")
        else:
            self.master.username = self.e1.get()
        self.master.server.send(self.master.username.encode())
        self.data = self.master.server.recv(1024).decode()
        if self.data == "TAKEN":
            print("!! Username Taken")
            self.l.configure(text="Username Taken",fg="#af0000",bg="#ffffff")
            self.e1.delete(0,END)
        else:
            self.root.destroy()
            self.master.main()



## -------------- Main  Class -------------- ##
class ClientG:
    def __init__(self,host,port,username):
        # -- Create Variables -- #
        self.host = host
        self.port = port
        self.username = username
        self.server = socket.socket()
        login = LoginWindow(self,host,port,username)
    def main(self):
        # -- Configure Window -- #
        self.root = Tk()
        self.root.configure(bg="#ffffff")
        self.root.bind("<Return>",self.send)
        self.root.title("Chat")
        self.root.protocol('WM_DELETE_WINDOW', self.close) # Intercepts destroy
        # -- Creating Widgets -- #
        self.msg = Listbox(self.root,width=40,bg="#ffffff",fg="#b7b7b7")
        self.msg.pack(pady=5,padx=10)
        self.ent = Entry(self.root,width=40,bg="#ffffff")
        self.ent.pack(padx=10,pady=5)
        for i in range(0,20): # Inserts blank string into first 20 lines so that color loop does not thow back error
            self.msg.insert(END," ")
        self.msg.insert(END,"----- Connected -----")
        threading.Thread(target=self.listen).start()
        threading.Thread(target=self.col).start()
        self.root.mainloop()
    def listen(self):
        print("Started listen loop")
        while True:
            try:
                self.msg.insert(END,self.server.recv(1024))
                self.msg.see(END)
            except:
                print("  - Listen loop closed")
                break
    def col(self):
        print("Started color loop")
        while True:
            try:
                self.msg.itemconfig(int(len(self.msg.get(0,END))-1),fg="#000000")
                self.msg.itemconfig(int(len(self.msg.get(0,END))-2),fg="#000000")
                self.msg.itemconfig(int(len(self.msg.get(0,END))-3),fg="#000000")
                self.msg.itemconfig(int(len(self.msg.get(0,END))-4),fg="#282828")
                self.msg.itemconfig(int(len(self.msg.get(0,END))-5),fg="#3f3f3f")
                self.msg.itemconfig(int(len(self.msg.get(0,END))-6),fg="#595959")
                self.msg.itemconfig(int(len(self.msg.get(0,END))-7),fg="#757575")
                self.msg.itemconfig(int(len(self.msg.get(0,END))-8),fg="#919191")
                self.msg.itemconfig(int(len(self.msg.get(0,END))-9),fg="#b7b7b7")
                self.msg.itemconfig(int(len(self.msg.get(0,END))-10),fg="#b7b7b7")
            except:
                break
        print("  - Color loop closed")
    def send(self,event=None):
        msg = self.ent.get()
        if msg == "/close":
            self.close()
        elif msg != "":
            self.server.send(msg.encode())
            self.msg.insert(END,"Me >"+str(msg))
            self.ent.delete(0,END)
        self.msg.see(END)
    def close(self):
        print("Closing Client...")
        self.root.destroy()
        print("  - Root Destroyed")
        try:
            self.server.close()
            print("  - Server connection closed")
        except:
            print("  - Server connection allready closed")
        print("..done")
        sys.exit()
ClientG("172.19.249.202",9009,"Ed")
