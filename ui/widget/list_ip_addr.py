from tkinter import Frame, Listbox, Label, LEFT, BOTH, W

from net.arp import ARPScanner


class ListIpAddrWidget(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.listbox = Listbox(self, height=10,
                               width=30,
                               bg="white",
                               activestyle='dotbox',
                               font="Helvetica",
                               fg="black")

        self.label = Label(self, text="IP List", anchor=W, justify=LEFT)
        self.label.pack(fill=BOTH)
        for idx, n in enumerate(ARPScanner().all()):
            self.listbox.insert(idx, n.to_string())
        self.listbox.pack()
