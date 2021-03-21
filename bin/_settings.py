from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import colorchooser
from bin import *

class main:
    def __init__(self, master, textBox, isAdminMode, idaMain):
        self.master = master
        self.textBox = textBox
        self.isAdminMode = False
        self.checkbuttonvar = IntVar()
        self.adminPassword = None
        master.title("Settings - Ida")
        master.iconbitmap(r"bin/logo.ico")
        master.minsize(270, 250)
        master.maxsize(270, 250)

        self.mainNotebook = ttk.Notebook(master)
        self.mainNotebook.pack(fill=BOTH, expand=True)

        self.generalPage = ttk.Frame(self.mainNotebook)
        self.fontPage = ttk.Frame(self.mainNotebook)
        self.adminPage = ttk.Frame(self.mainNotebook)
        self.packageManagerPage = ttk.Frame(self.mainNotebook)
        self.helpPage = ttk.Frame(self.mainNotebook)

        self.mainNotebook.add(self.generalPage, text="General")
        self.mainNotebook.add(self.fontPage, text="Font")
        self.mainNotebook.add(self.adminPage, text="Admin")
        self.mainNotebook.add(self.packageManagerPage, text="Package Manager")
        self.mainNotebook.add(self.helpPage, text="Help")
        
        #========================================= General Settings =======================================================

        #Language
        #self.languageLabel = ttk.Labelfame(self.generalPage, text="Language")
        #self.

        #========================================= Font Settings =======================================================

        # Font Selection
        self.fontLabel = ttk.Labelframe(self.fontPage, text="Font")
        self.fontListLabel = Label(self.fontLabel, text="Font:")
        self.fontMenu = OptionMenu(self.fontLabel, "Arial", *["Arial", "Courier New", "Comic Sans MS", "Fixedsys", "MS Sans Serif", "MS Serif", "Symbol", "System", "Times New ", "+Roman", "Verdana"])
        self.fontLabel.pack(padx=5, pady=5)
        self.fontListLabel.grid(column=0, row=1)
        self.fontMenu.grid(column=1, row=1)

        # Font Colour
        self.fontColourLabel = ttk.Labelframe(self.fontPage, text="Font Colour")
        self.textColourLabel = Label(self.fontColourLabel, text="Text Colour:")
        self.textColourButton = Button(self.fontColourLabel, text="Pick Colour", command=self._textColour)
        self.backgroundColourLabel = Label(self.fontColourLabel, text="Background Colour:")
        self.backgroundColourButton = Button(self.fontColourLabel, text="Pick Colour", command=self._backgroundColour)
        self.fontColourSeparator = ttk.Separator(self.fontColourLabel)
        self.resetColourLabel = Label(self.fontColourLabel, text="Reset Colours:")
        self.resetColourButton = Button(self.fontColourLabel, text="Reset Colour", command=self._resetColours)
        self.fontColourLabel.pack(padx=5, pady=5)
        self.textColourLabel.grid(column=0, row=3)
        self.textColourButton.grid(column=1, row=3)
        self.backgroundColourLabel.grid(column=0, row=4)
        self.backgroundColourButton.grid(column=1, row=4)
        self.fontColourSeparator.grid(row=5, sticky="ew")
        self.resetColourLabel.grid(column=0, row=6)
        self.resetColourButton.grid(column=1, row=6)

        self.mainNotebook.add(self.generalPage)
        self.mainNotebook.add(self.fontPage)

        #======================================== Admin Mode ===========================================================

        # Main
        self.adminMode = ttk.Labelframe(self.adminPage, text="General")
        self.adminModeToggle = Checkbutton(self.adminMode, text = "Admin Mode", variable=self.checkbuttonvar, command=self.on_checkbutton_click)
        self.adminModeToggle.select()
    
        self.adminMode.pack(padx=5, pady=5)
        self.adminModeToggle.grid(column=0, row=0)

        # Password
        self.passwordLabel = ttk.Labelframe(self.adminPage, text="Password Settings")
        self.setPasswordLabel = Label(self.passwordLabel, text="Set new password")
        self.passwordButton = Button(self.passwordLabel, text="Set Password")

        self.passwordLabel.pack(padx=5, pady=5)
        self.setPasswordLabel.grid(column=0, row=0)
        self.passwordButton.grid()

    def on_checkbutton_click(self):
        if self.checkbuttonvar.get() == 1:
            print("Checkbutton selected")
        else:
            print("Checkbutton not selected")

    def _textColour(self):
        self.textColour = colorchooser.askcolor(title="Choose a colour for the text")[1]
        self.textBox.config(fg=self.textColour)

    def _backgroundColour(self):
        self.backgroundColour = colorchooser.askcolor(title="Choose a colour for the background")[1]
        self.textBox.config(bg=self.backgroundColour)

    def _resetColours(self):
        if messagebox.askyesno("Reset preferences | Settings - Ida", "Are you sure you want to reset the colours?"):
            self.textBox.config(bg="white", fg="black")

    def exit(self):
        self.open = False
        self.master.destroy()
