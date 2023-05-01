import datetime
from customtkinter import *
from tkinter import messagebox, ttk
from tkinter import *
import tkinter as tk
import customtkinter as custom
from datetime import date
from datetime import timedelta
import mysql.connector as con
import random
from botAI import *

#All Required Packages Are Imported

# db1 = con.connect(host = 'localhost', user = 'root', password = 'admin')
# cursor = db1.cursor()
# cursor.execute("Create Database epustakalay")

#--------------DATABASE "EPUSTAKALAY CREATED" 

db1=con.connect(host = 'localhost', user = 'root', password = 'admin', database = 'epustakalay')
cursor = db1.cursor()

#----------CONNECT WITH THE DATABASE EPUSTAKALAY

# str = "Create Table Books(B_Id Varchar(4) , B_Name Varchar(30) , B_Author Varchar(30) , B_Category Varchar (30) , B_Quantity Int(5), B_Price Float(5,2))"
# cursor.execute(str)

# str = "Create Table Issue( Course_Id Int(4), B_Id Varchar(4), Student_Name Varchar(30), Issue_Date Varchar(30), Return_Date Varchar(30))"
# cursor.execute(str)

# str1 = "Create Table Book_Return( Course_Id Int(4), B_Id Varchar(4), Student_Name Varchar(30), Return_Date Varchar(30))"
# cursor.execute(str1)

# str1 = "Create Table Admin( AdminId Int(), Passcode Varchar(45))"
# cursor.execute(str1)

# str1 = "Create Table Admin( AdminId Int(), Passcode Varchar(45))"
# cursor.execute(str1)

# str1 = "Create Table Register( CourseId Int(), Name Varchar(45), Course Varchar(45), Password Varchar(45), Phone Int(10))"
# cursor.execute(str1)

#---------SQL QUERIES TO CREATE REQUIRED TABLES IN DATABASE 
#----------------------CAN BE EASILY DONE THROUGH ACCESSING THE MySQL Command Client

crs_Id, stu_Name , stu_Crs = None,None,None
custom.set_appearance_mode("Dark")

def add_placeholder(entry, placeholder):
    # Set the placeholder
    entry.placeholder = placeholder
    entry.insert(0, placeholder)
    entry.configure(fg_color="black")

    # Define focus in and focus out event handlers
    def on_entry_focus_in(event):
        if entry.get() == entry.placeholder:
            entry.delete(0, "end")
            entry.configure(fg_color="black")

    def on_entry_focus_out(event):
        if not entry.get():
            entry.insert(0, entry.placeholder)
            entry.configure(fg_color="gray")

    # Bind the focus in and focus out events to the entry widget
    entry.bind("<FocusIn>", on_entry_focus_in)
    entry.bind("<FocusOut>", on_entry_focus_out)

def A():

    id = u_id.get()
    name = u_name.get()
    author = u_author.get()
    category = u_category.get()
    quantity = u_qnt.get()
    price = u_mrp.get()

    if(id=="" or name=="" or author=="" or category=="" or quantity=="" or price==""):
        messagebox.showwarning("Mandatory Field*","All Fields Are Required")
    else:            
        sql = "Insert Into Books Values ('{}','{}','{}','{}',{},{}) ".format(id,name,author,category,quantity,price)
        cursor.execute(sql)
        db1.commit()

        u_id.delete(0, 'end')
        u_name.delete(0, 'end')
        u_author.delete(0, 'end')
        u_qnt.delete(0, 'end')
        u_mrp.delete(0, 'end')
        messagebox.showinfo("Status","Added Successfully")

def AddBooks():
    
    window.withdraw()
    
    custom.set_default_color_theme("blue")  
    
    root = custom.CTk()
    root.geometry("700x480+580+275")
    root.resizable(0,0)
    root.title("Add Record")
    
    title = custom.CTkLabel(root, text="ADDING NEW BOOKS", font= custom.CTkFont(size=18, weight= "bold"))
    title.pack(padx=10, pady=(25,25))
    
    frame = custom.CTkFrame(root, height=320)
    frame.pack(fill="x", padx = 30)
    
    id = custom.CTkLabel(frame, text="Enter Book ID : ", font=custom.CTkFont(size=14))
    id.place(x=120,y=40)
    
    global u_id

    u_id = custom.CTkEntry(frame, width=150)
    u_id.place(x=360,y=40)

    name = custom.CTkLabel(frame, text="Enter Book Name : ", font=custom.CTkFont(size=14))
    name.place(x=120,y=80)
    
    global u_name

    u_name = custom.CTkEntry(frame, width=150)
    u_name.place(x=360,y=80)
    
    author = custom.CTkLabel(frame, text="Enter Book Author : ", font=custom.CTkFont(size=14))
    author.place(x=120,y=120)
    
    global u_author
    
    u_author = custom.CTkEntry(frame, width=150)
    u_author.place(x=360,y=120)
    
    
    category = custom.CTkLabel(frame, text="Select Book Category : ", font=custom.CTkFont(size=14))
    category.place(x=120,y=160)

    global u_category
    
    u_category = custom.CTkComboBox(frame, font=custom.CTkFont(size=14), values=['Business','Fiction','Programming','Romance','Thriller'], width=150)
    u_category.place(x=360,y=160)

    qnt = custom.CTkLabel(frame, text="Enter Book Quantity : ", font=custom.CTkFont(size=14))
    qnt.place(x=120,y=200)

    global u_qnt

    u_qnt = custom.CTkEntry(frame, width=150)
    u_qnt.place(x=360,y=200)

    mrp = custom.CTkLabel(frame, text="Enter Book Price : ", font=custom.CTkFont(size=14))
    mrp.place(x=120,y=240)

    global u_mrp

    u_mrp = custom.CTkEntry(frame, width=150)
    u_mrp.place(x=360,y=240)
    
    add_placeholder(u_id, "")
    add_placeholder(u_name, "")
    add_placeholder(u_author, "")
    add_placeholder(u_qnt, "")
    add_placeholder(u_mrp, "")
    
    add = custom.CTkButton(root, text="Add Record !", font=custom.CTkFont(size=14), command=A, hover_color="green")
    add.place(x=180,y=420)
    
    ex = custom.CTkButton(root, text="Exit Out!!", font= custom.CTkFont(size=14), command=lambda:[root.destroy() , window.deiconify()], hover_color="red")
    ex.place(x=380,y=420)

    root.mainloop()
    
def D():
    
    del_id = d_id.get()

    if(del_id==""):
        messagebox.showwarning("Mandatory Field*","Book ID Required")
    else:  
        cursor = db1.cursor()
        sql = "DELETE FROM Books WHERE B_Id = '"+del_id+"'"
        cursor.execute(sql)
        if cursor.rowcount > 0:
            db1.commit()
            messagebox.showinfo("Success!", "Record(s) Deleted Successfully.")
        else:
            db1.rollback()
            messagebox.showerror("Error!", "No book with ID '{}' found.".format(del_id))


def DeleteBooks():

    # panel.withdraw()
    
    root = custom.CTk()
    root.geometry("550x250+680+435")
    root.resizable(0,0)
    root.configure(bg = "azure")
    root.title("Delete Record")
    
    title = custom.CTkLabel(root, text="DELETION OF BOOKS", font= custom.CTkFont(size=18, weight= "bold"))
    title.pack(padx=10, pady=(25,25))
    
    id = custom.CTkLabel(root, text="Enter Book ID : ", font=custom.CTkFont(size=14))
    id.place(x=120,y=80)

    global d_id

    d_id = custom.CTkEntry(root, width=150)
    d_id.place(x=300,y=80)
    
    add_placeholder(d_id, "B123")
    
    dele = custom.CTkButton(root, text="Delete Record!", font=custom.CTkFont(size=14), command=D, hover_color="orange")
    dele.place(x=120,y=140)
    
    ex = custom.CTkButton(root, text="Exit Out!!", font=custom.CTkFont(size=14), command=lambda:[root.destroy()], hover_color="red")
    ex.place(x=310,y=140)
        
    root.mainloop()
    

def UpdateBooks(bid, issue_qty):
    sel = "SELECT * FROM Books WHERE B_Id = %s"
    data = (bid,)
    cursor = db1.cursor()
    cursor.execute(sel, data)
    result = cursor.fetchall()
    update = result[0][4]
    updatedQty = update + issue_qty
    sql = "UPDATE Books SET B_Quantity = %s WHERE B_Id = %s"
    cursor.execute(sql, (updatedQty, bid))
    db1.commit()


def Search():
    # Get the search query entered by the user
    search_query = u_srch.get()
    
    if search_query == "":
        messagebox.showwarning("Mandatory Field*", "Search Field Is Required")
    else:
        # Execute an SQL query to search for the book in the database
        sql = "SELECT * FROM Books WHERE B_Name LIKE '%{}%' OR B_Author LIKE '%{}%'".format(search_query, search_query)
        cursor.execute(sql)
        search_results = cursor.fetchall()

        # Create a new window to display the search results
        search_window = custom.CTk()
        search_window.title("Results Found")
        search_window.geometry("600x365+680+470")
        search_window.resizable(0,0)

        # Create a table to display the search results
        table = ttk.Treeview(search_window)
        st = ttk.Style(search_window)
        st.theme_use("classic")
        
        st.configure("Treeview",
                            background="#2a2d2e",
                            foreground="white",
                            rowheight=55,
                            fieldbackground="#343638",
                            bordercolor="white",
                            relief="flat",
                            borderwidth=6,
                            font=('TkDefaultFont', 14))
    
        st.map('Treeview', background=[('selected', 'gray')])
    
        st.configure("Treeview.Heading",
                            background="#22559b",
                            foreground="white",
                            rowheight = 50,
                            font=('TkDefaultFont', 16))
        st.map("Treeview.Heading",
                      background=[('active', '#22559b')])
        
        table["columns"] = ("B_Id", "B_Name", "B_Author", "B_Category", "B_Quantity", "B_Price")
        table.column("#0", width=0, stretch="NO")
        table.column("B_Id", anchor="center", width=140)
        table.column("B_Name", anchor="center", width=140)
        table.column("B_Author", anchor="center", width=140)
        table.column("B_Category", anchor="center", width=140)
        table.column("B_Quantity", anchor="center", width=140)
        table.column("B_Price", anchor="center", width=140)
        table.heading("#0", text="", anchor="w")
        table.heading("B_Id", text="Book ID", anchor="center")
        table.heading("B_Name", text="Book Name", anchor="center")
        table.heading("B_Author", text="Author", anchor="center")
        table.heading("B_Category", text="Category", anchor="center")
        table.heading("B_Quantity", text="Quantity", anchor="center")
        table.heading("B_Price", text="Price", anchor="center")
        table.pack(fill="both", expand=True)

        for book in search_results:
            table.insert("", "end", text="", values=book)

        search_window.mainloop()
        

def SearchRecord():
    
    window.withdraw()

    root = custom.CTk()
    root.geometry("700x580+600+250")
    root.resizable(0,0)
    root.title("Search Record")

    title = custom.CTkLabel(root, text="SEARCH BOOKS", font= custom.CTkFont(size=18, weight= "bold"))
    title.pack(padx=10, pady=(25,25))
    
    srch = custom.CTkLabel(root, text="Search By Name or Author : ", font=custom.CTkFont(size=14))
    srch.place(x=120,y=70)
    
    global u_srch
    
    u_srch = custom.CTkEntry(root, width=150)
    u_srch.place(x=340,y=70)
    
    add = custom.CTkButton(root, text="Search!", font=custom.CTkFont(size=14), command=Search, hover_color="green" , width=80)
    add.place(x=500,y=70)
    
    frame = custom.CTkFrame(root, height=350, width=600)
    frame.place(x=60,y=120)
    
    tree = ttk.Treeview(frame)
    st = ttk.Style(frame)
    st.theme_use("classic")
    
    st.configure("Treeview",
                            background="#2a2d2e",
                            foreground="white",
                            rowheight=55,
                            fieldbackground="#343638",
                            bordercolor="white",
                            relief="flat",
                            borderwidth=6,
                            font=('TkDefaultFont', 14))
    
    st.map('Treeview', background=[('selected', 'gray')])
    
    st.configure("Treeview.Heading",
                            background="#22559b",
                            foreground="white",
                            rowheight = 50,
                            font=('TkDefaultFont', 16))
    st.map("Treeview.Heading",
                      background=[('active', '#22559b')])
    
    tree["columns"]=("B_Id","B_Name","B_Author","B_Category","B_Quantity","B_Price")

    tree.heading("#0", text ="", anchor=tk.CENTER)
    tree.heading("B_Id",text = "B_Id",anchor=tk.CENTER)
    tree.heading("B_Name",text = "B_Name",anchor=tk.CENTER)
    tree.heading("B_Author",text = "B_Author",anchor=tk.CENTER)
    tree.heading("B_Category",text ="B_Category",anchor=tk.CENTER)
    tree.heading("B_Quantity",text = "B_Quantity",anchor=tk.CENTER)
    tree.heading("B_Price", text = "B_Price",anchor=tk.CENTER)

    tree.column("#0", width=0, stretch=NO)
    tree.column("B_Id",minwidth=0,width=140,anchor=tk.CENTER)
    tree.column("B_Name",minwidth=0,width=140,anchor=tk.CENTER)
    tree.column("B_Author",minwidth=0,width=140,anchor=tk.CENTER)
    tree.column("B_Category",minwidth=0,width=140,anchor=tk.CENTER)
    tree.column("B_Quantity",minwidth=0,width=140,anchor=tk.CENTER)
    tree.column("B_Price",minwidth=0,width=140,anchor=tk.CENTER)

    index=0
    iid =0

    sel = "Select * From Books Where B_Quantity>=0"
    cursor = db1.cursor()
    cursor.execute(sel)
    display = cursor.fetchall()

    for i in display:
        tree.insert("",index,iid, value=i)
        index = iid=index+1

    scr = ttk.Scrollbar(frame,orient="vertical")
    scr.configure(command=tree.yview)
    tree.configure(yscrollcommand=scr.set)
    scr.pack(fill=BOTH,side=RIGHT)
    tree.pack()
    
    close = custom.CTkButton(root, text="CLOSE!", font=custom.CTkFont(size=14), command=lambda:[(root.destroy(),window.deiconify())], hover_color="red")
    close.place(x=270,y=530)
    
    root.mainloop()
    


def IssueRecord():
    
    window.withdraw()

    root = custom.CTk()
    root.geometry("620x580+600+250")
    root.resizable(0,0)
    root.title("Issue Record")

    title = custom.CTkLabel(root, text="ISSUED BOOKS", font= custom.CTkFont(size=18, weight= "bold"))
    title.pack(padx=10, pady=(25,25))
    
    frame = custom.CTkFrame(root, height=350, width=600)
    frame.place(x=60,y=80)
    
    tree = ttk.Treeview(frame)
    st = ttk.Style(frame)
    st.theme_use("classic")
    
    st.configure("Treeview",
                            background="#2a2d2e",
                            foreground="white",
                            rowheight=55,
                            fieldbackground="#343638",
                            bordercolor="white",
                            relief="flat",
                            borderwidth=6,
                            font=('TkDefaultFont', 14))
    
    st.map('Treeview', background=[('selected', 'gray')])
    
    st.configure("Treeview.Heading",
                            background="#22559b",
                            foreground="white",
                            rowheight = 50,
                            font=('TkDefaultFont', 16))
    st.map("Treeview.Heading",
                      background=[('active', '#22559b')])
    
    tree["columns"]=("Course_Id","B_Id","Stud_Name","Issued_On","Return_Date")

    tree.heading("#0", text ="", anchor=tk.CENTER)
    tree.heading("Course_Id",text = "Course_Id",anchor=tk.CENTER)
    tree.heading("B_Id",text = "B_Id",anchor=tk.CENTER)
    tree.heading("Stud_Name",text ="Stud_Name",anchor=tk.CENTER)
    tree.heading("Issued_On",text = "Issued_On",anchor=tk.CENTER)
    tree.heading("Return_Date", text = "Return_Date",anchor=tk.CENTER)

    tree.column("#0", width=0, stretch=NO)
    tree.column("Course_Id",minwidth=0,width=140,anchor=tk.CENTER)
    tree.column("B_Id",minwidth=0,width=140,anchor=tk.CENTER)
    tree.column("Stud_Name",minwidth=0,width=140,anchor=tk.CENTER)
    tree.column("Issued_On",minwidth=0,width=140,anchor=tk.CENTER)
    tree.column("Return_Date",minwidth=0,width=140,anchor=tk.CENTER)

    index=0
    iid =0

    sel = "Select * From Issue"
    cursor = db1.cursor()
    cursor.execute(sel)
    display = cursor.fetchall()

    for i in display:
        tree.insert("",index,iid, value=i)
        index = iid=index+1

    scr = ttk.Scrollbar(frame,orient="vertical")
    scr.configure(command=tree.yview)
    tree.configure(yscrollcommand=scr.set)
    scr.pack(fill=BOTH,side=RIGHT)
    tree.pack()
    
    close = custom.CTkButton(root, text="CLOSE!", font=custom.CTkFont(size=14), command=lambda:[root.destroy(),window.deiconify()], hover_color="red")
    close.place(x=235,y=510)
    
    root.mainloop()
    
def ReturnRecord():
    
    window.withdraw()

    root = custom.CTk()
    root.geometry("620x580+600+250")
    root.resizable(0,0)
    root.title("Return Record")

    title = custom.CTkLabel(root, text="RETURNED BOOKS", font= custom.CTkFont(size=18, weight= "bold"))
    title.pack(padx=10, pady=(25,25))
    
    frame = custom.CTkFrame(root, height=350, width=600)
    frame.place(x=60,y=80)
    
    tree = ttk.Treeview(frame)
    st = ttk.Style(frame)
    st.theme_use("classic")
    
    st.configure("Treeview",
                            background="#2a2d2e",
                            foreground="white",
                            rowheight=55,
                            fieldbackground="#343638",
                            bordercolor="white",
                            relief="flat",
                            borderwidth=6,
                            font=('TkDefaultFont', 14))
    
    st.map('Treeview', background=[('selected', 'gray')])
    
    st.configure("Treeview.Heading",
                            background="#22559b",
                            foreground="white",
                            rowheight = 50,
                            font=('TkDefaultFont', 16))
    st.map("Treeview.Heading",
                      background=[('active', '#22559b')])
    
    tree["columns"]=("Course_Id","B_Id","Stud_Name","Return_Date","Fine_Imposed")

    tree.heading("#0", text ="", anchor=tk.CENTER)
    tree.heading("Course_Id",text = "Course_Id",anchor=tk.CENTER)
    tree.heading("B_Id",text = "B_Id",anchor=tk.CENTER)
    tree.heading("Stud_Name",text ="Stud_Name",anchor=tk.CENTER)
    tree.heading("Return_Date",text ="Return_Date",anchor=tk.CENTER)
    tree.heading("Fine_Imposed", text = "Fine_Imposed",anchor=tk.CENTER)

    tree.column("#0", width=0, stretch=NO)
    tree.column("Course_Id",minwidth=0,width=140,anchor=tk.CENTER)
    tree.column("B_Id",minwidth=0,width=140,anchor=tk.CENTER)
    tree.column("Stud_Name",minwidth=0,width=140,anchor=tk.CENTER)
    tree.column("Return_Date",minwidth=0,width=140,anchor=tk.CENTER)
    tree.column("Fine_Imposed",minwidth=0,width=140,anchor=tk.CENTER)

    index=0
    iid =0

    sel = "Select * From Book_Return"
    cursor = db1.cursor()
    cursor.execute(sel)
    display = cursor.fetchall()

    for i in display:
        tree.insert("",index,iid, value=i)
        index = iid=index+1

    scr = ttk.Scrollbar(frame,orient="vertical")
    scr.configure(command=tree.yview)
    tree.configure(yscrollcommand=scr.set)
    scr.pack(fill=BOTH,side=RIGHT)
    tree.pack()
    
    close = custom.CTkButton(root, text="CLOSE!", font=custom.CTkFont(size=14), command=lambda:[root.destroy(),window.deiconify()], hover_color="red")
    close.place(x=235,y=510)
    
    root.mainloop()


def Reset():
    c_id.delete(0,END)
    u_pass.delete(0,END)

def Clr():
    a_id.delete(0,END)
    a_pass.delete(0,END)
    

def Return():
    
    cursor = db1.cursor()
    try:
        sql = "INSERT INTO Book_Return VALUES ({},'{}','{}','{}',{})".format(rid,rbook,rname,curDate,fineImposed)
        cursor.execute(sql)
        UpdateBooks(rbook,1)
        sel = "DELETE FROM Issue WHERE B_Id ='{}'".format(rbook)
        cursor.execute(sel)
        db1.commit()
        messagebox.showinfo("Status","Book Is Successfully Returned")
        root.destroy()
        window.deiconify()
    except Exception as e:
        db1.rollback()
        messagebox.showerror("Error", "An error occurred: {}".format(str(e)))
    finally:
        cursor.close()


def check_checkbox():
        if checked.get():
            global fineImposed
            fineImposed=0
            fineImposed = fineImposed+500
            global fine,label
            label = custom.CTkLabel(frame, text="Fine Imposed : ", font=custom.CTkFont(size=14))
            label.place(x=150,y=225)
            fine = custom.CTkEntry(frame,width=120)
            fine.insert(END, fineImposed)   
            fine.place(x=300,y=225)
            fine.configure(state="disabled")           
        else:
            fineImposed = 0
            fine.place_forget()
            label.place_forget()
                   
def ReturnBooks():
    
    window.withdraw()

    global root

    root = custom.CTk()
    root.geometry("660x500+650+275")
    root.resizable(0,0)
    root.title("Return Book")
    
    title = custom.CTkLabel(root, text="RETURN A BOOK", font= custom.CTkFont(size=18, weight= "bold"))
    title.pack(padx=10, pady=(25,25))
    
    sql = "SELECT * FROM Issue WHERE Course_Id = %s"
    cursor.execute(sql, (loginID,))
    result = cursor.fetchall()
    
    if len(result) > 0:
        db1.commit()
        
        global rid,rbook,rname,rIss,rRet
        rid,rbook,rname,rIss,rRet = result[0]
        
        global frame
        
        frame = CTkFrame(root, height=410,width=580)
        frame.place(x=35,y=70)

        custom.CTkLabel(frame, text="Issued Book : ", font=custom.CTkFont(size=14)).place(x=150,y=25)
        v1 = custom.CTkEntry(frame,width=120)
        v1.insert(END, rbook)   
        v1.place(x=300,y=25)
        v1.configure(state="disabled")
        
        custom.CTkLabel(frame, text="Date Of Issue : ", font=custom.CTkFont(size=14)).place(x=150,y=65)
        v1 = custom.CTkEntry(frame,width=120)
        v1.insert(END, rIss)   
        v1.place(x=300,y=65)
        v1.configure(state="disabled")
        
        custom.CTkLabel(frame, text="To Return By : ", font=custom.CTkFont(size=14)).place(x=150,y=105)
        v1 = custom.CTkEntry(frame,width=120)
        v1.insert(END, rRet)   
        v1.place(x=300,y=105)
        v1.configure(state="disabled")
        
        custom.CTkLabel(frame, text="Date Of Return : ", font=custom.CTkFont(size=14)).place(x=150,y=145)
        v2 = custom.CTkEntry(frame,width=120)
        global curDate
        curDate = datetime.datetime.now().date()
        v2.insert(END, curDate) 
        v2.place(x=300,y=145)
        v2.configure(state="disabled")
        
        global checked
        checked = custom.BooleanVar()
        checkbox = custom.CTkCheckBox(frame, text="Is there any damages to the book", font=custom.CTkFont(size=16), variable=checked, command=check_checkbox, fg_color="green")
        checkbox.place(x=150, y=185)
        
        ret = custom.CTkButton(frame, text="Return Now !", command=Return ,font=custom.CTkFont(size=14), hover_color="orange",width=90)
        ret.place(x=160,y=275)
    
        ex = custom.CTkButton(frame, text="Exit Out!",width=90, font= custom.CTkFont(size=14), command=lambda:[root.destroy(),window.deiconify()], hover_color="red")
        ex.place(x=310,y=275)
        
    else:
        frame = CTkFrame(root, height=400,width=480)
        frame.place(x=50,y=70)
        custom.CTkLabel(frame, text = "No Book(s) Issued On Your Profile" ,font= custom.CTkFont(size=14, weight= "bold")).place(x=120,y=160)
        custom.CTkButton(frame, text = "CLOSE", command= lambda:[(root.destroy(),window.deiconify())] ,font= custom.CTkFont(size=14, weight= "bold"),width=80, hover_color="red").place(x=200,y=250)

    root.mainloop()
    
def Verify():
    
    ret= v2.get()
    retDays = int(ret)
    current_date = datetime.datetime.now().date()
    retDate = current_date + datetime.timedelta(days=retDays)
    issDate = datetime.datetime.now().date()    
    sql = "Insert Into Issue Values ({},'{}','{}','{}','{}')".format(loginID,iss_id,loginName,issDate,retDate)
    cursor.execute(sql)
    db1.commit()
    
    issBook = str(iss_id)
    UpdateBooks(issBook,-1)
    
    messagebox.showinfo("Status","Book Is Successfully Issued")

def Iss():

    global iss_id
    iss_id = i_id.get()
   
    if(iss_id==""):
        messagebox.showwarning("Mandatory Field*","Book ID Required")
    else:
        cursor = db1.cursor()
        sel = "SELECT * FROM Books WHERE B_ID = '{}' AND B_Quantity > 0".format(iss_id)
        cursor.execute(sel)
        result = cursor.fetchall()
        if len(result) > 0:
            db1.commit()
            messagebox.showinfo("Status","Book Is Available")
            chk = messagebox.askquestion("Confirm","Do You Really Want To Issue")
            if chk=="yes":
                    i_id.delete(0,'end')
                    root = custom.CTk()
                    root.geometry("650x400+650+270")
                    root.resizable(0,0)
                    root.title("Issue")
                    custom.CTkLabel(root, text = "ISSUE DETAILS",font=custom.CTkFont(size=18)).place(x=250,y=25)
                    
                    custom.CTkLabel(root, text="CourseID : ", font=custom.CTkFont(size=14)).place(x=200,y=85)
                    v1 = custom.CTkEntry(root, width=120)
                    v1.insert(END, loginID)   
                    v1.place(x=340,y=85)
                    v1.configure(state="disabled")
                    
                    custom.CTkLabel(root, text="Issued By : ", font=custom.CTkFont(size=14)).place(x=200,y=125)
                    v1 = custom.CTkEntry(root, width=120)
                    v1.insert(END, loginName)   
                    v1.place(x=340,y=125)
                    v1.configure(state="disabled")
                    
                    custom.CTkLabel(root, text="Course Deptt : ", font=custom.CTkFont(size=14)).place(x=200,y=165)
                    v1 = custom.CTkEntry(root, width=120)
                    v1.insert(END, loginCourse)   
                    v1.place(x=340,y=165)
                    v1.configure(state="disabled")
                    
                    custom.CTkLabel(root, text="Issued Book : ", font=custom.CTkFont(size=14)).place(x=200,y=205)
                    v1 = custom.CTkEntry(root, width=120)
                    v1.insert(END, iss_id)   
                    v1.place(x=340,y=205)
                    v1.configure(state="disabled")
                    
                    custom.CTkLabel(root, text="Select Days : ", font=custom.CTkFont(size=14)).place(x=200,y=245)
                    global v2 
                    v2 = custom.CTkComboBox(root, font=custom.CTkFont(size=14), values=['7','10','15'], width=120)
                    v2.place(x=340,y=245) 
                    
                    custom.CTkButton(root, text="Issue Now !", command=Verify ,font=custom.CTkFont(size=14), width=80 ,hover_color="purple").place(x=230,y=295)
                    
                    ex = custom.CTkButton(root, text="Cancel", font=custom.CTkFont(size=14), width=80 ,command=lambda:[root.destroy()], hover_color="red")
                    ex.place(x=340,y=295) 
                    
                    root.mainloop()                
            else:
                i_id.delete(0,'end')
        else:
            db1.rollback()
            messagebox.showerror("Error","Book Is Not Available")
            i_id.delete(0,'end')


def IssueBooks():

    window.withdraw()

    root = custom.CTk()
    root.geometry("550x250+650+275")
    root.resizable(0,0)
    root.title("Issue RBook")
    
    title = custom.CTkLabel(root, text="ISSUE A BOOK", font= custom.CTkFont(size=18, weight= "bold"))
    title.pack(padx=10, pady=(25,25))
    
    id = custom.CTkLabel(root, text="Enter Book ID : ", font=custom.CTkFont(size=14))
    id.place(x=120,y=80)

    global i_id

    i_id = custom.CTkEntry(root, width=150)
    i_id.place(x=300,y=80)
    
    add_placeholder(i_id, "B123")
    
    iss = custom.CTkButton(root, text="Search ID!", font=custom.CTkFont(size=14), command=Iss, hover_color="purple")
    iss.place(x=120,y=140)
    
    ex = custom.CTkButton(root, text="Exit Out!!", font=custom.CTkFont(size=14), command=lambda:[(root.destroy(), window.deiconify())], hover_color="red")
    ex.place(x=310,y=140)
        
    root.mainloop()
    
    
def Student():
    
    frame = custom.CTkFrame(display, height=280,width=600)
    frame.place(x=100,y=100)
    
    title = custom.CTkLabel(frame, text="Enter Credentials To Proceed", font= custom.CTkFont(family="Times New Roman",size=18, weight= "bold"))
    title.place(x=180,y=35)
    
    course = custom.CTkLabel(frame, text="Enter CourseID  : ", font= custom.CTkFont(size=14))
    course.place(x=140,y=100)
    
    global c_id
    
    c_id = custom.CTkEntry(frame, width=150)
    c_id.place(x=300,y=100)
    
    passw = custom.CTkLabel(frame, text="Enter Password  : ", font= custom.CTkFont(size=14))
    passw.place(x=140,y=140)
    
    global u_pass
    
    u_pass = custom.CTkEntry(frame, show = "*" ,width=150)
    u_pass.place(x=300,y=140)
    
    log = custom.CTkButton(frame, text = "Log In" , command=Login , font=custom.CTkFont(size=14), hover_color="orange", width=100)
    log.place(x=160, y=190)
    
    add_placeholder(u_pass,"")
    add_placeholder(c_id,"")
    
    ex = custom.CTkButton(frame, text="Reset", command=Reset, font=custom.CTkFont(size=14), width=100)
    ex.place(x=310,y=190)
    
    reg = custom.CTkLabel(frame, text="Is it your first time here? Click here to Register", font= custom.CTkFont(family="Times New Roman",size=12), text_color="gray")
    reg.place(x=160,y=230)
    
    def on_enter(e):
        reg.configure(text_color='white', cursor='hand2')

    def on_leave(e):
        reg.configure(text_color='gray', cursor='arrow')
        
    reg.bind("<Enter>", on_enter)
    reg.bind("<Leave>", on_leave)
    reg.bind("<Button-1>", lambda event: Register())
    
    global admin
    
    admin = custom.CTkButton(display, text="Switch To Admin Panel", command = Admin ,font=custom.CTkFont(size=16,family="Times New Roman"), width=100, fg_color="purple")
    admin.place(x=300,y=420)
    custom.CTkLabel(display, text="Copyright 2023. All Rights Reserved To The Creator", font= custom.CTkFont(family="Times New Roman",size=10, weight= "bold")).place(x=265,y=470)
    
    
def Admin():
    
    admin.place_forget()
    
    frame = custom.CTkFrame(display, height=280,width=600)
    frame.place(x=100,y=100)
    title = custom.CTkLabel(frame, text="Welcome To Admin Panel ", font= custom.CTkFont(family="Times New Roman",size=18, weight= "bold"))
    title.place(x=180,y=35)
    course = custom.CTkLabel(frame, text="Enter Admin ID  : ", font= custom.CTkFont(size=14))
    course.place(x=140,y=100)
    
    global a_id
    
    a_id = custom.CTkEntry(frame, width=150)
    a_id.place(x=300,y=100)
    
    passw = custom.CTkLabel(frame, text="Enter Passcode  : ", font= custom.CTkFont(size=14))
    passw.place(x=140,y=140)
    
    global a_pass
    
    a_pass = custom.CTkEntry(frame, show = "*" ,width=150)
    a_pass.place(x=300,y=140)
    
    add_placeholder(a_id,"")
    add_placeholder(a_pass,"")
    
    log = custom.CTkButton(frame, text = "Log In", command = LoginAdmin , font=custom.CTkFont(size=14), hover_color="purple", width=100)
    log.place(x=160, y=190)
    ex = custom.CTkButton(frame, text="Reset", command=Clr, font=custom.CTkFont(size=14), width=100)
    ex.place(x=310,y=190)
    stud = custom.CTkButton(frame, text="Back To Student Panel", command = Student ,font=custom.CTkFont(family="Times New Roman",size=16), width=100, fg_color="green")
    stud.place(x=200,y=245)
    
    
def Main():
    
    global display
    
    display = custom.CTk()
    display.geometry("800x500+510+195")
    display.resizable(0,0)
    display.title("Dashboard")
    
    title = custom.CTkLabel(display, text="ePUSTAKALAY", text_color='orange', font=custom.CTkFont(size=34, weight="bold", family="Times New Roman"))

    title.pack(padx=12, pady=(25,25))
    title = custom.CTkLabel(display, text="..world of wisdom!", text_color= 'cyan', font= custom.CTkFont(size=18, weight= "bold",family="Times New Roman"))
    title.place(x=350,y=60)
    
    
    frame = custom.CTkFrame(display, height=280,width=600)
    frame.place(x=100,y=100)
    
    title = custom.CTkLabel(frame, text="Enter Credentials To Proceed", font= custom.CTkFont(family="Times New Roman",size=18, weight= "bold"))
    title.place(x=180,y=35)
    
    course = custom.CTkLabel(frame, text="Enter CourseID  : ", font= custom.CTkFont(size=14))
    course.place(x=140,y=100)
    
    global c_id
    
    c_id = custom.CTkEntry(frame, width=150)
    c_id.place(x=300,y=100)
    
    passw = custom.CTkLabel(frame, text="Enter Password  : ", font= custom.CTkFont(size=14))
    passw.place(x=140,y=140)
    
    global u_pass
    
    u_pass = custom.CTkEntry(frame, show = "*" ,width=150)
    u_pass.place(x=300,y=140)
    
    add_placeholder(u_pass,"")
    add_placeholder(c_id,"")
    
    log = custom.CTkButton(frame, text = "Log In" , command=Login , font=custom.CTkFont(size=14), hover_color="orange", width=100)
    log.place(x=160, y=190)
    
    ex = custom.CTkButton(frame, text="Reset", command=Reset, font=custom.CTkFont(size=14), width=100)
    ex.place(x=310,y=190)
    
    reg = custom.CTkLabel(frame, text="Is it your first time here? Click here to Register", font= custom.CTkFont(size=12,family="Times New Roman"), text_color="gray")
    reg.place(x=160,y=230)
    
    def on_enter(e):
        reg.configure(text_color='white', cursor='hand2')

    def on_leave(e):
        reg.configure(text_color='gray', cursor='arrow')

    reg.bind("<Enter>", on_enter)
    reg.bind("<Leave>", on_leave)
    reg.bind("<Button-1>", lambda event: Register())
    
    global admin
    
    admin = custom.CTkButton(display, text="Switch To Admin Panel", command = Admin ,font=custom.CTkFont(size=16,family="Times New Roman"), width=100, fg_color="purple")
    admin.place(x=300,y=420)
    custom.CTkLabel(display, text="Copyright 2023. All Rights Reserved To The Creator", font= custom.CTkFont(family="Times New Roman",size=10, weight= "bold")).place(x=265,y=470)
    display.mainloop()
    
    
def Login():
    courseId = c_id.get()
    coursePass = u_pass.get()

    if courseId == "" or coursePass == "":
        
        messagebox.showwarning("Input","Both Fields Are Required")
    else:
        
        sql = "SELECT courseid,name,course FROM register WHERE courseid = '{}' AND password = '{}'".format(courseId, coursePass)
        cursor.execute(sql)
        result = cursor.fetchall()
        if result:
            crs_Id, stu_Name, stu_Crs = result[0]
            global loginID
            loginID = str(crs_Id)   
            global loginName
            loginName = str(stu_Name)
            global loginCourse
            loginCourse = str(stu_Crs)
            Reset()
            Window()
        else:
            messagebox.showerror("Failed","Invalid ID or Password")
        
def LoginAdmin():
    
    adminId = a_id.get()
    adminCode = a_pass.get()
    
    sql = "SELECT * FROM admin WHERE adminid = '{}' AND passcode = '{}'".format(adminId, adminCode)
    cursor.execute(sql)
    result = cursor.fetchall()
    if result:
        WindowAdmin()
    else:
        messagebox.showerror("Failed","Invalid ID or Password")
    
def Reg():
    
    first = fname.get()
    last = lname.get()
    course = u_course.get()
    password = u_ps.get()
    phone = u_ph.get()
    
    if(first=="" or last=="" or course=="" or password=="" or phone==""):
        messagebox.showwarning("Mandatory Field*","All Fields Are Required")
    else:
        crs_id = random.randint(100000,999999)
        name = (first+" "+last)
        sql = "Insert Into Register Values ({},'{}','{}','{}',{}) ".format(crs_id,name,course,password,phone)
        cursor.execute(sql)
        db1.commit()
        
        crs = str(crs_id)
        
        frame = custom.CTkFrame(app, height=320,width=300)
        frame.place(x=465,y=30)
        frame.configure(fg_color = "black")
        
        msg = custom.CTkLabel(frame, text="--------------------------------------------------", font=custom.CTkFont(size=16))
        msg.place(x=35,y=10)
        msg = custom.CTkLabel(frame, text=" Registered Successfully ", font=custom.CTkFont(family="Times New Roman",size=16))
        msg.place(x=70,y=35)
        msg = custom.CTkLabel(frame, text="--------------------------------------------------", font=custom.CTkFont(size=16))
        msg.place(x=35,y=60)
        
        time = datetime.datetime.now().time()
        current = time.strftime('%H:%M:%S')
        acc = str(current)
        
        custom.CTkLabel(frame, text="Registered As :  ' "+name+" ' ", font=custom.CTkFont(family="Times New Roman",size=14)).place(x=55,y=150)
        custom.CTkLabel(frame, text="Course ID  Is :  ' "+crs+" ' ", font=custom.CTkFont(family="Times New Roman",size=14)).place(x=55,y=180)
        custom.CTkLabel(frame, text="Registered At :  "+acc+" ", font=custom.CTkFont(family="Times New Roman",size=14)).place(x=55,y=120)
        
        custom.CTkLabel(frame, text="Use your above CourseID and Password for Login(s)", font=custom.CTkFont(family="Times New Roman",size=12)).place(x=22,y=260)
        
        fname.delete(0, 'end')
        lname.delete(0, 'end')
        u_ps.delete(0, 'end')
        u_ph.delete(0, 'end')

def Register():
    
    global app
    
    app = custom.CTk()
    app.geometry("800x380+510+290")
    app.resizable(0,0)
    app.title("Registration")
    
    title = custom.CTkLabel(app, text="STUDENT REGISTRATION", font= custom.CTkFont(family="Times New Roman",size=18, weight= "bold"))
    title.place(x=110,y=25)
    
    f = custom.CTkLabel(app, text="Enter First Name  : ", font=custom.CTkFont(size=14))
    f.place(x=65,y=80)
    
    global fname
    
    fname = custom.CTkEntry(app, width=150)
    fname.place(x=250,y=80)
    
    l = custom.CTkLabel(app, text="Enter Last Name : ", font=custom.CTkFont(size=14))
    l.place(x=65,y=120)
    
    global lname

    lname = custom.CTkEntry(app, width=150)
    lname.place(x=250,y=120)
    
    course = custom.CTkLabel(app, text="Select Course Deptt : ", font=custom.CTkFont(size=14))
    course.place(x=65,y=160)
    
    global u_course
    
    u_course = custom.CTkComboBox(app, font=custom.CTkFont(size=14), values=['BCA','BBA','MCA','MBA','Law'], width=150)
    u_course.place(x=250,y=160)

    ps = custom.CTkLabel(app, text="Enter The Password : ", font=custom.CTkFont(size=14))
    ps.place(x=65,y=200)
    
    global u_ps

    u_ps = custom.CTkEntry(app, show = "*", width=150)
    u_ps.place(x=250,y=200)

    ph = custom.CTkLabel(app, text="Enter Phone Number : ", font=custom.CTkFont(size=14))
    ph.place(x=65,y=240)
    
    global u_ph

    u_ph = custom.CTkEntry(app, width=150)
    u_ph.place(x=250,y=240)
    
    add_placeholder(u_ph,"")
    add_placeholder(u_ps,"")
    add_placeholder(lname,"")
    add_placeholder(fname,"")
    
    reg = custom.CTkButton(app, text="Register!",  command=Reg,font=custom.CTkFont(size=14), hover_color="green", width=100)
    reg.place(x=185,y=300)

    app.mainloop() 
    
def Window():
    
    display.withdraw()
    global window
    window = custom.CTk()
    window.geometry("800x480+510+290")
    window.resizable(0,0)
    window.title("StudentPanel")
    
    title = custom.CTkLabel(window, text="ePUSTAKALAY", text_color= 'orange', font= custom.CTkFont(family="Times New Roman",size=18, weight= "bold", ))
    title.pack(padx=12, pady=(15,15))
    title = custom.CTkLabel(window, text="User : "+loginName+" ", font= custom.CTkFont(family="Times New Roman",size=14, weight= "bold"))
    title.place(x=10,y=20)
    
    logout = custom.CTkButton(window, text="Logout", command= lambda:[(display.deiconify()),(window.destroy())], font= custom.CTkFont(family="Times New Roman",size=14), width=60, fg_color="red", hover_color="red")
    logout.place(x=710,y=20)
    
    title =custom.CTkLabel(window, text="Select The Operation, Want To Proceed", font= custom.CTkFont(family="Times New Roman",size=16, weight= "bold"))
    title.place(x=255,y=80)
    
    b1 = custom.CTkButton(window, text="Issue Book", command=IssueBooks , font= custom.CTkFont(size=16,family="Times New Roman"), width=100)
    b1.place(x=170,y=170)
    
    b2 = custom.CTkButton(window, text="Search Books", command=SearchRecord,  font= custom.CTkFont(size=16,family="Times New Roman"), width=100)
    b2.place(x=345,y=170)

    b3 = custom.CTkButton(window, text="Return Book", command=ReturnBooks,  font= custom.CTkFont(size=16,family="Times New Roman"), width=100)
    b3.place(x=530,y=170)
    
    f1 = custom.CTkFrame(window, height=220,width=500)
    f1.place(x=150,y=230)
    
    title =custom.CTkLabel(f1, text="Book-Worm-Zone", font= custom.CTkFont(family="Times New Roman",size=20, weight= "bold"))
    title.place(x=175,y=25)
    title =custom.CTkLabel(f1, text="Getting Bored? Go Get Some Books...", font= custom.CTkFont(family="Times New Roman",size=16))
    title.place(x=140,y=65)
    bot = custom.CTkButton(f1, text = "Explore" ,command=Bot ,font= custom.CTkFont(family="Times New Roman",size=16),width=100, fg_color= "#00A67E", hover_color="#00A67E")
    bot.place(x=200,y=145)
        
    window.mainloop()
    
def WindowAdmin():
    
    global window
    display.withdraw()

    Reset()
    
    window = custom.CTk()
    window.geometry("800x480+510+290")
    window.resizable(0,0)
    window.title("AdminPanel")
    
    title = custom.CTkLabel(window, text="ePUSTAKALAY", text_color= 'orange', font= custom.CTkFont(family="Times New Roman",size=18, weight= "bold", ))
    title.pack(padx=12, pady=(15,15))
    
    logout = custom.CTkButton(window, text="Logout", command= lambda:[(window.destroy(),display.deiconify())], font= custom.CTkFont(family="Times New Roman",size=14), width=60, fg_color="red", hover_color="red")
    logout.place(x=710,y=20)

    title =custom.CTkLabel(window, text="Select The Operation, Want To Proceed", font= custom.CTkFont(family="Times New Roman",size=16, weight= "bold"))
    title.place(x=255,y=80)
    
    b1 = custom.CTkButton(window, text="Add Book", command=AddBooks , font= custom.CTkFont(size=16,family="Times New Roman"), width=100)
    b1.place(x=170,y=170)
    b2 = custom.CTkButton(window, text="Search Books", command=SearchRecord,  font= custom.CTkFont(size=16,family="Times New Roman"), width=100)
    b2.place(x=345,y=170)
    b3 = custom.CTkButton(window, text="Delete Book", command=DeleteBooks,  font= custom.CTkFont(size=16,family="Times New Roman"), width=100)
    b3.place(x=530,y=170)
    b4 = custom.CTkButton(window, text="Issue Records", command=IssueRecord,  font= custom.CTkFont(size=16,family="Times New Roman"), width=120)
    b4.place(x=235,y=240)
    b5 = custom.CTkButton(window, text="Return Records", command=ReturnRecord,  font= custom.CTkFont(size=16,family="Times New Roman"), width=120)
    b5.place(x=440,y=240)
    
    window.mainloop()  

Main()
