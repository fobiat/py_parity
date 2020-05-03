#req, pillow for image, pip install pillow 
# import tkinter
from tkinter import *
# import menu module
from tkinter import Menu
# import webbrowser module
import webbrowser
# import logo module
from PIL import Image
from PIL import ImageTk

#set variables
url = 'http://github.com/thattkyle/py_parity'
#open website for user help
def openwebsite():
    webbrowser.open_new(url)

#def logo(self):
#    self.img = ImageTk.PhotoImage(Image.open("logo.png"))
#def logo():
#    load = image.open("logo.png")
#    render = imageTK.PhotoImage(load)
#    img = Label(self, image=render)
#    img.image = render
#    img.place(x=0, y=0)

#set main.window
window = Tk()
#set window.size
window.geometry("750x300")
#set window.title
window.title("pyParity")

#create menu
menu = Menu(window)
menu.help = Menu(menu, tearoff=0)
menu.help.add_command(label="Help", command = openwebsite)
menu.help.add_command(label="Quit", command = menu.quit)
menu.add_cascade(label='File', menu=menu.help)

#create logo
load = Image.open("logo.png")
render = ImageTk.PhotoImage(load)
img = Label(self, image=render)
img.image = render
img.place(x=0, y=0)



window.config(menu=menu)
window.mainloop()