from tkinter import *
#from tkinter import ttk
from tkinter import colorchooser
from tkinter.font import Font
#from bin import tkinterp

class fontMenu:
    def __init__(self, master, textBox):
        self.textBox = textBox
        self.open = True
        self.master = master

        master.title("Font - Ida")
        master.iconbitmap(r"bin/logo.ico")
        #master.lift()
        #master.attributes("-topmost", True)
        master.minsize(210, 150)
        master.maxsize(210, 150)

        self.headerLabel = Label(master, text="Font")
        self.fontLabel = Label(master, text="Font:")
        self.fontMenu = OptionMenu(master, "Arial", *["Arial", "Courier New", "Comic Sans MS", "Fixedsys", "MS Sans Serif", "MS Serif", "Symbol", "System", "Times New Roman", "Verdana"])
        self.textColourLabel = Label(master, text="Text Colour:")
        self.textColourButton = Button(master, text="Pick Colour", command=self._textColour)
        self.fgColourIndicator = Label(master, text="⬛⬛", fg="black")
        self.backgroundColourLabel = Label(master, text="Background Colour")
        self.backgroundColourButton = Button(master, text="Pick Colour", command=self._backgroundColour)
        self.bgColourIndicator = Label(master, text="⬛⬛", bg="white")
        self.saveButton = Button(master, text="Save", command=self.save)
        self.cancelButton = Button(master, text="Cancel", command=self.cancel)

        self.headerLabel.grid(column=1, row=0)
        self.fontLabel.grid(column=0, row=1)
        self.fontMenu.grid(column=1, row=1)
        self.textColourLabel.grid(column=0, row=2)
        self.textColourButton.grid(column=1, row=2)
        self.fgColourIndicator.grid(column=2, row=2)
        self.backgroundColourLabel.grid(column=0, row=3)
        self.backgroundColourButton.grid(column=1, row=3)
        self.bgColourIndicator.grid(column=2, row=3)
        self.saveButton.grid(column=0, row=4)
        self.cancelButton.grid(column=1, row=4)

    def _textColour(self):
        self.textColour = colorchooser.askcolor(title="Choose a colour for the text")[1]
        self.textBox.config(fg=self.textColour)
        self.fgColourIndicator.config(fg=self.textColour)

    def _backgroundColour(self):
        self.backgroundColour = colorchooser.askcolor(title="Choose a colour for the background")[1]
        self.textBox.config(bg=self.backgroundColour)
        self.bgColourIndicator.config(bg=self.backgroundColour)

    def cancel(self):
        self.textBox.config(bg="white")
        self.textBox.config(fg="black")
        self.exit()
    
    def save(self):
        pass

    def exit(self):
        self.open = False
        self.master.destroy()
