from tkinter import *
window=Tk()
window.geometry("400x500")
window.title("Calculator")
text_input=StringVar()
operator=""


top=Frame(window,height=50,width=150)
top.pack(side="top")

L1=Label(top,font=("arial",20,"bold"),text="Calculator",fg="green",bd=10)
L1.place(x=0,y=0)
L1.configure(bg="black")
def buttonclick(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)
def cleardisplay():
    global operator
    operator = ""
    text_input.set("")
def equal():
    global operator
    sum = str(eval(operator))
    text_input.set(sum)
    operator = ""

textarea=Entry(window,font=("arial",12,"bold"),textvariable=text_input,bd=10,insertwidth=2)
textarea.place(x=50,y=50)
but7=Button(window,font=("arial",15,"bold"),bd=10,text=7,fg="black",command=lambda:buttonclick(7))
but7.place(x=50,y=100)
but8=Button(window,font=("arial",15,"bold"),bd=10,text=8,fg="black",command=lambda:buttonclick(8))
but8.place(x=100,y=100)
but9=Button(window,font=("arial",15,"bold"),bd=10,text=9,fg="black",command=lambda:buttonclick(9))
but9.place(x=150,y=100)
butplus=Button(window,font=("arial",15,"bold"),bd=10,text="+",fg="black",command=lambda:buttonclick("+"))
butplus.place(x=200,y=100)

but4=Button(window,font=("arial",15,"bold"),bd=10,text=4,fg="black",command=lambda:buttonclick(4))
but4.place(x=50,y=150)
but5=Button(window,font=("arial",15,"bold"),bd=10,text=5,fg="black",command=lambda:buttonclick(5))
but5.place(x=100,y=150)
but6=Button(window,font=("arial",15,"bold"),bd=10,text=6,fg="black",command=lambda:buttonclick(6))
but6.place(x=150,y=150)
butmulti=Button(window,font=("arial",15,"bold"),bd=10,text="*",fg="black",command=lambda:buttonclick("*"))
butmulti.place(x=200,y=150)

but1=Button(window,font=("arial",15,"bold"),bd=10,text=1,fg="black",command=lambda:buttonclick(1))
but1.place(x=50,y=200)
but2=Button(window,font=("arial",15,"bold"),bd=10,text=2,fg="black",command=lambda:buttonclick(2))
but2.place(x=100,y=200)
but3=Button(window,font=("arial",15,"bold"),bd=10,text=3,fg="black",command=lambda:buttonclick(3))
but3.place(x=150,y=200)
butsub=Button(window,font=("arial",15,"bold"),bd=10,text="-",fg="black",command=lambda:buttonclick("-"))
butsub.place(x=200,y=200)

butclear=Button(window,font=("arial",15,"bold"),bd=10,text="c",fg="black",command=cleardisplay)
butclear.place(x=50,y=250)
butzero=Button(window,font=("arial",15,"bold"),bd=10,text=0,fg="black",command=lambda:buttonclick(0))
butzero.place(x=100,y=250)
butequal=Button(window,font=("arial",15,"bold"),bd=10,text="=",fg="black",command=equal)
butequal.place(x=150,y=250)
butdiv=Button(window,font=("arial",15,"bold"),bd=10,text="/",fg="black",command=lambda:buttonclick("/"))
butdiv.place(x=200,y=250)




window.mainloop()
