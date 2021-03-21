from tkinter import *
from tkinter import filedialog, messagebox, ttk
from tkinter.scrolledtext import ScrolledText
from bin import _font, _console, _packageManager, _settings


class CoreIda:
    def __init__(self, master):
        self.currentOpen = None
        self.isFileOpen = False
        self.statusBarProgress = 0
        self.fontRoot = None
        self.isPackageManager = False
        self.isAdminMode = False
        self.examMode = False

        self.master = master
        master.title("Untitled - Ida")
        master.iconbitmap(r"bin/logo.ico")
        master.minsize(200, 200) #NEW!

        self.text = ScrolledText(master)
        self.text.pack(fill=BOTH, expand=True)

        self.statusMenu = Frame(master)
        self.statusText = Label(self.statusMenu, text="Operation Complete")
        self.statusProgress = ttk.Progressbar(self.statusMenu, orient='horizontal', mode='determinate', variable=self.statusBarProgress)
        self.statusSizegrip = ttk.Sizegrip(self.statusMenu)

        self.statusProgress.pack(side=RIGHT)
        self.statusText.pack(side=LEFT)
        self.statusSizegrip.pack(side="right", anchor="s")
        self.statusMenu.pack(fill=X, side=BOTTOM)
        

        # MENU BAR ======================================================================

        self.menubar = Menu(master)

        """ ==== Menubar Cascades ======================================================================================
            ============================================================================================================ """

        self._windowmenu = Menu(self.menubar, tearoff=0)
        self._windowmenu.add_command(label="Console", command=self._consoleMenu)

        """ ====== File Bar ============================================================================================
            ============================================================================================================ """

        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New", accelerator="Ctrl+N", command=self.new)
        self.filemenu.add_command(label="Open", accelerator="Ctrl+O", command=self.open)
        self.filemenu.add_command(label="Save", command=self.saveas)
        self.filemenu.add_command(label="Save as...", accelerator="Ctrl+S", command=self.saveas)
        self.filemenu.add_command(label="Close", command=self.exit)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.exit)

        """ ===== Edit Menu ============================================================================================
            =========================================================================================================== """

        self.editmenu = Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Undo", accelerator="Ctrl+Z", command=lambda: master.focus_get().event_generate('<<Undo>>'))
        self.editmenu.add_command(label="Redo", accelerator="Ctrl+Y", command=lambda: master.focus_get().event_generate('<<Redo>>'))
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: master.focus_get().event_generate('<<Cut>>'))
        self.editmenu.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: master.focus_get().event_generate('<<Copy>>'))
        self.editmenu.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: master.focus_get().event_generate('<<Paste>>'))
        self.editmenu.add_command(label="Delete", accelerator="Delete", command=lambda: master.focus_get().event_generate('<<Delete>>'))
        self.editmenu.add_command(label="Select All", accelerator="Ctrl+A", command=lambda: master.focus_get().event_generate('<<SelectAll>>'))

        """ ===== View Menu ============================================================================================
            ============================================================================================================ """

        self.formatmenu = Menu(self.menubar, tearoff=0)
        self.formatmenu.add_command(label="Font...", command=self._fontMenu)

        """ ===== View Menu ============================================================================================
            ============================================================================================================ """

        self.viewmenu = Menu(self.menubar, tearoff=0)
        self.viewmenu.add_cascade(label="Windows...", menu=self._windowmenu)

        """ ===== Options Menu =========================================================================================
            ============================================================================================================ """

        self.optionsmenu = Menu(self.menubar, tearoff=0)
        self.optionsmenu.add_command(label="Settings", command=self._settingsMenu, )

        self.exammenu = Menu(self.menubar, tearoff=0)

        """ ===== Mouse Menu ===========================================================================================
            ==============================================================w============================================== """

        self.mousemenu = Menu(master, tearoff=0)
        self.mousemenu.add_command(label="Undo", command=self.donothing)
        self.mousemenu.add_command(label="Redo", command=self.donothing)

        self.mousemenu.add_separator()

        self.mousemenu.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: master.focus_get().event_generate('<<Cut>>'))
        self.mousemenu.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: master.focus_get().event_generate('<<Copy>>'))
        self.mousemenu.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: master.focus_get().event_generate('<<Paste>>'))
        self.mousemenu.add_command(label="Delete", command=self.donothing)
        self.mousemenu.add_command(label="Select All", accelerator="Ctrl+A", command=lambda: master.focus_get().event_generate('<<SelectAll>>'))  # ==!

        """ ===== Production ===========================================================================================
            ============================================================================================================ """

        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        self.menubar.add_cascade(label="Format", menu=self.formatmenu)
        self.menubar.add_cascade(label="View", menu=self.viewmenu)
        self.menubar.add_cascade(label="Options", menu=self.optionsmenu)
        self.menubar.add_command(label="Package Manager", command=self._initPackageManager)

        def popup(event):
            self.mousemenu.post(event.x_root, event.y_root)

        self.text.bind("<Button-3>", popup)

        master.protocol("WM_DELETE_WINDOW", self.exit)
        master.config(menu=self.menubar)

    def new(self):
        self.statusProgress.configure(mode='indeterminate')
        self.statusProgress.start(10)
        self.statusText.config(text="Alert! Do you want to open a file.")
        if messagebox.askokcancel('Open', ' Do you really want to create a new file! All unsaved progress will be lost!'):
            self.statusText.config(text="Creating New File...")
            self.master.title("Untitled - Ida")
            self.currentOpen = None
            self.text.delete('1.0', END)
            self.isFileOpen = False
        self.statusProgress.stop()
        self.statusText.config(text="Operation Complete")
        self.statusProgress.configure(mode='determinate')

    def open(self):
        self.statusProgress.configure(mode='indeterminate')
        self.statusProgress.start(10)
        self.statusText.config(text="Alert! Do you want to open a file.")
        if messagebox.askokcancel('Open', ' Do you really want to open a file! All unsaved progress will be lost!'):
            self.statusText.config(text="Opening...")
            file = filedialog.askopenfile(parent=self.master, mode='rb', title='Select a file to open',
                                          filetypes=(("Text files", "*.txt"),
                                                     ("Python files", "*.py;*.pyw"),
                                                     ("HTML files", "*.html;*.htm"),
                                                     ("Javascript files", "*.js"),
                                                     ("CSS files", "*.css"),
                                                     ("Ruby files", "*.rb"),
                                                     ('Perl code files', '*.pl;*.pm'),
                                                     ('Java code files', '*.java'),
                                                     ('C++ code files', '*.cpp;*.h'),
                                                     ("All files", "*.*")))

            if file is not None:
                contents = file.read()
                self.text.delete('1.0', END)
                self.text.insert('1.0', contents)
                file.close()
                self.currentOpen = file.name
                self.master.title("[" + str(file.name) + "] - Ida")
                self.isFileOpen = True

        self.statusProgress.stop()
        self.statusText.config(text="Operation Complete")
        self.statusProgress.configure(mode='determinate')

    def saveas(self):
        self.statusProgress.configure(mode='indeterminate')
        self.statusProgress.start(10)
        self.statusText.config(text="Saving...")
        file = filedialog.asksaveasfile(mode='w', title='Select where to save your file.',
                                        filetypes=(("Text files", "*.txt"),
                                                   ("Python files", "*.py;*.pyw"),
                                                   ("HTML files", "*.html;*.htm"),
                                                   ("Javascript files", "*.js"),
                                                   ("CSS files", "*.css"),
                                                   ("Ruby files", "*.rb"),
                                                   ('Perl code files', '*.pl;*.pm'),
                                                   ('Java code files', '*.java'),
                                                   ('C++ code files', '*.cpp;*.h'),
                                                   ("All files", "*.*")))

        if file is not None:
            data = self.text.get('1.0', END + '-1c')
            file.write(data)
            file.close()
            self.currentOpen = file
            self.master.title("[" + str(file.name) + "] - Ida")
            self.isFileOpen = True

        self.statusProgress.stop()
        self.statusText.config(text="Operation Complete")
        self.statusProgress.configure(mode='determinate')

    def save(self):
        if not self.isFileOpen:
            data = self.text.get('1.0', END + '-1c')
            file = open(self.currentOpen, 'w')
            file.write(data)
            file.close()
        else:
            self.saveas()

    def donothing(self):
        print("Error")
        messagebox.showerror("Error", "Currently not supported!")

    def _fontMenu(self):
        messagebox.showinfo("Deprecated Menu - Ida", "Font is deprecated. Font is now in settings")
        self.fontRoot = Tk()
        self.mainFont = _font.fontMenu(self.fontRoot, self.text)
        self.fontRoot.mainloop()

    def _consoleMenu(self):
        self.consoleRoot = Tk()
        self.mainConsole = _console.main(self.consoleRoot, self)
        self.consoleRoot.mainloop()

    def _initPackageManager(self):
        packManApp = _packageManager.packageManagerApp()

    def _settingsMenu(self):
        self.settingsRoot = Tk()
        self.mainSettings = _settings.main(self.settingsRoot, self.text, self.isAdminMode, self)
        self.settingsRoot.mainloop()

    def exit(self):
        if messagebox.askokcancel('Exit', ' Do you really want to exit! All unsaved progress will be lost!'):
            self.master.destroy()
            if self.fontRoot is not None:
                if not self.mainFont.open:
                    self.fontRoot.destroy()
            else:
                pass
        else:
            pass
