from tkinter import *
from password_generator import generate_password


class Application(Frame):
    def say_hi(self):
        print("hi there, everyone!")

    def exit_widget(self):
        self.exit = Button(self)
        self.exit["text"] = "Close Program"
        self.exit["fg"] = "red"
        self.exit["command"] = self.quit

        self.exit.pack({"side": "right"})

    def password_option_widget(self, option):
        self.options = Checkbutton(self)
        self.options["text"] = option

        self.options.pack({"side": "top"}, padx=20, pady=20)

    def generate_pass_widget(self):
        self.generate_pass = Button(self)
        self.generate_pass["text"] = 'Generate Password',
        self.generate_pass["command"] = generate_password('all_characters', password_length=25)

        self.generate_pass.pack({"side": "right"}, padx=20)

    def create_widgets(self):
        self.exit_widget()
        self.generate_pass_widget()
        self.password_option_widget(option='Letters only')
        self.password_option_widget(option='Letters and numbers only')
        self.password_option_widget(option='All characters (includes symbols)')


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()


root = Tk(className='nutcracker')
app = Application(master=root)
app.mainloop()
root.destroy()
