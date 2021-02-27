import tkinter as tk
from ui import application as ui


def main():
    root = tk.Tk()
    app = ui.Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
