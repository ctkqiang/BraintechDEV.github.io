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
from tkinter import ttk, Image
from tkinter import *


# Windows Configuration ::
window = tkinter.Tk()
window.title("Braintech Braiwave Monitor")
window.geometry("560x210+550+300")
window.iconbitmap("icon.ico")
window.resizable(False, False)
window.attributes("-fullscreen", "false")

outter_layer_frame = LabelFrame(window, text="Credits")
outter_layer_frame.pack(fill="both", expand="yes")

#braintech_logo = PhotoImage(file="icon.png")
#braintech_logo_RESIZED = braintech_logo.subsample(3,3)
#Label(outter_layer_frame, image=braintech_logo_RESIZED).pack(side=TOP)

inner_layer_label = Label(outter_layer_frame, text="\n\n Braintech Brainwave Monitor" +
        " (Community Edition) \n\n POWERED BY PYTHON \n\n John@braintechgroup.com \n Copyright (C) BRAINTECH SDN BHD MALAYSIA")

inner_layer_label_donation = Label(outter_layer_frame, text="Donate : https://www.paypal.me/johnmelody ")
inner_layer_label.pack()
inner_layer_label_donation.pack()
window.mainloop()