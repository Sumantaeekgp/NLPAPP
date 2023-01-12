from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API

class NLPApp:

    def __init__(self):

        self.dbo=Database()##creating database object
        self.apio=API()  #creating API object
        # loading of login GUI
        self.root = Tk()             ## creating GUI
        self.root.title('NLPAPP')   ##title of GUI
        self.root.iconbitmap("Resources/favicon.ico") ##icon after converting to favicon.It should be ico format
        self.root.geometry("350x600")  ##size of GUI
        self.root.configure(bg="#AED6F1") ##color of GUI
        self.login_gui()

        self.root.mainloop()        ##to keep GUI on screen


    def login_gui(self):

        self.clear()

        heading = Label(self.root,text='NLPApp',bg="#AED6F1", fg="blue")
        heading.pack(pady=(20,20)) ##place heading in GUI.pady 30,30 means upper and lower portion gap is 30
        heading.configure(font=("verdana",20,"bold"))

        label_email=Label(self.root,text='Enter Email')
        label_email.pack(pady=(10,10))

        self.email_input = Entry(self.root,width = 30)
        self.email_input.pack(pady=(10,10), ipady=4)

        label_pswrd = Label(self.root, text='Enter Password')
        label_pswrd.pack(pady=(10, 10))

        self.pswrd_input = Entry(self.root, width=30,show='*')
        self.pswrd_input.pack(pady=(10, 10), ipady=4)

        login_btn=Button(self.root,text="Login",width=8,height=2,command=self.perform_login) ##we can give height in button
        login_btn.pack(pady=(10,10))

        label_3 = Label(self.root, text='Not a member? Register')
        label_3.pack(pady=(20, 10))

        redirect_to_reg_btn = Button(self.root, text="Register Now", width=15, height=2,command=self.register_gui) ##this command will detect the press the button  ##we can give height
        redirect_to_reg_btn.pack(pady=(10, 10))



    def register_gui(self):
        self.clear()  ##at first clear existing GUI

        heading = Label(self.root, text='NLPApp', bg="#AED6F1", fg="blue")
        heading.pack(pady=(20, 20))  ##place heading in GUI.pady 30,30 means upper and lower portion gap is 30
        heading.configure(font=("verdana", 20, "bold"))

        label_name = Label(self.root, text='Enter your name')
        label_name.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=30)
        self.name_input.pack(pady=(10, 10), ipady=4)

        label_email = Label(self.root, text='Enter Email')
        label_email.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=30)
        self.email_input.pack(pady=(10, 10), ipady=4)

        label_pswrd = Label(self.root, text='Enter Password')
        label_pswrd.pack(pady=(10, 10))

        self.pswrd_input = Entry(self.root, width=30, show='*')
        self.pswrd_input.pack(pady=(10, 10), ipady=4)

        login_btn = Button(self.root, text="Register", width=8, height=2, command=self.perform_registration)  ##we can give height in button
        login_btn.pack(pady=(10, 10))

        label_3 = Label(self.root, text='Already a member? Login')
        label_3.pack(pady=(20, 10))

        redirect_to_login_btn = Button(self.root, text="Login Now", width=15, height=2,
        command=self.login_gui)  ##this command will detect the press the button  ##we can give height
        redirect_to_login_btn.pack(pady=(10, 10))

    def clear(self):  ##function that clear the existing GUI
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        name=self.name_input.get() ##get will fetch the input from above name_input button
        email=self.email_input.get()
        pswrd=self.pswrd_input.get()

        response=self.dbo.add_data(name,email,pswrd)
        if response:
            messagebox.showinfo('Success','Registration successful.You can login now')
        else:
            messagebox.showerror('Error','email already exists')

    def perform_login(self):
        email = self.email_input.get()
        pswrd = self.pswrd_input.get()
        response=self.dbo.search(email,pswrd)
        if response:
            self.home_gui()

    def home_gui(self):
        self.clear()
        sentiment_btn = Button(self.root, text="Sentiment Analysis", width=20, height=4,command=self.sentiment_gui)
        sentiment_btn.pack(pady=(30, 10))

        abuse_btn = Button(self.root, text="Abuse Detection", width=20, height=4,command=self.abuse_gui)
        abuse_btn.pack(pady=(30, 10))

        emotion_btn = Button(self.root, text="Emotion detection", width=20, height=4,command=self.emotion_gui)
        emotion_btn.pack(pady=(30, 10))

        redirect_to_login_btn = Button(self.root, text="log out", width=15, height=2,
        command=self.login_gui)
        redirect_to_login_btn.pack(pady=(20, 10))

    def sentiment_gui(self):
        self.clear()

        heading1 = Label(self.root, text='NLPApp', bg="#AED6F1", fg="blue")
        heading1.pack(pady=(20, 20))  ##place heading in GUI.pady 30,30 means upper and lower portion gap is 30
        heading1.configure(font=("verdana", 20, "bold"))

        heading2 = Label(self.root, text='Sentiment Analysis', bg="#AED6F1", fg="blue")
        heading2.pack(pady=(20, 20))  ##place heading in GUI.pady 30,30 means upper and lower portion gap is 30
        heading2.configure(font=("verdana", 20))

        self.label1= Label(self.root, text='Enter text here')
        self.label1.pack(pady=(10, 10))

        self.text_input = Entry(self.root, width=30)
        self.text_input.pack(pady=(10, 10), ipady=10)

        sentiment_ana_btn = Button(self.root, text="Analize Sentiment ", width=20, height=2,command=self.do_sentiment_analysis)
        sentiment_ana_btn.pack(pady=(30, 10))

        self.sentiment_result= Label(self.root, bg="#AED6F1" ,text='')
        self.sentiment_result.pack(pady=(10, 10))

        back_btn = Button(self.root, text="Go Back", width=15, height=2, command=self.home_gui)
        back_btn.pack(pady=(30, 10))

    def do_sentiment_analysis(self):
        text=self.text_input.get()
        #print(text)
        result=self.apio.sentiment_analysis(text)
        #print(result)
        text = ''
        for i in result["sentiment"]:
            text=text+i+'>>'+str(result["sentiment"][i]) + '\n'
        self.sentiment_result["text"]=text  ## to print the result in that label

    def abuse_gui(self):
        self.clear()

        heading1 = Label(self.root, text='NLPApp', bg="#AED6F1", fg="blue")
        heading1.pack(pady=(20, 20))  ##place heading in GUI.pady 30,30 means upper and lower portion gap is 30
        heading1.configure(font=("verdana", 20, "bold"))

        heading2 = Label(self.root, text='Abuse Detection', bg="#AED6F1", fg="blue")
        heading2.pack(pady=(20, 20))  ##place heading in GUI.pady 30,30 means upper and lower portion gap is 30
        heading2.configure(font=("verdana", 20))

        self.label1 = Label(self.root, text='Enter text here')
        self.label1.pack(pady=(10, 10))

        self.text_input = Entry(self.root, width=30)
        self.text_input.pack(pady=(10, 10), ipady=10)

        ner_btn = Button(self.root, text="Detect Abuse", width=20, height=2,
        command=self.do_abuse_detection)
        ner_btn.pack(pady=(30, 10))

        self.abuse_result = Label(self.root, bg="#AED6F1", text='')
        self.abuse_result.pack(pady=(10, 10))

        back_btn = Button(self.root, text="Go Back", width=15, height=2, command=self.home_gui)
        back_btn.pack(pady=(30, 10))

    def do_abuse_detection(self):
        text = self.text_input.get()
        result = self.apio.abuse_detection(text)
        print(result)
        string = ''
        for i in result:
            string=string+i+'>>'+str(result[i]) + '\n'
        self.abuse_result["text"]=string  ## to print the result in that label

    def emotion_gui(self):
        self.clear()

        heading1 = Label(self.root, text='NLPApp', bg="#AED6F1", fg="blue")
        heading1.pack(pady=(20, 20))  ##place heading in GUI.pady 30,30 means upper and lower portion gap is 30
        heading1.configure(font=("verdana", 20, "bold"))

        heading2 = Label(self.root, text='Emotion Detection', bg="#AED6F1", fg="blue")
        heading2.pack(pady=(20, 20))  ##place heading in GUI.pady 30,30 means upper and lower portion gap is 30
        heading2.configure(font=("verdana", 20))

        self.label1 = Label(self.root, text='Enter text here')
        self.label1.pack(pady=(10, 10))

        self.text_input = Entry(self.root, width=30)
        self.text_input.pack(pady=(10, 10), ipady=10)

        ner_btn = Button(self.root, text="Detect Emotion", width=20, height=2,
        command=self.do_emotion_detection)
        ner_btn.pack(pady=(30, 10))

        self.emotion_result = Label(self.root, bg="#AED6F1", text='')
        self.emotion_result.pack(pady=(10, 10))

        back_btn = Button(self.root, text="Go Back", width=15, height=2, command=self.home_gui)
        back_btn.pack(pady=(30, 10))

    def do_emotion_detection(self):
        text = self.text_input.get()
        result = self.apio.emotion_detection(text)
        print(result)
        string = ''
        for i in result['emotion']:
            string=string+i+'>>'+str(result['emotion'][i]) + '\n'
        self.emotion_result["text"]=string  ## to print the result in that label


nlp = NLPApp()

