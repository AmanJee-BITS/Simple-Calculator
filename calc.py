from tkinter import*

#creating frame for calculator

def iCalc(source,side):
    storeObj = Frame(source, borderwidth = 4, bd = 4, bg = "powder blue")
    storeObj.pack(side=side, expand = YES, fill = BOTH)
    return storeObj

#creating Button

def button(source, side,text, command = NONE):
    storeObj = Button(source, text = text, command = command)
    storeObj.pack(side=side, expand = YES, fill = BOTH)
    return  storeObj