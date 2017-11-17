import socket, sys, time, select, threading, os
from tkinter import *
## ------------ Pretty  Opening ------------ ##
print("  ___       ___ _         _   \n | _ \_  _ / __| |_  __ _| |_ \n |  _/ || | (__| ' \/ _` |  _|\n |_|  \_, |\___|_||_\__,_|\__|\n      |__/                 v0\n")


## --------------- Functions --------------- ##
def helpwin():
    print("Usage: python main.py <command> [<args>]\n\nAvailable commands are:")
    print("  -s                     Selects server mode")
    print("  -c                     Selects client mode")
    print("  -cg                    Selects GUI client mode")
    print("  --port <port>          Port to connect/host with")
    print("  --host <host>          Host to connect/host with")
    print("  --username <username>  Enter username for client only")
    print("  -h                     Displays help information")
    print("\n(If multiple modes are selected the last one typed is used)")
    sys.exit()
def get_host(): # Returns host ip address
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    x = s.getsockname()[0]
    s.close()
    return str(x)


## --------------- Arguments --------------- ##
mode = ""
port = 0
host = ""
username = ""
args = sys.argv[1:]
for arg in args:
    if arg == "-h":
        helpwin()
    elif arg == "-s":
        mode = "Server"
    elif arg == "-c":
        mode = "Client"
    elif arg == "-cg":
        mode = "ClientG"
    elif arg == "--port":
        port = args[args.index(arg)+1]
        args.remove(args[args.index(arg)+1])
    elif arg == "--host":
        host = args[args.index(arg)+1]
        args.remove(args[args.index(arg)+1])
    elif arg == "--username":
        username = args[args.index(arg)+1]
        args.remove(args[args.index(arg)+1])
    else:
        if arg[0] == "-":
            print("***Unknown Command***")
            helpwin()

if mode == "": # Mode not entered
    mode = input("Please enter mode: Client/Server\n  >")
    while mode != "Client" or mode != "Server":
        print("***Unkown Mode***")
        mode = input("Please enter mode: Client/Server\n  >")
if host == "" and mode == "Server": # Host = Computer IP because computer is server
    host = get_host()
elif host == "" and mode == "Client": # Ask Host
    host = input("Enter host to connect to: (IP)\n  >")
if port == 0 and mode != "ClientG":
    print("!! Using program default port 9009")
else:
    try:
        port = int(port)
    except ValueError: # They typed a string :P
        port = 9009
        print("!! Invalid port given, using program default 9009")


## ------------- Main  Program ------------- ##
if mode == "Server":
    print("------ Server Mode Selected ------")
    cc = __import__("server")
    server = cc.Server()
    server.main_method()
elif mode == "Client":
    print("------ Client Mode Selected ------")
    cc = __import__("client")
    client = cc.Client(host,port,username) # get_host needs replacing for server addr
else:
    print("---- Client GUI Mode Selected ----")
    cc = __import__("clientG")
    login = cc.ClientG(host,port,username)
    sys.exit()
