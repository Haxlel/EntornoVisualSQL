from tkinter import *
from mainFrame import MainFrame

def main():
    root = Tk()
    root.wm_title('Login')
    root.geometry('925x500+300+200')
    root.configure(bg='#fff')
    root.resizable(False,False) 

    img = PhotoImage(file='.\login.png')
    Label(root,image=img,bg='white').place(x=30,y=80)

    app = MainFrame(root)
    app.mainloop()

if __name__ =="__main__":
    main()