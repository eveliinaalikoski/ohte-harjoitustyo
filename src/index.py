from tkinter import Tk
from ui import UI

def main():
    window = Tk()
    window.title("jippii")

    ui = UI(window)
    ui.start()
    window.mainloop()

if __name__=="__main__":
    main()