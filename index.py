from tkinter import *
from tkinter import ttk
import win32clipboard
from playsound import playsound

root = Tk()
frm  = ttk.Frame(root, padding=20)
frm.grid()
ttk.Label(frm, text="System Clipboard Notifications Settings").grid(column=0, row=0)

def getClipboard():
    win32clipboard.OpenClipboard()
    clipboardText = win32clipboard.GetClipboardData()
    
    ttk.Label(frm, text="pre-render").grid(column=0, row=2)    
    ttk.Label(frm, text=clipboardText).grid(column=0, row=3)
    ttk.Label(frm, text="render").grid(column=0, row=4)
    playsound('audio/copied.mp3')
getClipboard()
root.mainloop()