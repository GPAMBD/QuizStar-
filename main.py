from tkinter import *
from PIL import ImageTk,Image
import sqlite3
import time
import random
import datetime
import requests
pk=0
# Home page :
#global base1
base1 = Tk()
base1.title("Exam quiz software")
base1.geometry("1350x690")
base1.geometry("+1+1")


#===============================================================
def create_quiz():

    Quiz_code=random.randint(111111,999999)
    print("Quiz Code : ",Quiz_code)

    # def teacher_interface3():
    # ==================================================================================================
    def teacher_interface3():

        dat11 = quize_name.get()
        dat12 = question.get()
        dat13 = a.get()
        dat14 = b.get()
        dat15 = c.get()
        dat16 = d.get()
        dat17 = str(ans.get())
        print("ans :", dat17)
        # connecting with another table to store a quiz_code and Quiz_name
        con=sqlite3.connect("Quizstar.db")
        cur=con.cursor()
        query1="insert into quiz_code values('"+dat11+"','"+str(Quiz_code)+"','"+teach_pass+"')"
        cur.execute(query1)
        print("Succesfully Quiz code Submitted...")
        con.commit()
        con.close()

        con = sqlite3.connect("Quizstar.db")
        cur = con.cursor()
        query = str("insert into " + teach_pass + " (quiz_name,sr_no,question,a,b,c,d,ans) values ('" + dat11 + "','" + str(
            num) + "','" + dat12 + "','" + dat13 + "','" + dat14 + "','" + dat15 + "','" + dat16 + "','" + dat17 + "')")
        cur.execute(query)
        con.commit()
        print("Succesfully Question Submitted..")
        con.close()

        # teacher_Interface image
        int1 = Image.open("teacher_interface.jpg")
        int2 = int1.resize((1350, 690))
        int2.save("teacher_interface.jpg")
        int3 = Image.open("teacher_interface.jpg")
        int4 = ImageTk.PhotoImage(int3)
        int5 = Label(image=int4)
        int5.image = int4
        int5.place(x=0, y=0)

        # teacher_interface Page body
        exit_tea_interface = Button(base1, text="Exit", width=8, font=("Arial Rounded MT Bold", 18), height=1,
                                    bg="white", fg="black", bd=0, command=teacher_login)
        exit_tea_interface.place(x=1130, y=50)

        i_btn1 = Button(base1, text="Create Quiz", font=("Arial Rounded MT Bold", 20), width=10, height=1, bd=0,
                        bg="white", command=create_quiz)
        i_btn1.place(x=310, y=300)
        i_btn2 = Button(base1, text="My Quizes", font=("Arial Rounded MT Bold", 20), width=10, height=1, bd=0,
                        bg="white", command=my_quizzes)
        i_btn2.place(x=650, y=300)
        i_btn3 = Button(base1, text="Responses", font=("Arial Rounded MT Bold", 20), width=10, height=1, bd=0,
                        bg="white", command=response)
        i_btn3.place(x=410, y=550)
        i_btn4 = Button(base1, text=" My Profile ", font=("Arial Rounded MT Bold", 20), width=10, height=1, bd=0, bg="white",command=teacher_profile)
        i_btn4.place(x=760, y=550)
    # ======================================================================================
    global num
    num = 1
    global x
    x=50
    global y
    y=80

    def add_new_question():

        quize_name.place_forget()
        global y,num
        y = y + 40
        num = num + 1

        dat11=quize_name.get()
        dat12=question.get()
        dat13=a.get()
        dat14 = b.get()
        dat15 = c.get()
        dat16 = d.get()
        dat17 = str(ans.get())

        quize_name1 = Label(base1, text=dat11,width=35, font=("Arial Rounded MT Bold", 18), bd=0,bg="#fafafa",fg="black")
        quize_name1.place(x=600, y=55)

        con=sqlite3.connect("Quizstar.db")
        cur=con.cursor()
        query=str("insert into "+teach_pass+" (quiz_name,sr_no,question,a,b,c,d,ans) values ('" + dat11 + "','" +str(num-1)+ "','" + dat12 + "','" + dat13 + "','" + dat14 + "','" + dat15 + "','" + dat16 + "','" + dat17 + "')")
        cur.execute(query)
        con.commit()
        print("Succesfully Question Submitted..")
        con.close()

        #quize_name.destroy()
        heading.configure(text="Quize name",width="54")
        question_num.configure(text=("Q",num,":"))
        question.delete(0,END)
        a.delete(0,END)
        b.delete(0, END)
        c.delete(0, END)
        d.delete(0, END)

        #configuree all radio buttuons
        dis_que = Label(base1, text=("Q", num-1, ":"), font=("Arial Rounded MT Bold", 17), width=22, height=1,bg="#d5b8ea")
        dis_que.place(x=x, y=y)

    # create quiz image
    quiz1 = Image.open("create_quiz1.jpg")
    quiz2 = quiz1.resize((1350, 690))
    quiz2.save("create_quiz1.jpg")
    quiz3 = Image.open("create_quiz1.jpg")
    quiz4 = ImageTk.PhotoImage(quiz3)
    quiz5 = Label(image=quiz4)
    quiz5.image = quiz4
    quiz5.place(x=0, y=0)

    # create quiz body
    code1=Label(base1,text=Quiz_code,font=("Arial Rounded MT Bold", 19), width=10, height=1, bd=0,fg="White", bg="#070707")
    code1.place(x=125,y=55)
    heading = Label(base1, text="Enter Quiz Name : ", font=("Arial Rounded MT Bold", 19), width=15, height=1, bd=4,fg="Black", bg="White")
    heading.place(x=430, y=50)
    quize_name=Entry(base1, width=45, font=("Arial", 18), bd=0)
    quize_name.place(x=700,y=55)
    question_num = Label(base1,text=("Q",num,":"),font=("Arial Rounded MT Bold", 19), width=4, height=1, bd=0,fg="Black", bg="white")
    question_num.place(x=470, y=330)
    question = Entry(base1, width=48, font=("Arial", 20), bd=0)
    question.place(x=540, y=330)

    q_btn1 = Button(base1, text="Add new Question", font=("Arial Rounded MT Bold", 15), width=13, height=1, bd=0,
                    fg="White", bg="#070707", command=add_new_question)
    q_btn1.place(x=488, y=153)
    q_btn2 = Button(base1, text="Complete paper", font=("Arial Rounded MT Bold", 16), width=13, height=1, bd=0,
                    fg="White", bg="#070707", command=teacher_interface3)
    q_btn2.place(x=770, y=150)
    q_btn3 = Button(base1, text="Exit", font=("Arial Rounded MT Bold", 17), width=13, height=1, bd=0, fg="White",
                    bg="#070707", command=teacher_interface2)
    q_btn3.place(x=1050, y=150)

    a=Entry(base1, width=24, font=("Arial", 18),bg="#bf0707",fg="white",bd=0)
    a.place(x=480,y=478)
    b = Entry(base1, width=24, font=("Arial", 18), bg="#eb8f0a", fg="white", bd=0)
    b.place(x=940, y=478)
    c = Entry(base1, width=24, font=("Arial", 18), bg="#072563", fg="white", bd=0)
    c.place(x=480, y=598)
    d = Entry(base1, width=24, font=("Arial", 18), bg="#1b6d07", fg="white", bd=0)
    d.place(x=940, y=598)

    global ans
    ans= IntVar()
    r_a=Radiobutton(base1,width=2,height=2,bg="#bf0707",variable=ans,value=1)
    r_a.place(x=800,y=475)
    r_a.select()
    r_b = Radiobutton(base1, width=2,height=2,bg="#eb8f0a",variable=ans,value=2)
    r_b.place(x=1260, y=475)
    r_c = Radiobutton(base1,width=2,height=2, bg="#072563",variable=ans,value=3)
    r_c.place(x=800, y=595)
    r_d = Radiobutton(base1,width=2,height=2, bg="#1b6d07",variable=ans,value=4)
    r_d.place(x=1260, y=595)

#Display Quiz
#================================================================================================
def display_quiz(event):

    # MY quizzes image
    quiz1 = Image.open("xyz.jpg")
    quiz2 = quiz1.resize((1350, 690))
    quiz2.save("xyz.jpg")
    quiz3 = Image.open("xyz.jpg")
    quiz4 = ImageTk.PhotoImage(quiz3)

    quiz5 = Label(image=quiz4)
    quiz5.image = quiz4
    quiz5.place(x=0, y=0)

    # Connecting to the data base
    con = sqlite3.connect("Quizstar.db")
    cur = con.cursor()
    cur.execute("select* from " + teach_pass)
    dat13 = cur.fetchall()
    con.commit()
    con.close()
    print("dat13 :",type(dat13))
    a = event.widget.cget("text")
    num=0
    for one in dat13:
        ls=list(one)
        if ls[0]==a:
            print("It Goes")
            num=num+1

    total_que_num=num

    h=120
    for j in range(1,total_que_num+1):
        dis_que = Label(base1,text=("Q",j,":"),font=("Arial Rounded MT Bold", 17), width=22, height=1,bg="#d5b8ea")
        dis_que.place(x=50, y=h)
        h=h+55
    #next_quiz function
    def next_quiz():
        for oneline in dat13:
            ls1 = list(oneline)

            print("before : ",dat13)
            dat13.remove(oneline)
            print("ls1 : ",ls1)
            print("after : ", dat13)
            global a
            a = event.widget.cget("text")
            print(a)
            #for i in ls1:
            if ls1[0]==a:
                num=ls1[1]
                con=sqlite3.connect("Quizstar.db")
                cur=con.cursor()
                cur.execute("select* from quiz_code")
                quiz_data=cur.fetchall()
                con.commit()
                con.close()
                for one in quiz_data:
                    ls=list(one)
                    if ls[2]==teach_pass:
                        code1 = Label(base1, text=ls[1], font=("Arial Rounded MT Bold", 19), width=10, height=1, bd=0, fg="White",bg="#070707")
                        code1.place(x=125, y=55)

                quize_name = Label(base1,text=a, width=67,bg="#fafafa", font=("Arial", 17), bd=0)
                quize_name.place(x=430, y=55)

                question_num = Label(base1, text=("Q",num,":"), font=("Arial Rounded MT Bold", 19), width=4, height=1, bd=0,fg="Black", bg="#fafafa")
                question_num.place(x=470, y=330)

                question = Label(base1, width=48,text=ls1[2],font=("Arial", 19), bd=0,bg="#fafafa")
                question.place(x=540, y=330)

                q_btn1 = Button(base1, text="Next", font=("Arial Rounded MT Bold", 17), width=19, height=1, bd=0,fg="White", bg="#070707", command=next_quiz)
                q_btn1.place(x=490, y=150)


                q_btn2 = Button(base1, text="Exit", font=("Arial Rounded MT Bold", 17), width=19, height=1, bd=0,fg="White", bg="#070707",command=teacher_interface2)
                q_btn2.place(x=950, y=150)



                a = Label(base1,text=ls1[3],width=25, font=("Arial", 18), bg="#bf0707", fg="white", bd=0)
                a.place(x=480, y=478)
                b = Label(base1,text=ls1[4], width=25, font=("Arial", 18), bg="#eb8f0a", fg="white", bd=0)
                b.place(x=940, y=478)
                c = Label(base1,text=ls1[5], width=25, font=("Arial", 18), bg="#072563", fg="white", bd=0)
                c.place(x=480, y=598)
                d = Label(base1,text=ls1[6], width=25, font=("Arial", 18), bg="#1b6d07", fg="white", bd=0)
                d.place(x=940, y=598)

                if ls1[7] == "1":
                    r_a = Radiobutton(base1, width=2, height=2,bg="#bf0707")
                    r_a.place(x=800, y=475)

                if ls1[7] == "2":
                    r_b = Radiobutton(base1, width=2, height=2, bg="#eb8f0a")
                    r_b.place(x=1260, y=475)

                if ls1[7] == "3":
                    r_c = Radiobutton(base1, width=2, height=2, bg="#072563")
                    r_c.place(x=800, y=595)

                if ls1[7] == "4":
                    r_d = Radiobutton(base1, width=2, height=2, bg="#1b6d07")
                    r_d.place(x=1260, y=595)

                print("ls1[7] : ",type(ls1[7]))


                break

    next_quiz()
#=====================================================================================
#teacher interface function again check after making class
def teacher_interface2():

        # teacher_Interface image
        int1 = Image.open("teacher_interface.jpg")
        int2 = int1.resize((1350, 690))
        int2.save("teacher_interface.jpg")
        int3 = Image.open("teacher_interface.jpg")
        int4 = ImageTk.PhotoImage(int3)
        int5 = Label(image=int4)
        int5.image = int4
        int5.place(x=0, y=0)

        # teacher_interface Page body
        exit_tea_interface = Button(base1, text="Exit", width=8, font=("Arial Rounded MT Bold", 18), height=1,
                                    bg="white", fg="black", bd=0,command=teacher_login)
        exit_tea_interface.place(x=1130, y=50)

        i_btn1 = Button(base1, text="Create Quiz", font=("Arial Rounded MT Bold", 20), width=10, height=1, bd=0, bg="white",command=create_quiz)
        i_btn1.place(x=310, y=300)

        i_btn2 = Button(base1, text="My Quizes", font=("Arial Rounded MT Bold", 20), width=10, height=1, bd=0, bg="white",command=my_quizzes)
        i_btn2.place(x=650, y=300)

        i_btn3 = Button(base1, text="Responses", font=("Arial Rounded MT Bold", 20), width=10, height=1, bd=0, bg="white",command=response)
        i_btn3.place(x=410, y=550)

        i_btn4 = Button(base1, text=" My Profile ", font=("Arial Rounded MT Bold", 20), width=10, height=1, bd=0, bg="white",command=None)
        i_btn4.place(x=760, y=550)

#======================================================================================
def response():

    # Results image
    quiz1 = Image.open("response.jpg")
    quiz2 = quiz1.resize((1350, 690))
    quiz2.save("response.jpg")
    quiz3 = Image.open("response.jpg")
    quiz4 = ImageTk.PhotoImage(quiz3)
    quiz5 = Label(image=quiz4)
    quiz5.image = quiz4
    quiz5.place(x=0, y=0)

    close = Button(base1, text="Exit", font=("Arial Rounded MT Bold", 17), width=8, height=1, bd=0, fg="White",bg="#070707", command=teacher_interface2)
    close.place(x=1100, y=20)

    con=sqlite3.connect("Quizstar.db")
    cur=con.cursor()
    cur.execute("select* from stu_res")
    tea_res=cur.fetchall()
    print("fetched")
    con.commit()
    con.close()
    ls_imp=[]
    ls1=[]
    for oneline in tea_res:

        ls2=list(oneline)
        print("ls2 :",ls2)
        print("ls2[-2] : ",ls2[-2])
        print("teach_pass : ",teach_pass)
        if ls2[-2]==teach_pass:
            print("yes")
            print(ls2[1])
            print(ls2[0])
            print(ls2[2])
            print(ls2[3])
            ls1=[]
            ls1.append(ls2[1])
            ls1.append(ls2[0])
            ls1.append(ls2[2])
            ls1.append(ls2[3])
            ls_imp.append(ls1)
            print("ls1 : ",ls1)
            print("ls imp :",ls_imp)

    # response body
    #total_quiz = 12
    d = 168
    u = 480
    v = 790
    w = 960
    t = 180

    for oneline in ls_imp:
        ls3=list(oneline)
        quiz_name = Label(base1, text=ls3[0], font=("Arial Rounded MT Bold", 14), width=23,height=1, bd=1, fg="black", bg="#e7e5e6")
        quiz_name.place(x=d, y=t)
        stu_name = Label(base1, text=ls3[1], font=("Arial Rounded MT Bold", 14), width=23, height=1,bd=1, fg="black", bg="#e7e5e6")
        stu_name.place(x=u, y=t)

        # coonecting to the database to calculate total number of questions
        con=sqlite3.connect("Quizstar.db")
        cur=con.cursor()
        cur.execute("select* from "+teach_pass)
        questions = cur.fetchall()
        con.commit()
        con.close()
        qu=0
        for one in questions:
            ques=list(one)
            if ques[0]==ls3[0]:
                qu=qu+1

        #temp=(ls3[2]/qu)*20
        marks = Label(base1, text= str(ls3[2])+"/"+str(qu), font=("Arial Rounded MT Bold", 14), width=11, height=1, bd=1,fg="black", bg="#e7e5e6")
        marks.place(x=v, y=t)

        date_time = Label(base1, text=ls3[3], font=("Arial Rounded MT Bold", 14), width=22, height=1, bd=1, fg="black",bg="#e7e5e6")
        date_time.place(x=w, y=t)

        t = t + 40
#========================================================================================
def my_quizzes():

    # MY quizzes image
    quiz1 = Image.open("my_quizzes.jpg")
    quiz2 = quiz1.resize((1350, 690))
    quiz2.save("my_quizzes.jpg")
    quiz3 = Image.open("my_quizzes.jpg")
    quiz4 = ImageTk.PhotoImage(quiz3)

    quiz5 = Label(image=quiz4)
    quiz5.image = quiz4
    quiz5.place(x=0, y=0)

    exit_my_quiz = Button(base1, text="Exit", width=8, font=("Arial Rounded MT Bold", 18), height=1, bg="white",
                          fg="black", bd=0,command=teacher_interface2)
    exit_my_quiz.place(x=1100, y=90)

    con = sqlite3.connect("Quizstar.db")
    cur=con.cursor()
    cur.execute("select* from "+teach_pass)
    dat12=cur.fetchall()
    con.commit()
    con.close()
    global ls1
    count=0
    ls1=[]
    for oneline in dat12:
        ls = oneline
        ls2=[]
        ls2.append(ls[0])
        print("ls :",ls)
        for i in ls2:
            print("i : ",i)
            if i not in dat12:
                if i not in ls1:
                    ls1.append(i)
                    count=count+1

    total_quiz=count #retrive from databse
    print("count :",count)

    u = 200
    t = 230
    for i in range(0, total_quiz):
        quiz = Button(base1, text=ls1[i], font=("Arial Rounded MT Bold", 17), width=25, height=2, bd=0,fg="White", bg="#070707")
        quiz.place(x=u, y=t)
        quiz.bind("<Button-1>", display_quiz)
        t = t + 90
        if i==3:
            u=800
            t=230

#+========================================================================

# Teacher login *************Original
def teacher_login():

    # new Teacher : **********
    def new_teacher():

        # new teacher image :
        new_t1 = Image.open("new_teacher.jpg")
        new_t2 = new_t1.resize((1350, 690))
        new_t2.save("new_teacher.jpg")
        new_t3 = Image.open("new_teacher.jpg")
        new_t4 = ImageTk.PhotoImage(new_t3)
        new_t5 = Label(image=new_t4)
        new_t5.image = new_t4
        new_t5.place(x=0, y=0)

        # submit student Form
        def submit_teacher():
            # store in database
            dat6 = t_en6.get()
            dat7 = t_en7.get()

            # Checking that the new password and Confirm password is same or not...
            if dat6 == dat7:
                dat1 = t_en1.get()
                dat2 = t_en2.get()
                dat3 = t_en3.get()
                dat4 = t_en4.get()
                dat5 = t_en5.get()

                con = sqlite3.connect("Quizstar.db")
                query1 = "insert into new_teacher(name,email_id,phone_no,subject,college_name,new_pass,confirm_pass) values ('" + dat1 + "','" + dat2 + "','" + dat3 + "','" + dat4 + "','" + dat5 + "','" + dat6 + "','" + dat7 + "')"
                cur=con.cursor()
                cur.execute(query1)
                #con.commit()
                print("Succesfully Data Saved...")

                query2 = '''CREATE TABLE '''+dat2+'''(
                   quiz_name VARCHAR(20),
                   sr_no INT(20) NOT NULL,
                   question VARCHAR(50),
                   a VARCHAR(20),
                   b VARCHAR(20),
                   c VARCHAR(20),
                   d VARCHAR(20),
                   ans VARCHAR(2)
                )'''

                cur.execute(query2)
                con.commit()
                con.close()
                # Pausing for while
                time.sleep(1)
                # Calling to the new techer login functions
                teacher_login()
            else:
                t_en6.delete(0, END)
                t_en7.delete(0, END)
                t_en6.focus()

        # new teacher body :
        # name
        t_en1 = Entry(base1, width=35, font=("Arial", 17), bd=0)
        t_en1.place(x=120, y=140)
        # email
        t_en2 = Entry(base1, width=35, font=("Arial", 17), bd=0)
        t_en2.place(x=120, y=285)
        # phone no
        t_en3 = Entry(base1, width=35, font=("Arial", 17), bd=0)
        t_en3.place(x=120, y=430)
        # subject
        t_en4 = Entry(base1, width=35, font=("Arial", 17), bd=0)
        t_en4.place(x=120, y=570)
        # institute
        t_en5 = Entry(base1, width=35, font=("Arial", 17), bd=0)
        t_en5.place(x=780, y=140)
        # new password
        t_en6 = Entry(base1, width=35, font=("Arial", 17), bd=0)
        t_en6.place(x=780, y=295)
        # confirm password
        t_en7 = Entry(base1, width=35, font=("Arial", 17), bd=0)
        t_en7.place(x=780, y=430)

        # Clear teacherForm
        def clear_new_teacher():
            t_en1.delete(0, END)
            t_en2.delete(0, END)
            t_en3.delete(0, END)
            t_en4.delete(0, END)
            t_en5.delete(0, END)
            t_en6.delete(0, END)
            t_en7.delete(0, END)
            # base5.destroy()

        t_btn1 = Button(base1, text="Clear", font=("Arial Rounded MT Bold", 20), width=8, height=1, bd=0, fg="white",
                        bg="#c00000", command=clear_new_teacher)
        t_btn1.place(x=815, y=555)
        t_btn1 = Button(base1, text="Submit", font=("Arial Rounded MT Bold", 20), width=8, height=1, bd=0, fg="white",
                        bg="#c00000", command=submit_teacher)
        t_btn1.place(x=1065, y=555)

#==============================================================================================
    # Teacher Interface :***********
# ==============================================================================================

    def teacher_interface():

        def teacher_profile():

            # base1 = Tk()
            # base1.title("Exam quiz software")
            # base1.geometry("1350x690")
            # base1.geometry("+1+1")


            # reset password image
            quiz1 = Image.open("teacher_profile.jpg")
            quiz2 = quiz1.resize((1350, 690))
            quiz2.save("teacher_profile.jpg")
            quiz3 = Image.open("teacher_profile.jpg")
            quiz4 = ImageTk.PhotoImage(quiz3)
            quiz5 = Label(image=quiz4)
            quiz5.image = quiz4
            quiz5.place(x=0, y=0)

            con=sqlite3.connect("Quizstar.db")
            cur=con.cursor()
            cur.execute("select* from new_teacher")
            tea_data=cur.fetchall()

            con.commit()
            con.close()

            for one in tea_data:
                tea=list(one)
                if tea[1]==teach_pass:

                    lb1 = Label(base1, text=tea[0], font=("Arial", 17), width=28, height=1, bd=0, bg="white")
                    lb1.place(x=120, y=170)
                    lb2 = Label(base1, text=tea[1], font=("Arial", 17), width=28, height=1, bd=0, bg="white")
                    lb2.place(x=120, y=250)
                    lb3 = Label(base1, text=tea[2], font=("Arial", 17), width=28, height=1, bd=0, bg="white")
                    lb3.place(x=120, y=330)
                    lb4 = Label(base1, text=tea[3], font=("Arial", 17), width=28, height=1, bd=0, bg="white")
                    lb4.place(x=120, y=410)
                    lb5 = Label(base1, text=tea[4], font=("Arial", 17), width=28, height=1, bd=0, bg="white")
                    lb5.place(x=120, y=490)
                    tea_pass=list(tea[5])
                    len_pass=len(tea_pass)
                    fi=[]
                    for i in range(len_pass):
                        if i>=3:
                            fi.append("*")
                        else:
                            fi.append(tea_pass[i])

                    lb6 = Label(base1, text=fi, font=("Arial", 17), width=28, height=1, bd=0, bg="white")
                    lb6.place(x=120, y=560)

                    change_pass = Button(base1, text="Change\nPassword", width=12, font=("Arial Rounded MT Bold", 12), height=2,
                                         bg="#c00000", fg="white", bd=0, command=forget_password2)
                    change_pass.place(x=245, y=610)

                    exit_btn = Button(base1, text="Exit", width=8, font=("Arial Rounded MT Bold", 18), height=1, bg="#c00000",
                                      fg="white", bd=0, command=teacher_interface2)
                    exit_btn.place(x=1140, y=40)

            photo = PhotoImage(file=r"power.png")
            print("Rahul3")
            img = Button(base1, bg="white", bd=0, width=55, height=55, command=teacher_login)
            img.configure(image=photo)
            print("Rahul2")
            img.place(x=1249, y=596)
            print("Rahul")
            base1.mainloop()

        # ============================================================================================
        #==================================================
        global teach_pass
        teach_pass = en1.get()
        dat2 = en2.get()
        print(teach_pass)
        print(dat2)
        con = sqlite3.connect("Quizstar.db")
        cur = con.cursor()
        query = "select* from new_teacher"
        cur.execute(query)
        dat3 = cur.fetchall()
        print("dat3", dat3)
        # checking that entered password and username is right or wrong

        for oneline in dat3:
            ls = oneline
            if ls[1] == teach_pass:
                print("ls1 : ",ls[1])
                print("dat1 : ",teach_pass)
                if ls[6] == dat2:

                    print("ls6 : ", ls[6])
                    print("dat2 : ", dat2)

                    # teacher_Interface image
                    int1 = Image.open("teacher_interface.jpg")
                    int2 = int1.resize((1350, 690))
                    int2.save("teacher_interface.jpg")
                    int3 = Image.open("teacher_interface.jpg")
                    int4 = ImageTk.PhotoImage(int3)
                    int5 = Label(image=int4)
                    int5.image = int4
                    int5.place(x=0, y=0)

                    # teacher_interface Page body
                    exit_tea_interface = Button(base1, text="Exit", width=8, font=("Arial Rounded MT Bold", 18),
                                                height=1,
                                                bg="white", fg="black", bd=0, command=teacher_login)
                    exit_tea_interface.place(x=1130, y=50)

                    i_btn1 = Button(base1, text="Create Quiz", font=("Arial Rounded MT Bold", 20), width=10, height=1, bd=0, bg="white",command=create_quiz)
                    i_btn1.place(x=310, y=300)

                    i_btn2 = Button(base1, text="My Quizes", font=("Arial Rounded MT Bold", 20), width=10, height=1, bd=0, bg="white",command=my_quizzes)
                    i_btn2.place(x=650, y=300)

                    i_btn3 = Button(base1, text="Responses", font=("Arial Rounded MT Bold", 20), width=10, height=1, bd=0, bg="white",command=response)
                    i_btn3.place(x=410, y=550)

                    i_btn4 = Button(base1, text=" My Profile ", font=("Arial Rounded MT Bold", 20), width=10, height=1, bd=0, bg="white",command=teacher_profile)
                    i_btn4.place(x=760, y=550)
                else:
                    en1.delete(0, END)
                    en2.delete(0,END)
                    en1.focus()
                    lb3 = Label(base1, text="Invalid Username or Password !", font=("Arial Rounded MT Bold", 17), width=30,height=1, bd=0, fg="#c00000", bg="white")
                    lb3.place(x=470, y=570)
            '''else:
                en1.delete(0, END)
                en2.delete(0, END)
                en1.focus()
                lb2 = Label(base1, text="Invalid Username or Password !", font=("Arial Rounded MT Bold", 17), width=30,height=1, bd=0, fg="#c00000", bg="white")
                lb2.place(x=470, y=570)'''

    def forget_password2():

        # forget password image
        quiz1 = Image.open("forget_password.jpg")
        quiz2 = quiz1.resize((1350, 690))
        quiz2.save("forget_password.jpg")
        quiz3 = Image.open("forget_password.jpg")
        quiz4 = ImageTk.PhotoImage(quiz3)
        quiz5 = Label(image=quiz4)
        quiz5.image = quiz4
        quiz5.place(x=0, y=0)

        # Forget password body
        # mobile no
        en1 = Entry(base1, width=30, font=("Arial", 15), bd=0)
        en1.place(x=520, y=415)

        #============================================================================
        def otp():

            phone_no=en1.get()
            # connecting database
            con=sqlite3.connect("Quizstar.db")
            cur=con.cursor()
            cur.execute("select* from new_teacher")

            new_data=cur.fetchall()
            con.commit()
            con.close()

            for one in new_data:
                ls_data=list(one)
                if int(ls_data[2])==int(phone_no):

                    otp = str(random.randint(11111, 99999))
                    url = "https://www.fast2sms.com/dev/bulk"
                    txt_msg2 = ("*********QUIZSTAR*********")
                    txt_msg0 = ("\nHi " + ls_data[0])
                    txt_msg3 = (" Your OTP to reset /access QuizStar Account is  : ")
                    txt_msg4 = ("\nIt will be valid for 3 minutes.")
                    txt_msg5 = ("\n\n- QUIZSTAR")
                    txt_msg6 = ("\n***********")
                    try:
                        querystring = {
                            "authorization": "GLHtK9z17QesfiEhAKeBfPFK5czH4mj2bRksYxKqoVIvQRYcK8Q53UQS6IQv",
                            "sender_id": "FSTSMS",
                            "message": txt_msg2 + txt_msg0 + txt_msg3 + otp + txt_msg4 + txt_msg5 + txt_msg6,
                            "language": "english", "route": "p", "numbers": phone_no
                        }

                        headers = {
                            'cache-control': "no-cache"
                        }

                        response = requests.request("GET", url, headers=headers, params=querystring)

                        print(response.text)
                    except:
                        lb1 = Label(base1, text="Technical Error Try Again Later",
                                    font=("Arial Rounded MT Bold", 17),
                                    width=30, height=1, bd=0, fg="#c00000", bg="white")
                        lb1.place(x=470, y=570)

                    print("----------------------------------------------------")
                    #=================================================================================================

                    #time.sleep(1)
                    # OTP image
                    quiz1 = Image.open("otp.jpg")
                    quiz2 = quiz1.resize((1350, 690))
                    quiz2.save("otp.jpg")
                    quiz3 = Image.open("otp.jpg")
                    quiz4 = ImageTk.PhotoImage(quiz3)
                    quiz5 = Label(image=quiz4)
                    quiz5.image = quiz4
                    quiz5.place(x=0, y=0)

                    # OTP body
                    # otp
                    en_otp = Entry(base1, width=30, font=("Arial", 15), bd=0)
                    en_otp.place(x=520, y=340)
                    #==============================================================================================
                    def reset_password():
                        new_otp=en_otp.get()
                        if int(otp)==int(new_otp):

                            # reset password image
                            quiz1 = Image.open("reset_password.jpg")
                            quiz2 = quiz1.resize((1350, 690))
                            quiz2.save("reset_password.jpg")
                            quiz3 = Image.open("reset_password.jpg")
                            quiz4 = ImageTk.PhotoImage(quiz3)
                            quiz5 = Label(image=quiz4)
                            quiz5.image = quiz4
                            quiz5.place(x=0, y=0)

                            def new_pass():
                                new=en11.get()
                                confirm = en21.get()
                                print("new : ",new)
                                print("confirm : ",confirm)
                                if new==confirm:

                                    con = sqlite3.connect("Quizstar.db")
                                    cur = con.cursor()

                                    cur.execute("""Update new_teacher set new_pass = ?,confirm_pass= ? where phone_no = ? """,
                                                (confirm,confirm,phone_no))
                                    print("password changed succesfully")
                                    lb1.config(text="Password Reset Succesfully !",fg="green")
                                    con.commit()
                                    con.close()

                                else:
                                    lb1.config(text="Password Did Not Matched  !")

                            # reset_password body
                            #new pass
                            en11 = Entry(base1, width=30, font=("Arial", 15), bd=0)
                            en11.place(x=520, y=325)

                            lb1 = Label(base1, text="",
                                        font=("Arial Rounded MT Bold", 17),
                                        width=30, height=1, bd=0, fg="#c00000", bg="white")
                            lb1.place(x=470, y=570)

                            en21 = Entry(base1, width=30, font=("Arial", 15), bd=0)
                            en21.place(x=520, y=410)

                            btn1 = Button(base1, text="Reset Password", font=("Arial Rounded MT Bold", 20), width=20, height=1,
                                          bd=0, fg="white", bg="#c00000", command=new_pass)
                            btn1.place(x=510, y=480)

                            btn2 = Button(base1, text="Back to Login", font=("Arial Rounded MT Bold", 16), width=36, height=1,
                                          bd=0, fg="black", bg="#d0cecf", command=teacher_login)
                            btn2.place(x=440, y=630)

                        else:
                            lb1 = Label(base1, text="OTP did not matched !", font=("Arial Rounded MT Bold", 17),width=30,height=1, bd=0, fg="#c00000", bg="white")
                            lb1.place(x=470, y=570)
                            en_otp.delete(0,END)
                            en_otp.focus()
                    # ==============================================================================================

                    btn1 = Button(base1, text=" Submit OTP ", font=("Arial Rounded MT Bold", 20), width=20, height=1, bd=0,
                                  fg="white", bg="#c00000", command=reset_password)
                    btn1.place(x=510, y=480)

                    btn2 = Button(base1, text="Back to Login", font=("Arial Rounded MT Bold", 16), width=36, height=1, bd=0,
                                  fg="black", bg="#d0cecf", command=teacher_login)
                    btn2.place(x=440, y=630)
                    break
         #============================================================================

        btn1 = Button(base1, text="Send OTP", font=("Arial Rounded MT Bold", 20), width=20, height=1, bd=0,
                      fg="white", bg="#c00000", command=otp)
        btn1.place(x=510, y=480)

        btn2 = Button(base1, text="Back to Login", font=("Arial Rounded MT Bold", 16), width=36, height=1, bd=0,
                      fg="black", bg="#d0cecf", command=teacher_login)
        btn2.place(x=440, y=630)
        #=================================================================================================

    #teacher_login image
    t1 = Image.open("teacher_login.jpg")
    t2 = t1.resize((1350, 690))
    t2.save("teacher_login.jpg")
    t3 = Image.open("teacher_login.jpg")
    t4 = ImageTk.PhotoImage(t3)
    t5 = Label(image=t4)
    t5.image = t4
    t5.place(x=0, y=0)

    #login_page body
    en1= Entry(base1, width=30, font=("Arial", 15), bd=0)
    en1.place(x=520, y=220)
    en2 = Entry(base1, width=30, font=("Arial", 15), bd=0,show = "*")
    en2.place(x=520, y=300)

    btn1 = Button(base1, text="Login", font=("Arial Rounded MT Bold", 20), width=20, height=1, bd=0,fg="white",bg="#c00000",command=teacher_interface)
    btn1.place(x=510, y=465)
    btn2 = Button(base1, text="New user ? Sign Up! ", font=("Calibri (Body)", 15), width=30, height=1, bd=0, bg="white",command=new_teacher)
    btn2.place(x=500, y=350)

    btn3 = Button(base1, text="Forget password ? ", font=("Calibri (Body)", 14), width=30, height=1, bd=0, bg="white",command=forget_password2)
    btn3.place(x=500, y=390)

    btn4 = Button(base1, text="<  Back to Homepage  >", font=("Arial Rounded MT Bold", 16), width=36, height=1, bd=0,
                  fg="black", bg="#d0cecf", command=first)
    btn4.place(x=440, y=630)

#===================================================================================]
# new student login function......
#==================================================================================

def student_login():
    #flag1=0
    global student_user
    #base1.destroy()
    '''base3 = Tk()
    base3.title("Exam quiz software")
    base3.geometry("1350x690")
    base3.geometry("+1+1")'''

    # new Student : **********
    def new_student():

        # new Student image :
        new_s1 = Image.open("new_student.jpg")
        new_s2 = new_s1.resize((1350, 690))
        new_s2.save("new_student.jpg")
        new_s3 = Image.open("new_student.jpg")
        new_s4 = ImageTk.PhotoImage(new_s3)
        new_s5 = Label(image=new_s4)
        new_s5.image = new_s4
        new_s5.place(x=0, y=0)

        # new Student body :
        s_en1 = Entry(base1, width=35, font=("Arial", 17), bd=0)
        s_en1.place(x=120, y=140)
        s_en2 = Entry(base1, width=35, font=("Arial", 17), bd=0)
        s_en2.place(x=120, y=285)
        s_en3 = Entry(base1, width=35, font=("Arial", 17), bd=0)
        s_en3.place(x=120, y=430)
        s_en4 = Entry(base1, width=35, font=("Arial", 17), bd=0)
        s_en4.place(x=120, y=570)
        s_en5 = Entry(base1, width=35, font=("Arial", 17), bd=0)
        s_en5.place(x=780, y=140)
        s_en6 = Entry(base1, width=35, font=("Arial", 17), bd=0)
        s_en6.place(x=780, y=295)
        s_en7 = Entry(base1, width=35, font=("Arial", 17), bd=0)
        s_en7.place(x=780, y=430)

        # Clear student Form
        def clear_new_student():
            s_en1.delete(0,END)
            s_en2.delete(0,END)
            s_en3.delete(0,END)
            s_en4.delete(0,END)
            s_en5.delete(0,END)
            s_en6.delete(0,END)
            s_en7.delete(0,END)

        # submit student Form
        def submit_student():
            global student_user
            dat6 = s_en6.get()
            dat7 = s_en7.get()
            if dat6==dat7:

                #store in database
                dat1 = s_en1.get()
                student_user = s_en2.get()
                dat3 = s_en3.get()
                dat4 = s_en4.get()
                dat5 = s_en5.get()
                dat6 = s_en6.get()

                con = sqlite3.connect("Quizstar.db")
                query1 = "insert into new_student(name,email_id,phone_no,enroll,class,pass) values ('" + dat1 + "','" + student_user + "','" + dat3 + "','" + dat4 + "','" + dat5 + "','" + dat6 + "')"
                con.execute(query1)

                #creating another table
                query2 = '''CREATE TABLE ''' + student_user + '''(
                                   quiz_name VARCHAR(20),
                                   sr_no INT(20) NOT NULL,
                                   stu_ans INT(20)
                                )'''
                con.execute(query2)
                print("The each table is created..!!")
                con.commit()
                print("Succesfully Data Saved...")

                con.close()
                #Calling to new student login function
                time.sleep(1)
                student_login()
                #base6.destroy()
            else:
                s_en6.delete(0,END)
                s_en7.delete(0,END)
                s_en6.focus()

        s_btn1 = Button(base1, text="Clear", font=("Arial Rounded MT Bold", 20), width=8, height=1, bd=0, fg="white",bg="#c00000", command=clear_new_student)
        s_btn1.place(x=815, y=555)
        s_btn1 = Button(base1, text="Submit", font=("Arial Rounded MT Bold", 20), width=8, height=1, bd=0, fg="white",bg="#c00000", command=submit_student)
        s_btn1.place(x=1065, y=555)

    # Start Quiz Info
    #============================================
    def start_quiz():

        # Answer Quiz
        def answer_quiz():
            global ans1, num,teach,stu_name,quiz_cd
            dat1 = en1.get()
            dat2 = en2.get()
            dat3 = en3.get()
            stu_name=dat1
            quiz_cd=str(dat3)

            con=sqlite3.connect("Quizstar.db")
            cur=con.cursor()
            query1="select* from quiz_code"
            cur.execute(query1)
            dat11=cur.fetchall()
            con.commit()
            con.close()
            flag=0
            for oneline in dat11:
                ls1=list(oneline)

                if ls1[1]==int(dat3):
                    flag=1
                    quiz_name = ls1[0]
                    teach = ls1[2]
                    print("Quiz name : ",quiz_name)
                    print("teach pass : ", teach)

            if flag==0:
                print("yessss")
                lb.configure(text="Invalid Exam Code !")
                en3.delete(0,END)
                en3.focus()
                return
            #==================================================================
            #next question
            #====================================================================
            # Answer quiz image
            quiz1 = Image.open("answer_quiz.jpg")
            quiz2 = quiz1.resize((1350, 690))
            quiz2.save("answer_quiz.jpg")
            quiz3 = Image.open("answer_quiz.jpg")
            quiz4 = ImageTk.PhotoImage(quiz3)
            quiz5 = Label(image=quiz4)
            quiz5.image = quiz4
            quiz5.place(x=0, y=0)

            con = sqlite3.connect("Quizstar.db")
            cur = con.cursor()
            query1 = "select* from "+str(teach)
            cur.execute(query1)
            dat12 = cur.fetchall()
            con.commit()
            con.close()
            ls=[]

            def final_ques():
                global num,student_user
                te = str(ans1.get())
                con = sqlite3.connect("Quizstar.db")
                cur = con.cursor()
                print("before")
                query2 = "insert into "+stu+"(quiz_name,sr_no,stu_ans) values('" + quiz_name + "','" + str(num) + "','" + te + "')"
                cur.execute(query2)
                print("Succesfully Data Inserted..!!!")
                con.commit()

                query3="select* from "+teach
                cur.execute(query3)
                tea_ans=cur.fetchall()
                print("Succesfully Teacher Data Retrived for marks calculation.!!!")
                con.commit()

                query4="select* from "+stu
                cur.execute(query4)
                stu_ans=cur.fetchall()

                con.commit()
                con.close()

                marks=0
                for (a,b) in zip(tea_ans,stu_ans):
                    ds1=list(a)
                    ds2=list(b)
                    print("ds1 : ",ds1)

                    #print("ds2 : ",ds2)
                    #for i in ds1:
                    #print("ds1[i] : ",i)
                    #for j in ds2:
                    if ds1[0]==ds2[0]:
                        if int(ds1[-1])==int(ds2[-1]):
                            marks=marks+1

                    #break

                now = datetime.datetime.now()
                quiz_time = (now.strftime('%Y-%m-%d %H:%M:%S'))

                con=sqlite3.connect("Quizstar.db")
                cur=con.cursor()
                cur.execute("select* from quiz_code")
                quiz_code_data=cur.fetchall()
                con.commit()
                con.close()

                con=sqlite3.connect("Quizstar.db")
                cur=con.cursor()
                cur.execute("select* from new_student")
                temp_data=cur.fetchall()
                con.commit()
                con.close()
                for one in temp_data:
                    temp=list(one)
                    if temp[1]==stu:
                        s_name=temp[0]

                for oneline in quiz_code_data:
                    data1=list(oneline)
                    for i in data1:
                        if int(data1[1])==int(quiz_cd):
                            teach_table=data1[2]
                            break

                print("Student_user:",stu)
                con=sqlite3.connect("Quizstar.db")
                cur=con.cursor()
                query5="insert into stu_res values('"+str(s_name)+"','"+str(quiz_name)+"','"+str(marks)+"','"+str(quiz_time)+"','"+str(teach_table)+"','"+str(stu)+"')"
                cur.execute(query5)
                con.commit()
                con.close()
                student_interface()

            def next_ques():#1
                global temp,num,flag1,student_user,pk

                if pk==1:
                    te=str(ans1.get())
                    con = sqlite3.connect("Quizstar.db")
                    cur = con.cursor()
                    print("before")
                    query2 = "insert into "+stu+"(quiz_name,sr_no,stu_ans) values('"+quiz_name+"','"+str(num)+"','"+te+"')"
                    cur.execute(query2)
                    print("Succesfully Data Inserted..!!!")

                    con.commit()
                    con.close()
                pk=1

                for oneline in dat12:
                    ls1 = list(oneline)
                    ls.append(oneline)
                    dat12.remove(oneline)

                    if ls1[0] == quiz_name:
                        num = ls1[1]
                        question_num = Label(base1, text=("Q", num, ":"), font=("Arial Rounded MT Bold", 19), width=4,height=1,bd=0, fg="Black", bg="#fafafa")
                        question_num.place(x=470, y=330)
                        question = Label(base1, text=ls1[2], width=43, font=("Arial Rounded MT Bold", 19),bd=0,fg="black", bg="#fafafa")
                        question.place(x=540, y=330)
                        q_btn1 = Button(base1, text="Next", font=("Arial Rounded MT Bold", 17), width=13, height=1,bd=0,fg="White", bg="#070707", command=next_ques)
                        q_btn1.place(x=480, y=150)
                        q_btn2 = Button(base1, text="Submit", font=("Arial Rounded MT Bold", 17), width=13, height=1,
                                        bd=0, fg="White", bg="#070707", command=final_ques)
                        q_btn2.place(x=768, y=150)
                        q_btn3 = Button(base1, text="Exit", font=("Arial Rounded MT Bold", 17), width=13, height=1,
                                        bd=0, fg="White", bg="#070707", command=student_interface)
                        q_btn3.place(x=1050, y=150)

                        a = Label(base1, text=ls1[3], width=23, font=("Arial", 18), bg="#bf0707", fg="white", bd=0)
                        a.place(x=480, y=478)
                        b = Label(base1, text=ls1[4], width=23, font=("Arial", 18), bg="#eb8f0a", fg="white", bd=0)
                        b.place(x=940, y=478)
                        c = Label(base1, text=ls1[5], width=23, font=("Arial", 18), bg="#072563", fg="white", bd=0)
                        c.place(x=480, y=598)
                        d = Label(base1, text=ls1[6], width=23, font=("Arial", 18), bg="#1b6d07", fg="white", bd=0)
                        d.place(x=940, y=598)

                        temp = ans1.get()
                        print("ans :",temp)

                        return
                        #break
                        # var =IntVar()
                        # r_a = Radiobutton(base1, width=2, height=2,variable=var,value=1,bg="#bf0707")
                        # r_a.place(x=800, y=475)
                        # r_b = Radiobutton(base1, width=2, height=2, bg="#eb8f0a",variable=var,value=2)
                        # r_b.place(x=1260, y=475)
                        # r_c = Radiobutton(base1, width=2, height=2, bg="#072563",variable=var,value=3)
                        # r_c.place(x=800, y=595)
                        # r_d = Radiobutton(base1, width=2, height=2, bg="#1b6d07",variable=var,value=4)
                        # r_d.place(x=1260, y=595)
            #+=========================================================================
            ans1 = IntVar()
            r_a = Radiobutton(base1, width=2, height=2, bg="#bf0707", variable=ans1, value=1)
            r_a.place(x=800, y=475)
            r_a.deselect()
            r_b = Radiobutton(base1, width=2, height=2, bg="#eb8f0a", variable=ans1, value=2)
            r_b.place(x=1260, y=475)
            r_b.deselect()
            r_c = Radiobutton(base1, width=2, height=2, bg="#072563", variable=ans1, value=3)
            r_c.place(x=800, y=595)
            r_c.deselect()
            r_d = Radiobutton(base1, width=2, height=2, bg="#1b6d07", variable=ans1, value=4)
            r_d.place(x=1260, y=595)
            r_d.deselect()

            code1 = Label(base1, text=dat3, font=("Arial Rounded MT Bold", 19), width=10, height=1, bd=0,
                          fg="White", bg="#070707")
            code1.place(x=130, y=390)
            heading = Label(base1, text=quiz_name, font=("Arial Rounded MT Bold", 19), width=51,
                            height=1, bd=4, fg="Black", bg="#fafafa")
            heading.place(x=450, y=45)
            name = Label(base1, text=st_name, width=22, font=("Arial", 15), bg="#fafafa", fg="black",
                         bd=0)
            name.place(x=100, y=225)
            enr = Label(base1, text=st_enroll, width=22, font=("Arial", 15), bg="#fafafa", fg="black", bd=0)
            enr.place(x=100, y=305)

            total_quiz = len(dat12) # retrive from database

            u = 80
            t = 450
            for i in range(1, total_quiz + 1):
                quiz = Label(base1, text=("Q", i), font=("Arial Rounded MT Bold", 17), width=4, height=1, bd=1,
                             fg="White", bg="#c00000")
                quiz.place(x=u, y=t)
                u = u + 70
                if i == 4:

                    u = 80
                    t = 490
                elif i == 8:
                    u = 80
                    t = 530
                elif i == 12:
                    u = 80
                    t = 570
                elif i == 16:
                    u = 80
                    t = 610
            pk = 0
            next_ques()
        #+=============================================================
        # Create quiz image
        quiz1 = Image.open("start_quiz.jpg")
        quiz2 = quiz1.resize((1350, 690))
        quiz2.save("start_quiz.jpg")
        quiz3 = Image.open("start_quiz.jpg")
        quiz4 = ImageTk.PhotoImage(quiz3)
        quiz5 = Label(image=quiz4)
        quiz5.image = quiz4
        quiz5.place(x=0, y=0)

        # create quiz body :
        con=sqlite3.connect("Quizstar.db")
        cur=con.cursor()
        cur.execute("select* from new_student")
        student_data=cur.fetchall()
        con.commit()
        con.close()

        global st_name,st_enroll
        for oneline in student_data:
            ls100=list(oneline)
            if ls100[1]==stu:
                #student name
                lab1=Label(base1,text=ls100[0],font=("arial",15),bg="white")
                st_name=ls100[0]
                lab1.place(x=520,y=220)
                lab2 = Label(base1, text=ls100[3], font=("arial", 15),bg="white")
                lab2.place(x=520, y=300)
                st_enroll=ls100[3]
                en3 = Entry(base1, width=30, font=("Arial", 15), bd=0)
                en3.place(x=520, y=385)
                btn1 = Button(base1, text="Start Exam", font=("Arial Rounded MT Bold", 20), width=20, height=1, bd=0,
                              fg="white", bg="#c00000", command=answer_quiz)
                btn1.place(x=500, y=495)
                btn4 = Button(base1, text="<  Back to Interface  >", font=("Arial Rounded MT Bold", 16), width=36,
                              height=1, bd=0, fg="black", bg="#d0cecf", command=student_interface)
                btn4.place(x=440, y=630)

    #====================================================================================
    # Student Interface :***********
    def student_interface():
        #==============================================================
        def student_profile():



            # base1 = Tk()
            # base1.title("Exam quiz software")
            # base1.geometry("1350x690")
            # base1.geometry("+1+1")

            # reset password image
            quiz1 = Image.open("student_profile.jpg")
            quiz2 = quiz1.resize((1350, 690))
            quiz2.save("student_profile.jpg")
            quiz3 = Image.open("student_profile.jpg")
            quiz4 = ImageTk.PhotoImage(quiz3)
            quiz5 = Label(image=quiz4)
            quiz5.image = quiz4
            quiz5.place(x=0, y=0)



            con = sqlite3.connect("Quizstar.db")
            cur = con.cursor()
            cur.execute("select* from new_student")
            stu_data = cur.fetchall()

            con.commit()
            con.close()

            for one in stu_data:
                s_data = list(one)
                if s_data[1] == stu:

                    lb1 = Label(base1, text=s_data[0], font=("Arial", 17), width=28, height=1, bd=0, bg="white")
                    lb1.place(x=120, y=170)
                    lb2 = Label(base1, text=s_data[1], font=("Arial", 17), width=28, height=1, bd=0, bg="white")
                    lb2.place(x=120, y=250)
                    lb3 = Label(base1, text=s_data[2], font=("Arial", 17), width=28, height=1, bd=0, bg="white")
                    lb3.place(x=120, y=330)
                    lb4 = Label(base1, text=s_data[3], font=("Arial", 17), width=28, height=1, bd=0, bg="white")
                    lb4.place(x=120, y=410)
                    lb5 = Label(base1, text=s_data[4], font=("Arial", 17), width=28, height=1, bd=0, bg="white")
                    lb5.place(x=120, y=490)
                    s_pass = list(s_data[5])
                    len_pass = len(s_pass)
                    fi = []
                    for i in range(len_pass):
                        if i >= 3:
                            fi.append("*")
                        else:
                            fi.append(s_pass[i])

                    lb6 = Label(base1, text=fi, font=("Arial", 17), width=28, height=1, bd=0, bg="white")
                    lb6.place(x=120, y=560)

                    change_pass = Button(base1, text="Change\nPassword", width=12, font=("Arial Rounded MT Bold", 12), height=2,
                                         bg="#c00000", fg="white", bd=0,command=forget_password)
                    change_pass.place(x=245, y=615)

                    exit_btn = Button(base1, text="Exit", width=8, font=("Arial Rounded MT Bold", 18), height=1, bg="#c00000",
                                      fg="white", bd=0,command=student_interface)
                    exit_btn.place(x=1140, y=40)

            photo = PhotoImage(file=r"power.png")
            print("Rahul3")
            img = Button(base1, bg="white", bd=0,width=55,height=55, command=student_login)
            img.configure(image=photo)
            print("Rahul2")
            img.place(x=1249, y=596)
            print("Rahul")
            base1.mainloop()



            #base1.mainloop()
    #====================================================================
        def results():

            # Results image
            quiz1 = Image.open("results.jpg")
            quiz2 = quiz1.resize((1350, 690))
            quiz2.save("results.jpg")
            quiz3 = Image.open("results.jpg")
            quiz4 = ImageTk.PhotoImage(quiz3)
            quiz5 = Label(image=quiz4)
            quiz5.image = quiz4
            quiz5.place(x=0, y=0)

            close = Button(base1, text="Exit", font=("Arial Rounded MT Bold", 17), width=8, height=1, bd=0, fg="White",bg="#070707", command=student_interface)
            close.place(x=50, y=20)

            # Results Body
            con=sqlite3.connect("Quizstar.db")
            cur=con.cursor()
            cur.execute("select* from stu_res")
            print("Yes2")
            all_quiz_data = cur.fetchall()
            con.commit()
            con.close()

            ls=[]
            ls_main=[]
            for oneline in all_quiz_data: #  2 3
                data2 = list(oneline)
                if data2[-1]==stu:
                    print("Yes4")
                    #num=num+1
                    ls=[]
                    teach=data2[-2]
                    ls.append(data2[1])
                    ls.append(int(data2[2]))
                    ls.append(data2[3])
                    ls_main.append(ls)
                    print("ls_main : ",ls_main)

            #total_quiz = num
            u = 50
            v = 400
            w = 570
            t = 250
            for oneline in ls_main:
                print("Yes5")
                ls1=list(oneline)
                quiz_name = Label(base1, text=ls1[0], font=("Arial Rounded MT Bold", 17),
                                  width=23, height=1, bd=1, fg="black", bg="#ffe699")
                quiz_name.place(x=u, y=t)

                # connecting to the database to calculate total number of questions
                con = sqlite3.connect("Quizstar.db")
                cur = con.cursor()
                cur.execute("select* from " + teach)
                questions = cur.fetchall()
                con.commit()
                con.close()
                qu = 0
                for one in questions:
                    ques = list(one)
                    if ques[0] == ls1[0]:
                        qu = qu + 1

                #temp=(ls1[1]/qu)*20
                marks = Label(base1, text=str(ls[1])+"/"+str(qu), font=("Arial Rounded MT Bold", 17), width=10, height=1,
                              bd=1, fg="black", bg="#ffe699")
                marks.place(x=v, y=t)

                date_time = Label(base1, text=ls1[2], font=("Arial Rounded MT Bold", 17), width=17,
                                  height=1, bd=1, fg="black", bg="#ffe699")
                date_time.place(x=w, y=t)

                t = t + 40

        #=====================================================================
        #======================================================================
        global stu
        dat1=en1.get()
        stu=dat1
        dat2=en2.get()
        print(dat1)
        print(dat2)
        con = sqlite3.connect("Quizstar.db")
        cur =con.cursor()
        query="select* from new_student"
        cur.execute(query)
        dat3 = cur.fetchall()
        print("dat3",dat3)

        #checking that entered password and username is right or wrong

        for oneline in dat3:
            ls=oneline
            if ls[1]==dat1:
                if ls[5]==dat2:

                    # student_Interface image
                    int1 = Image.open("student_interface.jpg")
                    int2 = int1.resize((1350, 690))
                    int2.save("student_interface.jpg")
                    int3 = Image.open("student_interface.jpg")
                    int4 = ImageTk.PhotoImage(int3)
                    int5 = Label(image=int4)
                    int5.image = int4
                    int5.place(x=0, y=0)

                    # student_interface Page body
                    exit_std_interface = Button(base1, text="Exit", width=8, font=("Arial Rounded MT Bold", 18),
                                                height=1, bg="white", fg="black", bd=0,command=student_login)
                    exit_std_interface.place(x=1110, y=580)

                    s_btn1 = Button(base1, text="Answer \nQuiz", font=("Arial Rounded MT Bold", 20), width=6, height=2, bd=0,bg="white", command=start_quiz)
                    s_btn1.place(x=260, y=350)
                    s_btn2 = Button(base1, text="Results", font=("Arial Rounded MT Bold", 20), width=10, height=1, bd=0,bg="white", command=results)
                    s_btn2.place(x=590, y=400)
                    s_btn3 = Button(base1, text=" My Profile ", font=("Arial Rounded MT Bold", 20), width=10, height=1, bd=0,bg="white", command=student_profile)
                    s_btn3.place(x=990, y=400)
                else:
                    en1.delete(0,END)
                    en2.delete(0,END)
                    en1.focus()
                    lb2 = Label(base1, text="Invalid Username or Password !", font=("Arial Rounded MT Bold", 17), width=30,height=1, bd=0, fg="#c00000", bg="white")
                    lb2.place(x=470, y=570)

    def forget_password():

        # forget password image
        quiz1 = Image.open("forget_password.jpg")
        quiz2 = quiz1.resize((1350, 690))
        quiz2.save("forget_password.jpg")
        quiz3 = Image.open("forget_password.jpg")
        quiz4 = ImageTk.PhotoImage(quiz3)
        quiz5 = Label(image=quiz4)
        quiz5.image = quiz4
        quiz5.place(x=0, y=0)

        # Forget password body
        # mobile no
        en1 = Entry(base1, width=30, font=("Arial", 15), bd=0)
        en1.place(x=520, y=415)

        #============================================================================
        def otp():

            phone_no=en1.get()
            # connecting database
            con=sqlite3.connect("Quizstar.db")
            cur=con.cursor()
            cur.execute("select* from new_student")
            new_data=cur.fetchall()
            con.commit()
            con.close()

            for one in new_data:
                ls_data=list(one)
                print("DB No : ",ls_data[2])
                print("phone : ",phone_no)
                if int(ls_data[2])==int(phone_no):

                    # =================================================================================================
                    otp = str(random.randint(11111, 99999))
                    url = "https://www.fast2sms.com/dev/bulk"
                    txt_msg2 = ("*********QUIZSTAR*********")
                    txt_msg0=("\nHi "+ls_data[0])
                    txt_msg3 = (" Your OTP to reset /access QuizStar Account is  : ")
                    txt_msg4 = ("\nIt will be valid for 3 minutes.")
                    txt_msg5 = ("\n\n- QUIZSTAR")
                    txt_msg6 = ("\n***********")
                    try:
                        querystring = {
                            "authorization": "GLHtK9z17QesfiEhAKeBfPFK5czH4mj2bRksYxKqoVIvQRYcK8Q53UQS6IQv",
                            "sender_id": "FSTSMS", "message": txt_msg2 +txt_msg0+ txt_msg3 + otp + txt_msg4 + txt_msg5 + txt_msg6,
                            "language": "english", "route": "p", "numbers": phone_no
                        }
                        headers = {
                            'cache-control': "no-cache"
                        }
                        response = requests.request("GET", url, headers=headers, params=querystring)
                        print(response.text)
                    except:
                        lb1 = Label(base1, text="Technical Error Try Again Later",
                                    font=("Arial Rounded MT Bold", 17),
                                    width=30, height=1, bd=0, fg="#c00000", bg="white")
                        lb1.place(x=470, y=570)
                    print("----------------------------------------------------")
                    #=================================================================================================
                    time.sleep(2)
                    # OTP image
                    quiz1 = Image.open("otp.jpg")
                    quiz2 = quiz1.resize((1350, 690))
                    quiz2.save("otp.jpg")
                    quiz3 = Image.open("otp.jpg")
                    quiz4 = ImageTk.PhotoImage(quiz3)
                    quiz5 = Label(image=quiz4)
                    quiz5.image = quiz4
                    quiz5.place(x=0, y=0)

                    # OTP body
                    # otp
                    en_otp = Entry(base1, width=30, font=("Arial", 15), bd=0)
                    en_otp.place(x=520, y=340)
                    #==============================================================================================
                    def reset_password():
                        new_otp=en_otp.get()

                        if int(otp)==int(new_otp):
                            # reset password image
                            quiz1 = Image.open("reset_password.jpg")
                            quiz2 = quiz1.resize((1350, 690))
                            quiz2.save("reset_password.jpg")
                            quiz3 = Image.open("reset_password.jpg")
                            quiz4 = ImageTk.PhotoImage(quiz3)
                            quiz5 = Label(image=quiz4)
                            quiz5.image = quiz4
                            quiz5.place(x=0, y=0)

                            def new_pass():
                                new=en11.get()
                                confirm = en21.get()

                                if new==confirm:
                                    con = sqlite3.connect("Quizstar.db")
                                    cur = con.cursor()

                                    cur.execute("""Update new_student set pass = ? where phone_no = ? """,
                                                (confirm,phone_no))
                                    #new_data = cur.fetchall()
                                    print("password changed succesfully")
                                    lb1.config(text="Password Reset Succesfully !",fg="green")
                                    con.commit()
                                    con.close()

                                else:
                                    lb1.config(text="Password Did Not Matched  !")

                            # reset_password body
                            #new pass
                            en11 = Entry(base1, width=30, font=("Arial", 15), bd=0)
                            en11.place(x=520, y=325)
                            lb1 = Label(base1, text="",
                                        font=("Arial Rounded MT Bold", 17),
                                        width=30, height=1, bd=0, fg="#c00000", bg="white")
                            lb1.place(x=470, y=570)
                            en21 = Entry(base1, width=30, font=("Arial", 15), bd=0)
                            en21.place(x=520, y=410)
                            btn1 = Button(base1, text="Reset Password", font=("Arial Rounded MT Bold", 20), width=20, height=1,
                                          bd=0, fg="white", bg="#c00000", command=new_pass)
                            btn1.place(x=510, y=480)
                            btn2 = Button(base1, text="Back to Login", font=("Arial Rounded MT Bold", 16), width=36, height=1,
                                          bd=0, fg="black", bg="#d0cecf", command=student_login)
                            btn2.place(x=440, y=630)

                        else:
                            lb1 = Label(base1, text="OTP did not matched !", font=("Arial Rounded MT Bold", 17),width=30,height=1, bd=0, fg="#c00000", bg="white")
                            lb1.place(x=470, y=570)
                    # ==============================================================================================

                    btn1 = Button(base1, text=" Submit OTP ", font=("Arial Rounded MT Bold", 20), width=20, height=1, bd=0,
                                  fg="white", bg="#c00000", command=reset_password)
                    btn1.place(x=510, y=480)
                    btn2 = Button(base1, text="Back to Login", font=("Arial Rounded MT Bold", 16), width=36, height=1, bd=0,
                                  fg="black", bg="#d0cecf", command=student_login)
                    btn2.place(x=440, y=630)

                    break
        #============================================================================
        btn1 = Button(base1, text="Send OTP", font=("Arial Rounded MT Bold", 20), width=20, height=1, bd=0,
                      fg="white", bg="#c00000", command=otp)
        btn1.place(x=510, y=480)
        btn2 = Button(base1, text="Back to Login", font=("Arial Rounded MT Bold", 16), width=36, height=1, bd=0,
                      fg="black", bg="#d0cecf", command=student_login)
        btn2.place(x=440, y=630)
        #=======================================================================================
    # Student_login image
    s1= Image.open("student_login.jpg")
    s2 = s1.resize((1350, 690))
    s2.save("Student_login.jpg")
    s3 = Image.open("student_login.jpg")
    s4 = ImageTk.PhotoImage(s3)
    s5 = Label(image=s4)
    s5.image = s4
    s5.place(x=0, y=0)

    # login_page body
    en1 = Entry(base1, width=30, font=("Arial", 15), bd=0)
    en1.place(x=520, y=220)
    en2 = Entry(base1, width=30, font=("Arial", 15), bd=0,show = "*")
    en2.place(x=520, y=300)
    btn1 = Button(base1, text="Login", font=("Arial Rounded MT Bold", 20), width=20, height=1, bd=0, fg="white",bg="#c00000",command=student_interface)
    btn1.place(x=510, y=465)
    btn2 = Button(base1, text="New user ? Sign Up! ", font=("Calibri (Body)", 15), width=30, height=1, bd=0, bg="white",command=new_student)
    btn2.place(x=500, y=350)
    btn3 = Button(base1, text="Forget password ? ", font=("Calibri (Body)", 14), width=30, height=1, bd=0, bg="white",command=forget_password)
    btn3.place(x=500, y=390)
    btn4 = Button(base1, text="<  Back to Homepage  >", font=("Arial Rounded MT Bold", 16), width=36, height=1, bd=0, fg="black",bg="#d0cecf", command=first)
    btn4.place(x=440, y=630)

def first():

    # home page image
    home_page = Image.open("home_page.jpg")
    new_home_page=home_page.resize((1350,690))

    new_home_page.save("home_page.jpg")
    my=Image.open("home_page.jpg")
    my_hp = ImageTk.PhotoImage(my)
    my_hp2=Label(image=my_hp)
    my_hp2.image=my_hp
    my_hp2.place(x=0,y=0)

    #home page body******************
    btn1=Button(base1,text="Teacher",font=("Arial Rounded MT Bold", 20), width=10, height=1, bd=0,bg="white",command=teacher_login)
    btn1.place(x=770,y=160)
    btn2=Button(base1,text="Student",font=("Arial Rounded MT Bold", 20), width=10, height=1, bd=0,bg="white",command=student_login)
    btn2.place(x=1080,y=320)
    base1.mainloop()

first()