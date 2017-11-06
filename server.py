from tkinter import *
import socket
import time
import random
import threading
import sys
import select

class Server():
    def __init__(self,typ,master,window=None):
        self.go = True
        self.master = master
        if typ == "client":
            self.serv = False
            self.go = True
            print("[Creating Server Client.....")
            print(".....Server client created]")
            self.ip = self.master.master.master.ip
            self.port = self.master.master.master.port
            self.sock = socket.socket()
            try:
                self.sock.connect((self.ip,self.port))
                print("###### Connected ######")
            except:
                print("#######################")
                print("######## Error ########")
                print("   Unable to connect   ")
                print("#######################")
                print("#######################")
                self.master.master.root.destroy()
        else:
            self.serv = True
            print("[Setting Up Server.....")
            print("  Getting Host and Port information...")
            self.root = window
            self.root.bind("<Return>",self.sendmsg)
            self.HOST = self.get_host()
            self.SOCKET_LIST = []
            self.RECV_BUFFER = 4096
            self.PORT = 9009
            print("  ...Done")
            self.name_list = []
            self.msg = ["","","","","","","",""]
            print("  Starting chat server...")
            self.chat_server()
    def client_loop2(self):
        print("  Listening Loop Started")
        while True:
            if self.go == False:
                break
            try:
                data = self.sock.recv(1024).decode()
            except:# If server is closed
                break
            if "%%d" in data:
                print("A Client Disconnected")
                name = data[data.index("%%d")+4:]
                self.master.master.master.messages.append("["+str(name)+"]Disconnected")                
            else:
                while len(data) > 55:
                    self.master.master.master.messages.append(data[:55])
                    data = data[55:]
                self.master.master.master.messages.append(data)
            
        print("   ...Client Loop #2 Closed")
    def client_loop(self):
        print("  Client Loop Started...")
        while self.go == True:
            try:
                self.master.l1.configure(text=self.master.master.master.messages[len(self.master.master.master.messages)-1])
                self.master.l2.configure(text=self.master.master.master.messages[len(self.master.master.master.messages)-2])
                self.master.l3.configure(text=self.master.master.master.messages[len(self.master.master.master.messages)-3])
                self.master.l4.configure(text=self.master.master.master.messages[len(self.master.master.master.messages)-4])
                self.master.l5.configure(text=self.master.master.master.messages[len(self.master.master.master.messages)-5])
                self.master.l6.configure(text=self.master.master.master.messages[len(self.master.master.master.messages)-6])
                self.master.l7.configure(text=self.master.master.master.messages[len(self.master.master.master.messages)-7])
                self.master.l8.configure(text=self.master.master.master.messages[len(self.master.master.master.messages)-8])
                time.sleep(0.05)
            except:
                if self.go == False:
                    break
                else:
                    time.sleep(1)
            if self.go == False:
                break
        print("   ...Client Loop #1 Closed")
    def send(self,event=None,message=None):
        if message != None:
            self.sock.send(message.encode())
        else:
            x = self.master.ent.get()
            if x == "/fullscreen":
                self.master.maxmin()
            elif x == "/clean":
                self.master.master.master.messages = ["","","","","","","",""]
            elif x == "/help":
                self.master.master.master.messages.append("Possable Commands:")
                self.master.master.master.messages.append(" - /fullscreen")
                self.master.master.master.messages.append(" - /help")
                self.master.master.master.messages.append(" - /clean")
                self.master.master.master.messages.append(" - /exit")
            elif x == "/exit":
                print("Closing Connection to Server...")
                msg = "%%d "+str(self.master.master.master.username)
                self.sock.send(msg.encode())
                self.sock.close()
                print("  Sent Closing Message To Server")
                self.go = False
                print("  Stopped running threads")
                self.master.root.destroy()
                print("  Destroyed main window")
            else:
                if len(x) > 275:
                    print("Message Too Long Try Sendng A Shorter Message")
                    self.master.master.master.messages.append("## Message Too Long ##")
                else:
                    if len(x) > 55:
                        b = "[Me]: " + str(x)
                        while len(b) > 55:
                            self.master.master.master.messages.append(b[:55])
                            b = b[55:]
                        self.master.master.master.messages.append(b)
                    else:
                        self.master.master.master.messages.append("[Me]: "+ x)
                    data = "["+self.master.master.master.username+"] " + x
                    print("Sending: "+data)
                    self.sock.send(data.encode())
            try:
                self.master.ent.delete(0,END)
            except: # Root has been destroyed
                pass
    def get_host(self): # Returns host ip address
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(("8.8.8.8",80))
        x = s.getsockname()[0]
        s.close()
        return str(x)
    def chat_server(self):
        HOST = self.HOST
        PORT = self.PORT
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket= server_socket
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(10)

        # Add server objects to list of readable connections
        self.SOCKET_LIST.append(server_socket)
        # Return sucess to console
        msg = "Server now listening on "+str(HOST)+":"+str(PORT)+" at "+time.strftime("%H:%M:%S")# 55 char long       
        self.master.msg.append(msg)
        self.master.done = True
        while 1:
            ready_to_read,ready_to_write,in_error = select.select(self.SOCKET_LIST,[],[],0)
            for sock in ready_to_read:
                # New connection request
                if sock == server_socket:
                    sockfd, addr = server_socket.accept()
                    self.SOCKET_LIST.append(sockfd)
                    self.master.msg.append("["+time.strftime("%H:%M:%S")+"] Client Connection From (%s, %s)" % addr)
                    self.broadcast("[%s:%s] entered our chatting room" % addr, sockfd)
                # a message from a client, not a new connection
                else:
                    #print("Data not client connection")
                    try:
                        # receiving data from the socket.
                        data = sock.recv(1024).decode()
                        if data:
                            # there is something in the socket
                            #print("Recieved Data")
                            if data[0:3] == "%%u":
                                self.name_list.append(data[4:])
                            else:
                                if len(data) < 55:
                                    self.master.msg.append(data)
                                else:
                                    b = data
                                    print("Recieved long message")
                                    while len(b) > 55:
                                        self.master.msg.append(b[:55])
                                        b = b[55:]
                                    self.master.msg.append(b)
                                broadcast(str(data),sock)  
                        else:
                            #print("Recieved no data")
                            # remove the socket that's broken    
                            if sock in SOCKET_LIST:
                                self.SOCKET_LIST.remove(sock)
                    except:
                        ##broadcast(server_socket, sock, "Client (%s, %s) is offline" % addr)
                        continue
            if self.go == False:
                break
        try:
            server_socket.close()
        except:
            pass
    def broadcast (self,message,sock=None):
        if sock != None:
            print("Sock != None")
            for socket in self.SOCKET_LIST:
                # send the message only to peer
                if socket != self.server_socket and socket != sock :
                    try:
                        socket.send(message)
                    except:
                        # broken socket connection
                        socket.close()
                        if socket in self.SOCKET_LIST:
                            self.SOCKET_LIST.remove(socket)
                else:
                    continue
            if self.serv == True:
                self.master.msg.append(message)
        else:
            print("Socket == None")
            for socket in self.SOCKET_LIST:
                try:
                    socket.send(message)
                except:
                    socket.close()
                    if socket in self.SOCKET_LIST:
                        self.SOCKET_LIST.remove(socket)
    def sendmsg(self,event=None,message=None):
        if message == None:
            message = self.master.ent.get()
            self.master.ent.delete(0,END)
        if message[0] == "/":
            message = message[1:]
            if message == "help":
                self.master.msg.append("## Help 1/1 ##")
                self.master.msg.append("  - fullscreen")
                self.master.msg.append("  - clean")
                self.master.msg.append("  - list")
                self.master.msg.append("  - host # Gives IP")
                self.master.msg.append("  - export [filename]# Exports chat")
                self.master.msg.append("  - close")
            elif message == "clean":
                for i in range(0,8):
                    self.master.msg.append("")
            elif message == "fullscreen":
                self.master.maxmin()
            elif message == "close":
                print("Closing Server...")
                self.master.msg.append("## SERVER CLOSED ##")
                for socket in self.SOCKET_LIST:
                    if socket != self.server_socket:
                        message = "%%d SERVER CLOSED"
                        socket.send(message.encode())
                print("   Closing Message Sent To All Connected Clients")
                self.go = False
                self.master.go = False
                print("   All Threads Stopped")
                try:
                    self.server_socket.close()
                    print("   Server Socket Closed")
                except:
                    print("  Server Socket Allready Closed")
                self.master.master.root.destroy()
                print("  Main Window Closed")
                print("...Done")
            elif message == "list":
                print(self.name_list)
                self.master.msg.append("## Connected Users ##")
                self.master.msg.append("   - {SERVER}")
                for user in self.name_list:
                    self.master.msg.append("   - "+user)
            elif message == "host":
                self.master.msg.append("## IP: ["+str(self.HOST)+"] ##")
            elif message[0:6] == "export":
                fName = message[7:]
                f = open(fName+'.txt','w')
                print("Exporting:\n"+str(self.master.msg[8:])+" ...")
                f.write(self.master.msg[8]+"\n")
                for i in self.master.msg[9:]:
                    f.write("  "+i+"\n")
                f.close()
                print("... Done")
            else:
                self.master.msg.append("## Unknown Command: "+str(message)+" ##")
        else:
            message = "{Admin} "+str(message)
            if len(message) > 255:
                print("## Message Too Long ##")
                self.master.msg.append("## Message Too Long ##")
            else:
                if len(message) > 55:
                    b = message
                    while len(b) > 55:
                        self.master.msg.append(b[:55])
                        b = b[55:]
                    self.master.msg.append(b)
                else:
                    self.master.msg.append(message)
                for socket in self.SOCKET_LIST:
                    if socket != self.server_socket:
                        socket.send(message.encode())
    def kill(self):
        self.server_socket.close()
