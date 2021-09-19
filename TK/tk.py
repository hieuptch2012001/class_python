from tkinter import *


class TK_extended(Tk):
    def __init__(self, master, title):
        self.master = master
        self.title = title

    def create(self):
        self.master = Tk()
        self.master.title(self.title)

    def resize(self, width, height):
        self.master.geometry(f"{width}x{height}")

    def generate(self):
        self.master.mainloop()


def main():
    hei = int(input("Enter height: "))
    wid = int(input("Enter width: "))

    win = TK_extended("root", "Window")
    win.create()
    win.resize(wid, hei)
    win.generate()


if __name__ == '__main__':
    main()
