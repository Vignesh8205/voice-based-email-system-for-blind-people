from tkinter import *
global main_screen
from tkinter import Tk, font, messagebox
from tkcalendar import Calendar, DateEntry
global root,password,username,password_entry,username_entry,idma
import spe
import mysql.connector

mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="voice_email"
            )
mycursor = mydb.cursor()
def log_again():
    spe.spe("one to login-in again  ,two to quit ")
    log_again_val = spe.tex()
    if log_again_val==1:
        test()
    else:
        quit()

def test():
    global idma
    spe.spe("Tell me your personal id to login")
    id = spe.tex()

    idma=id
    e.insert(END, id)
    spe.spe(id)
    print(id)

    sql = "select name from register_user where id = %s; "
    mycursor.execute(sql,[(id)])
    results = mycursor.fetchone()
    # print(len(results))
    if len(results) is not None:
        speak_res=f"Welcome to voice based email {results}"
        spe.spe(speak_res)
        spe.spe("logged-in Successfully  ")
        voice_mod()
    else:
        spe.spe("check your loggin Id ,Loggin Unsuccessfull  ")
        log_again()


def login_by_voice():
    global e, root1
    main_screen.destroy()
    root1 = Tk()
    root1.geometry('600x300')
    root1.title("User voice login Form")
    Label(root1, text="LOGIN By VOICE-PORTAL ", bg="#4169e1", width="300", height="3",
          font=("Times New Roman", 18, 'bold', 'italic')).pack()
    Label(text="").pack()

    voice_id = Label(root1, text="Login ID", bg="#4169e1", width=20,
                     font=("Times New Roman", 16, 'bold', 'italic'))
    voice_id.place(x=10, y=130)
    e = Entry(root1, width=22,
              bg='#89c8ff', font=("Times New Roman", 16, 'bold', 'italic'))
    e.place(x='280', y='130', height=30, width=300)

    test()
    # voice_mod()


def voice_mod():
    global  vroot1

    spe.spe("1 for open mail")
    spe.spe(" 2 for view unopened mail")
    spe.spe(" 3 for view All mail")
    spe.spe(" 4 for logout or close")
    id = spe.tex()
    print(id)
    print(type(id))



    def vopen():
        # root1.destroy()
        vop = Tk()
        vop.geometry('700x600')
        vop.title("Mail open by voice")
        Label(vop, text="Voice Message Compose Page", bg="#4169e1", width="300", height="3",
              font=("Times New Roman", 16, 'bold', 'italic')).pack()
        Label(text="").pack()
        Label(vop, width=20, height=1, text="From", bg='#89c8ff', font=("Times New Roman", 16, 'bold', 'italic')).place(
            x=20, y=100)

        fromtex = Entry(vop, width=30, bg='#89c8ff'
                        , font=("Times New Roman", 16, 'bold', 'italic'))
        fromtex.place(x=320, y=100)

        Label(vop, text="Subject", width=20, height=1, bg='#89c8ff'
              , font=("Times New Roman", 16, 'bold', 'italic')).place(x=20, y=200)
        content = Entry(vop, width=30,
                        bg='#89c8ff', font=("Times New Roman", 16, 'bold', 'italic'))
        content.place(x=320, y=200)
        Label(vop, text="TO ", width=20, height=1, bg='#89c8ff'
              , font=("Times New Roman", 16, 'bold', 'italic')).place(x=20, y=300)

        totex = Entry(vop, width=30,
                      bg='#89c8ff', font=("Times New Roman", 16, 'bold', 'italic'))
        totex.place(x=320, y=300)

        spe.spe(" please tell  the from adress or login id")
        fromid = spe.tex()
        spe.spe(fromid)
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="voice_email"
        )
        mycursor = mydb.cursor()
        mycursor = mydb.cursor()
        sql = f"select name from register_user where id = %s; "
        mycursor.execute(sql, [(fromid)])
        results = mycursor.fetchone()
        print(results)
        if results is not None:
            spe.spe(results)
            spe.spe(" please tell  the message ")
            msgid = spe.tex()
            spe.spe(msgid)
            content.insert(END, msgid)

            spe.spe(" please tell  To adress or login id")
            toid = spe.tex()
            spe.spe(toid)
            totex.insert(END, toid)

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="voice_email"
            )
            mycursor = mydb.cursor()
            sql = "select name from register_user where id = %s; "
            mycursor.execute(sql, [(toid)])
            results = mycursor.fetchone()
            if results is not None:
                sendnamespe = f"sender name is {results[0]}"
                spe.spe(sendnamespe)
                mycursor1 = mydb.cursor()
                sql1 = "insert into compose (fromid,subject,toid,readmsg) values(%s,%s,%s,%s); "
                val = (fromid, msgid, toid, '0')
                mycursor1.execute(sql1, val)
                mydb.commit()
                messagebox.showinfo("showinfo", "Message send Sucessfully")
                vop.mainloop()
            else:
                messagebox.showinfo("showinfo", "wrong id")
        else:
            messagebox.showinfo("showinfo", "id not found or not registered")
        # fromtex.insert(END, fromid)

    def vview():
        t = 0
        # root1.destroy()
        vvi = Tk()
        vvi.geometry('1000x600')
        vvi.title("View Mail open by voice")
        spe.spe("welcome to inbox message reading")
        con = mysql.connector.connect(host="localhost", user="root", password="", database="voice_email")
        cur = con.cursor()
        print('idma=',idma)
        cur.execute(f"SELECT * from compose where toid={idma} and readmsg='0';")
        res = cur.fetchall()
        # print(res)
        if len(res) == 0:
            Label(vvi, text="All Message has been readed", bg="#4169e1", width="300", height="3",
                  font=("Times New Roman", 16, 'bold', 'italic')).pack()
            Label(text="").pack(pady=20, padx=10)
        else:
            i = 1
            for n in res:
                for j in range(len(n)):
                    e = Label(vvi, width=25, fg="blue", text=n[j], borderwidth=2, relief="ridge", anchor="w",
                              padx=5,
                              pady=8)
                    e.grid(row=i, column=j)
                    e = Label(vvi, width=25, fg="#000", text="id", borderwidth=2, relief="ridge", anchor="w",
                              padx=10, pady=8)
                    e.grid(row=0, column=0)
                    e = Label(vvi, width=25, fg="#000", text="fromid", borderwidth=2, relief="ridge", anchor="w",
                              padx=10, pady=8)
                    e.grid(row=0, column=1)
                    e = Label(vvi, width=25, fg="#000", text="subject", borderwidth=2, relief="ridge",
                              anchor="w",
                              padx=10, pady=8)
                    e.grid(row=0, column=2)
                    e = Label(vvi, width=25, fg="#000", text="toid", borderwidth=2, relief="ridge",
                              anchor="w",
                              padx=10, pady=8)
                    e.grid(row=0, column=3)
                    e = Label(vvi, width=25, fg="#000", text="readmsg", borderwidth=2, relief="ridge",
                              anchor="w",
                              padx=10, pady=8)
                    e.grid(row=0, column=4)

                    # e.insert(END,res[j])
                i = i + 1

        mycursor = mydb.cursor()

        mycursor.execute(f"SELECT fromid,subject FROM compose where  toid={idma} and readmsg='0'; ")
        myresult = mycursor.fetchall()

        if len(myresult) >= 1:
            for x, y in myresult:
                rems = f"From ID is {x}"
                spe.spe(rems)
                rems1 = f"Subject is {y} "
                spe.spe(rems1)
                sql = f"UPDATE compose SET readmsg = '1' WHERE fromid = {x};"
                mycursor.execute(sql)
                mydb.commit()
                t = t + 1
                readcount = f" ..........,{t} message readed "
                spe.spe(readcount)
                # print(mycursor.rowcount)
        else:
            spe.spe("TILL now  ALL the  message has been readedd")
        vvi.mainloop()

    def veiwall():
        # root1.destroy()
        t = 0
        viall = Tk()
        viall.geometry('1000x600')
        viall.title("Veiw all Mail open by voice")
        con = mysql.connector.connect(host="localhost", user="root", password="", database="voice_email")
        cur = con.cursor()
        cur.execute(f"SELECT * from compose where fromid={idma} ")
        # print(id)
        res = cur.fetchall()
        print(res)
        if len(res) == 0:
            Label(viall, text="All Message has been readed", bg="#4169e1", width="300", height="3",
                  font=("Times New Roman", 16, 'bold', 'italic')).pack()
            Label(text="").pack(pady=20, padx=10)


        else:
            i = 1
            for n in res:
                for j in range(len(n)):
                    e = Label(viall, width=25, fg="blue", text=n[j], borderwidth=2, relief="ridge", anchor="w",
                              padx=5,
                              pady=8)
                    e.grid(row=i, column=j)
                    e = Label(viall, width=25, fg="#000", text="id", borderwidth=2, relief="ridge", anchor="w",
                              padx=10, pady=8)
                    e.grid(row=0, column=0)
                    e = Label(viall, width=25, fg="#000", text="fromid", borderwidth=2, relief="ridge",
                              anchor="w",
                              padx=10, pady=8)
                    e.grid(row=0, column=1)
                    e = Label(viall, width=25, fg="#000", text="subject", borderwidth=2, relief="ridge",
                              anchor="w",
                              padx=10, pady=8)
                    e.grid(row=0, column=2)
                    e = Label(viall, width=25, fg="#000", text="toid", borderwidth=2, relief="ridge",
                              anchor="w",
                              padx=10, pady=8)
                    e.grid(row=0, column=3)
                    e = Label(viall, width=25, fg="#000", text="readmsg", borderwidth=2, relief="ridge",
                              anchor="w",
                              padx=10, pady=8)
                    e.grid(row=0, column=4)

                    # e.insert(END,res[j])
                i = i + 1


        if len(res) >= 1:
            for a, x, y, z, b in res:
                rems = f"From ID is {x}"
                spe.spe(rems)
                rems1 = f"Subject is {y} "
                spe.spe(rems1)
                rems2 = f"Tooo I d is {z} "
                spe.spe(rems2)
                sql = f"UPDATE compose SET readmsg = '1' WHERE fromid = {x};"
                cur.execute(sql)
                mydb.commit()
                t = t + 1
                readcount = f" ..........,{t} message readed "
                spe.spe(readcount)
                # print(mycursor.rowcount)
        else:
            spe.spe("TILL now  ALL the  message has been readedd")
        viall.mainloop()

    def close():
        spe.spe("closing the app")
        # root1.destroy()
        quit()



    if id=="open" or id =="open " or id=='1' :

        vopen()
        voice_mod()

    elif id== "un open" or id== "unopen" or id== "TWO" or id=='2' :

        vview()
        voice_mod()
    elif id=="view all" or id=="view all" or id=="view all" or id== '3' or id=='free' or id=='cri':

        veiwall()
        voice_mod()
    elif id=="logout" or id=="logout" or id=="for" or id=='44' :
        spe.spe("closing application")
        close()
    else:
        spe.spe("give the correct command")
        voice_mod()

    vview()
def admin_view_user():
    ad_view_user=Tk()
    ad_view_user.title("Register")
    ad_view_user.geometry("800x650")
    con = mysql.connector.connect(host="localhost", user="root", password="", database="voice_email")
    cur = con.cursor()
    cur.execute(f"SELECT * from register_user")
    res = cur.fetchall()
    i = 0
    for n in res:
        for j in range(len(n)):
            e = Label(ad_view_user, width=15, fg="blue", text=n[j], borderwidth=2, relief="ridge", anchor="w", padx=10,
                      pady=8)
            e.grid(row=i, column=j)
            e = Label(ad_view_user, width=15, fg="#000", text="name", borderwidth=2, relief="ridge", anchor="w",
                      padx=10, pady=8)
            e.grid(row=0, column=0)
            e = Label(ad_view_user, width=15, fg="#000", text="date", borderwidth=2, relief="ridge", anchor="w",
                      padx=10, pady=8)
            e.grid(row=0, column=1)
            e = Label(ad_view_user, width=15, fg="#000", text="finger", borderwidth=2, relief="ridge", anchor="w",
                      padx=10, pady=8)
            e.grid(row=0, column=2)
            e = Label(ad_view_user, width=15, fg="#000", text="message", borderwidth=2, relief="ridge", anchor="w",
                      padx=10, pady=8)
            e.grid(row=0, column=3)

            # e.insert(END,res[j])
        i = i + 1

def admin_reg_user():
    global fname,mail,cal

    root = Tk()
    root.geometry('600x500')
    root.title("User Registration Form")
    fullname=StringVar()
    email=StringVar()

    Label(root, text="Admin Register & view Page", bg="#4169e1", width="300", height="3",
          font=("Times New Roman", 16, 'bold', 'italic')).pack()
    Label(text="").pack(pady=20, padx=10)

    label_1 = Label(root, text="FullName", bg="#4169e1",width=20, font=("Times New Roman", 16, 'bold', 'italic'))
    label_1.place(x=10, y=130)

    fname = Entry(root, textvariable=fullname, width=22, bg='#89c8ff'
                           , font=("Times New Roman", 16, 'bold', 'italic'))
    fname.place(x=280, y=130,height=30,width=300)

    label_2 = Label(root, text="Email",  bg="#4169e1",width=20, font=("Times New Roman", 16, 'bold', 'italic'))
    label_2.place(x=10, y=180)

    mail = Entry(root, textvariable=email, width=22, bg='#89c8ff'
                  , font=("Times New Roman", 16, 'bold', 'italic'))
    mail.place(x=280, y=180, height=30, width=300)

    label_3 = Label(root, text="Gender",  bg="#4169e1",width=20, font=("Times New Roman", 16, 'bold', 'italic'))
    label_3.place(x=10, y=230)
    var = IntVar()
    gen=Radiobutton(root, text="Male",  variable=var,width=10 ,font=("Times New Roman", 14, 'bold', 'italic'), value=1)
    gen.place(x=255, y=230)
    gen1=Radiobutton(root, text="Female",width=10, font=("Times New Roman", 14, 'bold', 'italic'), variable=var, value=2)
    gen1.place(x=380, y=230)

    label_4 = Label(root, text="Age:",  bg="#4169e1",width=20, font=("Times New Roman", 16, 'bold', 'italic'))
    label_4.place(x=10, y=280)


    cal = DateEntry(root, width=30, background="#89c8ff", foreground="#89c8fh", bd=2)
    cal.place(x=280, y=280, height=30, width=300)

    # **************************----insert valuses in  MYSQL database-----******************************

    def user_login():
        print("fname = ", fname.get())
        print("email = ", mail.get())
        print("date = ", cal.get())

        us_lo_name=fname.get()
        us_lo_email=mail.get()
        us_lo_date=cal.get()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="voice_email"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO register_user (name,email,DOB) VALUES (%s, %s,%s)"
        val = (us_lo_name,us_lo_email,us_lo_date)
        mycursor.execute(sql, val)
        mydb.commit()
        # print(mycursor.rowcount, "record inserted.")
        messagebox.showinfo("showinfo", "Registered Sucessfully")
        # adminv1.destroy()

        # **************************----insert valuses in  MYSQL database finishes-----******************************



        root.destroy()

        # login_by_voice()


    Button(root, text='Submit', width=20, bg="#4169e1",command=user_login, font=("Times New Roman", 16, 'bold', 'italic')
           , fg='white').place(x=190, y=340)
    root.mainloop()
    print("registration form  seccussfully created...")

def admin_veiw():
    global adminv1
    register_screen.destroy()
    adminv1 = Tk()
    adminv1.title("Register")
    adminv1.geometry("500x450")
    # Label(adminv1,text="Admin Register & view Page", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    # Label(text="").pack()
    Label(adminv1, text="Admin Register & view Page", bg="#4169e1", width="300", height="3",
          font=("Times New Roman", 16, 'bold', 'italic')).pack()
    Label(text="").pack(pady=20, padx=10)

    # create Login Button
    Button(adminv1,text="Register user", bg="#4169e1", width="30", height="2",
          font=("Times New Roman", 16, 'bold', 'italic'), command=admin_reg_user).pack(padx=10,pady=20)
    Label(text="").pack()

    # create a register button
    Button(adminv1,text="Veiw User",bg="#4169e1", width="30", height="2",
          font=("Times New Roman", 16, 'bold', 'italic'),command=admin_view_user).pack(padx=10,pady=30)
    Label(text="").pack()
    adminv1.mainloop()

def admin_login():
    global main_screen,password,username,username_entry,password_entry,register_screen
    # main_screen.dest
    main_screen.destroy()
    register_screen = Tk()
    register_screen.title("Admin Login")
    register_screen.geometry("500x450")

    # Set text variables
    username = StringVar()
    password = StringVar()

    # Set label for user's instruction
    Label(register_screen,text="Admin registration", bg="#4169e1", width="300", height="3",
          font=("Times New Roman", 16, 'bold', 'italic')).pack()
    Label(text="").pack(pady=20,padx=10)

    # Set username label
    Label(register_screen,width=20,height=1, text="Username * "
                           ,bg='#89c8ff',font=("Times New Roman", 16,'bold','italic')).pack(padx=10,pady=20)

    # Set username entry
    # The Entry widget is a standard Tkinter widget used to enter or display a single line of text.

    username_entry = Entry(register_screen, textvariable=username,width=22,bg='#89c8ff'
                           ,font=("Times New Roman", 16,'bold','italic'))
    username_entry.pack(padx=10,pady=10)


    # Set password label
    Label(register_screen, text="Password * ",width=20,height=1,bg='#89c8ff'
                           ,font=("Times New Roman", 16,'bold','italic')).pack(padx=10,pady=10)

    # Set password entry
    password_entry = Entry(register_screen, textvariable=password, show='*',width=22,
                           bg='#89c8ff',font=("Times New Roman", 16,'bold','italic'))
    password_entry.pack(padx=10,pady=10)

    Label(register_screen, text="").pack()

    def value():
        print("pass = ", password_entry.get())
        print("username = ", username_entry.get())
        aname=password_entry.get()
        auser=username_entry.get()
        if aname=="admin" and auser=="admin" :
            admin_veiw()
        else:
            messagebox.showinfo("showinfo", "Login Failed")
            quit()

    # Set register button
    Button(register_screen, text="Register", width=10, height=1,
           bg="#4169e1",font=("Times New Roman", 16,'bold','italic'), command=value).pack()
    # main_screen.mainloop()

def main_account_screen():
    global main_screen
    main_screen = Tk()  # create a GUI window
    main_screen.geometry("500x450")  # set the configuration of GUI window
    main_screen.title("Account Login")  # set the title of GUI window

    # create a Form label
    Label(text="Choose Login Or Register", bg="#4169e1", width="300", height="3", font=("Times New Roman", 16,'bold','italic')).pack()
    Label(text="").pack()

    # create Login Button
    Button(text="Admin", height="2", width="30",bg='#4169e1',font=("Times New Roman", 16,'bold','italic'),command=admin_login).pack()
    Label(text="").pack()

    # create a register button
    Button(text="User", height="2", width="30",bg='#4169e1',font=("Times New Roman", 16,'bold','italic'),command=login_by_voice).pack()

    main_screen.mainloop()  # start the GUI


main_account_screen()
