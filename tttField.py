import numpy as np

class Playfield:
    # when class is created the field is empty
    def __init__(self):
        self.state = np.zeros((3, 3), dtype=int)
        self.turns = 0

    def move(self, player, p1, p2):
        if self.state[p2, p1] == 0:
            self.state[p2, p1] = player
            self.turns += 1
            return 0
        else:
            return 1

    def giveboard(self):
        # output 7 strings
        # 4 divider (d) strings and 3 playing strings
        d = " ---" * 3
        pre_p = list("|   ")

        pfill = [pre_p, pre_p, pre_p]
        pfill = [pfill, pfill, pfill]

        # we have 9 positions to print, so lets go!
        strlife = ["", "", ""]
        for col in range(0, 3):
            rowstring = ""
            for row in range(0, 3):
                pfill[row][col][2] = self.converter(self.state[row, col])
                rowstring = rowstring + ''.join(pfill[row][col])
            strlife[col] = rowstring + "|"

        return [d, strlife[0], d, strlife[1], d, strlife[2], d]

    def printboard(self):
        toprint = self.giveboard()
        print("TURN %d \n \n" % self.turns)
        for element in toprint:
            print(element)
        print("\n \n")

    def givearray(self):
        return self.state

    def converter(self, value):
        if value == 0:
            return " "
        elif value == 1:
            return "X"
        elif value == 2:
            return "O"

    # def gamebus(self):
    #     # available squares
    #     avSqrs = 0 in self.state
    #     # did u win
    #     duw = exercise26.wincheck(self.givearray())
    #     if duw in [1, 2, 3]:
    #         return False
    #     else:
    #         return True

