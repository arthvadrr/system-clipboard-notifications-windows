from   tkinter   import *
from   tkinter   import ttk
from   playsound import playsound
from   PIL import Image, ImageDraw
import win32clipboard
import pystray
import time

# root = Tk()
# root.protocol("WM_DELETE_WINDOW", root.iconify)
# root.mainloop()

# frm  = ttk.Frame(root, padding=20)
# frm.grid()
# ttk.Label(frm, text="System Clipboard Notifications Settings").grid(column=0, row=0)

def scnw_init():
    # ttk.Label(frm, text="pre-render").grid(column=0, row=2)    
    # ttk.Label(frm, text="render").grid(column=0, row=4)
    scnw_systray()
    scnw_listener()

def scnw_listener():
    listening = True
    cached_clipboard_text = ''

    while listening:
        win32clipboard.OpenClipboard()
        current_clipboard_text = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()

        if current_clipboard_text != cached_clipboard_text:
            cached_clipboard_text = current_clipboard_text
            playsound('audio/copied.mp3')
        time.sleep(0.5)

def create_image(width, height, color1, color2):
    image = Image.new('RGB', (width, height), color1)
    drawn = ImageDraw.Draw(image)
    drawn.rectangle((width // 2, 0, width, height // 2), fill=color2)
    drawn.rectangle((0, height // 2, width // 2, height), fill=color2)
    return image

def scnw_systray():
    icon = pystray.Icon('Clipboard Notifications Settings', icon=create_image(64, 64, 'black', 'white'))
    icon.run()

scnw_init()