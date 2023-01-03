# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from random import randint,choice,shuffle



# ---------------------------- SAVE PASSWORD ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from tkinter import messagebox
import json
w1=Tk()
w1.config(padx=20,pady=20)
w1.minsize(500,300)
p1=PhotoImage(file="logo.png")
w1.title("Password Generator")
c1=Canvas(width=200,height=200)
c1.create_image(100,100,image=p1)
c1.grid(column=1,row=0)
l1=Label(text="Website:")
l1.grid(row=1,column=0)
e1=Entry(width=40)
e1.focus()
e1.grid(row=1,column=1,columnspan=1)
l2=Label(text="Email/Username:")
l2.grid(row=2,column=0)
e2=Entry(width=40)
e2.insert(0,"aroradivyam3@gmail.com")
e2.grid(row=2,column=1,columnspan=2)
l3=Label(text="Password")
l3.grid(row=3,column=0)
pass1=Label(text="")
pass1.grid(row=3,column=1)
def gen():
    l1=[]
    alpha=list("abcdefghijklmnopqrstuvwxyz")
    sym=list("!@#$%^&*")
    for i in range(0,5):
        l1.append(str(randint(0,9)))
    for i in range(0,3):
        l1.append(choice(alpha))
    for i in range(0,2):
        l1.append(choice(sym))
    shuffle(l1)
    x="".join(l1)
    pass1["text"]=x
b1=Button(text="Generate",width=6,command=gen)
b1.grid(row=3,column=2)
def passsave():
    newdata={f"{e1.get()}":{"email":f"{e2.get()}","password":f"{pass1['text']}" }}
    if e1.get()=="" or e2.get()=="":
        messagebox.askokcancel(message="Please fill all the details!",title="Warning")
    else:
        is_ok=messagebox.askokcancel(title=e1.get(),message=f"Email: {e2.get()}\nPassword: {pass1['text']}\nAre you fine with the above mentioned details? ")
        if is_ok:
            try:
                with open("Passwords.json","r") as f:
                    data=json.load(f)
                    data.update(newdata)
            except FileNotFoundError:
                with open("Passwords.json","w") as f:
                    json.dump(newdata,f)
                    e1.delete(0,END)
                    pass1["text"]=""
            else:
                with open("Passwords.json","w") as f:
                    json.dump(data,f)
                    e1.delete(0,END)
                    pass1["text"]=""
b2=Button(text="Add",width=35,command=passsave)
b2.grid(row=4,column=1,columnspan=3)

def search():
    website=e1.get()
    with open("Passwords.json","r") as f:
        dict1=json.load(f)
        try:
            messagebox.askokcancel(title=website,message=f"Email: {dict1[website]['email']}\nPassword:{dict1[website]['password']}")
        except:
            messagebox.askokcancel(title=website, message=" NOT FOUND")
b3=Button(text="search",command=search)
b3.grid(row=1,column=2)










w1.mainloop()