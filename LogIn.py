from tkinter import *
from tkinter.ttk import *
import Controls
import Strings

root = Tk()
root.title(string="Log In Page")
mainFrame = Frame(root)

Controls.addEmail(mainFrame, 1, 0)
Controls.addPassword(mainFrame, 2, 0)
Controls.addRememberMe(mainFrame, 3, 0)
Controls.addLogIn(mainFrame, 4, 1)

mainFrame.pack()
root.mainloop()