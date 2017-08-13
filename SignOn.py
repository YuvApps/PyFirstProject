from tkinter import *
from tkinter.ttk import *
import Controls
import Strings

Controls.addLabel(Controls.signOnFrame, Strings.first_name, 0, 0)
Controls.addLabel(Controls.signOnFrame, Strings.last_name, 1, 0)
Controls.addEmail(Controls.signOnFrame, 2, 0)
Controls.addEmail(Controls.signOnFrame, 3, 0, Strings.email_address_valid)
Controls.addPassword(Controls.signOnFrame, 4, 0)
Controls.addPassword(Controls.signOnFrame, 5, 0, Strings.password_valid)
Controls.addSignOn(Controls.signOnFrame, 6, 1)