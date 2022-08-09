from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class BillClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Stockpile Management System")
        self.root.config(bg="white")

        #===title===#
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Stockpile Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #===title====
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=0,height=50,width=150)
        
        #====clock====
        self.lbl_clock=Label(self.root,text="Welcome To Stockpile Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
#==============product frame===========
        Product_frame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Product_frame1.place(x=6,y=110,width=410,height=550)

        pTitle=Label(Product_frame1,text="All Products",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
#=====================prod search frame==================
        self.var_search=StringVar()
        Product_frame2=Frame(Product_frame1,bd=2,relief=RIDGE,bg="white")
        Product_frame2.place(x=2,y=42,width=398,height=90) 

        lbl_search=Label(Product_frame2,text="Search Product | By Name",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)
        
        lbl_search=Label(Product_frame2,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=2,y=45)
        txt_search=Entry(Product_frame2,textvariable=self.var_search,font=("times new roman",15),bg="lightyellow").place(x=128,y=47,width=150,height=22)
        btn_search=Button(Product_frame2,text="Search",command=self.search,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=285,y=45,width=100,height=25)
        btn_show_all=Button(Product_frame2,text="Show All",command=self.show,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=285,y=10,width=100,height=25)
        
        productFrame3=Frame(Product_frame1,bd=3,relief=RIDGE)
        productFrame3.place(x=2,y=140,width=398,height=375)

        scrolly=Scrollbar(productFrame3,orient=VERTICAL)
        scrollx=Scrollbar(productFrame3,orient=HORIZONTAL)

        self.product_Table=ttk.Treeview(productFrame3,columns=("pid","name","price","quantity","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)

        self.product_Table.heading("pid",text="P ID")
        self.product_Table.heading("name",text="Name")
        self.product_Table.heading("price",text="Price")
        self.product_Table.heading("quantity",text="Quantity")
        self.product_Table.heading("status",text="Status")
        self.product_Table["show"]="headings"

        self.product_Table.column("pid",width=40)
        self.product_Table.column("name",width=100)
        self.product_Table.column("price",width=100)
        self.product_Table.column("quantity",width=40)
        self.product_Table.column("status",width=90)
        self.product_Table.pack(fill=BOTH,expand=1)
        #self.product_Table.bind("<ButtonRelease-1>",self.get_data)
        lbl_note=Label(Product_frame1,text="Note: 'Enter 0 quantity to remove product from the cart'",font=("goudy old style",12),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)
      

        #==========customer frame=====================
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        Customerframe=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Customerframe.place(x=420,y=110,width=530,height=70)
        
        cTitle=Label(Customerframe,text="Customer Details",font=("goudy old style",15),bg="lightgrey").pack(side=TOP,fill=X)
        lbl_name=Label(Customerframe,text="Name",font=("times new roman",15),bg="white").place(x=5,y=35)
        txt_name=Entry(Customerframe,textvariable=self.var_cname,font=("times new roman",13),bg="lightyellow").place(x=80,y=35,width=180)
        
        lbl_contact=Label(Customerframe,text="Contact No",font=("times new roman",15),bg="white").place(x=270,y=35)
        txt_contact=Entry(Customerframe,textvariable=self.var_contact,font=("times new roman",13),bg="lightyellow").place(x=380,y=35,width=140)
        Cal_Cart_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Cal_Cart_frame.place(x=420,y=190,width=530,height=360)
         
        #=============Calculator Frame=========================
        self.var_cal_input=StringVar() 
        
        Cal_frame=Frame(Cal_Cart_frame,bd=9,relief=RIDGE,bg="white")
        Cal_frame.place(x=5,y=10,width=268,height=340)


        txt_cal_input=Entry(Cal_frame,textvariable=self.var_cal_input,font=('arial',15,'bold'),width=21,bd=10,relief=GROOVE,state='readonly',justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)

        btn_7=Button(Cal_frame,text='7',font=('arial',15,'bold'),command=lambda:self.get_input(7),bd=5,width=4,pady=10,cursor='hand2').grid(row=1,column=0)
        btn_8=Button(Cal_frame,text='8',font=('arial',15,'bold'),command=lambda:self.get_input(8),bd=5,width=4,pady=10,cursor='hand2').grid(row=1,column=1)
        btn_9=Button(Cal_frame,text='9',font=('arial',15,'bold'),command=lambda:self.get_input(9),bd=5,width=4,pady=10,cursor='hand2').grid(row=1,column=2)
        btn_sum=Button(Cal_frame,text='+',font=('arial',15,'bold'),command=lambda:self.get_input('+'),bd=5,width=4,pady=10,cursor='hand2').grid(row=1,column=3)
        btn_4=Button(Cal_frame,text='4',font=('arial',15,'bold'),command=lambda:self.get_input(4),bd=5,width=4,pady=10,cursor='hand2').grid(row=2,column=0)
        btn_5=Button(Cal_frame,text='5',font=('arial',15,'bold'),command=lambda:self.get_input(5),bd=5,width=4,pady=10,cursor='hand2').grid(row=2,column=1)
        btn_6=Button(Cal_frame,text='6',font=('arial',15,'bold'),command=lambda:self.get_input(6),bd=5,width=4,pady=10,cursor='hand2').grid(row=2,column=2)
        btn_sub=Button(Cal_frame,text='-',font=('arial',15,'bold'),command=lambda:self.get_input('-'),bd=5,width=4,pady=10,cursor='hand2').grid(row=2,column=3)
        btn_1=Button(Cal_frame,text='1',font=('arial',15,'bold'),command=lambda:self.get_input(1),bd=5,width=4,pady=10,cursor='hand2').grid(row=3,column=0)
        btn_2=Button(Cal_frame,text='2',font=('arial',15,'bold'),command=lambda:self.get_input(2),bd=5,width=4,pady=10,cursor='hand2').grid(row=3,column=1)
        btn_3=Button(Cal_frame,text='3',font=('arial',15,'bold'),command=lambda:self.get_input(3),bd=5,width=4,pady=10,cursor='hand2').grid(row=3,column=2)
        btn_mul=Button(Cal_frame,text='*',font=('arial',15,'bold'),command=lambda:self.get_input('*'),bd=5,width=4,pady=10,cursor='hand2').grid(row=3,column=3)
        btn_0=Button(Cal_frame,text='0',font=('arial',15,'bold'),command=lambda:self.get_input(0),bd=5,width=4,pady=15,cursor='hand2').grid(row=4,column=0)
        btn_c=Button(Cal_frame,text='c',font=('arial',15,'bold'),command=self.clear_cal,bd=5,width=4,pady=15,cursor='hand2').grid(row=4,column=1)
        btn_eq=Button(Cal_frame,text='=',font=('arial',15,'bold'),command=self.perform_cal,bd=5,width=4,pady=15,cursor='hand2').grid(row=4,column=2)
        btn_div=Button(Cal_frame,text='/',font=('arial',15,'bold'),command=lambda:self.get_input('/'),bd=5,width=4,pady=15,cursor='hand2').grid(row=4,column=3)
        
        cart_frame=Frame(Cal_Cart_frame,bd=3,relief=RIDGE)
        cart_frame.place(x=280,y=8,width=245,height=342)

        cartTitle=Label(cart_frame,text="Cart \t Total Product: [0]",font=("goudy old style",15),bg="lightgrey").pack(side=TOP,fill=X)

        scrolly=Scrollbar(cart_frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_frame,orient=HORIZONTAL)

        self.cart_Table=ttk.Treeview(cart_frame,columns=("pid","name","price","quantity","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.cart_Table.xview)
        scrolly.config(command=self.cart_Table.yview)

        self.cart_Table.heading("pid",text="P ID")
        self.cart_Table.heading("name",text="Name")
        self.cart_Table.heading("price",text="Price")
        self.cart_Table.heading("quantity",text="Qty")
        self.cart_Table.heading("status",text="Status")
        self.cart_Table["show"]="headings"

        self.cart_Table.column("pid",width=40)
        self.cart_Table.column("name",width=100)
        self.cart_Table.column("price",width=90)
        self.cart_Table.column("quantity",width=40)
        self.cart_Table.column("status",width=90)
        self.cart_Table.pack(fill=BOTH,expand=1)
        #self.cart_Table.bind("<ButtonRelease-1>",self.get_data)
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()

        Add_CartWidgetsFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Add_CartWidgetsFrame.place(x=420,y=550,width=530,height=110)
    
        lbl_p_name=Label(Add_CartWidgetsFrame,text="product name",font=("times new roman",15),bg="white").place(x=5,y=5)     
        txt_p_name=Entry(Add_CartWidgetsFrame,textvariable=self.var_pname,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=5,y=35,width=190,height=22)

        lbl_p_price=Label(Add_CartWidgetsFrame,text="Price Per Qty",font=("times new roman",15),bg="white").place(x=230,y=5)     
        txt_p_price=Entry(Add_CartWidgetsFrame,textvariable=self.var_price,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=230,y=35,width=150,height=22)     

        lbl_p_qty=Label(Add_CartWidgetsFrame,text="Quantity",font=("times new roman",15),bg="white").place(x=390,y=5)     
        txt_p_qty=Entry(Add_CartWidgetsFrame,textvariable=self.var_qty,font=("times new roman",15),bg="lightyellow",).place(x=390,y=35,width=120,height=22)               
        
        self.lbl_instock=Label(Add_CartWidgetsFrame,text="In stock [9999]",font=("times new roman",15),bg="white")
        self.lbl_instock.place(x=5,y=70)     

        btn_clear_cart=Button(Add_CartWidgetsFrame,text="Clear",font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=180,y=70,width=150,height=30)
        btn_add_cart=Button(Add_CartWidgetsFrame,text="Add | Update Cart",font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=340,y=70,width=180,height=30)
        
        #===============billing area==================
        billFrame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        billFrame.place(x=953,y=110,width=410,height=410)

        BTitle=Label(billFrame,text="Customer Bill Area",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)

        self.txt_bill_area=Text(billFrame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)
        #=============billing area==========================
        billFrame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        billFrame.place(x=953,y=110,width=410,height=410)

        BTitle=Label(billFrame,text="Customer Bill Area",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        self.txt_bill_area=Text(billFrame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)

        #=========billing buttons=============
        billMenuFrame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        billMenuFrame.place(x=953,y=520,width=410,height=140)

        self.lbl_amnt=Label(billMenuFrame,text='Bill Amount\n[0]',font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white")
        self.lbl_amnt.place(x=2,y=5,width=120,height=70)

        self.lbl_discount=Label(billMenuFrame,text='Discount\n[5%]',font=("goudy old style",15,"bold"),bg="#8bc34a",fg="white")
        self.lbl_discount.place(x=124,y=5,width=120,height=70)

        self.lbl_net_pay=Label(billMenuFrame,text='Net Pay\n[0]',font=("goudy old style",15,"bold"),bg="#607d8b",fg="white")
        self.lbl_net_pay.place(x=246,y=5,width=120,height=70)

        btn_print=Button(billMenuFrame,text='Print',cursor='hand2',font=("goudy old style",15,"bold"),bg="lightgreen",fg="white")
        btn_print.place(x=2,y=80,width=120,height=70)

        btn_clear_all=Button(billMenuFrame,text='Clear All',cursor='hand2',font=("goudy old style",15,"bold"),bg="gray",fg="white")
        btn_clear_all.place(x=124,y=80,width=120,height=70)

        btn_generate=Button(billMenuFrame,text='Generate/Save Bill',cursor='hand2',font=("goudy old style",15,"bold"),bg="#009688",fg="white")
        btn_generate.place(x=246,y=80,width=120,height=70)

        #================Footer===========================
        footer=Label(self.root,text="SMS-Stockpile Management System | For Any Technical Issue Contact :998xxxxx30",font=("times new roman",11),bg="#4d636d",fg="white",bd=0,cursor="hand2").pack(side=BOTTOM,fill=X)
        self.show()





        #all functions of calculator====================

    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)

    def clear_cal(self):
        self.var_cal_input.set('')

    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

    def show(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            cur.execute("Select pid,name,price,quantity,status from product")
            rows=cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def search(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error"," Search input must be required",parent=self.root)
            else:
                cur.execute("Select pid,name,price,quantity,status from product where name Like '%"+self.var_search.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_Table.delete(*self.product_Table.get_children())
                    for row in rows:
                        self.product_Table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)




if __name__=="__main__":
    root=Tk()
    obj=BillClass(root)
    root.mainloop()