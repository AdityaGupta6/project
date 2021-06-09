import tkinter
import cv2
import PIL.Image,PIL.ImageTk
from functools import partial
import threading
import imutils
import time

stream=cv2.VideoCapture("clip.mp4")
flag=True
def play(speed):
    global flag
    # print(f"You clicked on play . Speed is {speed}")
    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)
    
    grabbed, frame=stream.read()
    if not grabbed:
        exit()

    frame=imutils.resize(frame,width=Set_WIDTH,height=Set_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    if flag:
        canvas.create_text(132,25,fill="black",font="Times 26 bold",text="Decision pending")
    flag=not flag

def pending(decision):
    # display decision pending image
    frame=cv2.cvtColor(cv2.imread("pending.png"), cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=Set_WIDTH,height=Set_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    # wait for 1 sec 
    time.sleep(1)
    # display seponser image
    frame=cv2.cvtColor(cv2.imread("sponsor.png"), cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=Set_WIDTH,height=Set_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    # wai 1.5 sec
    time.sleep(1.5)
    # display out or not out image
    if decision == 'out':
        decisionImg="out.png"
    else:
        decisionImg="not_out.png"
    
    frame=cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=Set_WIDTH,height=Set_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

def out():
    thread=threading.Thread(target=pending,args=("out",))
    thread.daemon=1
    thread.start()
    # print("Player is out")

def not_out():
    thread=threading.Thread(target=pending,args=("not out",))
    thread.daemon=1
    thread.start()

    # print("Player is not out")


# width and height of our screen
Set_WIDTH=650
Set_HEIGHT=368

# tinter gui starts here
window=tkinter.Tk()
window.title("Third empire decision reveiew system")
cv_img=cv2.cvtColor(cv2.imread("welcome.png"), cv2.COLOR_BGR2RGB)
canvas=tkinter.Canvas(window,width=Set_WIDTH, height=Set_HEIGHT)
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))

image_on_canvas=canvas.create_image(0,0,ancho=tkinter.NW,image=photo)
canvas.pack()

# buttons to control playback
btn=tkinter.Button(window, text="<< previous (fast)",width=50,command=partial(play,-5))
btn.pack()
btn=tkinter.Button(window, text="<< previous (slow)",width=50,command=partial(play,-2))
btn.pack()
btn=tkinter.Button(window, text=" Next (fast)>>",width=50,command=partial(play,5))
btn.pack()
btn=tkinter.Button(window, text=" Next (slow)>>",width=50,command=partial(play,2))
btn.pack()
btn=tkinter.Button(window, text="Give out",width=50,command=out)
btn.pack()
btn=tkinter.Button(window, text="Give not out",width=50,command=not_out)
btn.pack()

window.mainloop()




















































































































































































