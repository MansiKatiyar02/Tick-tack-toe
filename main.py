def sum(a,b,c):
    return a+b+c

def Board(xState, yState):
    zero = 'X' if xState[0] else ('O' if yState[0] else 0)
    one = 'X' if xState[1] else ('O' if yState[1] else 0)
    two = 'X' if xState[2] else ('O' if yState[2] else 0)
    three = 'X' if xState[3] else ('O' if yState[3] else 0)
    four = 'X' if xState[4] else ('O' if yState[4] else 0)
    five = 'X' if xState[5] else ('O' if yState[5] else 0)
    six = 'X' if xState[6] else ('O' if yState[6] else 0)
    seven = 'X' if xState[7] else ('O' if yState[7] else 0)
    eight = 'X' if xState[8] else ('O' if yState[8] else 0)
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")

def checkWin(xState, yState):
    win = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for s in win:
        if(sum(xState[s[0]], xState[s[1]], xState[s[2]]) == 3):
            print("X won the match")
            return 1
        if(sum(yState[s[0]],yState[s[1]],yState[s[2]]) == 3):
            print("0 win the match")
            return 0
    return -1    
print("Welcome to Tick-Tack-Toe game")
xState = [0,0,0,0,0,0,0,0,0]
yState = [0,0,0,0,0,0,0,0,0]
# 1 for X and 0 for 0
turn = 1
while(True):
    Board(xState, yState)
    if(turn == 1):
        print("X's chance")
        value = int(input("Enter a value: "))
        xState[value]=1
    else:
        print("Y's chance")
        value = int(input("Enter a value: "))
        yState[value]=1
    cwin = checkWin(xState, yState)
    if(cwin!= -1):
        print("Match Over")
        break
    turn = 1-turn