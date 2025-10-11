from tkinter import *

#create table

def start_new(container):
    #Making container
    name_field=Frame(container)
    name_field.grid(row=0, column=0, sticky=NSEW)

    buttons=Frame(container)
    buttons.grid(row=1, column=0, sticky=NSEW)

    #Label
    message=Label(name_field,text="Enter your name:")

    #Making textbox
    entry=Entry(name_field)
    name=entry.get()

    #Making buttons
    tab="\t"
    enter=Button(name_field, text=f"{tab}Ok{tab}",command=lambda: print("Hello"))
    exit=Button(name_field, text=f"{tab}Exit{tab}", command=lambda: print("Hello"))

    #placing in containter
    message.grid(row=0, column=1, padx=5, pady=5, columnspan=2)
    entry.grid(row=1, column=1, padx=5, pady=5, columnspan=2)
    enter.grid(row=2,column=1, padx=5, pady=5)
    exit.grid(row=2,column=2, padx=5, pady=5)
    name_field.tkraise()


    

def disp_leaderboard():
    print("hello")

def add_Question():
    print("hello")

def exit_game():
    print("hello")


def disp_leaderboard():
    print("hello")

def welcome_page():
    window=Tk()
    window.title("Multiplayer Quiz")

    welc_Frame= Frame(window)
    welc_Frame.grid(row=0, column=0, sticky=NSEW)
    welcome=Label(welc_Frame, text="WELCOME TO THE QUIZ GAME!", font=("Arial", 14 , "bold"))
    welcome.grid(row=0, column=1, padx=10, pady=15)
    
    #Buttons
    main_button=(
        ("Start New Game",lambda: start_new(window)),
        ("Display Leaderboard",disp_leaderboard),
        ("Add New Question",add_Question),
        ("Exit",exit_game)
    )
    btns=[]
    i=1
    for button, commands in main_button:
        btn= Button(welc_Frame, text=button, command=commands)
        btn.grid(row=i,column=1, padx=10, pady=15)
        i+=1
        btns.append(btn)

    welc_Frame.tkraise()
    window.mainloop()


welcome_page()

