#Import module
from tkinter import *
from tkinter import messagebox
import os
import sys

#Create a game window
game_window =Tk()

#variables
status = StringVar()
status.set("Match on")
counter = 0

#Create 9 StringVar to display text on button
varlist = { var: StringVar() for var in range(10)}

#Create 9 variables to store the value of StringVar
txtlist = []
for x in range (9):
    txtlist.append("1")

#Update the value of StringVar in those Variables
def update_list():
    for x in range (9):
        txtlist[x] = varlist[x].get()

played_my_turn = False

#Check if win
def check_if_win():
    
        if txtlist[0]==txtlist[2]==txtlist[1]==player or txtlist[4]==txtlist[5]==txtlist[3]==player or txtlist[7]==txtlist[8]==txtlist[6]==player:
            #messagebox.showinfo("Result",player + " wins")
            status.set(player + " wins! Game over. To start a new game press replay.")
            
        elif txtlist[0]==txtlist[3]==txtlist[6]==player or txtlist[1]==txtlist[4]==txtlist[7]==player or txtlist[2]==txtlist[5]==txtlist[8]==player:
            #messagebox.showinfo("Result",player + " wins")
            status.set(player + " wins! Game over. To start a new game press replay.")
        elif txtlist[0]==txtlist[4]==txtlist[8]==player or txtlist[2]==txtlist[4]==txtlist[6]==player:
            #messagebox.showinfo("Result",player + " wins")
            status.set(player + " wins! Game over. To start a new game press replay.")
        
    
        
#Swtiching between players:
def change_player():
    global played_my_turn, player, counter
    update_list()
    check_if_win()
    
    while played_my_turn == True:
        if player == "X":
            player = "O"
        else:
            player = "X"
        played_my_turn = False
        if counter == 8:
            status.set("It's a tie!! Press Replay to play again or Exit to close")
        counter+= 1
        
        
#Destroy 
def exit():
    game_window.destroy()

#Replay
def replay():
    game_window.destroy()
    os.startfile("Tic-Tac-Toe.py")


#Create 9 functions for 9 squares
def selectSqaure1():
    global played_my_turn
    varlist[0].set(player)  
    played_my_turn = True
    change_player()
    square1['state']= DISABLED
def selectSqaure2():
    global played_my_turn
    varlist[1].set(player)
    played_my_turn = True
    change_player()
    square2['state']= DISABLED  
def selectSqaure3():
    global played_my_turn
    varlist[2].set(player)
    played_my_turn = True
    change_player()  
    square3['state']= DISABLED
def selectSqaure4():
    global played_my_turn
    varlist[3].set(player)  
    played_my_turn = True
    change_player()
    square4['state']= DISABLED
def selectSqaure5():
    global played_my_turn
    varlist[4].set(player)  
    played_my_turn = True
    change_player()
    square5['state']= DISABLED
def selectSqaure6():
    global played_my_turn
    varlist[5].set(player)
    played_my_turn = True
    change_player()  
    square6['state']= DISABLED
def selectSqaure7():
    global played_my_turn
    varlist[6].set(player) 
    played_my_turn = True
    change_player() 
    square7['state']= DISABLED
def selectSqaure8():
    global played_my_turn
    varlist[7].set(player) 
    played_my_turn = True
    change_player() 
    square8['state']= DISABLED
def selectSqaure9():
    global played_my_turn
    varlist[8].set(player)  
    played_my_turn = True
    change_player()
    square9['state']= DISABLED




#Create 9 buttons or squares
square1 = Button(game_window, width = 15, height =5, textvariable = varlist[0], command = selectSqaure1)
square1.grid(row = 1, column = 0)
square2 = Button(game_window, width = 15, height =5, textvariable = varlist[1], command = selectSqaure2)
square2.grid(row = 1, column = 1)
square3 = Button(game_window, width = 15, height =5, textvariable = varlist[2], command = selectSqaure3)
square3.grid(row = 1, column = 2)
square4 = Button(game_window, width = 15, height =5, textvariable = varlist[3], command = selectSqaure4)
square4.grid(row = 2, column = 0)
square5 = Button(game_window, width = 15, height =5, textvariable = varlist[4], command = selectSqaure5)
square5.grid(row = 2, column = 1)
square6 = Button(game_window, width = 15, height =5, textvariable = varlist[5], command = selectSqaure6)
square6.grid(row = 2, column = 2)
square7 = Button(game_window, width = 15, height =5, textvariable = varlist[6], command = selectSqaure7)
square7.grid(row = 3, column = 0)
square8 = Button(game_window, width = 15, height =5, textvariable = varlist[7], command = selectSqaure8)
square8.grid(row = 3, column = 1)
square9 = Button(game_window, width = 15, height =5, textvariable = varlist[8], command = selectSqaure9)
square9.grid(row = 3, column = 2)
Label(game_window, textvariable = status).grid(row = 4, columnspan = 3)
Button(game_window, width = 10, height = 2, text = "Replay", command = replay).grid(row = 5, column = 0,columnspan = 2)
Button(game_window, width = 10, height = 2, text = "Exit", command = exit).grid(row = 5, column = 1, columnspan = 2)



#Create a player
player = "X"


#Start
game_window.mainloop()