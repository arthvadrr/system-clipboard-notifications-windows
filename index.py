from tkinter import *
from tkinter import ttk
import time
import win32clipboard
from playsound import playsound

root = Tk()
frm  = ttk.Frame(root, padding=20)
frm.grid()
ttk.Label(frm, text="System Clipboard Notifications Settings").grid(column=0, row=0)

def getClipboard():
    ttk.Label(frm, text="pre-render").grid(column=0, row=2)    
    ttk.Label(frm, text="render").grid(column=0, row=4)
    listener()

def listener():
    listening = True
    cached_clipboard_text = ''

    while listening:
        win32clipboard.OpenClipboard()
        current_clipboard_text = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()

        if current_clipboard_text != cached_clipboard_text:
            cached_clipboard_text = current_clipboard_text
            playsound('audio/copied.mp3')
            print('copied')
        time.sleep(0.5)

getClipboard()
root.mainloop()