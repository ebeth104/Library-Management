# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 11:25:16 2022

@author: elisa
"""

from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import tkinter
import mysql.connector

class LibraryManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title = "Library Management System"
        self.root.geometry("1580x800+0+0")
        
        #============================Variable=====================================================================
        self.member_var=StringVar()
        self.reg_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.bookgenre_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()

        lbtitle = Label(self.root, bd ="10", relief = GROOVE, text = "LIBRARY MANAGEMENT SYSTEM", fg = "Brown", bg = "#FFFF7F" ,font = ("garamond",50,"bold"))
        lbtitle.pack(side=TOP,fill=X)
        
        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=90, width=1279, height=400)
        
        # ========================DateFrame Left==================================================================
        
        DataFrameLeft=LabelFrame(frame, bd=10, text = "Library Memebership Information", fg = "Black", bg = "#FFFF7F" ,font = ("garamond",20,"bold"))
        DataFrameLeft.place(x=-14, y=5, width=710, height=365)
        
        lblmember=Label(DataFrameLeft, bg="#FFFF7F", text = "Member type", font = ("garamond",15,"bold"), padx=2, pady=6 )
        lblmember.grid(row=0, column=0, sticky=W)
        
        comMember=ttk.Combobox(DataFrameLeft, textvariable=self.member_var, font = ("garamond",15,"bold"), width=20, state="readonly")
        comMember["value"]=("Admin","Student","Lecturer")
        comMember.grid(row=0, column=1)
        
        lblPRN_No=Label(DataFrameLeft, bg="#FFFF7F", text = "Reg_N", font = ("garamond",15,"bold"), padx=2, pady=6)
        lblPRN_No.grid(row=1, column=0, sticky=W)
        txtPRN_No=Entry(DataFrameLeft, textvariable=self.reg_var, font = ("garamond",16,"bold"), width=20)
        txtPRN_No.grid(row=1, column=1)
        
        lblTitle=Label(DataFrameLeft, bg="#FFFF7F", text = "ID:", font = ("garamond",15,"bold"), padx=2, pady=6)
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle=Entry(DataFrameLeft, textvariable=self.id_var, font = ("garamond",16,"bold"), width=20)
        txtTitle.grid(row=2, column=1)
        
        lblFirstName=Label(DataFrameLeft, bg="#FFFF7F", text = "First Name", font = ("garamond",15,"bold"), padx=2, pady=6)
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName=Entry(DataFrameLeft, textvariable=self.firstname_var, font = ("garamond",16,"bold"), width=20)
        txtFirstName.grid(row=3, column=1)
        
        lblLastName=Label(DataFrameLeft, bg="#FFFF7F", text = "Last Name", font = ("garamond",15,"bold"), padx=2, pady=6)
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName=Entry(DataFrameLeft, textvariable=self.lastname_var, font = ("garamond",16,"bold"), width=20)
        txtLastName.grid(row=4, column=1)
        
        lblAddress1=Label(DataFrameLeft, bg="#FFFF7F", text = "Address 1", font = ("garamond",15,"bold"), padx=2, pady=6)
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAddress1=Entry(DataFrameLeft, textvariable=self.address1_var, font = ("garamond",16,"bold"), width=20)
        txtAddress1.grid(row=5, column=1)
        
        lblAddress2=Label(DataFrameLeft, bg="#FFFF7F", text = "Address 2", font = ("garamond",15,"bold"), padx=2, pady=6)
        lblAddress2.grid(row=6, column=0, sticky=W)
        txtAddress2=Entry(DataFrameLeft, textvariable=self.address2_var, font = ("garamond",16,"bold"), width=20)
        txtAddress2.grid(row=6, column=1)
        
        lblMobile=Label(DataFrameLeft, bg="#FFFF7F", text = "Mobile No:", font = ("garamond",15,"bold"), padx=2, pady=6)
        lblMobile.grid(row=7, column=0, sticky=W)
        txtMobile=Entry(DataFrameLeft, textvariable=self.mobile_var, font = ("garamond",16,"bold"), width=20)
        txtMobile.grid(row=7, column=1)
        
        lblBookID=Label(DataFrameLeft, bg="#FFFF7F", text = "Book ID", font = ("garamond",15,"bold"), padx=2, pady=6)
        lblBookID.grid(row=0, column=2, sticky=W)
        txtBookID=Entry(DataFrameLeft, textvariable=self.bookid_var, font = ("garamond",16,"bold"), width=20)
        txtBookID.grid(row=0, column=3)
        
        lblBookTitle=Label(DataFrameLeft, bg="#FFFF7F", text = "Book Title", font = ("garamond",15,"bold"), padx=2, pady=6)
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle=Entry(DataFrameLeft, textvariable=self.booktitle_var, font = ("garamond",16,"bold"), width=20)
        txtBookTitle.grid(row=1, column=3)
        
        lblBookGenre=Label(DataFrameLeft, bg="#FFFF7F", text = "Book Genre", font = ("garamond",15,"bold"), padx=2, pady=6)
        lblBookGenre.grid(row=2, column=2, sticky=W)
        txtBookGenre=Entry(DataFrameLeft, textvariable=self.bookgenre_var, font = ("garamond",16,"bold"), width=20)
        txtBookGenre.grid(row=2, column=3)
        
        lblAuthor=Label(DataFrameLeft, bg="#FFFF7F", text = "Author Name", font = ("garamond",15,"bold"), padx=2, pady=6)
        lblAuthor.grid(row=3, column=2, sticky=W)
        txtAuthor=Entry(DataFrameLeft, textvariable=self.author_var, font = ("garamond",16,"bold"), width=20)
        txtAuthor.grid(row=3, column=3)
        
        lblB_Date=Label(DataFrameLeft, bg="#FFFF7F", text = "Date Borrowed:", font = ("garamond",15,"bold"), padx=2, pady=6)
        lblB_Date.grid(row=4, column=2, sticky=W)
        txtB_Date=Entry(DataFrameLeft, textvariable=self.dateborrowed_var, font = ("garamond",16,"bold"), width=20)
        txtB_Date.grid(row=4, column=3)
        
        lblD_Date=Label(DataFrameLeft, bg="#FFFF7F", text = "Date Due:", font = ("garamond",15,"bold"), padx=2, pady=6)
        lblD_Date.grid(row=5, column=2, sticky=W)
        txtD_Date=Entry(DataFrameLeft, textvariable=self.datedue_var, font = ("garamond",16,"bold"), width=20)
        txtD_Date.grid(row=5, column=3)
        
        lblLateReturnFine=Label(DataFrameLeft, bg="#FFFF7F", text = "Late Return Fine", font = ("garamond",15,"bold"), padx=2, pady=6)
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft, textvariable=self.latereturnfine_var, font = ("garamond",16,"bold"), width=20)
        txtLateReturnFine.grid(row=6, column=3)
        
        lblDateOverDue=Label(DataFrameLeft, bg="#FFFF7F", text = "Date Over Due:", font = ("garamond",15,"bold"), padx=2, pady=6)
        lblDateOverDue.grid(row=7, column=2, sticky=W)
        txtDateOverDue=Entry(DataFrameLeft, textvariable=self.dateoverdue_var, font = ("garamond",16,"bold"), width=20)
        txtDateOverDue.grid(row=7, column=3)
        
        # ========================DateFrame Right=================================================================
        
        DataFrameRight=LabelFrame(frame, bd=10, text = "Book Details", fg = "Black", bg = "#FFFF7F" ,font = ("garamond",20,"bold"))
        DataFrameRight.place(x=695, y=5, width=538, height=365)
        
        self.txtBox=Text(DataFrameRight, font = ("garamond",16,"bold"), width=29, height=12, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)
        
        listScrollbar=Scrollbar(DataFrameRight, orient = "vertical")
        listScrollbar.grid(row=0, column=1, sticky="ns")
        
        listScrollbar=Scrollbar(DataFrameRight, orient = "horizontal")
        listScrollbar.grid(row=1, column=0, sticky="ns")
        
        listbooks=['Data Smart','Integration of the Indian States','Slaughterhouse Five','Structure & Interpretation of Computer Programs',
                   'Analysis Vol I','The Complete Sherlock Holmes - Vol I','The Complete Sherlock Holmes - Vol II','Jurassic Park','Econometric Analysis',
                   'Angels & Demons','Crime and Punishment','The Last Mughal','Free Will','The Theory of Everything','Murder on the Orient Express','Diary of a Young Girl']
        
        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="Data Smart"):
                self.bookid_var.set("198574")
                self.booktitle_var.set("Data Smart")
                self.bookgenre_var.set("Data Science")
                self.author_var.set("John W. Foreman")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs. 25")
                self.dateoverdue_var.set("NO")
                
            elif (x=="Integration of the Indian States"):
                self.bookid_var.set("167846")
                self.booktitle_var.set("Integration of the Indian States")
                self.bookgenre_var.set("History")
                self.author_var.set("V. P. Menon")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs. 25")
                self.dateoverdue_var.set("NO")
                
            elif (x=="Slaughterhouse Five"):
                self.bookid_var.set("142947")
                self.booktitle_var.set("Slaughterhouse Five")
                self.bookgenre_var.set("Fiction")
                self.author_var.set("Kurt Vonnegut")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs. 25")
                self.dateoverdue_var.set("NO")
                
            elif (x=="Structure & Interpretation of Computer Programs"):
                self.bookid_var.set("195430")
                self.booktitle_var.set("Structure & Interpretation of Computer Programs")
                self.bookgenre_var.set("CS")
                self.author_var.set("Gerald Jay Sussman")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs. 25")
                self.dateoverdue_var.set("NO")
                
            elif (x=="Analysis Vol I"):
                self.bookid_var.set("231065")
                self.booktitle_var.set("Analysis Vol I")
                self.bookgenre_var.set("Data Science")
                self.author_var.set("Terence Tao")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs. 25")
                self.dateoverdue_var.set("NO")
                
            elif (x=="The Complete Sherlock Holmes - Vol I"):
                self.bookid_var.set("162846")
                self.booktitle_var.set("The Complete Sherlock Holmes - Vol I")
                self.bookgenre_var.set("Fiction")
                self.author_var.set("Arthur Conan Doyle")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs. 25")
                self.dateoverdue_var.set("NO")  
                
            elif (x=="The Complete Sherlock Holmes - Vol II"):
                self.bookid_var.set("162847")
                self.booktitle_var.set("The Complete Sherlock Holmes - Vol II")
                self.bookgenre_var.set("Fiction")
                self.author_var.set("Arthur Conan Doyle")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs. 25")
                self.dateoverdue_var.set("NO")
                
            elif (x=="Jurassic Park"):
                self.bookid_var.set("716340")
                self.booktitle_var.set("Jurassic Park")
                self.bookgenre_var.set("Fiction")
                self.author_var.set("Michael Crichton")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs. 25")
                self.dateoverdue_var.set("NO")
                
            elif (x=="Econometric Analysis"):
                self.bookid_var.set("476208")
                self.booktitle_var.set("Econometric Analysis")
                self.bookgenre_var.set("Economics")
                self.author_var.set("William H. Greene")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs. 25")
                self.dateoverdue_var.set("NO")
                
            elif (x=="Angels & Demons"):
                self.bookid_var.set("230934")
                self.booktitle_var.set("Angels & Demons")
                self.bookgenre_var.set("Fiction")
                self.author_var.set("Dan Brown")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs. 25")
                self.dateoverdue_var.set("NO")
                
            elif (x=="Crime and Punishment"):
                self.bookid_var.set("369045")
                self.booktitle_var.set("Crime and Punishment")
                self.bookgenre_var.set("Fiction")
                self.author_var.set("Fyodor Dostoevskey")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs. 25")
                self.dateoverdue_var.set("NO")
                
            elif (x=="The Last Mughal"):
                self.bookid_var.set("476208")
                self.booktitle_var.set("The Last Mughal")
                self.bookgenre_var.set("History")
                self.author_var.set("William Dalrymple")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs. 25")
                self.dateoverdue_var.set("NO")
                
            elif (x=="Free Will"):
                self.bookid_var.set("230945")
                self.booktitle_var.set("Free Will")
                self.bookgenre_var.set("Philosophy")
                self.author_var.set("Sam Harris")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs. 25")
                self.dateoverdue_var.set("NO")
                
            elif (x=="The Theory of Everything"):
                self.bookid_var.set("546038")
                self.booktitle_var.set("The Theory of Everything")
                self.bookgenre_var.set("Physics")
                self.author_var.set("Stephen Hawking")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs. 25")
                self.dateoverdue_var.set("NO")
                
            elif (x=="Murder on the Orient Express"):
                self.bookid_var.set("426947")
                self.booktitle_var.set("Murder on the Orient Express")
                self.bookgenre_var.set("Fiction")
                self.author_var.set("Agatha Christie")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs. 25")
                self.dateoverdue_var.set("NO")
                
            elif (x=="Diary of a Young Girl"):
                self.bookid_var.set("836045")
                self.booktitle_var.set("Diary of a Young Girl")
                self.bookgenre_var.set("Biography")
                self.author_var.set("Anne Frank")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs. 25")
                self.dateoverdue_var.set("NO")
        
        listBox=Listbox(DataFrameRight, font = ("garamond",16,"bold"), width=20, height=12)
        listBox.bind("<<ListboxSelect>>", SelectBook)
        listBox.grid(row=0,column=0, padx=0)
        listScrollbar.config(command=listBox.yview)
        listScrollbar.config(command=listBox.xview)
        
        for item in listbooks:
            listBox.insert(END,item)
        
        # ========================Buttons Frame=====================================================================
        
        FrameButton=Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameButton.place(x=0, y=475, width=1279, height=70)
        
        btnShowData=Button(FrameButton, command=self.show_Data, text="Show Data", font=("garamond",16,"bold"), width=16, fg = "white", bg = "saddle brown")
        btnShowData.grid(row=0,column=0)
        
        btnAddData=Button(FrameButton, command=self.add_Data, text="Add Data", font=("garamond",16,"bold"), width=16, fg = "white", bg = "saddle brown")
        btnAddData.grid(row=0,column=1)
        
        btnUpdateData=Button(FrameButton, command=self.update, text="Update Data", font=("garamond",16,"bold"), width=16, fg = "white", bg = "saddle brown")
        btnUpdateData.grid(row=0,column=2)
        
        btnDeleteData=Button(FrameButton, command=self.delete_Data, text="Delete Data", font=("garamond",16,"bold"), width=16, fg = "white", bg = "saddle brown")
        btnDeleteData.grid(row=0,column=3)
        
        btnReset=Button(FrameButton, command=self.reset, text="Reset", font=("garamond",16,"bold"), width=16, fg = "white", bg = "saddle brown")
        btnReset.grid(row=0,column=4)
        
        btnExit=Button(FrameButton, command=self.iExit, text="Exit", font=("garamond",16,"bold"), width=16, fg = "white", bg = "saddle brown")
        btnExit.grid(row=0,column=5)
        
        # ========================Informations Frame====================================================================
         
        FrameDetails=Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=544, width=1279, height=110)
        
        Table_frame=Frame(FrameDetails, bd=6, relief=RIDGE, padx=20, bg="powder blue")
        Table_frame.place(x=-10, y=2, width=1230, height=85)
        
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.library_table=ttk.Treeview(Table_frame,column=("membertype","regn","id","firstname","lastname","address1","address2","mobile","bookid",
                                                            "booktitle","bookgenre","author","dateborrowed","datedue","latereturnfine","dateoverdue"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        self.library_table.heading("membertype", text="Member Type")
        self.library_table.heading("regn", text="Reg_N")
        self.library_table.heading("id", text="ID")
        self.library_table.heading("firstname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("address1", text="Address 1")
        self.library_table.heading("address2", text="Address 2")
        self.library_table.heading("mobile", text="Mobile")
        self.library_table.heading("bookid", text="Book ID")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("bookgenre", text="Book Genre")
        self.library_table.heading("author", text="Author")
        self.library_table.heading("dateborrowed", text="Date Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("latereturnfine", text="Late Return Fine")
        self.library_table.heading("dateoverdue", text="Date Over Due")
        
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)
        
        self.library_table.column("membertype", width=100)
        self.library_table.column("regn", width=100)
        self.library_table.column("id", width=100)
        self.library_table.column("firstname", width=100)
        self.library_table.column("lastname", width=100)
        self.library_table.column("address1", width=100)
        self.library_table.column("address2", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("bookid", width=100)
        self.library_table.column("booktitle", width=100)
        self.library_table.column("bookgenre", width=100)
        self.library_table.column("author", width=100)
        self.library_table.column("dateborrowed", width=100)
        self.library_table.column("datedue", width=100)
        self.library_table.column("latereturnfine", width=100)
        self.library_table.column("dateoverdue", width=100)
        
        self.fetch_Data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)
    
    def add_Data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="elib20#", database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                          self.member_var.get(),
                                                                                                          self.reg_var.get(),
                                                                                                          self.id_var.get(),
                                                                                                          self.firstname_var.get(),
                                                                                                          self.lastname_var.get(),
                                                                                                          self.address1_var.get(),
                                                                                                          self.address2_var.get(),
                                                                                                          self.mobile_var.get(),
                                                                                                          self.bookid_var.get(),
                                                                                                          self.booktitle_var.get(),
                                                                                                          self.bookgenre_var.get(),
                                                                                                          self.author_var.get(),
                                                                                                          self.dateborrowed_var.get(),
                                                                                                          self.datedue_var.get(),
                                                                                                          self.latereturnfine_var.get(),
                                                                                                          self.dateoverdue_var.get()  
                                                                                                          ))
        conn.commit()
        conn.close()
        self.fetch_Data()
        messagebox.showinfo("Success","Member has been inserted successfully")
    
    def update(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="elib20#", database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,Mobile=%s,BookID=%s,BookTitle=%s,BookGenre=%s,Author=%s,DateBorrowed=%s,DateDue=%s,LateReturnFine=%s,DateOverDue=%s where Reg_N=%s",(
                            self.member_var.get(),
                            self.id_var.get(),
                            self.firstname_var.get(),
                            self.lastname_var.get(),
                            self.address1_var.get(),
                            self.address2_var.get(),
                            self.mobile_var.get(),
                            self.bookid_var.get(),
                            self.booktitle_var.get(),
                            self.bookgenre_var.get(),
                            self.author_var.get(),
                            self.dateborrowed_var.get(),
                            self.datedue_var.get(),
                            self.latereturnfine_var.get(),
                            self.dateoverdue_var.get(),
                            self.reg_var.get()
                            ))
        conn.commit()
        self.fetch_Data()
        self.reset()
        conn.close()
        
        messagebox.showinfo("Success","Data has been updated")
    
    def fetch_Data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="elib20#", database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows = my_cursor.fetchall()
        
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END, values=i)
            conn.commit()    
        conn.close()
    
    def get_cursor(self, event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']
        
        self.member_var.set(row[0]),
        self.reg_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.mobile_var.set(row[7]),
        self.bookid_var.set(row[8]),
        self.booktitle_var.set(row[9]),
        self.bookgenre_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.latereturnfine_var.set(row[14]),
        self.dateoverdue_var.set(row[15])
    
    def show_Data(self):
        self.txtBox.insert(END, "Memeber Type : \t\t"+ self.member_var.get() + "\n")
        self.txtBox.insert(END, "Reg N : \t\t"+ self.reg_var.get() + "\n")
        self.txtBox.insert(END, "ID : \t\t"+ self.id_var.get() + "\n")
        self.txtBox.insert(END, "First Name : \t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END, "Last Name : \t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END, "Address 1 : \t\t"+ self.address1_var.get() + "\n")
        self.txtBox.insert(END, "Address 2 : \t\t"+ self.address2_var.get() + "\n")
        self.txtBox.insert(END, "Mobile : \t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END, "Book ID : \t\t"+ self.bookid_var.get() + "\n")
        self.txtBox.insert(END, "Book Title : \t\t"+ self.booktitle_var.get() + "\n")
        self.txtBox.insert(END, "Book Genre : \t\t"+ self.bookgenre_var.get() + "\n")
        self.txtBox.insert(END, "Author : \t\t"+ self.author_var.get() + "\n")
        self.txtBox.insert(END, "Date Borrowed : \t\t"+ self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END, "Date Due : \t\t"+ self.datedue_var.get() + "\n")
        self.txtBox.insert(END, "Late Return Fine : \t\t"+ self.latereturnfine_var.get() + "\n")
        self.txtBox.insert(END, "Date Over Due : \t\t"+ self.dateoverdue_var.get() + "\n")
    
    def reset(self):
        self.member_var.set(""),
        self.reg_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.bookgenre_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set("")
        self.txtBox.delete("1.0",END)
    
    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management","Do you wish to exit?")
        if iExit>0:
            self.root.destroy()
            return
    
    def delete_Data(self):
        if self.reg_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First enter Reg_No and ID")
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="elib20#", database="mydata")
            my_cursor=conn.cursor()
            query="delete from library where Reg_N=%s"
            value=(self.reg_var.get(),)
            my_cursor.execute(query,value)
            
            conn.commit()
            self.fetch_Data()
            self.reset()
            conn.close()
            
            messagebox.showinfo("Success","Data has been deleted")
    
root = Tk()
ob = LibraryManagementSystem(root)
root = mainloop()