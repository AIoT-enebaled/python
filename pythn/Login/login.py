import filecmp
from tkinter import *
from winreg import OpenKeyEx
from PIL import ImageTk, Image

def closeye(e):
    eyeButton.config(images=closeye)

def user_enter(e):
    if usernameEntry.get() == "Username":
        usernameEntry.delete(0, END)
        usernameEntry.config(fg="black")

def password_enter(e):
    if passwordEntry.get() == "Password":
        passwordEntry.delete(0, END)
        passwordEntry.config(fg="black")

def hide():
    if passwordEntry['show'] == '*':
        passwordEntry.config(show="")
        eyeButton.config(images=closeye)
    else:
        passwordEntry.config(show="*")
        eyeButton.config(images=openeye)

login_wondow = Tk()

login_wondow.resizable(width=False, height=False)

login_wondow.geometry("990x660+50+50")

bgImage=ImageTk.PhotoImage(Image.open("images/bg.jpg"))

bgLabel=Label(login_wondow,image=bgImage)

bgLabel.grid (row=0,column=0,columnspan=3)
bgLabel.place(x=0,y=0)

heading=Label(login_wondow,text="USER LOGIN",font=("Microsoft Yahei UI Light", 23, 'bold'),
              fg="firebrick1",bg="#FFFFFF")
heading.place(x=590,y=115)

usernameEntry=Entry(login_wondow,font=("Microsoft Yahei UI Light", 11, 'bold'),fg="firebrick1",bd="0")
usernameEntry.place(x=590,y=200)
usernameEntry.insert(0,"Username")

usernameEntry.bind("<FocusIn>",user_enter)

frame1=Frame(login_wondow,width=250,height=2,bg="firebrick1")
frame1.place(x=590,y=220)

passwordEntry=Entry(login_wondow,font=("Microsoft Yahei UI Light", 11, 'bold'),fg="firebrick1",bd="0")
passwordEntry.place(x=590,y=250)
passwordEntry.insert(0,"Password")

passwordEntry.bind("<FocusIn>",password_enter)

frame2=Frame(login_wondow,width=250,height=2,bg="firebrick1")
frame2.place(x=590,y=270)



openeye=ImageTk.PhotoImage(Image.open("images/openeye.png"))
closeeye=ImageTk.PhotoImage(Image.open("images/closeye.png"))
eyeButton=Button(login_wondow,image=openeye,bd="0",bg="#FFFFFF", cursor="hand2",command=hide)
eyeButton.place(x=814,y=243)


login_wondow.mainloop()
