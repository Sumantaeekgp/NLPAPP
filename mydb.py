
import json
from tkinter import messagebox

class Database:

    def add_data(self,name,email,password):

        with open ('db.json','r') as rf:
            database= json.load(rf)

        if email in database:
            return 0
        else:
            database[email]=[name,password]
            with open ('db.json','w') as wf:
                json.dump(database,wf)
            return 1

    def search(self,email,password):
        with open ('db.json','r') as rf:
            data=json.load(rf)
            if email in data:
                if data[email][1]==password:
                    messagebox.showinfo('Success','login successful')
                    return 1
                else:
                    messagebox.showerror('Error', 'Incorrect password')
                    return 0
            else:
                messagebox.showerror('Error', 'Email does not exist.Register first')
                return 0



