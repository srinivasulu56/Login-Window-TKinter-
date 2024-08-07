from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def login_handle():
    email = email_input.get()
    password = pass_input.get()
    if email=="srinivas" and password=="123":
        messagebox.showinfo("Sucess","Login successful")

    else:
        messagebox.showerror("Denied","Login is unsucessful")


win = Tk()
win.title("Login Window")
win.configure(background="#101820")
win.geometry(("350x500"))
img = Image.open("spider-man logo.jpg")
img_resize = img.resize((150,100))
img = ImageTk.PhotoImage(img_resize)
img_lable = Label(win,image=img)
img_lable.pack(pady=(15,10))
text_lable = Label(win,text="SPIDER-MAN",fg="#CB0000",bg="#101820")
text_lable.pack()
text_lable.config(font=("Teko",30))
email_lable = Label(win,text="Enter your email",fg="white",bg="#101820")
email_lable.pack(pady=(16,12))
email_lable.config(font=("Teko",12))
email_input = Entry(win,width=35)
email_input.pack(ipady=6)
pass_lable = Label(win,text="Enter your password",fg="white",bg="#101820")
pass_lable.pack(pady=(16,12))
pass_lable.config(font=("Teko",12))
pass_input= Entry(win,width=35)
pass_input.pack(ipady=6)
log_but = Button(win,width=10,height=2,text="Login here",command=login_handle)
log_but.pack(pady=(12,12))
log_but.config(font=("Teko",12))
win.mainloop()