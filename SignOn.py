from tkinter import *
from tkinter.ttk import *
import Controls
import Strings

root = Tk()
root.title(string="Sign On Page")
mainFrame = Frame(root)

Controls.addLabel(mainFrame, Strings.first_name, 0, 0)
Controls.addLabel(mainFrame, Strings.last_namem, 1, 0)
Controls.addEmail(mainFrame, 2, 0)
Controls.addEmail(mainFrame, 3, 0, Strings.email_address_valid)
Controls.addPassword(mainFrame, 4, 0)
Controls.addPassword(mainFrame, 5, 0, Strings.password_valid)
Controls.addSignOn(mainFrame, 6, 1)

mainFrame.pack()
root.mainloop()
