from tkinter import *
from winreg import OpenKeyEx
from PIL import ImageTk, Image

root = Tk()

root.title("Chu Chu Chatbot")
root.geometry("500x570+100+30")
root.config(bg="blue4")

logoPic=PhotoImage(file="images/bot.jpeg")

logoPicLabel=Label(root,image=logoPic,bg="blue4")
logoPicLabel.pack()

root.mainloop()

