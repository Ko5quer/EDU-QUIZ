from tkinter import *
import array
#create table


def welcome_page():
    window=Tk()
    window.title("Multiplayer Quiz")
    welcome=Label(window, text="WELCOME TO THE QUIZ GAME!", font=("Arial", 14 , "bold"))
    welcome.grid(row=0, column=1, padx=10, pady=15)
    
    #Buttons
    main_button=["Start New Game", "Display Leaderboard","Add New Question", "Exit"]
    btns=[]
    i=1
    for button in main_button:
        btn= Button(window, text=button)
        btn.grid(row=i,column=1, padx=10, pady=15)
        i+=1
        btns.append(btn)

    window.mainloop()

welcome_page()

