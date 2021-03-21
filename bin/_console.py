from tkinter import *
from bin import *

class main:
    def __init__(self, master, idaMain):
        self.master = master
        self.idaMain = idaMain
        self.command = None

        master.title("Console - Ida")

        self.consoleInputFrame = Frame(master)
        self.consoleInput = Entry(self.consoleInputFrame, bg="black", fg="white")
        self.consoleExecuteButton = Button(self.consoleInputFrame, text="Execute", command=self.execute)
        self.consoleOutputFrame = Frame(master)
        self.consoleOutput = Text(self.consoleOutputFrame, bg="black", fg="white", state=DISABLED)

        self.consoleInput.bind("<<Return>>", self.execute)

        self.consoleInputFrame.pack(fill=BOTH, side=TOP)
        self.consoleInput.grid(column=0, row=0, pady=15, padx=15)
        self.consoleExecuteButton.grid(column=1, row=0, pady=15, padx=15)
        self.consoleOutputFrame.pack(fill=BOTH, side=BOTTOM)
        self.consoleOutput.grid(column=0, row=1, pady=15, padx=15)

    def consolePrint(self, string):
        self.consoleOutput.config(state='normal')
        self.consoleOutput.delete(1.0, END)
        self.consoleOutput.insert(END, string)
        self.consoleOutput.config(state=DISABLED)
        self.consoleInput.delete(1.0, END)

    def execute(self):
        self.command = self.consoleInput.get()

        if self.command == "test":
            self.consolePrint("Hello World!")

        else:
            self.consolePrint("The console is unable to interpret " + str(self.command))
