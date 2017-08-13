from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
import re
import Strings

isValidEmail = False

def checkEmail(frame, email, entry):
    pattern = r"[A-Za-z0-9._\-]+@[A-Za-z0-9._\-]+\.[A-Za-z]+"
    isValidEmail = bool(re.search(pattern, email))
    mainStyle = Style(frame)
    mainStyle.configure("Red.TEntry", foreground="red", background="red")
    mainStyle.configure("Black.TEntry", foreground="black", background="black")

    if isValidEmail != True:
        entry.configure(style="Red.TEntry")
    else:
        entry.configure(style="Black.TEntry")


def checkForLogIn():
    if isValidEmail == True:
        tkinter.messagebox.showinfo(Strings.email_valid_title, Strings.email_valid_con)
    else:
        tkinter.messagebox.showwarning(Strings.email_invalid_title, Strings.email_invalid_con)


def navigateToSignOn():
    signOnFrame.tkraise()


def checkForSignOn():
    tkinter.messagebox.showinfo(Strings.sign_on_title, Strings.sign_on_con)


def addLabel(frame, text, rowNo, colNo):
    lbl = Label(frame, text=text)
    lbl.grid(row=rowNo, column=colNo, sticky=W)
    ent = Entry(frame)
    ent.grid(row=rowNo, column=(colNo+1))
    return ent


def addEmail(frame, rowNo, colNo, text=Strings.email_address):
    lblEmail = Label(frame, text=text)
    lblEmail.grid(row=rowNo, column=colNo, sticky=W)
    entEmail = Entry(frame)
    entEmail.bind("<Leave>", lambda email: checkEmail(frame, entEmail.get(), entEmail))
    entEmail.grid(row=rowNo, column=(colNo+1))


def addPassword(frame, rowNo, colNo, text=Strings.password):
    lblPassword = Label(frame, text=text)
    lblPassword.grid(row=rowNo, column=colNo, sticky=W)
    entPassword = Entry(frame, show="*")
    entPassword.grid(row=rowNo, column=(colNo+1))


def addRememberMe(frame, rowNo, colNo):
    rememberValue = IntVar()
    rememberValue.set(1)
    chkRememberMe = Checkbutton(frame, text=Strings.remember, variable=rememberValue)
    chkRememberMe.grid(row=rowNo, column=colNo, columnspan=2)


def addLogIn(frame, rowNo, colNo):
    btnLogIn = Button(frame, text=Strings.log_in, command=checkForLogIn)
    btnLogIn.grid(row=rowNo, column=colNo, sticky=E)


def addCreateAccount(frame, rowNo, colNo):
    btnCreateAccount = Button(frame, text=Strings.create_account, command=lambda:navigateToSignOn())
    btnCreateAccount.grid(row=rowNo, column=colNo, sticky=W)


def addSignOn(frame, rowNo, colNo):
    btnSignOn = Button(frame, text=Strings.sign_on, command=checkForSignOn)
    btnSignOn.grid(row=rowNo, column=colNo, sticky=E)


root = Tk()
root.title(string="Log In Page")

mainFrame = Frame(root)
signOnFrame = Frame(root)

for frame in (mainFrame, signOnFrame):
    frame.grid(row=0, column=0, sticky='news')

addEmail(mainFrame, 1, 0)
addPassword(mainFrame, 2, 0)
addRememberMe(mainFrame, 3, 0)
addLogIn(mainFrame, 4, 1)
addCreateAccount(mainFrame, 4, 0)


addLabel(signOnFrame, Strings.first_name, 0, 0)
addLabel(signOnFrame, Strings.last_name, 1, 0)
addEmail(signOnFrame, 2, 0)
addEmail(signOnFrame, 3, 0, Strings.email_address_valid)
addPassword(signOnFrame, 4, 0)
addPassword(signOnFrame, 5, 0, Strings.password_valid)
addSignOn(signOnFrame, 6, 1)


mainFrame.tkraise()
root.mainloop()
