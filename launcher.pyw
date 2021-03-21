from tkinter import *
from bin import core
from bin import _console

def main():
    mainApp = Tk()
    mainApplication = core.CoreIda(mainApp)
    mainApp.mainloop()

if __name__ == '__main__':
    main()
    
