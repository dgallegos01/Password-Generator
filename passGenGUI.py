from tkinter import *
import os
import passwordGenerator

class PassGenGUI:
    def mainGUI(self, title, xPos, yPos):

        self.newPassword = ""

        self.app = Tk()
        self.app.title(title)
        
        self.centerWindow(xPos, yPos)

        self.app.configure(background="#2A2A2A", highlightthickness=8, highlightcolor="#32CD32")
        self.app.iconbitmap(
            "passkeyper_Icon.ico"
            )

        layer1 = Canvas(self.app, bg="#2A2A2A", highlightthickness=5, highlightbackground="#32CD32")
        layer1.pack(pady=10)
        layer1.config(width=600, height=700)

        scrollValue0 = IntVar()
        scrollValue1 = IntVar()
        scrollValue2 = IntVar()
        scrollValue3 = IntVar()
        scrollValue4 = IntVar()

        def submitPassword():
            self.createPassword(
            scrollValue0.get(),
            scrollValue1.get(),
            scrollValue2.get(),
            scrollValue3.get(),
            scrollValue4.get(),
            )

        label1 = Label(
            layer1, 
            text="Password Generator", 
            font="Times 40 bold underline", 
            fg="#32CD32", 
            bg="#2A2A2A"
            )
        label1.pack(padx=15, pady=5)

        layer2 = Label(layer1, bg="#2A2A2A")
        layer2.pack()

        value_check0 = IntVar()
        value_check1 = IntVar()
        value_check2 = IntVar()
        value_check3 = IntVar()
        value_check4 = IntVar()

        def disableCheckBox():
            checkBox1.config(state=DISABLED if value_check0.get() else NORMAL)
            checkBox2.config(state=DISABLED if value_check0.get() else NORMAL)
            slider0.config(state=NORMAL if value_check0.get() else DISABLED)
            slider0.set(0 if value_check0.get() else 0)
            slider1.config(state=DISABLED if value_check0.get() else NORMAL)
            slider2.config(state=DISABLED if value_check0.get() else NORMAL)

        checkBox0 = Checkbutton(
            layer2,
            variable=value_check0,
            text="Make it memorable(uses words)", 
            font="Times 20 bold", 
            bg="#2A2A2A", 
            fg="#32CD32",  
            bd=5, 
            activebackground="#32CD32", 
            activeforeground="#2A2A2A",
            selectcolor="#2A2A2A",
            command=lambda:[disableCheckBox()]
            )
        checkBox0.grid(row=0, column=0)

        slider0 = Scale(
            layer2,
            font="Times 12 bold", 
            from_=0, to=10, 
            orient=HORIZONTAL, 
            bg="#2A2A2A", 
            fg="#32CD32", 
            activebackground="#32CD32",
            variable=scrollValue0,
            sliderlength = 50,
            length=250
            )
        slider0.grid(row=1, column=0)
        slider0.config(state=NORMAL if value_check0.get() else DISABLED)

        checkBox1 = Checkbutton(
            layer2,
            variable=value_check1,
            text="Include Lowercase Letters", 
            font="Times 20 bold", 
            bg="#2A2A2A", 
            fg="#32CD32",  
            bd=5, 
            activebackground="#32CD32", 
            activeforeground="#2A2A2A",
            selectcolor="#2A2A2A",
            command=lambda:[
                slider1.config(state=NORMAL if value_check1.get() else DISABLED),
                slider1.set(0 if value_check1.get() else 0)
            ]
            )
        checkBox1.grid(row=2, column=0)

        slider1 = Scale(
            layer2,
            font="Times 12 bold", 
            from_=0, to=50, 
            orient=HORIZONTAL, 
            bg="#2A2A2A", 
            fg="#32CD32", 
            activebackground="#32CD32",
            variable=scrollValue1,
            sliderlength = 50,
            length=250,
            )
        slider1.grid(row=3, column=0)
        slider1.config(state=NORMAL if value_check1.get() else DISABLED)

        checkBox2 = Checkbutton(
            layer2,
            variable=value_check2,
            text="Include Uppercase Letters", 
            font="Times 20 bold", 
            bg="#2A2A2A", 
            fg="#32CD32",  
            bd=5, 
            activebackground="#32CD32", 
            activeforeground="#2A2A2A",
            selectcolor="#2A2A2A",
            command=lambda:[
                slider2.config(state=NORMAL if value_check2.get() else DISABLED),
                slider2.set(0 if value_check2.get() else 0)
            ]
            )
        checkBox2.grid(row=4, column=0)

        slider2 = Scale(
            layer2,
            font="Times 12 bold", 
            from_=0, to=50, 
            orient=HORIZONTAL, 
            bg="#2A2A2A", 
            fg="#32CD32", 
            activebackground="#32CD32",
            variable=scrollValue2,
            sliderlength = 50,
            length=250
            )
        slider2.grid(row=5, column=0)
        slider2.config(state=NORMAL if value_check2.get() else DISABLED)

        checkBox3 = Checkbutton(
            layer2,
            variable=value_check3,
            text="Include Numbers", 
            font="Times 20 bold", 
            bg="#2A2A2A", 
            fg="#32CD32",  
            bd=5, 
            activebackground="#32CD32", 
            activeforeground="#2A2A2A",
            selectcolor="#2A2A2A",
            command=lambda:[
                slider3.config(state=NORMAL if value_check3.get() else DISABLED),
                slider3.set(0 if value_check3.get() else 0)
            ]
            )
        checkBox3.grid(row=6, column=0)

        slider3 = Scale(
            layer2,
            font="Times 12 bold", 
            from_=0, to=50, 
            orient=HORIZONTAL, 
            bg="#2A2A2A", 
            fg="#32CD32", 
            activebackground="#32CD32",
            variable=scrollValue3,
            sliderlength = 50,
            length=250
            )
        slider3.grid(row=7, column=0)
        slider3.config(state=NORMAL if value_check3.get() else DISABLED)

        checkBox4 = Checkbutton(
            layer2,
            variable=value_check4,
            text="Include Symbols", 
            font="Times 20 bold", 
            bg="#2A2A2A", 
            fg="#32CD32",  
            bd=5, 
            activebackground="#32CD32", 
            activeforeground="#2A2A2A",
            selectcolor="#2A2A2A",
            command=lambda:[
                slider4.config(state=NORMAL if value_check4.get() else DISABLED),
                slider4.set(0 if value_check4.get() else 0)
            ]
            )
        checkBox4.grid(row=8, column=0)

        slider4 = Scale(
            layer2,
            font="Times 12 bold", 
            from_=0, to=50, 
            orient=HORIZONTAL, 
            bg="#2A2A2A", 
            fg="#32CD32", 
            activebackground="#32CD32",
            variable=scrollValue4,
            sliderlength = 50,
            length=250
            )
        slider4.grid(row=9, column=0)
        slider4.config(state=NORMAL if value_check4.get() else DISABLED)

        btn1 = Button(
            layer1, 
            text = "Generate Password", 
            width = 0, 
            height = 0, 
            font = "Times 18 bold", 
            bg = "#32CD32", 
            fg = "black", 
            activeforeground = "black", 
            activebackground = "#32CD32",
            bd = 5, 
            command=lambda:[submitPassword(), self.popup_window()]
            )
        btn1.pack(pady=10)

        copyrightLabel = Label(
            self.app,
            text="Copyright © 2021 Darrius Gallegos",
            font="Times 8",
            fg="#32CD32", 
            bg="#2A2A2A"
        )
        copyrightLabel.pack(pady=10)           

        self.app.mainloop()

    def centerWindow(self, w=300, h=300):
        # get screen width and height
        ws = self.app.winfo_screenwidth()
        hs = self.app.winfo_screenheight()
        # calculate position x, y
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        self.app.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def createPassword(self, amount1=0, amount2=0, amount3=0, amount4=0, amount5=0):
        passGen = passwordGenerator.passwordGenerator()
        passGen.numOfWords(amount1, "yes")
        passGen.numOfLettersLower(amount2)
        passGen.numOfLettersUpper(amount3)
        passGen.numOfNumbers(amount4)
        passGen.numOfSymbols(amount5)
        if amount1 > 0:
            self.newPassword = passGen.generatedMemorablePassword()
        else:
            self.newPassword = passGen.generatedPassword()

    def rerunProgram(self):
        os.startfile("Main.py")
        quit()

    def popup_window(self):
        self.app.destroy()

        def center_window2(w=450, h=250):
            # get screen width and height
            ws = win.winfo_screenwidth()
            hs = win.winfo_screenheight()
            # calculate position x, y
            x = (ws/2) - (w/2)    
            y = (hs/2) - (h/2)
            win.geometry('%dx%d+%d+%d' % (w, h, x, y))
            
        win = Tk()
        win.wm_title("New Password")
        win.configure(background="#2A2A2A",highlightthickness=8, highlightcolor="#32CD32")
        win.iconbitmap("passkeyper_Icon.ico")

        center_window2()

        def copy_button():
            clip = Tk()
            clip.withdraw()
            clip.clipboard_clear()
            clip.clipboard_append(self.newPassword)
            clip.destroy()

        label1 = Label(
            win,
            text="Your new password is:", 
            font="Times 20 bold", 
            fg="#32CD32", 
            bg="#2A2A2A"
        )
        label1.pack(pady=15)

        label2 = Label(
            win,
            text=self.newPassword, 
            font="Times 16", 
            fg="#32CD32", 
            bg="#4C4B4B",
            wraplength=426,
            justify=CENTER
        )
        label2.pack(pady=10)

        layer = Canvas(win)
        layer.pack()

        btn1 = Button(
            layer, 
            text="Copy to clipboard?", 
            font = "Times 15 bold", 
            bg = "#32CD32", 
            fg = "black", 
            activeforeground = "black", 
            activebackground = "#32CD32",
            bd = 5,
            command=copy_button
            )
        btn1.grid(row=0, column=0)

        btn2 = Button(
            layer, 
            text="Make Another?", 
            font = "Times 15 bold", 
            bg = "#32CD32", 
            fg = "black", 
            activeforeground = "black", 
            activebackground = "#32CD32",
            bd = 5,
            command=self.rerunProgram
            )
        btn2.grid(row=0, column=1)