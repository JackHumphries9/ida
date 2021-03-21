from tkinter import *
from tkinter import ttk

class progressWindow():

    def __init__(self, title, body, time):
        self.root = Tk()
        self.root.title(title)
        self.root.minsize(250, 100)
        self.root.maxsize(250, 100)

        self.textBody = Label(self.root, text=body)
        self.progressBar = ttk.Progressbar(self.root, orient='horizontal', mode='indeterminate')

        self.progressBar.pack(side=BOTTOM, padx=15, pady=15, fill=X)
        self.textBody.pack(side=BOTTOM, padx=15, pady=15, fill=X)
                              
        self.progressBar.start(time)

        self.root.mainloop()