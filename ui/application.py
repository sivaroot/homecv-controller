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

    def create_widgets(self):
        self.label_input_url = Label(self, text="Camera URL")
        self.label_input_url.pack(side="left")
        self.label_input_url.grid(row=0, column=0, sticky=W, pady=2)
        self.input_url = Entry(self, width=20)
        self.input_url.bind('<Return>', self.say_hi)
        self.input_url.grid(row=0, column=1)
        self.button_submit_url = Button(
            self, text="Scan", width=20, command=self.say_hi)
        self.button_submit_url.grid(row=0, column=2)

    def say_hi(self, event):
        print(self.input_url.get())
