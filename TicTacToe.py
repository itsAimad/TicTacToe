from tkinter import *
from tkinter import messagebox
window = Tk()
def center_screen(window,width,height):
    #screen's width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    #x and y to center the window
    x = (screen_width//2) - (width//2)
    y = (screen_height//2) - (height//2)

    window.geometry(f"{width}x{height}+{x}+{y}")

width = 600
height = 540
center_screen(window,width,height)
icon = PhotoImage(file=r"C:\Users\Aimad\PycharmProjects\pythonProject\TicTacToe\tictactoe.png")
window.iconphoto(True,icon)
window.title("TicTacToe by Aimad")
window.config(bg="black")



#Label for player's score
score_1 = 0
score_2 = 0

#score_Label = Label(window,text=(f"Player 1 : {score_1}\nPlayer 2 : {score_2}"),
#                    font=("Arial",15),fg="red",bg="black",pady=10)
#score_Label.pack()
#score_Label.place(x=4)


# player's turn
turn_label = Label(window,text=("Player 2 Now"),font=("Arial",20),bg="red",fg="#fff",
                   pady=10,justify="center")
turn_label.pack()



def check_win():
        # Check for rows
        for i in range(0, 9, 3):
            if buttons[i]["text"] == buttons[i + 1]["text"] == buttons[i + 2]["text"] != "":
                return True, [i,i+1,i+2]

        # Check for columns
        for i in range(3):
            if buttons[i]["text"] == buttons[i + 3]["text"] == buttons[i + 6]["text"] != "":
                return True, [i,i+3,i+6]

        # Check diagonals
        if buttons[0]["text"] == buttons[4]["text"] == buttons[8]["text"] != "":
            return True, [0,4,8]
        if buttons[2]["text"] == buttons[4]["text"] == buttons[6]["text"] != "":
            return True, [2,4,6]

        return False, []
def check_tie():
    for button in buttons:
        if button["text"] == "":
            return False
    return True

current_player = 1
def restart_game():
    global current_player
    current_player = 1
    turn_label.config(text='Player 2 Now')
    for button in buttons:
        button.config(text="",state='normal',bg='black')


def click(num):
    global current_player
    #global score_1,score_2
    button = buttons[num-1]


    if(current_player ==1):
        turn_label.config(text="Player 1 Now")
        button.config(text="X")
        current_player = 2
    else:
        turn_label.config(text="Player 2 Now")
        button.config(text="O")

        current_player = 1

    button.config(state="disabled")
    if(check_win())[0]:
        winning_indices = check_win()[1] #call it once
        for idx in winning_indices:
            buttons[idx].config(bg="green")
        winner = "Player 1" if current_player == 1 else "Player 2"
        turn_label.config(text=f"{winner} wins !!",font=("Arial",20),bg="red",pady=10,justify="center")
        ask = messagebox.askyesno(title="Play Again",message="Wanna play again?")

        if ask:
            restart_game()
        else:
            window.destroy()
    elif check_tie():
        turn_label.config(text="It's a tie!", font=("Arial", 20), bg="red", pady=10, justify='center')
        ask = messagebox.askyesno(title='Play Again',message="It's a tie, wanna play again ?")
        if ask:
            restart_game()
        else:
            window.destroy()





             #score_2 +=1
            #score_Label.config(text=f"Player 1 : {score_1-2}\nPlayer 2 : {score_2}", font=("Arial", 15), pady=15)




#function to create buttons
buttons = []
def create_buttons():
    for i in range(1,10):
        button = Button(frame_contains_buttons,bd=3,relief=RAISED,
                         bg="black",
                         fg="white",
                         activebackground="red",font=("Arial",57),width=4,
                         activeforeground="black",command=lambda num=i:click(num))


        button.grid(row=(i - 1)//3 ,column= (i - 1)%3)
        buttons.append(button)



#buttons
buttons_frame = Frame(window,bg="black",width=570,height=480)
buttons_frame.pack()
buttons_frame.pack_propagate(False)
buttons_frame.place(x=17,y=66)



frame_contains_buttons = Frame(buttons_frame,bg="red",width=500,height=300)
frame_contains_buttons.pack()
frame_contains_buttons.pack_propagate(False)
create_buttons()


window.mainloop()