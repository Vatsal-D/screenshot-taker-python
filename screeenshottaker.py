from ctypes import alignment
from turtle import Screen
from isort import place_module
import pyautogui
import tkinter as tk
from  tkinter.filedialog import *

window=tk.Tk()
window.configure()
a=tk.Canvas(window,width=150,height=150)
a.pack()
def ScreenShot():
    scrshot=pyautogui.screenshot()
    image=asksaveasfilename()
    scrshot.save(image+" ss.png")

b=tk.Button(text="Click Me",command=ScreenShot)
a.create_window(75,75,window=b)
window.mainloop()