import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

def GetValue(event):
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select["prod_id"])
    e2.insert(0,select["prod_name"])
    e3.insert(0,select["price"])
    e4.insert(0,select["quantity"])
    e5.insert(0,select["MFD"])

def Add():
    prod_id = e1.get()
    prod_name = e2.get()
    price = e3.get()
    quantity = e4.get()
    MFD = e5.get()

    con=mysql.connector.connect(host="localhost",user="root",passwd="",database='mysql')
    mycursor=con.cursor()
 
    try:
       sql = "INSERT INTO  product(prod_id,prod_name,price,quantity,MFD) VALUES (%s, %s, %s, %s, %s)"
       val = (prod_id,prod_name,price,quantity,MFD)
       mycursor.execute(sql, val)
       con.commit()

       messagebox.showinfo("Added","Product added successfully")
       e1.delete(0,END)
       e2.delete(0,END)
       e3.delete(0,END)
       e4.delete(0,END)
       e5.delete(0,END)
    except Exception as err:
        print(err)
        con.rollback()
        con.close()

def Update():
    prod_id = e1.get()
    prod_name = e2.get()
    price = e3.get()
    quantity = e4.get()
    MFD = e5.get()

    con=mysql.connector.connect(host="localhost",user="root",passwd="",database='mysql')
    mycursor=con.cursor()

    try:
        sql = "Update product set prod_name= %s, price = %s, quantity = %s, MFD = %s where prod_id = %s"
        val = (prod_name,price,quantity,MFD,prod_id)
        mycursor.execute(sql, val)
        con.commit()

        messagebox.showinfo("Added","Product UPDATED successfully")
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e1.focus_set()
    except Exception as err:
        print(err)
        con.rollback()
        con.close()

def Delete():
    prod_id = e1.get()
    con=mysql.connector.connect(host="localhost",user="root",passwd="",database='mysql')
    mycursor=con.cursor()

    try:
        sql = "delete from product where prod_id = %s"
        val = (prod_id,)
        mycursor.execute(sql, val)
        con.commit()

        messagebox.showinfo("info","record deleted")
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e1.focus_set()
    except Exception as err:
        print(err)
        con.rollback()
        con.close()

def show():
    con=mysql.connector.connect(host="localhost",user="root",passwd="",database='mysql')
    mycursor=con.cursor()
    mycursor.execute("select prod_id, prod_name, price, quantity, MFD from product")
    records = mycursor.fetchall()
    print(records)

    for i, (prod_id, prod_name, price, quantity, MFD) in enumerate(records, start =1):
        listBox.insert("","end",values = (prod_id, prod_name, price, quantity, MFD))
        con.close()

root = Tk()
root.configure(background = "green")
root.title("PROJECT-II")
root.geometry("1000x800")
global e1
global e2
global e3
global e4
global e5

tk.Label(root, text="PRODUCT DETAILS", fg="Black",bg = "red", font=(None, 20)).place(x=50, y=300)
tk.Label(root, text="ENTER DETAILS", fg="Black",bg = "red", font=(None, 20)).place(x=50, y=10)
tk.Label(root, text="PRODUCT ID",bg = "yellow").place(x=30, y=60)
Label(root, text="PRODUCT NAME",bg = "yellow").place(x=30, y=90)
Label(root, text="PRICE",bg = "yellow").place(x=30, y=120)
Label(root, text="QUANTITY",bg = "yellow").place(x=30, y=150)
Label(root, text="MFD",bg = "yellow").place(x=30, y=180)

e1 = Entry(root,bg = "white")
e1.place(x=160, y=60)
 
e2 = Entry(root,bg = "white")
e2.place(x=160, y=90)

e3 = Entry(root,bg = "white")
e3.place(x=160, y=120)
 
e4 = Entry(root,bg = "white")
e4.place(x=160, y=150)

e5 = Entry(root,bg = "white")
e5.place(x=160, y=180)
 
Button(root, text="Add",command = Add,height=4, width= 15,bg = "sky blue").place(x=350, y=100)
Button(root, text="Update",command = Update,height=4, width= 15,bg = "sky blue").place(x=550, y=100)
Button(root, text="Delete",command = Delete,height=4, width= 15,bg = "sky blue").place(x=750, y=100)
        
cols = ('prod_id', 'prod_name', 'price','quantity','MFD')
listBox = ttk.Treeview(root, columns=cols, show='headings')
 
for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=30, y=350)
 
show()
listBox.bind('<Double-Button-1>',GetValue)
 
root.mainloop()
