from tkinter import *
from password_generator import generate_password


class Application(Frame):
    def say_hi(self):
        print("hi there, everyone!")

    def create_widgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "Close Program"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.generate_pass = Checkbutton(self)
        self.generate_pass["text"] = "Generate Password",
        self.generate_pass["command"] = generate_password('all_characters', password_length=25)

        self.generate_pass.pack({"side": "left"}, padx=20)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()


root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
