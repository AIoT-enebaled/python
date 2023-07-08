from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("400x400")
root.config(bg="grey")
root.resizable(False, False)

Label_result = StringVar()
Label_result.set("")

Label(root, text="Calculator", font=("Arial", 20, "bold"), bg="grey").place(x=150, y=10)
Label(root, textvariable=Label_result).pack()

Button(root, text="1", font=("Arial", 20, "bold"), bg="grey").place(x=10, y=100)

root.mainloop()
