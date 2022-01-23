#MODULES

from tkinter import *
from tkinter import ttk,messagebox
import csv,os.path,pymongo
from time import strftime
from datetime import date , datetime
from random import randint


#DATABASE
myclient=pymongo.MongoClient("mongodb://localhost:27017/")

#WINDOW
window=Tk()
window.title("Login")
#window.geometry("690x750")
window.resizable(0,0)



#FUNCTIONS

def togetdate():
    today = date.today()
    return today


def togettime():
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    return time

def reset():
    username.delete(0,END)
    password.delete(0,END)
    messagebox.showinfo("Reset","Fields Has Been Reset..!")


def signup():
    root=Toplevel()
    root.title("SignUp From")
    #root.geometry("1400x730")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    size=str(screen_width)+'x'+str(screen_height)
    root.geometry(size)
    root.resizable(0,0)
    root.overrideredirect(True)
    registerimage=PhotoImage(file="images/register.png")
    resetimage=PhotoImage(file="images/reset.png")
    backto=PhotoImage(file="images/back.png")
    exitimage=PhotoImage(file="images/exit.png")
    bgimage=PhotoImage(file="images/bg.png")
    bg=Label(root,image=bgimage)
    bg.pack()
    signupframe=LabelFrame(bg,bg="white",width=1300,height=600,bd=0).place(x=50,y=50)
    lefticon=PhotoImage(file='images/xx.png')
    v=Label(root,image=lefticon,bd=0).place(x=50,y=52)
    '''rocket=PhotoImage(file='images/logo_white.png')
    vv=Label(root,image=rocket,bd=0,bg="blue").place(x=70,y=72)'''
    signuplabel=Label(root,text="SIGNUP HERE",font=("Rockwell Extra Bold",23,"bold"),bg='white',fg='Red').place(x=870,y=100)

    def quitt():
        root.destroy()

    def final(firstname,lastname,mobilenumber,username,password,gender):
        pop=Toplevel()
        pop.title("Confirmation")
        pop.geometry("610x610")
        pop.resizable(0,0)
        pop.config(bg="yellow")

        def close():
            pop.destroy()

        def togetdate():
            today = date.today()
            return str(today)


        def togettime():
            now = datetime.now()
            time = now.strftime("%H:%M:%S")
            return str(time)

        def create(firstname,lastname,mobilenumber,username,password,gender):         
            mydb=myclient["LIBRARY"]
            mytable=mydb["user_details"]  
            data={"USERNAME":username,"PASSWORD":password,"first_name":firstname,"last_name":lastname,"mobile":mobilenumber,"gender":gender,"DATE":str(togetdate()),"TIME":str(togettime())}
            mytable.insert_one(data)

            messagebox.showinfo("Done","Account Created Successfully.!",parent=pop)
            pop.destroy()
            
            
            

        Label(pop,text='    Confirm Your details',bg="yellow",fg="BLUE",font=("Berlin Sans FB Demi",30,"bold")).grid(row=0,column=0,columnspan=4)
        Label(pop,text='',bg="yellow",fg="BLUE",font=("Berlin Sans FB Demi",20,"bold")).grid(row=1,column=0,columnspan=4)
        Label(pop,text='  Name :',bg="yellow",fg="red",font=("Rockwell",18,"bold")).grid(sticky=W,row=2,column=0)
        Label(pop,text=firstname+" "+lastname,bg="yellow",fg="black",font=("Agency FB",20,"bold")).grid(sticky=W,row=2,column=2)
        Label(pop,text='  Mobile Number :',bg="yellow",fg="red",font=("Rockwell",18,"bold")).grid(sticky=W,row=3,column=0)
        Label(pop,text=mobilenumber,bg="yellow",fg="black",font=("Agency FB",20,"bold")).grid(sticky=W,row=3,column=2)
        Label(pop,text='  Username :',bg="yellow",fg="red",font=("Rockwell",18,"bold")).grid(sticky=W,row=4,column=0)
        Label(pop,text=username,bg="yellow",fg="black",font=("Agency FB",20,"bold")).grid(sticky=W,row=4,column=2)
        Label(pop,text='  Password :',bg="yellow",fg="red",font=("Rockwell",18,"bold")).grid(sticky=W,row=5,column=0)  
        Label(pop,text=password,bg="yellow",fg="black",font=("Agency FB",20,"bold")).grid(sticky=W,row=5,column=2)

        Label(pop,text='  Gender :',bg="yellow",fg="red",font=("Rockwell",18,"bold")).grid(sticky=W,row=6,column=0)  
        Label(pop,text=gender,bg="yellow",fg="black",font=("Agency FB",20,"bold")).grid(sticky=W,row=6,column=2)


        Label(pop,text='  Date Of Account Creation : ',bg="yellow",fg="red",font=("Rockwell",18,"bold")).grid(sticky=W,row=7,column=0)
        Label(pop,text=togetdate()+"  "+togettime(),bg="yellow",fg="black",font=("Agency FB",20,"bold")).grid(sticky=W,row=7,column=2)
        
        Label(pop,text='',bg="yellow",fg="red",font=("Rockwell",18,"bold")).grid(sticky=W,row=9,column=0)
        Label(pop,text='',bg="yellow",fg="red",font=("Rockwell",18,"bold")).grid(sticky=W,row=10,column=0)
        Button(pop,text='Create Account ',cursor="hand2",bg="Black",fg="white",font=("Rockwell",18,"bold"),command=lambda:create(firstname,lastname,mobilenumber,username,password,gender)).grid(sticky=N,row=11,column=0)
        Button(pop,text='   Retry   ',cursor="hand2",bg="Black",fg="white",font=("Rockwell",18,"bold"),command=close).grid(sticky=N,row=11,column=2)



                
        pop.mainloop()

    
    def reset():
        username.delete(0,END)
        password.delete(0,END)
        captcaentry.delete(0,END)
        mobilenumber.delete(0,END)
        lastname.delete(0,END)
        firstname.delete(0,END)
        messagebox.showinfo("Reset","Fields Has Been Reset..!",parent=root)
        mobilenumber.insert(0,'+91-')


    def signup(captcavalue,captcaentry,firstname,lastname,mobilenumber,username,password,gender,verify,verifyy):
        if verify==1:
            if captcavalue==str(captcaentry):
                if len(firstname) != 0 and firstname.isalpha():
                    if len(lastname) != 0 and lastname.isalpha():
                        if len(mobilenumber)!= 0 and mobilenumber[4:].isdigit() and len(mobilenumber)==14:
                            if len(username)!= 0 and username.isalnum():
                                if len(gender)!= 0 and gender !="Select Any One":
                                    if verifyy == "XYZ":
                                        usernames=[]
                                        mydb=myclient["LIBRARY"]
                                        mytable=mydb["user_details"]
                                        data=mytable.find()
                                        for i in data:
                                            usernames.append(i["USERNAME"])
                                        if username not in usernames:
                                            final(firstname,lastname,mobilenumber,username,password,gender)
                                        else:
                                            messagebox.showwarning("ERROR","Username Already Exixts.!",parent=root)

                                    else:
                                         messagebox.showwarning("ERROR","Please Enter Correct Verification code.!",parent=root)                              
                                        
                                else:
                                    messagebox.showwarning("ERROR","Please Enter Proper Gender.!",parent=root)
                            else:
                                messagebox.showwarning("ERROR","Please Enter Username.!",parent=root)
                        else:
                            messagebox.showwarning("ERROR","Please Enter Proper Mobilenumber.!",parent=root)
                    else:
                        messagebox.showwarning("ERROR","Please Enter Lastname.!",parent=root)
                else:
                    messagebox.showwarning("ERROR","Please Enter Firstname.!",parent=root)
            else:
                messagebox.showwarning("ERROR","CAPTCHA ERROR",parent=root)
        else:
             messagebox.showwarning("ERROR","You Have Not Agreed To Our Policy",parent=root)      


    #firstname label------------------------
    firstnamelable=Label(root,text="FIRST NAME:",font=("Bahnschrift",12,"bold"),bg='white',fg="blue").place(x=700,y=170)

    #firstname entery-----------------------
    firstname=Entry(root,width=20,bg="silver",font=(8),fg="black")
    firstname.place(x=700,y=195)

    #lastname label------------------------
    lastnamelable=Label(root,text="LAST NAME:",font=("Bahnschrift",12,"bold"),bg='white',fg="blue").place(x=1050,y=170)

    #lasttname entery-----------------------
    lastname=Entry(root,width=20,bg="silver",font=(8),fg="black")
    lastname.place(x=1050,y=195)

    #mobile label------------------------
    mobilenumberlable=Label(root,text="MOBILE NUMBER:",font=("Bahnschrift",12,"bold"),bg='white',fg="blue").place(x=700,y=235)

    #mobilenumber entery-----------------------
    mobilenumber=Entry(root,width=20,bg="silver",font=(8),fg="black")
    mobilenumber.insert(0,"+91-")
    mobilenumber.place(x=700,y=260)
    
    #gender lable ---------------------------
    genderlable=Label(root,text="GENDER:",font=("Bahnschrift",12,"bold"),bg='white',fg="blue").place(x=1050,y=240)

    #genderentery-----------------------
    clicker=StringVar()
    clicker.set("Select Any One")
    gender=OptionMenu(root,clicker,"Male","Female","Other")
    gender.place(x=1050,y=262)
    gender.config(bg="silver", fg="blue")
    gender["menu"].config(bg="Yellow")

    #captca label------------------------
    Captcalable=Label(root,text="CAPTCHA:",font=("Bahnschrift",12,"bold"),bg='white',fg="blue").place(x=1050,y=305)
    captcavalue=str(randint(1000,5000))
    captca=Label(root,text=captcavalue,font=("Rockwell",20,"bold"),bg='blue',fg="white").place(x=1100,y=335)

    #captcaentery-----------------------
    captcaentry=Entry(root,width=20,bg="silver",font=(8),fg="black")
    captcaentry.place(x=1050,y=385)

    #username label------------------------
    usernamelable=Label(root,text="USERNAME:",font=("Bahnschrift",12,"bold"),bg='white',fg="blue").place(x=700,y=300)


    #usernameentery-----------------------
    username=Entry(root,width=20,bg="silver",font=(8),fg="black")
    username.place(x=700,y=325)


    #password label------------------------
    passwordlable=Label(root,text="PASSWORD:",font=("Bahnschrift",12,"bold"),bg='white',fg="blue").place(x=700,y=363)

    #passwordentery-----------------------
    password=Entry(root,width=20,bg="silver",font=(8),fg="black")
    password.place(x=700,y=390)

    #verify label------------------------
    verifylable=Label(root,text="VERIFICATION CODE:",font=("Bahnschrift",12,"bold"),bg='white',fg="blue").place(x=700,y=440)

    #verifyentery-----------------------
    verifyy=Entry(root,width=10,bg="silver",font=(8),fg="brown")
    verifyy.place(x=860,y=440)

    #agreement------------------
    cb = IntVar()
    cb.set(0)
    verify=Checkbutton(root,variable=cb,text="Yes, I Agree To All The Terms & Conditions",font=("Bahnschrift",12,"bold"),onvalue=1,offvalue=0).place(x=700,y=490)
    

    signupbutton=Button(root,cursor="hand2", image=registerimage,command= lambda : signup(captcavalue,captcaentry.get(),firstname.get(),lastname.get(),mobilenumber.get(),username.get(),password.get(),clicker.get(),cb.get(),verifyy.get()),bd=0)
    signupbutton.place(x=800,y=540)

    resetbutton=Button(root,cursor="hand2",image=resetimage,command=reset,bd=0)
    resetbutton.place(x=1050,y=530)

    exitbutton=Button(root,cursor="hand2",image=exitimage,command=quitt,bd=0)
    exitbutton.place(x=1200,y=595) 

    root.mainloop()
    

def login(usernamee,passwordd):
    mydb=myclient["LIBRARY"]
    mytable=mydb["user_details"]
    a=int(mytable.estimated_document_count())

    if a!=0:
        if len(usernamee) !=0 :
            if len(passwordd) !=0 :
                alllogintry(usernamee,passwordd)
                mydb=myclient["LIBRARY"]
                mytable=mydb["user_details"]
                data=mytable.find_one({"USERNAME":usernamee,"PASSWORD":passwordd})
                
                if data==None:
                    intro="Username And Password Did Not Matched"
                    messagebox.showerror("Login",intro)

                else:
                    logindetails(usernamee)
                    username.delete(0,END)
                    password.delete(0,END)
                    mainwindow()

            else:
                messagebox.showwarning("WARNING","Please Enter Password.!")
        
        else:
            messagebox.showwarning("WARNING","Please Enter UserName.!")
    else:
        messagebox.showinfo("NO PRE-EXISTING DATA","No Pre-exesting username And Password Found!.\n\nCreate New profile")

def alllogintry(username,password):
    mydb=myclient["LIBRARY"]
    mytable=mydb["all_logins_attempts"]  
    data={"USERNAME":username,"PASSWORD":password,"DATE":str(togetdate()),"TIME":str(togettime())}
    mytable.insert_one(data)

def logindetails(username):
    mydb=myclient["LIBRARY"]
    mytable=mydb["login_details"]  
    data={"USERNAME":username,"DATE":str(togetdate()),"TIME":str(togettime())}
    mytable.insert_one(data)
    

def quit():
    window.quit()


#main program section =================================================================
def mainwindow():
    main=Tk()
    main.title("Login")
    main.geometry("1600x900")


    def boo():
        pass

    def submitbook(admissionnumber,bookid):
        mydb=myclient["LIBRARY"]
        mytable=mydb["allissuedbooks"] 
        query={"admission_number":str(admissionnumber),"book_id":str(bookid)}

        data=mytable.delete_one(query)
        a=data.deleted_count
        
        deleteee()
        issuedetail(admissionnumber)
        if a>0:
            messagebox.showinfo("Submitted","Successfully Submited")
        
        
    
    def issuedetail(admissionnumber):
        
        mydb=myclient["LIBRARY"]
        mytable=mydb["allissuedbooks"]  
        data=mytable.find({"admission_number":admissionnumber})
        
        xx,xx2,yy=20,110,190
        count=0
        for i in data:
            a=Label(disframe,text=i["book_id"],bg="grey",fg="yellow",font=('Consolas',14,'bold'))
            a.place(x=xx,y=yy)
            b=Label(disframe,text=i["book_name"],bg="grey",fg="yellow",font=('Consolas',13,'bold'))
            b.place(x=xx2,y=yy)
            yy=yy+40
            count=count+1
                        

        '''cancelbtn=Button(main,cursor="hand2",text="RESET",bg="blue",fg="white" ,font = ('calibri',10, 'bold'),command=deleteee,height=2,width=16,bd=1)
        cancelbtn.place(x=1340,y=770)'''

        if count==10:
            messagebox.showwarning("ALERT","10 Books already issued",parent=main)
            issue_btn["state"]=DISABLED
            return "nomore"
        elif count<10:
            issue_btn["state"]=NORMAL
            

    def deleteee():
            try:
                for label in disframe.children.values(): 
                    label.destroy()
                

            except RuntimeError:
                deleteee()

    def addbook():
        newbook=Toplevel()
        newbook.geometry("700x800")
        newbook.title("Add New Books")

        def reset():
            bookid.delete(0,END)
            classs.delete(0,END)
            category.delete(0,END)
            bookname.delete(0,END)
            authorname.delete(0,END)
            date_of_publish.delete(0,END)
            totalpage.delete(0,END)
            comment.delete(0,END)

        def addbook(bookid,classs,category,bookname,authorname,date_of_publish,totalpage,comment):
            mydb=myclient["LIBRARY"]
            mytable=mydb["allbooks"]
            book={"book_id":bookid,"class":classs,"category":category,"book_name":bookname,"author_name":authorname,"date_of_publish":date_of_publish,"total_pages":totalpage,"comment":comment}

            mytable.insert_one(book)
            messagebox.showinfo("Done","Book Added Successfully.!",parent=newbook)
            reset()






        bgimage=PhotoImage(file="images/bg.png")
        bg=Label(newbook,image=bgimage)
        bg.pack()

        a1=Frame(newbook,height=700,width=590,bg="white")
        a1.place(x=50,y=50)

        introlabel=Label(newbook,text="ADD BOOK HERE",font=("Rockwell Extra Bold",23,"bold"),bg='white',fg='blue')
        introlabel.place(x=55,y=55)

        # bookid section ------------------------------------------        
        bookidlable=Label(newbook,text="Book Id :",font=("Bahnschrift",15,"bold"),bg='white')
        bookidlable.place(x=55,y=110)
        bookid=Entry(newbook,width=30,bg="yellow",font=(8),fg="blue")
        bookid.place(x=290,y=117)

        # class & category sector------------------------------------------
        classslable=Label(newbook,text="Class :",font=("Bahnschrift",15,"bold"),bg='white')
        classslable.place(x=55,y=150)
        classs=Entry(newbook,width=10,bg="yellow",font=(8),fg="blue")
        classs.place(x=290,y=157)

        categorylable=Label(newbook,text="Category :",font=("Bahnschrift",15,"bold"),bg='white')
        categorylable.place(x=420,y=151)
        category=Entry(newbook,width=8,bg="yellow",font=(8),fg="blue")
        category.place(x=530,y=157)
        
        #bookname section ---------------------------------------------------------
        booknamelable=Label(newbook,text="Book Name :",font=("Bahnschrift",15,"bold"),bg='white')
        booknamelable.place(x=55,y=190)
        bookname=Entry(newbook,width=30,bg="yellow",font=(8),fg="blue")
        bookname.place(x=290,y=197)

        #author's name section-----------------------------------------------------------
        authornamelable=Label(newbook,text="Author's Name :",font=("Bahnschrift",15,"bold"),bg='white')
        authornamelable.place(x=55,y=230)
        authorname=Entry(newbook,width=30,bg="yellow",font=(8),fg="blue")
        authorname.place(x=290,y=237)

        #date of publish section-----------------------------------------------------------
        date_of_publishlable=Label(newbook,text="Date Of Publish :",font=("Bahnschrift",15,"bold"),bg='white')
        date_of_publishlable.place(x=55,y=270)
        date_of_publish=Entry(newbook,width=30,bg="yellow",font=(8),fg="blue")
        date_of_publish.place(x=290,y=277)

        #total page section-----------------------------------------------------------
        totalpagelable=Label(newbook,text="Total Pages :",font=("Bahnschrift",15,"bold"),bg='white')
        totalpagelable.place(x=55,y=310)
        totalpage=Entry(newbook,width=30,bg="yellow",font=(8),fg="blue")
        totalpage.place(x=290,y=317)

        #Comment section---------------------------------------------------------------------
        commentlable=Label(newbook,text="Additional Information :",font=("Bahnschrift",15,"bold"),bg='white')
        commentlable.place(x=55,y=350)
        comment=Entry(newbook,width=30,bg="yellow",font=(8),fg="blue")
        comment.place(x=290,y=357)

        #buttons section-------------------------------------------------------------------------
        addbutton=Button(newbook,text="ADD",command=lambda:addbook(bookid.get(),classs.get(),category.get(),bookname.get(),authorname.get(),date_of_publish.get(),totalpage.get(),comment.get()),cursor="hand2",bd=3)
        addbutton.place(x=200,y=475)

        resetbutton=Button(newbook,text="RESET",command=reset,cursor="hand2",bd=3)
        resetbutton.place(x=365,y=472)

        newbook.mainloop()

    def allbooks():
        allbook=Toplevel()
        allbook.geometry("1800x800")
        allbook.title("All Books")
        allbook.config(bg="white")

        tv=ttk.Treeview(allbook, show='headings',height=25)
        tv["columns"]=("","Serial Number","Book Id","Book Name","Class","Category","Author's Name","Date Of Publish","Total Pages","Comment")

        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")

        tv.column('#0',width=0,stretch=NO)
        tv.column("Serial Number",anchor=CENTER,width=100)
        tv.column("Book Id",anchor=CENTER,width=110)
        tv.column("Book Name",anchor=CENTER,width=300)
        tv.column("Class",anchor=CENTER,width=150)
        tv.column("Category",anchor=CENTER,width=150)
        tv.column("Author's Name",anchor=CENTER,width=150)
        tv.column("Date Of Publish",anchor=CENTER,width=150)
        tv.column("Total pages",anchor=CENTER,width=150)
        tv.column("Comment",anchor=CENTER,width=500)

        tv.heading("#0",text='',anchor=CENTER)
        tv.heading("Serial Number",text='Serial Number',anchor=CENTER)
        tv.heading("Book Number",text='Book Number',anchor=CENTER)
        tv.heading("Book Name",text="Book Name",anchor=CENTER)
        tv.heading("Class",text="Class",anchor=CENTER)
        tv.heading("Category",text="Category",anchor=CENTER)
        tv.heading("Author's Name",text="Date Of Birth",anchor=CENTER)
        tv.heading("Date Of Publish",text="Date Of Publish",anchor=CENTER)
        tv.heading("Total pages",text="Total pages",anchor=CENTER)
        tv.heading("Comments",text="Comments",anchor=CENTER)

        mydb=myclient["LIBRARY"]
        mytable=mydb["allbooks"]
        data=mytable.find({})
        c=0
        for i in data:
            print(i)
            tv.insert(parent='',index= c,iid=c,text='',values=(str(c),i["book_id"],i["book_name"],i["class"],i["category"],i["author_name"],i["date_of_publish"],i["total_pages"],i["comment"]))
            c=c+1

        Button(viewallstudents, text="Show Selected").pack()

        allbook.mainloop()

    def newtudent():
        addnewstudent=Toplevel()
        addnewstudent.geometry("700x800")
        addnewstudent.title("Add Student")
        
        def action(studentname,classs,section,fathername,mothername,dob,admissionnumber,address):
            with open("resources/allstudentrecord.csv","a",newline="") as myfile:
                csvw=csv.writer(myfile)
                lisss=[admissionnumber,studentname,fathername,mothername,dob,address,date.today(),strftime('%H:%M:%S %p')]
                csvw.writerow(lisss)
                
            with open("resources/classrecord.csv","a",newline="") as ffile:
                csvw=csv.writer(ffile)
                lis=[admissionnumber,classs,section]
                csvw.writerow(lis)

            messagebox.showinfo("Done","Record Added Successfully.!",parent=addnewstudent)

        def resetbtn():
            studentname.delete(0,END)
            classs.delete(0,END)
            section.delete(0,END)
            fathername.delete(0,END)
            mothername.delete(0,END)
            dob.delete(0,END)
            admissionnumber.delete(0,END)
            address.delete(0,END)

        # background for this window-----------------------
        bgimage=PhotoImage(file="images/newstudentbg.png")
        bg=Label(addnewstudent,image=bgimage)
        bg.pack()

        a1=Frame(addnewstudent,height=700,width=590,bg="white")
        a1.place(x=50,y=50)

        introlabel=Label(addnewstudent,text="ADD DETAILS HERE",font=("Rockwell Extra Bold",23,"bold"),bg='white',fg='blue')
        introlabel.place(x=55,y=55)

        # studentname section ------------------------------------------        
        studentnamelable=Label(addnewstudent,text="Student Name :",font=("Bahnschrift",15,"bold"),bg='white')
        studentnamelable.place(x=55,y=110)
        studentname=Entry(addnewstudent,width=30,bg="yellow",font=(8),fg="blue")
        studentname.place(x=250,y=117)

        # class & section sector------------------------------------------
        classslable=Label(addnewstudent,text="Class :",font=("Bahnschrift",15,"bold"),bg='white')
        classslable.place(x=55,y=150)
        classs=Entry(addnewstudent,width=10,bg="yellow",font=(8),fg="blue")
        classs.place(x=250,y=157)

        sectionlable=Label(addnewstudent,text="Section :",font=("Bahnschrift",15,"bold"),bg='white')
        sectionlable.place(x=365,y=151)
        section=Entry(addnewstudent,width=8,bg="yellow",font=(8),fg="blue")
        section.place(x=450,y=157)
        
        #father's name section ---------------------------------------------------------
        fathernamelable=Label(addnewstudent,text="Father's Name :",font=("Bahnschrift",15,"bold"),bg='white')
        fathernamelable.place(x=55,y=190)
        fathername=Entry(addnewstudent,width=30,bg="yellow",font=(8),fg="blue")
        fathername.place(x=250,y=197)

        #mother's name section-----------------------------------------------------------
        mothernamelable=Label(addnewstudent,text="Mothers's Name :",font=("Bahnschrift",15,"bold"),bg='white')
        mothernamelable.place(x=55,y=230)
        mothername=Entry(addnewstudent,width=30,bg="yellow",font=(8),fg="blue")
        mothername.place(x=250,y=237)

        #date of birth section-----------------------------------------------------------
        doblable=Label(addnewstudent,text="Date Of Birth :",font=("Bahnschrift",15,"bold"),bg='white')
        doblable.place(x=55,y=270)
        dob=Entry(addnewstudent,width=30,bg="yellow",font=(8),fg="blue")
        dob.place(x=250,y=277)

        #admission number section-----------------------------------------------------------
        admissionnumberlable=Label(addnewstudent,text="Admission Number :",font=("Bahnschrift",15,"bold"),bg='white')
        admissionnumberlable.place(x=55,y=310)
        admissionnumber=Entry(addnewstudent,width=30,bg="yellow",font=(8),fg="blue")
        admissionnumber.place(x=250,y=317)

        #address section---------------------------------------------------------------------
        addressable=Label(addnewstudent,text="Address :",font=("Bahnschrift",15,"bold"),bg='white')
        addressable.place(x=55,y=350)
        address=Entry(addnewstudent,width=30,bg="yellow",font=(8),fg="blue")
        address.place(x=250,y=357)

        #buttons section-------------------------------------------------------------------------
        addbutton=Button(addnewstudent,text="ADD",cursor="hand2",bd=3,command=lambda:action(studentname.get(),classs.get(),section.get(),fathername.get(),mothername.get(),dob.get(),admissionnumber.get(),address.get()))
        addbutton.place(x=200,y=475)

        resetbutton=Button(addnewstudent,text="RESET",command=resetbtn,cursor="hand2",bd=3)
        resetbutton.place(x=365,y=472)


        addnewstudent.mainloop()

    def viewallstudents():
        viewallstudents=Toplevel()
        viewallstudents.geometry('1800x800')
        viewallstudents.title("All Student Records")
        viewallstudents.config(bg="white")

        def show_selected():
            print(tv.selection())


        '''def update_item():
            selected = tv.focus()
            temp = tv.item(selected, 'values')
            sal_up = float(temp[0]) + 500
            tv.item(selected, values=(sal_up, temp[1], temp[2], temp[3], temp[4], temp[5], temp[6], temp[7]))'''

        tv=ttk.Treeview(viewallstudents, show='headings',height=25)
        tv["columns"]=("Serial Number","Admission Number","Student Name","Father's Name","Mother's Name","Date Of Birth","Address","Account Creation Time")

        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")

        tv.column('#0',width=0,stretch=NO)
        tv.column("Serial Number",anchor=CENTER,width=100)
        tv.column("Admission Number",anchor=CENTER,width=110)
        tv.column("Student Name",anchor=CENTER,width=150)
        tv.column("Father's Name",anchor=CENTER,width=150)
        tv.column("Mother's Name",anchor=CENTER,width=150)
        tv.column("Date Of Birth",anchor=CENTER,width=150)
        tv.column("Address",anchor=CENTER,width=500)
        tv.column("Account Creation Time",anchor=CENTER,width=150)

        tv.heading("#0",text='',anchor=CENTER)
        tv.heading("Serial Number",text='Serial Number',anchor=CENTER)
        tv.heading("Admission Number",text='Admission Number',anchor=CENTER)
        tv.heading("Student Name",text='Student Name',anchor=CENTER)
        tv.heading("Father's Name",text="Father's Name",anchor=CENTER)
        tv.heading("Mother's Name",text="Mother's Name",anchor=CENTER)
        tv.heading("Date Of Birth",text="Date Of Birth",anchor=CENTER)
        tv.heading("Address",text="Address",anchor=CENTER)
        tv.heading("Account Creation Time",text="Account Creation Time",anchor=CENTER)

        with open("resources/allstudentrecord.csv",'r') as myfile:
            csvr=csv.reader(myfile)
            c=0
            for i in csvr:
                tv.insert(parent='',index= c,iid=c,text='',values=(str(c),i[0],i[1],i[2],i[3],i[4],i[5],i[6]+i[7]))
                tv.pack()
                c=c+1
            

        '''Button(viewallstudents, text='Increment Salary', command=update_item).pack()'''
        Button(viewallstudents, text="Show Selected", command=show_selected).pack()

        viewallstudents.mainloop()


    def quitt():
        main.destroy()

    def time():
        today = date.today()
        string = strftime('%H:%M:%S %p')
        lbll.config(text=today)
        lbl.config(text = string)
        lbl.after(1000, time)
    
    
    def issue(admissionnumber,bookid):

        with open("resources/allstudentrecord.csv",'r') as myfile:
            csvw=csv.reader(myfile)
            for i in csvw:
                if str(i[0])==str(admissionnumber):
                    #admission number
                    admissionnumberr=str(i[0])
                    #name
                    nameee=str(i[1])
                    

        with open("resources/books.csv",'r',newline="") as myfile:
            csvw=csv.reader(myfile)
            for i in csvw:
                if str(i[0])==str(bookid):
                    #bookid
                    bookidd=i[0]
                    #bookname
                    booknameee=i[1]

        details={"admission_number":admissionnumber,
        "student_name":nameee,
        "book_id":bookidd,
        "book_name":booknameee,
        "date_of_issue":str(date.today())}

        mydb=myclient["LIBRARY"]
        mytable=mydb["allissuedbooks"]   
        mytable.insert_one(details) 

        issuedetail(admissionnumber)
    
        messagebox.showinfo("Issued","Book Has Been Issued",parent=main)    

    def viewdetails(admissionnumber):
        with open("resources/allstudentrecord.csv",'r') as myfile:
            
            deleteee()
            csvw=csv.reader(myfile)
            for i in csvw:
                if str(i[0])==str(admissionnumber):
                    issue_studentname.configure(text=i[1])
                    issue_fathername.configure(text=i[2])
                    view_name.configure(text=i[1])
                    view_admission.configure(text=admissionnumber)
                    issuedetail(admissionnumber)
                        

                                        
                    


                    
                    

        with open("resources/classrecord.csv",'r') as myfile:
            csvw=csv.reader(myfile)
            for i in csvw:
                if str(i[0])==str(admissionnumber):
                    issue_class.configure(text=i[1]+' '+i[2])
                    
    
    def viewbook(bookid):
        issue_booktitle.configure(text="")
        issue_writter.configure(text="")
        mydb=myclient["LIBRARY"]
        mytable=mydb["allbooks"]
        books=mytable.find_one({"book_id":bookid})
        issue_booktitle.configure(text=books["book_name"])
        issue_writter.configure(text=books["author_name"])

                    

                    
        

    #images-----
    timeimage=PhotoImage(file="images/time.png")
    srchbtnimage=PhotoImage(file="images/search.png")
    srchbtnimage1=PhotoImage(file="images/search1.png")
    studentimage=PhotoImage(file="images/student.png")
    parentimage=PhotoImage(file="images/parent.png")
    bookidimage=PhotoImage(file="images/bookid.png")
    authorimage=PhotoImage(file="images/author.png")
    




    Frame(main,bg="silver",height=100,width=1800).pack()
    lbl=Label(main, font = ('calibri', 20, 'bold'),background = 'silver',foreground = 'white')
    lbll=Label(main, font = ('calibri', 30, 'bold'),background = 'silver',foreground = 'purple')
    lbll.place(x=1350,y=28,anchor = 'center')
    lbl.place(x=1350,y=68,anchor = 'center')
    time()
    bg=Label(main,image=timeimage,bg="silver").place(x=1190,y=22)
    Frame(main,bg="yellow",height=1800,width=220).place(x=0,y=100)

    addbookbutton=Button(main,cursor="hand2",text="Add Book",bg="blue",fg="white" ,font = ('calibri',13, 'bold'),command=addbook,height=2,width=16,bd=1).place(x=55,y=120)

    seeallbookbutton=Button(main,cursor="hand2",text="See All Books",bg="blue",fg="white" ,font = ('calibri',13, 'bold'),command=allbooks,height=2,width=16,bd=1).place(x=55,y=190)

    addstudentbutton=Button(main,cursor="hand2",text="Add Student",bg="blue",fg="white" ,font = ('calibri',13, 'bold'),command=newtudent,height=2,width=16,bd=1).place(x=55,y=260)

    seestudentbutton=Button(main,cursor="hand2",text="View All Students",bg="blue",fg="white" ,font = ('calibri',13, 'bold'),command=viewallstudents,height=2,width=16,bd=1).place(x=55,y=330)

    seeborrowedbooks=Button(main,cursor="hand2",text="All Borrowed Books",bg="blue",fg="white" ,font = ('calibri',13, 'bold'),command=boo,height=2,width=16,bd=1).place(x=55,y=400)

    allusers=Button(main,cursor="hand2",text="All Users",bg="blue",fg="white" ,font = ('calibri',13, 'bold'),command=boo,height=2,width=16,bd=1).place(x=55,y=470)

    onlineissue=Button(main,cursor="hand2",text="Online Issue request",bg="green",fg="white" ,font = ('calibri',13, 
    'bold'),command=boo,height=2,width=16,bd=1).place(x=55,y=540)

    Button(main,cursor="hand2",text="CLOSE",bg="red",fg="white" ,font = ('calibri',13, 'bold'),command=quit,height=2,width=16,bd=1).place(x=55,y=750)

    #issue frame contents ----------------------------------------
    Frame(main,bg="orange",height=380,width=760).place(x=235,y=115)
    Label(main,text="Issue Book :-",bg="orange",fg="blue",font=('Bookman Old Style',20,'bold')).place(x=239,y=118)
    Label(main,text="Admission Number :",bg="orange",fg="black",font=("Agency FB",17,"bold")).place(x=279,y=160)
    a=Entry(main,width=10,bg="yellow",font=(8),fg="blue",bd=2)
    a.place(x=450,y=164)
    a.insert(0,"5741")
    search_btn=Button(main,image=srchbtnimage,bd=1,bg="orange",command=lambda:viewdetails(a.get()),cursor="hand2").place(x=570,y=150)

    Label(main,text="Student Name :",bg="orange",fg="black",font=("Agency FB",17,"bold")).place(x=279,y=200)
    Label(main,image=studentimage,bg="orange").place(x=239,y=200)
    issue_studentname=Label(main,text="  ",bg="orange",fg="blue",font=("Franklin Gothic Medium Cond",20,'bold'))
    issue_studentname.place(x=410,y=200)

    Label(main,text="Class :",bg="orange",fg="black",font=("Agency FB",17,"bold")).place(x=279,y=235)
    issue_class=Label(main,text="  ",bg="orange",fg="blue",font=("Franklin Gothic Medium Cond",20,'bold'))
    issue_class.place(x=410,y=235)

    Label(main,text="Father's Name :",bg="orange",fg="black",font=("Agency FB",17,"bold")).place(x=279,y=270)
    Label(main,image=parentimage,bg="orange").place(x=239,y=270)
    issue_fathername=Label(main,text="  ",bg="orange",fg="blue",font=("Franklin Gothic Medium Cond",20,'bold'))
    issue_fathername.place(x=410,y=270)

    Label(main,text="Book Id :",bg="orange",fg="black",font=("Agency FB",17,"bold")).place(x=279,y=325)
    Label(main,image=bookidimage,bg="orange").place(x=239,y=325)
    issue_bookid=Label(main,text="  ",bg="orange",fg="blue",font=("Franklin Gothic Medium Cond",20,'bold'))
    issue_bookid.place(x=410,y=325)
    b=Entry(main,width=10,bg="yellow",font=(8),fg="blue",bd=2)
    b.place(x=360,y=330)
    b.insert(0,"101")
    book_search_btn=Button(main,image=srchbtnimage1,bd=1,bg="orange",command=lambda:viewbook(b.get()),cursor="hand2").place(x=480,y=315)

    Label(main,text="Book Title :",bg="orange",fg="black",font=("Agency FB",17,"bold")).place(x=279,y=375)
    issue_booktitle=Label(main,text="  ",bg="orange",fg="blue",font=("Franklin Gothic Medium Cond",20,'bold'))
    issue_booktitle.place(x=410,y=375)

    Label(main,text="Author's Name :",bg="orange",fg="black",font=("Agency FB",17,"bold")).place(x=279,y=410)
    Label(main,image=authorimage,bg="orange").place(x=239,y=410)
    issue_writter=Label(main,text="  ",bg="orange",fg="blue",font=("Franklin Gothic Medium Cond",20,'bold'))
    issue_writter.place(x=410,y=410)

    issue_btn=Button(main,text="Issue Book",bd=3,bg="blue",fg="white",font = ('calibri',13, 'bold'),command=lambda:issue(a.get(),b.get()),cursor="hand2",state=DISABLED)
    issue_btn.place(x=800,y=450)

    
    #submitted frame content -------------------------------------
    Frame(main,bg="chocolate",height=290,width=760).place(x=235,y=520)
    Label(main,text="Submit Book :-",bg="chocolate",fg="blue",font=('Bookman Old Style',17,'bold')).place(x=239,y=523)

    Label(main,text="Admission Number :",bg="chocolate",fg="black",font=("Agency FB",17,"bold")).place(x=279,y=570)
    ab=Entry(main,width=10,bg="yellow",font=(8),fg="blue",bd=2)
    ab.place(x=450,y=570)
    ab.insert(0,"5741")

    Label(main,text="Book Id :",bg="chocolate",fg="black",font=("Agency FB",17,"bold")).place(x=279,y=610)
    ba=Entry(main,width=10,bg="yellow",font=(8),fg="blue",bd=2)
    ba.place(x=450,y=610)
    ba.insert(0,"100")
    submit_btn=Button(main,text="Submit Book",bd=3,bg="blue",fg="white",font = ('calibri',13, 'bold'),command=lambda:submitbook(ab.get(),ba.get()),cursor="hand2")
    submit_btn.place(x=800,y=750)



    #display frame content ---------------------------------------
    disframe=Frame(main,bg="grey",height=700,width=450)
    disframe.place(x=1025,y=115)
    Label(main,text="ISSUE RECORD",bg="grey",fg="white",font=('Consolas',20,'bold')).place(x=1150,y=118)
    Label(main,text="------------------------------------",bg="grey",fg="white",font=('Consolas',15,'bold')).place(x=1050,y=150)
    Label(main,text="Name :",bg="grey",fg="white",font=('Consolas',14,'bold')).place(x=1050,y=170)
    view_name=Label(main,text="",bg="grey",fg="yellow",font=('Consolas',15,'bold'))
    view_name.place(x=1130,y=172)



    Label(main,text="Admission Number :",bg="grey",fg="white",font=('Consolas',14,'bold')).place(x=1050,y=200)
    view_admission=Label(main,text="",bg="grey",fg="yellow",font=('Consolas',15,'bold'))
    view_admission.place(x=1250,y=199)

    
    
    Label(main,text="------------------------------------",bg="grey",fg="white",font=('Consolas',15,'bold')).place(x=1050,y=230)
    Label(main,text="Book Id :",bg="grey",fg="white",font=('Consolas',14,'bold')).place(x=1031,y=250)
    Label(main,text="Book Name:",bg="grey",fg="white",font=('Consolas',14,'bold')).place(x=1200,y=250)
    Label(main,text="┃\n┃\n┃\n┃\n┃\n┃\n┃\n┃\n┃\n┃\n┃\n┃\n┃\n┃\n┃\n┃\n┃\n┃\n",bg="grey",fg="white",font=('Consolas',15,'bold')).place(x=1110,y=290)
    Label(main,text="------------------------------------",bg="grey",fg="white",font=('Consolas',15,'bold')).place(x=1050,y=270)


    #Label(main,text="┃\n┃\n┃\n┃\n┃\n┃\n┃\n┃\n┃\n┃\n┃\n┃\n┃\n┃\n┃\n┃\n┃\n┃\n",bg="grey",fg="white",font=('Consolas',15,'bold')).place(x=1350,y=260)
    
    
    main.mainloop()


# Add a menu bar -----
menu=Menu(window)
window.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label="COMMANDS",menu=filemenu)
filemenu.add_command(label="Quit",command=quit)

bgimage=PhotoImage(file="images/bg1.png")
loginicon=PhotoImage(file="images/loginicon.png")
passicon=PhotoImage(file='images/passicon.png')
loginimage=PhotoImage(file="images/login.png")
registerimage=PhotoImage(file="images/register.png")
resetimage=PhotoImage(file="images/reset.png")
bg=Label(window,image=bgimage)
bg.pack()
loginframe=LabelFrame(bg,text="",bg="white",width=450,height=600,bd=0).place(x=100,y=100)
loginlabel=Label(window,text="LOGIN HERE",font=("Rockwell Extra Bold",23,"bold"),bg='white',fg='Red').place(x=215,y=190)
vv=Label(window,image=loginicon).place(x=150,y=305)
usernamelable=Label(window,text="USERNAME:",font=("Bahnschrift",15,"bold"),bg='white').place(x=150,y=270)
username=Entry(window,width=30,bg="silver",font=(8),fg="blue")
username.place(x=190,y=305)
username.insert(0,"bishalde")
vvv=Label(window,image=passicon).place(x=150,y=405)
passwordlable=Label(window,text="PASSWORD:",font=("Bahnschrift",15,"bold"),bg='white').place(x=150,y=370)
password=Entry(window,width=30,bg="silver",font=(8),fg="blue")
password.place(x=190,y=405)
password.insert(0,"5741")
loginbutton=Button(window,image=loginimage,cursor="hand2", command=lambda:login(str(username.get()),str(password.get())),bd=0)
loginbutton.place(x=200,y=475)
resetbutton=Button(window,cursor="hand2",image=resetimage,command=reset,bd=0)
resetbutton.place(x=365,y=472)
signupbutton=Button(window,cursor="hand2", image=registerimage,command=signup,bd=0)
signupbutton.place(x=380,y=595)
registerlable=Label(window,text="Are You A New User :",font=("Bahnschrift",14),fg="black",bg="white")
registerlable.place(x=190,y=600)


window.mainloop()




