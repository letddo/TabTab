from tkinter import *
import keyboard
import time
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


root = Tk() 
root.title("taptap")
root.geometry("250x250")
root.minsize(width=250, height=250)
root.maxsize(width=250, height=250)
root.wm_attributes('-transparentcolor', 'green', '-topmost', '1')
# 투명화&최상위 

image_mode = "1" # 1, 2, 3
image = PhotoImage(file=resource_path(image_mode+"\img1.png"))
canvas = Canvas(root, bg="green")
canvas.pack()
canvas.create_image(0,0, image=image, anchor=NW)

pngn=1

def off_key_press():
    image.config(file=resource_path(image_mode+"\img1.png"))
    
def on_key(event):
    global pngn
    if (pngn == 1):
        image.config(file=resource_path(image_mode+"\img2.png"))
        pngn = 0
    else:
        image.config(file=resource_path(image_mode+"\img3.png"))
        pngn = 1
    root.after(100, off_key_press)

def do_popup(event):
    try:
        menubar.tk_popup(event.x_root, event.y_root)
    finally:
        menubar.grab_release()
        
def change_1():
    global image_mode
    image_mode = "1"
    image.config(file=resource_path(image_mode+"\img1.png"))

def change_2():
    global image_mode
    image_mode = "2"
    image.config(file=resource_path(image_mode+"\img1.png"))

def change_3():
    global image_mode
    image_mode = "3"
    image.config(file=resource_path(image_mode+"\img1.png"))
    

menubar = Menu(root, tearoff=0)
menubar.add_command(label="1", command=change_ritsulazy)
menubar.add_command(label="2", command=change_ritsuwork)
menubar.add_command(label="3", command=change_ritsusmoi)

keyboard.on_press(on_key)
root.bind("<Button-3>", do_popup)
# 우클릭 팝업창

mainloop()
