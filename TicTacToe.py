#Kevin Dang
#Test TTT

from graphics import*
from random import*

#X at 0,0 = invisButton(win,0,0,1.5,1.5,X)
class invisButton:
    def __init__(self,win,xnum,ynum,height,width,XorO):
        self.win = win
        self.xnum = xnum
        self.ynum = ynum
        self.pos = True
        p1 = Point(1.5*width,1.5*height)
        if XorO == 'x':
            eye1 = Line(Point(3*xnum,3*ynum + 3),Point(3*xnum+3,3*ynum))
            eye1.setWidth(3)
            eye1.draw(win)
            eye2 = Line(Point(3 + 3*xnum,3 +3*ynum),Point(3*xnum,3*ynum))
            eye2.setWidth(3)
            eye2.draw(win)
        elif XorO == 'o':
            circ = Circle(Point(1.5*width,1.5*height),1.3)
            circ.draw(win)
        
    def getAlready():
        return self.pos
        
def main():
    win = GraphWin("Tic Tac Toe")
    win.setCoords(0,0,9,9)
    line1 = Line(Point(3,0),Point(3,9))
    line2 = Line(Point(6,0),Point(6,9))
    line3 = Line(Point(0,3),Point(9,3))
    line4 = Line(Point(0,6),Point(9,6))
    line1.draw(win)
    line2.draw(win)
    line3.draw(win)
    line4.draw(win)
    mainGame(win)

def mainGame(win):
    turn = 'x'
    i = 0
    while 1:
        if i%2 == 0:
            turn = 'x'
        else:
            turn = 'o'
        pt = win.getMouse()
        if pt.getX() <= 3.0:
            if pt.getY() <= 3:
                if Move(7,turn):
                   button = invisButton(win,0,0,1,1,turn)
                   list0[2][0]= turn
                   i+=1
                   
                else:
                    Move(7,turn)
                    
            elif pt.getY() <= 6:
                if Move(4,turn):
                    button = invisButton(win,0,1,3,1,turn)
                    list0[1][0]= turn
                    i+=1
                else:
                    Move(4,turn)
            else:
                if Move(1,turn):
                    button = invisButton(win,0,2,5,1,turn)
                    list0[0][0]= turn
                    i+=1
                else:
                    Move(1,turn)
        elif pt.getX() <=6:
            if pt.getY() <= 3:
                if Move(8,turn):
                    button = invisButton(win,1,0,1,3,turn)
                    list0[2][1]= turn
                    i+=1
                else:
                    Move(8,turn)
            elif pt.getY() <= 6:
                if Move(5,turn):
                    button = invisButton(win,1,1,3,3,turn)
                    list0[1][1]= turn
                    i+=1
                else:
                    Move(5,turn)
            else:
                if Move(2,turn):
                    button = invisButton(win,1,2,5,3,turn)
                    list0[0][1]= turn
                    i+=1
                else:
                    Move(2,turn)
        elif pt.getX() <=9:
            if pt.getY() <= 3:
                if Move(9,turn):
                    button = invisButton(win,2,0,1,5,turn)
                    list0[2][2]= turn
                    i+=1
                else:
                    Move(9,turn)
            elif pt.getY() <= 6:
                if Move(6,turn):
                    button = invisButton(win,2,1,3,5,turn)
                    list0[1][2]= turn
                    i+=1
                else:
                    Move(6,turn)
            else:
                if Move(3,turn):
                    button = invisButton(win,2,2,5,5,turn)
                    list0[0][2]= turn
                    i+=1
                else:
                    Move(3,turn)
        if Winning(turn):
            print turn +" Win"
            break
        else:
            print "Draw"
    win.close()
    win2 = GraphWin("Tic Tac Toe",100,100)
    Label = Text(Point(50,50),turn +"  Win")
    
    Label.draw(win2)
    win2.getMouse()
    win2.close()
        
list0 = [[1,2,3],[4,5,6],[7,8,9]]

##def AI():
##    p = Point(1-9,1-9)
##    return p
    
    
def DrawBoard():
    for i in range(len(list0)):
        for j in range(3):
            print " | ",list0[i][j],
        print " | "
        print ""
        
def check(num):
    for i in range(3):
        for j in range(len(list0[i])):
            if list0[i][j] == num:
                return True,i,j
    return False,i,j
    
      
def Move(numpos,letter):
    con,ind1,ind2 = check(numpos)
    if con:
        list0[ind1][ind2] = letter
        #DrawBoard()
        return True
    else:
        #DrawBoard()
        print "Spot already taken"
        return False
    
def Winning(letter):
    for i in range(3):
        if list0[0][i] == letter and list0[1][i] == letter and list0[2][i] == letter:
            return True
        if list0[i][0] == letter and list0[i][1] == letter and list0[i][2] == letter:
            return True
    if list0[0][0] == list0[1][1] and list0[1][1] == list0[2][2]:
        return True
    if list0[0][-1] == list0[1][-2] and list0[1][-2] == list0[2][-3]:
        return True
main()
#class Xpiece:
    
#def checkpos:

