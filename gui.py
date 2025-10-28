import tkinter as TK
import socket 
import threading
import sys
#For the server
class Start_Connection():
    def __init__(self):
        self.server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((socket.gethostname(),2000))
        self.server.listen (5)
        self.data=None

    def close(self):
        self.server.close()


    def receive(self,client_socket):
        data=client_socket.recv(1024)
        return data.decode()
    
    def send_message(self,client,message=None):
        if message==None:
            return 
        else:
            client.send(message.encode())

    def handle_client(self,client_socket):
        while True:
            data=client_socket.recv(1024)
            self.data=data.decode()


    def wait_for_client(self):
        while True:
            client, self.address = self.server.accept()
            thread=threading.Thread(target=self.handle_client, args=(client,))
            thread.start()

class connection():
    def __init__(self):
        self.client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def recieve(self):
        message=self.client.recv(1024)
        return message.decode()
    
    def send(self, message):
        self.client.send(message.encode())
    
    def close(self):
        self.client.close()

    def wait_for_server(self):
        self.client.connect((socket.gethostname(),2000))

class Gui():
    def __init__(self):
        self.window=TK.Tk()
        self.window.title("Multiplayer Quiz Game")
        self.Main_buttons=(
            ("Start New Game",lambda:(self.start_game())),
            ("Display Leaderboard",lambda:(self.display_leaderboard())),
            ("Add New Question",lambda:(self.add_Question())),
            ("Exit",lambda:(self.exit()))
        )
        self.Main_menu()
        self.window.mainloop()

    def exit (self):
        self.main_frame.quit()
        self.window.quit()
    
    def get_input(self,textbox):
        self.name= textbox.get()
        print(self.name)
        self.Main_menu()
        return

    

    def Main_menu(self):
        self.main_frame=TK.Frame(self.window)
        self.main_frame.grid(row=0,column=0,sticky="NSEW")
        main_label=TK.Label(self.main_frame, text="WELCOME TO THE QUIZ GAME!",font=("Arial",14,"bold"))
        main_label.grid(row=0, column=1,padx=10,pady=15)
        i=1
        for buttons,commands in self.Main_buttons:
            button=TK.Button(self.main_frame,text=buttons, command=commands)
            button.grid(row=i,column=1,pady=15,padx=10)
            i+=1
        self.main_frame.tkraise()

    def start_game(self):
        self.start_frame=TK.Frame(self.window)
        self.main_frame.grid_forget()
        self.start_frame.grid(row=0,column=0)
        name_label=TK.Label(self.start_frame,text="Enter your name:",font=("Arial",14),padx=10,pady=15)
        name_label.grid(row=0,columnspan=4)
        input_textbox=TK.Entry(self.start_frame)
        input_textbox.grid(row=2,columnspan=4,padx=10,)
        Ok=TK.Button(self.start_frame,text="OK", command=lambda:(self.get_input(input_textbox)))
        cancel=TK.Button(self.start_frame, text="Cancel", command=lambda:(self.Main_menu()))
        Ok.grid(row=3,column=0,sticky="NESW",padx=10,pady=15)
        cancel.grid(row=3,column=2, sticky="NESW",padx=10,pady=15)

    def display_leaderboard(self):

               




test=Gui()
test.Main_menu()
print(test.name)
