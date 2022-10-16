#tictactoe game using python

import numpy as np
board=np.array([['-','-','-'],['-','-','-'],['-','-','-']])
player=1
total_moves=0
end_check=0
def check():
    global board
    global end_check
    #for horizontal row
    for x in range(3):
        if board[x,0]==board[x,1] and board[x,1]==board[x,2] and board[x,0]!='-':
            print("player",board[x,0],"won")
            end_check=1
    #for vertical row
    for x in range(3):
        if board[0,x]==board[1,x] and board[1,x]==board[2,x] and board[0,x]!='-':
            print("player",board[0,x],"won")
            end_check=1
    #for diagonal row
    if board[0,0]==board[1,1] and board[1,1]==board[2,2] and board[0,0]!='-':
        print("player",board[0,0],"won")
        end_check=1
    if board[0,2]==board[1,1] and board[1,1]==board[2,0] and board[0,2]!='-':
        print("player",board[0,2],"won")
        end_check=1
    if np.all(board!='-') and end_check==0:
        print("draw")
        end_check=1
print("game start")
print(board)
while True:

    if player==1:
        p1_input=input("player 1:")
        if p1_input.isdigit():
            row=int(p1_input[0])
            col=int(p1_input[1])
            if row>2 or col>2 or row<0 or col<0:
                print("invalid input")
                continue
            if board[row,col]!='-':
                print("place already filled")
                continue
            board[row,col]='x'
            total_moves+=1
            player=2
            print(board)
            check()
    else:
        p2_input=input("player 2:")
        if p2_input.isdigit():
            row=int(p2_input[0])
            col=int(p2_input[1])
            if row>2 or col>2 or row<0 or col<0:
                print("invalid input")
                continue
            if board[row,col]!='-':
                print("place already filled")
                continue
            board[row,col]='o'
            total_moves+=1
            player=1
            print(board)
            check()
    if total_moves==9 or end_check==1:
        break

