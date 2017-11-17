import socket
import threading as thread
import time
import sys

## ------------- Functions ------------- ##
def get_host(): # Returns host ip address
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    x = s.getsockname()[0]
    s.close()
    return str(x)

# This takes the server's input
def command():
    def loop():
        global server
        while True:
            x = input()
            if x != "":
                if x == "/shutdown":
                    break
                elif x == "/list":
                    print("**Connected Users**")
                    for name in users:
                        print("  "+str(name))
                else:
                    broadcast("Server",x)
            else:
                pass
            time.sleep(0.3)
        print("\nClosing Server")
        sys.exit()
        server.close()
    thread.Thread(target=loop).start()

def accept(conn):
    def threaded():
        global server
        while True:
            try:
                name = conn.recv(1024).decode()
            except socket.error:
                continue
            if name in users:
                msg = "TAKEN"
                conn.send(msg.encode())
            elif name:
                conn.setblocking(False)
                conn.send("SUCCESS".encode())
                users[name] = conn
                broadcast(name, "+++ %s arrived +++" % name)
                break
    thread.Thread(target=threaded).start()
 
def broadcast(name, message):
    if name != "Server":
        print(message)
    for to_name, conn in users.items():
        if to_name != name:
            try:
                conn.send(message.encode())
            except socket.error:
                pass

## --------------- Setup --------------- ##
HOST = get_host()
PORT = 9009

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.setblocking(False)
server.bind((HOST, PORT))
server.listen(1)
# Pretty output
print("  Host:",HOST,"\n"+" Port:",PORT)
print("----------------------------------")
# Server is running successfully
print("Listening on %s" % ("%s:%s" % server.getsockname()))
command() # Start's listening for commands
server_msg = ""


## ------------- Main Loop ------------- ##
users = {}
while True:
    try:
        while True:
            try: # Try's to accept new connection
                conn, addr = server.accept()
            except socket.error:
                break
            accept(conn)
        for name, conn in users.items(): # For name and socket in users
            try: # Try's to revieve a message
                message = conn.recv(1024).decode()
            except socket.error: # If there is an error in the socket
                continue
            if not message:
                # Empty string is given on disconnect.
                del users[name] #!#!# This is not working #!#!#
                broadcast(name, "--- %s leaves ---" % name)
            else: # Send's message out to clients
                broadcast(name, "%s> %s" % (name, message.strip()))
        time.sleep(.1)
    except (SystemExit, KeyboardInterrupt):
        break
