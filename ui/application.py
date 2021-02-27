import tkinter as tk
from tkinter import Label, W, Entry, Button, Listbox, Frame, LEFT
from net.arp import ARPScanner
from ui.widget.list_ip_addr import ListIpAddrWidget
class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("1024x600")
        self.list_box_ip_addr = ListIpAddrWidget(self)
        self.list_box_ip_addr.pack()
        self.pack(side="left", fill="both")

    def say_hi(self, event):
        print(self.input_url.get())
