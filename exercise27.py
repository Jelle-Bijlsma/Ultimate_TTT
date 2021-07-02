import exercise26 as winna
import tttField
from drawscreen import Screenclass


def getinput(player):
    symbols = {
        1: "X",
        2: "O"
    }
    coords = input("player %d (%s): required input 'XY' \n " % (player, symbols[player]))
    [x, y] = int(coords[0]), int(coords[1])
    x = x - 1
    y = y - 1
    return [x, y]


# initialize game

fields = ["first ones empty lol"]
maxFields = 10

for fieldNum in range(0, maxFields):
    fields.append(tttField.Playfield())

selectmatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

player = 1

if __name__ == "__main__":
    thescreen = Screenclass()
    # 3 is just a random take
    thescreen.drawall(fields[3].giveboard())

    thescreen.gamemsg("Player 1 tell Player 2 where to begin",3)
    [x, y] = thescreen.getinput(1)
    thescreen.gamemsg("                         " * 2, 3)
    thescreen.gamemsg("%d %d" % (x, y),4)
    currentfield = fields[selectmatrix[x][y]]
    player = 2

    while winna.gamebus(fields[10].givearray()):
        windownumber = selectmatrix[x][y]
        thescreen.drawone(currentfield.giveboard(), windownumber, 1)
        xold, yold = x, y
        [x, y] = thescreen.getinput(player)
        while currentfield.move(player, x, y) == 1:
            thescreen.gamemsg("this square is occupied, try again", 3)
            [x, y] = thescreen.getinput(player)
        thescreen.gamemsg("                  "*2, 3)

        thescreen.drawone(currentfield.giveboard(), windownumber, 0)
        #thescreen.gamemsg(str(currentfield.givearray()),10)
        result = winna.wincheck(currentfield.givearray())

        # moving and winchecking
        if result != 0:
            fields[10].move(result, xold, yold)
            duw = winna.wincheck(fields[10].givearray())
            if duw != 0:
                thescreen.gamemsg(("player %d won!!!" % player), 3)
                break

        # switch it up
        if player == 1:
            player = 2
        else:
            player = 1

        #thescreen.gamemsg(str(fields[10].givearray()), 0)

        # change the current field
        selmat = selectmatrix[x][y]
        currentfield = fields[selmat]
        thescreen.gamemsg("u go to % d" % selmat, 3)

        while not winna.gamebus(currentfield.givearray()):
            thescreen.gamemsg("player %d, free pass! go where?" % player, 3)
            [x, y] = thescreen.getinput(player)
            currentfield = fields[selectmatrix[x][y]]

    # # some boilerplate cause i cant seem to get the wrapper function to work
# screen = curses.initscr()
# curses.noecho()
# curses.cbreak()
# screen.keypad(True)
#
# # actual code
# screen.clear()
# screen.addstr("my nigga")
# c = screen.getch()
#
#
# # and this you got to do to exit it
# screen.keypad(False)
# curses.nocbreak()
# curses.echo()
# curses.endwin()
