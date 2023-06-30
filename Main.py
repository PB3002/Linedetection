from tkinter import * 
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog as fd
import cv2
import numpy as np

win = Tk()
frame = Frame(win).pack(side=tk.BOTTOM,padx=15,pady=15)
win.title("Tìm đường thẳng")
win.geometry('800x600') 

lbl = Label(win)
lbl.pack()

def browse_image():
    global new_image
    win.filename = fd.askopenfilename(title="Chọn ảnh", filetypes=(('image files', ('.png', '.jpg')),("all files","*.*")))
    my_image = Image.open(win.filename)
    resized = my_image.resize((600,400),Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized)
    lbl.configure(image=new_image)
    lbl.image=new_image

def HoughLine():
    img1 = cv2.imread(win.filename)
    gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    canimg = cv2.Canny(gray, 50,150,apertureSize=3)

    lines = cv2.HoughLines(canimg, rho=1, theta=np.pi/180, threshold=thanhtruot.get())

    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a)) 

        cv2.line(img1,(x1,y1),(x2,y2),(0,0,255),2)    

    cv2.imwrite(r'Output/hough.jpg',img1)
    cv2.imwrite(r'./Output/Canny.jpg',canimg)
    my_image = Image.open(r"Output/hough.jpg")
    resized = my_image.resize((600,400),Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized)
    lbl.configure(image=new_image)
    lbl.image=new_image


def tangthanhtruot():
    thanhtruot.set(thanhtruot.get()+50)

def giamthanhtruot():
    thanhtruot.set(thanhtruot.get()-50)


tangslider=Button(win,text=">",command=tangthanhtruot)
tangslider.place(height=25,relx=0.6,rely=0.74,anchor=CENTER)

giamslider=Button(win,text="<",command=giamthanhtruot)
giamslider.place(height=25,relx=0.4,rely=0.74,anchor=CENTER)

thanhtruot= Scale(win, from_=100,to=1000,orient=HORIZONTAL)
thanhtruot.place(relx=0.5,rely=0.73,anchor=CENTER)

nut_chonanh = Button(win,text="Chọn ảnh",command=browse_image)
nut_chonanh.place(relx=0.5,rely=0.8,anchor=CENTER)

nut_timline = Button(win,text="Tìm đường thẳng",command=HoughLine)
nut_timline.place(relx=0.5,rely=0.85,anchor=CENTER)

nut_thoat = Button(win,text="Thoát", command=lambda:exit())
nut_thoat.place(relx=0.5,rely=0.9,anchor=CENTER)

win.mainloop()

