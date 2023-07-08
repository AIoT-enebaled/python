from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("570x600+100+200")
root.config(bg="#17161b")
root.resizable(False, False)

Label_result = StringVar(Label(root, text="", font=("Arial", 20, "bold"), bg="grey", bd=10, width=28, justify=RIGHT))
Label_result.set("")


Label(root, text="Calculator", font=("Comic Sans MS", 20, "bold"), bg="grey").place(x=150, y=20)
Label(root, textvariable=Label_result).pack()

Button(root, text="C", font=("Arial", 20, "bold"), bg="grey").place(x=10, y=100)
Button(root, text="CE", font=("Arial",20, "bold"), bg="orange").place(x=100, y=100)
Button(root, text="%", font=("Arial", 20, "bold"), bg="grey").place(x=190, y=100)
Button(root, text="/", font=("Arial", 20, "bold"), bg="grey").place(x=280, y=100)
Button(root, text="*", font=("Arial", 20, "bold"), bg="grey").place(x=10, y=170)
Button(root, text="-", font=("Arial", 20, "bold"), bg="grey").place(x=100, y=170)
Button(root, text="+", font=("Arial", 20, "bold"), bg="grey").place(x=280, y=170)

Button(root, text="7", font=("Arial", 20, "bold"), bg="grey").place(x=10, y=240)
Button(root, text="8", font=("Arial", 20, "bold"), bg="grey").place(x=100, y=240)
Button(root, text="9", font=("Arial", 20, "bold"), bg="grey").place(x=190, y=240)
Button(root, text="4", font=("Arial", 20, "bold"), bg="grey").place(x=10, y=310)
Button(root, text="5", font=("Arial", 20, "bold"), bg="grey").place(x=100, y=310)
Button(root, text="6", font=("Arial", 20, "bold"), bg="grey").place(x=190, y=310)


Button(root, text="1", font=("Arial", 20, "bold"), bg="grey").place(x=10, y=380)
Button(root, text="2", font=("Arial", 20, "bold"), bg="grey").place(x=100, y=380)
Button(root, text="3", font=("Arial", 20, "bold"), bg="grey").place(x=190, y=380)
Button(root, text="0", font=("Arial", 20, "bold"), bg="grey").place(x=10, y=450)
Button(root, text=".", font=("Arial", 20, "bold"), bg="grey").place(x=100, y=450)
Button(root, text="=", font=("Arial", 20, "bold"), bg="grey").place(x=190, y=450)
Button(root, text="00", font=("Arial", 20, "bold"), bg="grey").place(x=280, y=240)
Button(root, text="000", font=("Arial", 20, "bold"), bg="grey").place(x=280, y=310)


root.mainloop()
