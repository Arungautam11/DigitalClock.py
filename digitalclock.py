from tkinter import*
from PIL import ImageTk,Image
import time
root=Tk()
root.title("Digital Clock by Arun Gautam")
root.geometry("1366x768+0+0")
#root.config(bg="#081923")

#canvas=Canvas(root,width=1366,height=100)
image=ImageTk.PhotoImage(Image.open("D:\\Download Data\\image.png"))
my_label=Label(image=image)
my_label.pack()

def clock():
    h=str(time.strftime("%H"))
    m=str(time.strftime("%M"))
    s=str(time.strftime("%S"))
    #CONFIG THE NOON.
    if int(h)>=12 and int(m)>=0:
        lb1_noon.config(text="PM")
    if int(h)>12:
        h=str((int(h)-12))
        
    lb1_hr.config(text=h)
    lb1_min.config(text=m)
    lb1_sec.config(text=s)

    lb1_hr.after(200,clock)


lb1_hr=Label(root,text="12",font=("times new roman",50,"bold"),bg="#0875B7",fg="white")
lb1_hr.place(x=350,y=200,width=150,height=150)

lb1_hr2=Label(root,text="HOUR",font=("times new roman",20,"bold"),bg="#0875B7",fg="white")
lb1_hr2.place(x=350,y=360,width=150,height=50)

lb1_min=Label(root,text="12",font=("times new roman",50,"bold"),bg="#008EA4",fg="white")
lb1_min.place(x=520,y=200,width=150,height=150)

lb1_min2=Label(root,text="MINUTE",font=("times new roman",20,"bold"),bg="#008EA4",fg="white")
lb1_min2.place(x=520,y=360,width=150,height=50)

lb1_sec=Label(root,text="12",font=("times new roman",50,"bold"),bg="#DF002A",fg="white")
lb1_sec.place(x=690,y=200,width=150,height=150)

lb1_sec2=Label(root,text="SECOND",font=("times new roman",20,"bold"),bg="#DF002A",fg="white")
lb1_sec2.place(x=690,y=360,width=150,height=50)

lb1_noon=Label(root,text="AM",font=("times new roman",50,"bold"),bg="#DF002A",fg="white")
lb1_noon.place(x=860,y=200,width=150,height=150)

lb1_noon2=Label(root,text="NOON",font=("times new roman",20,"bold"),bg="#DF002A",fg="white")
lb1_noon2.place(x=860,y=360,width=150,height=50)

clock()
root.mainloop()