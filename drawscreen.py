import curses


class Screenclass:
    # start curses
    # has a few variables. stdscr, windows

    def __init__(self):
        self.stdscr = curses.initscr()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        # turns off echoing of keys. we gonna need this off
        curses.echo()

        # turn off the enter to confirm
        # curses.cbreak()
        # use page up, home as escape sequence
        self.stdscr.keypad(True)

        # stdscr.addstr() add a string

        # Legacy ting. update screen only when needed
        # stdscr.refresh()

        self.windows = []
        self.windows.append("empty lol")
        self.maxWindows = 9
        self.winrange = range(1, self.maxWindows+1)

        ydist = 10
        xdist = 20

        for windowNum in self.winrange:
            if windowNum <= 3:
                y = 0
            elif windowNum < 7:
                y = ydist*1
            else:
                y = ydist*2

            x = (windowNum % 3)
            if x != 0:
                x = (x-1)*xdist
            else:
                x = xdist*2

            self.windows.append(curses.newwin(10, 15, y, x))

        # create a place where messages can queue
        self.scoreboard = curses.newwin(ydist*3, xdist*2, 0, xdist*4)
        self.scoreboard.insstr("Welcome to Extrme TicTacTo")
        self.scoreboard.refresh()

    def drawone(self, supstr, winnum, color):
        # supstr = supplystring
        # winnum = window number
        self.windows[winnum].clear()
        if color == 1:
            counter = 1
            for element in supstr:
                if counter % 2 == 1:
                    self.windows[winnum].addstr(element + "\n", curses.color_pair(1))
                else:
                    self.windows[winnum].addstr(element + "\n")
                counter += 1
        else:
            for element in supstr:
                self.windows[winnum].addstr(element + "\n")
        self.windows[winnum].refresh()

    def drawall(self, inistr):
        for element in range(1, 10):
            self.drawone(inistr, element,0)

    def wait(self):
        self.windows[1].getkey()

    def gamemsg(self, instr, layer):
        self.scoreboard.addstr(layer, 0, instr)
        self.scoreboard.refresh()

    def getinput(self, player):
        symbols = {
            1: "X",
            2: "O"
        }

        allowed = ["11", "12", "13", "21", "22", "23", "31", "32", "33"]
        coords = [0, 0, 0]
        while coords not in allowed:
            self.gamemsg("player %d (%s): required input 'XY' \n " % (player, symbols[player]), 4)
            self.scoreboard.addstr(6, 0, "  ")
            coords = self.scoreboard.getstr(6, 0, 2).decode(encoding="utf-8")
            if coords not in allowed:
                self.gamemsg("move not allowed", 3)

        self.gamemsg("                    ", 3)

        [x, y] = int(coords[0]), int(coords[1])
        x = x - 1
        y = y - 1
        return [x, y]

    def endscreen(self):
        # to succesfully close it
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        self.stdscr.clear()
        curses.endwin()

# if __name__ == "__main__":
#     thisterm = Screenclass()
#     thisterm.drawall(thefield.giveboard())

#     thisterm.gamemsg("Player 1, make a move: \n")
#     thisterm.wait()
#
#     thisterm.endscreen()
