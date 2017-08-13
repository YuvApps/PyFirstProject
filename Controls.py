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

def checkForSignOn():
    tkinter.messagebox.showinfo(Strings.signed_on_title, Strings.signed_on_con)

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

def addSignOn(frame, rowNo, colNo):
    btnSignOn = Button(frame, text=Strings.sign_on, command=checkForSignOn)
    btnSignOn.grid(row=rowNo, column=colNo, sticky=E)
