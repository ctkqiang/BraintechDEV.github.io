#!/usr/bin/env python3
######################################
# BRAINTECH PRIVATE LIMITED
# JOHN MELODY MELISSA
######################################
# यह स्क्रिप्ट John Melody द्वारा लिखा गया है।
# PYTHON में पूरी तरह  से द्वारा संचालित. सभी
# अधिकार सुरक्षित |  इस स्क्रिप्ट का कोई भी
# हिस्सा अनधिकृत पार्टी द्वारा
# पुनरुत्पादित किया जा सकता है।
######################################
import tkinter
from tkinter import ttk, Menu
from tkinter import *
import serial
import serial.tools.list_ports
import os

# Windows Configuration ::
window = tkinter.Tk()
window.title("Braintech Braiwave Monitor")
window.geometry("1400x700")
window.iconbitmap("icon.ico")
window.config(bg="white")

# Menubar Configuration ::
Menubar = Menu(window)
window.config(menu=Menubar)
window.resizable(True, True)

# Menubar Functions ::
# FileMenu declaration ::
fileMenu = Menu(Menubar, tearoff=0)
fileMenu.add_command(label="New (N)")
fileMenu.add_separator()
fileMenu.add_command(label="Quit (Q)", command=window.destroy)
Menubar.add_cascade(label="File", menu=fileMenu)
Menubar.add_cascade(label="Edit")

# Window Menu ::
def dmgr():
    os.system("devmgmt.msc")

def textEditor():
    import notepad as texteditor
    return textEditor()

def terminal():
    os.system("start terminal.py")

WindowMenu = Menu(Menubar, tearoff=0)
WindowMenu.add_command(label="Text Editor (K)", command=textEditor)
WindowMenu.add_command(label="Braintech Terminal (B) ", command=terminal)
WindowMenu.add_command(label="Device Manager (D)", command=dmgr)
Menubar.add_cascade(label="Window", menu=WindowMenu)

# Pereference Menu ::
def themeDark():
    window.configure(background="#2B1B17")
    return

PereferenceMenu = Menu(Menubar, tearoff=0)
Themes = Menu(PereferenceMenu, tearoff=0)
Themes.add_command(label="Night Theme", command=themeDark)
PereferenceMenu.add_cascade(label="Themes (T) \t ", menu=Themes)
Menubar.add_cascade(label="Pereferences", menu=PereferenceMenu)

# Help Menu ::
def credit():
    import credit as software_creditnm
    software_credit()

HelpMenu = Menu(Menubar, tearoff=0)
HelpMenu.add_command(label="About (I) ", command=credit)
Menubar.add_cascade(label="Help", menu=HelpMenu)

##====================================================================================##
# Main Function ::
Serial_Port_Communication_LF = LabelFrame(window, text="Electroencephalography Monitor")
Serial_Port_Communication_LF.pack(fill="both", expand="yes")


window.mainloop()