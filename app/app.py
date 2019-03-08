#!/usr/bin/env python3

"""Password generator GUI"""

from tkinter import *
from password_generator import generate_password


class Application(Frame):
    def pop_up_msg(self):
        popup = Tk()
        popup.wm_title("No Option Selected")
        label = Label(popup, text="Please select at least one password option.", padx=10, pady=10)
        label.pack(side="top", fill="x", pady=10)
        btn = Button(popup, text="Okay", command=popup.destroy)
        btn.pack(padx=10, pady=10)

    def generate_pass(self):
        symbols_selected = bool(self.symbols_val.get())
        letters_selected = bool(self.letters_val.get())
        numbers_selected = bool(self.numbers_val.get())
        if symbols_selected or letters_selected or numbers_selected:
            self.generated_pwd_val.set(
                generate_password(
                    symbols=symbols_selected,
                    letters=letters_selected,
                    numbers=numbers_selected,
                    password_length=self.pwd_length_val.get()
                )
            )
        else:
            self.pop_up_msg()

    def exit_widget(self):
        exit_btn = Button(self, text="Close Program", fg="red", command=self.quit)
        exit_btn.pack({"side": "left"}, padx=20, pady=10)

    def generate_pass_widget(self):
        generate_pass_btn = Button(self, text='Generate Password', fg="green", command=self.generate_pass)
        generate_pass_btn.pack({"side": "right"}, padx=20, pady=20)

    def pwd_options(self):
        group = LabelFrame(text="Password Options:", padx=5, pady=5)
        group.pack({"side": "top"}, padx=25, pady=25)
        Checkbutton(group, text='Letters', var=self.letters_val).pack(padx=20, pady=10, anchor=W)
        Checkbutton(group, text='Symbols', var=self.symbols_val).pack(padx=20, pady=10, anchor=W)
        Checkbutton(group, text='Numbers', var=self.numbers_val).pack(padx=20, pady=10, anchor=W)

    def pwd_length_scale(self):
        Scale(
            from_=8, to=50, orient=HORIZONTAL, var=self.pwd_length_val, label="Password length:", length=220
        ).pack({"side": "top"}, pady=30)

    def generated_pwd_field(self):
        Entry(textvariable=self.generated_pwd_val, width=30).pack({'side': 'top'}, expand=True, pady=20)

    def create_widgets(self):
        self.generated_pwd_field()
        self.pwd_options()
        self.pwd_length_scale()
        self.generate_pass_widget()
        self.exit_widget()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.symbols_val = IntVar()
        self.letters_val = IntVar()
        self.numbers_val = IntVar()
        self.pwd_length_val = IntVar()
        self.generated_pwd_val = StringVar()
        self.pack()
        self.create_widgets()


root = Tk()
app = Application(master=root)
app.master.title("THE NUTCRACKER: a password generator")
app.master.minsize(1000, 600)
app.mainloop()
root.destroy()
