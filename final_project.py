import mysql.connector as conn
from tkinter import *
from tkinter import messagebox

app=Tk()
db=conn.connect(host="localhost", user="root", password="123456", database="Admission")
app.title("COLLEGE MANAGEMENT SYSTEM")
app.geometry("500x400")
app.configure(bg='#585858')

admission_data={}
reg_no=1100

name_entry=None
age_entry=None
course_entry=None

available_books={"Python Programming": "MK Singh",
      "Data Structure": "Jenni Stuart",
      "Science": "Martha Linda",
      "Mathematics": "John Berry"}
regi_entry=None
books_entry=None

rg_entry=NONE
pay_entry=None
total_entry=None

def account():
     
    global name_entry,age_entry,course_entry
    
    acont=Toplevel(app)
    acont.title("Account Office")
    acont.geometry("400x400")
    acont.configure(bg="#a65959")
    
    
    
    head=Label(acont, text="WELCOME TO ACCOUNT OFFICE", bg="#e61919", fg="white", font="Helvetica,30" ,width=60)
    head.pack(pady=20)
    
    name=Label(acont, text="Name", bg="#e61919", fg="white", font="Helvetica,20",width=10)
    name.place(x=70, y=70)
    name_entry=Entry(acont, bg='#ffe6e6', width=20)
    name_entry.place(x=180, y=70)
    
    age=Label(acont, text="Age", bg="#e61919", fg="white", font="Helvetica,20",width=10)
    age.place(x=70, y=110)
    age_entry=Entry(acont, bg='#ffe6e6', width=20)
    age_entry.place(x=180, y=110)
    
    course=Label(acont, text="Course", bg="#e61919", fg="white", font="Helvetica,20",width=10)
    course.place(x=70, y=150)
    course_entry=Entry(acont, bg='#ffe6e6', width=20)
    course_entry.place(x=180,y=150)
    
    submit=Button(acont, text="Submit",bg="#e61919", fg="white", font="Helvetica,20",width=10, command=submitt)
    submit.pack(pady=140)
    

def submitt(): 
    global reg_no
    name=name_entry.get()
    age=age_entry.get()
    course=course_entry.get()
    
    if name==" " and age==" " and course==" ":
        messagebox.showerror("Input Error","Please fill this field")
    
   
    reg_no+=1
    admission_data[reg_no]={'Name': name, 'Age': age, 'Course': course} 
     
    # messagebox.showinfo(f"{name} is registered with Reg_no.: {reg_no}")
    
    cursor=db.cursor()
    insert_data='insert into student1122(id,name,age,course) values(%s, %s, %s, %s)'
    values=(reg_no,name,age,course)
    cursor.execute(insert_data,values)
    db.commit()
    cursor.close()
    messagebox.showinfo("Admission successful",f"{name} is registered with Reg_no.: {reg_no}")
    
    
def library():
    global admission_data
    global regi_entry,books_entry
    
    libry=Toplevel(app)
    libry.title("Library ")
    libry. geometry("400x400")
    libry.configure(bg='#666699') 
     
    welcme=Label(libry, text="WELCOME TO THE LIBRARY" ,bg='#29293d', fg='white', font='Helvetica,20', width=60)
    welcme.pack(pady=20)
    
    regi_no=Label(libry, text="Enter Registration no. ", bg="#29293d", fg='white', font='Helvetica,20')
    regi_no.pack(pady=10)
    regi_entry=Entry(libry, bg='#f0f0f5', width=20)
    regi_entry.pack()
    
    book_name=Label(libry, text="Book Name", bg="#29293d", fg='white', font='Helvetica,20')
    book_name.pack(pady=10)
    books_entry=Entry(libry,  bg='#f0f0f5', width=20)
    books_entry.pack()
    
    issue=Button(libry, text="Issue Book" , bg="#52527a", fg='white', font='Helvetica,20', command=issue_book)
    issue.pack(pady=10)
    
    retun=Button(libry, text="Return Book" ,bg="#52527a", fg='white', font='Helvetica,20', command=return_book)
    retun.pack(pady=5)

def issue_book():
    regi_no=regi_entry.get()
    books_name=books_entry.get()
    if books_name in available_books:
          messagebox.showinfo("Issue Book", f"{books_name} is issued to student with Registration No: {regi_no}")
    else:
          messagebox.showerror("Error", f"Sorry, {books_name} is not available.")
      
def return_book():
    regi_no=regi_entry.get()
    books_name=books_entry.get()
    if books_name in available_books:
          messagebox.showinfo("Issue Book", f"{books_name} is returned by student with Registration No: {regi_no}")
    else:
          messagebox.showerror("Error", f"Sorry, {books_name} is not found.")
          
          
          
    
def fees():
    
    global rg_entry,pay_entry,total_entry
    
    fee=Toplevel(app)
    fee.title("Fees Clearance")
    fee.geometry("400x400")
    fee.configure(bg="#392613")
    
    welce=Label(fee, text="FEES PAYEMENT" , bg="#d2a679", fg="black", font="Verdana,30", width=60)
    welce.pack(pady=20)    
    
    rg_no=Label(fee, text="Please Enter Your Registration no.: ", bg="#d2a679", fg="black", font="Verdana,30")
    rg_no.pack(pady=20)
    rg_entry=Entry(fee, bg="#e6ccb3", width=35)
    rg_entry.pack()
    
    total_fee=Label(fee, text="Enter total fees :", bg="#d2a679", fg="black", font="Verdana,30")
    total_fee.pack(pady=20)
    total_entry=Entry(fee, bg="#e6ccb3", width=30)
    total_entry.pack()
    
    paymnt=Label(fee, text="Enter the fees paid by Student: ", bg="#d2a679", fg="black", font="Verdana,30")
    paymnt.pack(pady=20)
    pay_entry=Entry(fee, bg="#e6ccb3", width=30)
    pay_entry.pack()
    
    btn=Button(fee, text="Submit", bg="#c68c53", fg="black", font="Verdana,30", command=calulate)
    btn.pack(pady=20)
    
def calulate():
    rg_no=rg_entry.get()
    paymnt=float(pay_entry.get())
    total_fee=float(total_entry.get())
    
    
    if paymnt<total_fee:
        result=total_fee-paymnt
        messagebox.showinfo("Payment",f"Remaining balance : {result}")
    
    else:
        messagebox.showerror("MESSAGE","Balance Cleared....")
       
    
        
    
    
    

well=Label(app, text="WELCOME TO COLLEGE MANAGEMENT SYSTEM", font='arial,10',fg='white',bg='#282828')
well.pack(pady=20)
choose=Label(app, text="Choose an Option : ", bg='#080808', font='Impact,30', fg='White')
choose.pack(pady=20)

acount=Button(app, text="Account Office", bg='#080808', font='Impact,30', fg='White',command=account)
acount.pack(pady=5)

libray=Button(app, text="  Library  ", bg='#080808', font='Impact,30', fg='White', command=library)
libray.pack(pady=5)

fees_pay=Button(app, text="  Clearance  ", bg='#080808', font='Impact,30', fg='White', command=fees)
fees_pay.pack(pady=5)
    

app.mainloop()