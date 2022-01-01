#MODULES----------------------------------------------------------------------
from tkinter import *
from tkinter import ttk,messagebox
import csv,os.path,pymongo
from time import strftime
from datetime import date , datetime
from random import randint

#DATABASE----------------------------------------------------------------------
myclient=pymongo.MongoClient("mongodb://localhost:27017/")


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
    root.geometry("1400x730")
    root.iconphoto(False,impp)

    '''screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    size=str(screen_width)+'x'+str(screen_height)
    root.geometry(size)
    root.overrideredirect(True)'''

    root.resizable(0,0)

    #___________Photos_________________

    registerimage=PhotoImage(file="images/register.png")
    resetimage=PhotoImage(file="images/reset.png")
    backto=PhotoImage(file="images/back.png")
    exitimage=PhotoImage(file="images/exit.png")
    bgimage=PhotoImage(file="images/bg.png")
    lefticon=PhotoImage(file='images/xx.png')

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


def mainwindow():
    main=Toplevel()
    main.title("Login")
    main.geometry("690x750")

    def quitt():
        main.destroy()


    Label(main,text="Work In Progress.!!",font=("Bahnschrift",20,"bold"),bg='white').pack()
    Button(main,text="Exit",command=quitt).pack()

    main.mainloop()

#WINDOW-------------------------------------------------------------------------
window=Tk()
window.title("Login")
window.geometry("670x770")
impp=PhotoImage(file="images/imap.png")
window.iconphoto(False,impp)
#window.geometry("1535x863") ------ my pc resolutuion

'''To get your Monitor's width'''
#screen_width = window.winfo_screenwidth()

'''To get your Monitor's height'''
#screen_height = window.winfo_screenheight()

'''Inserting values'''
#size=str(screen_width)+'x'+str(screen_height)
#window.geometry(size)

'''Make window Non-Resizable'''
window.resizable(0,0)

''' Remove maximize,minimize,cancel buttons'''
#window.overrideredirect(True)



# Add a menu bar--------------------------------------------------------------------
menu=Menu(window)
window.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label="COMMANDS",menu=filemenu)
filemenu.add_command(label="Quit",command=quit)


#MAIN CODE ---------------------------------------------------------------------------

'''Images'''
randomnumber=str(randint(1,3))
bgimage=PhotoImage(file="images/bg"+randomnumber+".png")
loginicon=PhotoImage(file="images/loginicon.png")
passicon=PhotoImage(file='images/passicon.png')
loginimage=PhotoImage(file="images/login.png")
registerimage=PhotoImage(file="images/register.png")
resetimage=PhotoImage(file="images/reset.png")
bg=Label(window,image=bgimage)
bg.pack()

'''++++++++++++Contents++++++++++++++++'''


'''Login contents'''
loginframe=LabelFrame(bg,text="",bg="white",width=450,height=600,bd=0)
loginframe.place(x=100,y=100)

loginlabel=Label(window,text="LOGIN HERE",font=("Rockwell Extra Bold",23,"bold"),bg='white',fg='Red')
loginlabel.place(x=215,y=190)



'''username contents'''
vv=Label(window,image=loginicon)
vv.place(x=150,y=305)

usernamelable=Label(window,text="USERNAME:",font=("Bahnschrift",15,"bold"),bg='white')
usernamelable.place(x=150,y=270)

username=Entry(window,width=30,bg="silver",font=(8),fg="blue")
username.place(x=190,y=305)



'''password contents'''
vvv=Label(window,image=passicon)
vvv.place(x=150,y=405)

passwordlable=Label(window,text="PASSWORD:",font=("Bahnschrift",15,"bold"),bg='white')
passwordlable.place(x=150,y=370)

password=Entry(window,width=30,bg="silver",font=(8),fg="blue")
password.place(x=190,y=405)

'''login button'''
loginbutton=Button(window,image=loginimage,cursor="hand2", command=lambda : login(str(username.get()),str(password.get())),bd=0)
loginbutton.place(x=200,y=478)

'''reset button'''
resetbutton=Button(window,cursor="hand2",image=resetimage,command=reset,bd=0)
resetbutton.place(x=365,y=472)

'''signup contents'''
registerlable=Label(window,text="Are You A New User :",font=("Bahnschrift",14),fg="black",bg="white")
registerlable.place(x=190,y=600)

signupbutton=Button(window,cursor="hand2", image=registerimage,command=signup,bd=0)
signupbutton.place(x=380,y=595)




window.mainloop()