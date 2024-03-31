from tkinter import*
root=Tk()
root.geometry("1000x500")
root.title("Bill Management System")
root.resizable(False,False)
def Reset():
    entry_coffee.delete(0,END)
    entry_tea.delete(0,END)
    entry_bread_toast.delete(0,END)
    entry_dosa.delete(0,END)
    entry_burger.delete(0,END)
    entry_pizza.delete(0,END)
    entry_sandwich.delete(0,END)
def  Total():
    try:a1=int(coffee.get())
    except:a1=0

    try:a2=int(tea.get())
    except:a2=0

    try:a3=int(bread_toast.get())
    except:a3=0

    try:a4=int(dosa.get())
    except:a4=0
 
    try:a5=int(burger.get())
    except:a5=0

    try:a6=int(pizza.get())
    except:a6=0

    try:a7=int(sandwich.get())
    except:a7=0

#define cost of each item   
    c1=30*a1
    c2=25*a2
    c3=40*a3
    c4=60*a4
    c5=80*a5
    c6=240*a6
    c7=50*a7

    lb1_total=Label(f2,font=('aria',20,'bold'),text="Total",width=16,fg="lightyellow",bg="black")
    lb1_total.place(x=0,y=50)

    entry_total=Entry(f2,font=('aria',20,'bold'),textvariable=Total_bill,bd=6,width=15,bg="lightgreen")
    entry_total.place(x=20,y=100)

    totalcost=c1+c2+c3+c4+c5+c6+c7
    string_bill="Rs.",str('%.2f'%totalcost)
    Total_bill.set(string_bill)

Label(text="BILL MANAGEMENT SYSTEM",bg="black",fg="white",font=("calibri",33),width="300",height="2").pack()

#Menu card

f=Frame(root,bg="orange",highlightbackground="black",highlightthickness=1,width=300,height=370)
f.place(x=10,y=118)
Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="orange").place(x=80,y=0)
Label(f,font=("Lucida Callgraphy",15,'bold'),text="coffee..........Rs.30/plate",fg="black",bg="orange").place(x=10,y=80)
Label(f,font=("Lucida Callgraphy",15,'bold'),text="tea.............Rs.25/plate",fg="black",bg="orange").place(x=10,y=110)
Label(f,font=("Lucida Callgraphy",15,'bold'),text="bread_toast.....Rs.40/plate",fg="black",bg="orange").place(x=10,y=140)
Label(f,font=("Lucida Callgraphy",15,'bold'),text="Dosa............Rs.60/plate",fg="black",bg="orange").place(x=10,y=170)
Label(f,font=("Lucida Callgraphy",15,'bold'),text="Burger..........Rs.80/plate",fg="black",bg="orange").place(x=10,y=200)
Label(f,font=("Lucida Callgraphy",15,'bold'),text="pizza...........Rs.240/plate",fg="black",bg="orange").place(x=10,y=230)
Label(f,font=("Lucida Callgraphy",15,'bold'),text="Sandwich........Rs.50/plate",fg="black",bg="orange").place(x=10,y=260)

#Billl
f2=Frame(root,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)
Bill=Label(f2,text="Bill",font=('calibri',20),bg="lightyellow")
Bill.place(x=120,y=10)


#work
f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()
coffee=StringVar()
tea=StringVar()
bread_toast=StringVar()
dosa=StringVar()
burger=StringVar()
pizza=StringVar()
sandwich=StringVar()
Total_bill=StringVar()

#
lb1_coffee=Label(f1,font=("aria",20,'bold'),text="Coffee",width=12,fg="green")
lb1_tea=Label(f1,font=("aria",20,'bold'),text="tea",width=12,fg="green")
lb1_bread_toast=Label(f1,font=("aria",20,'bold'),text="Bread_toast",width=12,fg="green")
lb1_dosa=Label(f1,font=("aria",20,'bold'),text="Dosa",width=12,fg="green")
lb1_burger=Label(f1,font=("aria",20,'bold'),text="Burger",width=12,fg="green")
lb1_pizza=Label(f1,font=("aria",20,'bold'),text="Pizza",width=12,fg="green")
lb1_sadwich=Label(f1,font=("aria",20,'bold'),text="Sandwich",width=12,fg="green")

lb1_coffee.grid(row=1,column=0)
lb1_tea.grid(row=2,column=0)
lb1_dosa.grid(row=3,column=0)
lb1_bread_toast.grid(row=4,column=0)
lb1_burger.grid(row=5,column=0)
lb1_pizza.grid(row=6,column=0)
lb1_sadwich.grid(row=7,column=0)
#Entry
entry_coffee=Entry(f1,font=("aria",20,'bold'),textvariable=coffee,bd=6,width=8,bg="lightpink")
entry_tea=Entry(f1,font=("aria",20,'bold'),textvariable=tea,bd=6,width=8,bg="lightpink")
entry_dosa=Entry(f1,font=("aria",20,'bold'),textvariable=dosa,bd=6,width=8,bg="lightpink")
entry_bread_toast=Entry(f1,font=("aria",20,'bold'),textvariable=bread_toast,bd=6,width=8,bg="lightpink")
entry_burger=Entry(f1,font=("aria",20,'bold'),textvariable=burger,bd=6,width=8,bg="lightpink")
entry_pizza=Entry(f1,font=("aria",20,'bold'),textvariable=pizza,bd=6,width=8,bg="lightpink")
entry_sandwich=Entry(f1,font=("aria",20,'bold'),textvariable=sandwich,bd=6,width=8,bg="lightpink")

entry_coffee.grid(row=1,column=1)
entry_tea.grid(row=2,column=1)
entry_dosa.grid(row=3,column=1)
entry_bread_toast.grid(row=4,column=1)
entry_burger.grid(row=5,column=1)
entry_pizza.grid(row=6,column=1)
entry_sandwich.grid(row=7,column=1)

#button
btn_reset=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,'bold'),width=10,text="Reset",command=Reset)

btn_reset.grid(row=8,column=0)
btn_total=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,'bold'),width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)

root.mainloop()