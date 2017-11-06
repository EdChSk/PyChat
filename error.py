from tkinter import *
import socket
import time
import random
import threading

class ErrorWindow():
    def __init__(self,msg):
        print("Building Error Window")
        root = Tk()
        self.root = root
        root.configure(bg="#ffffff")
        root.title("Error!")
        l = Label(root,text="Unexpected Error:",bg="#ffffff",fg="red").pack(padx=30)
        l = Label(root,text=msg,bg="#ffffff").pack(pady=5,padx=5)
        b = Button(root,text="Exit",bg="#ffffff",command=self.close).pack(pady=10)
    def close(self):
        print("Closing Error window")
        self.root.destroy()
