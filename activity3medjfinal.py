from tkinter import*
import sqlite3

root=Tk()
root.title('vince project')
root.geometry ("500x500")

conn=sqlite3.connect ('mydata.db')

c=conn.cursor()


def submit():
    conn=sqlite3.connect('C:/Users/User/Documents/mydata.db')
    c=conn.cursor()
    c.execute("INSERT INTO mydata VALUES(:f_name,:L_name,:age,:address,:email)",
              {
                  'f_name':f_name.get(),
                  'L_name':L_name.get(),
                  'age':age.get(),
                  'address':address.get(),
                  'email':email.get(),
                  })
    conn.commit()  
    conn.close()

    f_name.delete(0,END)
    L_name.delete (0,END)
    age.delete (0,END)
    address.delete (0,END)
    email.delete (0,END)

def query():
        conn=sqlite3.connect('C:/Users/User/Documents/mydata.db')
        c=conn.cursor()
        c.execute("SELECT *,oid FROM mydata")
        records=c.fetchall()

        print_records=''
        for record in records:
            print_records+=str(record[0])+" "+str(record[1])+" "+str(record[2])+" "+str(record[3])+" "+(record[4])+" "+"\t"+str(record[5])+"\n"
           
        query_label=Label(root,text=print_records)
        query_label.grid(row=30,column=0,columnspan=2)

        conn.commit()
        conn.close()
                                                                                     
'''
c.execute("""CREATE TABLE "mydata" (
"f_name" TEXT,
"L_name" TEXT,
"age" INTEGER,
"address" TEXT,
"email" TEXT
)""")
'''

def delete():

    conn=sqlite3.connect("C:/Users/User/Documents/mydata.db")

    c=conn.cursor()

    c.execute("DELETE from mydata WHERE oid="+delete_box.get())
             
    delete_box.delete(0,END)    
   
    conn.commit()  
    conn.close()


def edit():
    editor = Tk()
    editor.title('Update Record from Database')
    editor.geometry("500x500")

    conn = sqlite3.connect('C:/Users/User/Documents/mydata.db')
    c = conn.cursor()

    record_id = delete_box.get()

    if not record_id.isdigit():
        error_label = Label(editor, text="Please enter a valid ID number.")
        error_label.grid(row=0, column=0, columnspan=2)
        return

    c.execute("SELECT * FROM mydata WHERE oid=?", (record_id,))
    record = c.fetchone()

    if not record:
        error_label = Label(editor, text="Record not found!")
        error_label.grid(row=0, column=0, columnspan=2)
        return

    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, pady=(10, 0))
    f_name_editor.insert(0, record[0])

    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, padx=10, pady=(10, 0))

   
    L_name_editor = Entry(editor, width=30)
    L_name_editor.grid(row=1, column=1, pady=(10, 0))
    L_name_editor.insert(0, record[1])

    L_name_label = Label(editor, text="Last Name")
    L_name_label.grid(row=1, column=0, padx=10, pady=(10, 0))

   
    age_editor = Entry(editor, width=30)
    age_editor.grid(row=2, column=1, pady=(10, 0))
    age_editor.insert(0, record[2])

    age_label = Label(editor, text="Age")
    age_label.grid(row=2, column=0, padx=10, pady=(10, 0))

 
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=3, column=1, pady=(10, 0))
    address_editor.insert(0, record[3])

    address_label = Label(editor, text="Address")
    address_label.grid(row=3, column=0, padx=10, pady=(10, 0))


    email_editor = Entry(editor, width=30)
    email_editor.grid(row=4, column=1, pady=(10, 0))
    email_editor.insert(0, record[4])

    email_label = Label(editor, text="Email")
    email_label.grid(row=4, column=0, padx=10, pady=(10, 0))

    def save_update():
        updated_f_name = f_name_editor.get()
        updated_L_name = L_name_editor.get()
        updated_age = age_editor.get()
        updated_address = address_editor.get()
        updated_email = email_editor.get()

        c.execute('''UPDATE mydata SET
                        f_name = ?, L_name = ?, age = ?, address = ?, email = ?
                        WHERE oid = ?''',
        (updated_f_name, updated_L_name, updated_age, updated_address, updated_email, record_id))

        conn.commit()
        conn.close()

        editor.destroy()

        query()

    save_btn = Button(editor, text="Save Changes", command=save_update)
    save_btn.grid(row=5, column=0, columnspan=2, pady=20, padx=10, ipadx=104)

    editor.mainloop()



def update():

    conn=sqlite3.connect("C:/Users/User/Documents/mydata.db")

    c=conn.cursor()

    record_id=delete_box.get()
    c.execute(""" UPDATE mydata SET
        f_name=:first,
        L_name:last,
        age=:age,
        address=:address,
        email=:email,

        WHERE old=:oid"""),
    (
        'first',f_name_editor.get(),
        'last',L_name_editor.get(),
        'age',age_editor.get(),
        'address',address_editor.get(),
        'email',email_editor.get(),
        'oid',record_id
        )


   
    conn.commit()  
    conn.close()

f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)
L_name=Entry (root,width=30)
L_name.grid(row=1,column=1,padx=20)
age=Entry(root,width=30)
age.grid(row=2,column=1,padx=20)
address=Entry(root,width=30)
address.grid(row=3,column=1,padx=20)
email=Entry(root,width=30)
email.grid (row=4,column=1,padx=20)
delete_box=Entry(root,width=30)
delete_box.grid(row=10,column=1,padx=30)

f_name_label=Label(root,text="First Name")
f_name_label.grid(row=0,column=0)
L_name_label=Label(root,text= "Last Name")
L_name_label.grid(row=1,column=0)
age_label=Label(root,text= "Age")
age_label.grid(row=2,column=0)
address_label=Label(root,text= "Address")
address_label.grid(row=3,column=0)
email_label=Label(root,text= "Email")
email_label.grid(row=4,column=0)

delete_box_label=Label(root,text="Select ID No.")
delete_box_label.grid(row=10,column=0)

submit_btn=Button(root,text= "Add Record to Database",command=submit)
submit_btn.grid(row=6,column=0,columnspan=2, pady=10, padx=10, ipadx=100)

query_btn=Button(root,text= "Show records",command=query)
query_btn.grid (row=7,column=0,columnspan=2, pady=10, padx=10, ipadx=137)

query_btn=Button(root,text="Delete Records",command=delete)
query_btn.grid(row=12,column=0,columnspan=2,pady=10,padx=10,ipadx=136)

update_btn=Button(root,text="Edit Records",command=edit)
update_btn.grid(row=13,column=0,columnspan=2,pady=10,padx=10,ipadx=140)


conn.commit()
conn.close()

root.mainloop()                


