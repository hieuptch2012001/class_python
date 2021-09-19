1- Create a class called TK_extended which inherits from TK class and having the attributes:

- Master: that represents the name of the main window
- title: that represents the title of the main window

      from tkinter import *

      class TK_extended(Tk):
          def __init__(self, master, title):
              self.master = master
              self.title = title

2 - Create a method called create() that creates the window

    def create(self):
        self.master = Tk()
        self.master.title(self.title)

3 - Create a method called resize(width, height) that can resize the window.

    def resize(self, width, height):
        self.master.geometry(f"{width}x{height}")

4 - Create a method called generate() to generate the window

    def generate(self):
        self.master.mainloop()
