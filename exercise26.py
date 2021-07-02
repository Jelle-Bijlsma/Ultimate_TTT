""""Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the
 moves were made.

If a game of Tic Tac Toe is represented as a list of lists, like so:

game = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2
 put their token in that space.

Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone
 has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a
 diagonal. Don’t worry about the case where TWO people have won - assume that in every board there will only be one
  winner."""

import numpy as np

# special array
sparray = range(0, 3)


def hnvcheck(board):
    for x in sparray:
        # occurrence 1 horizontal
        oc1h = (board[x, :].tolist()).count(1)
        oc2h = (board[x, :].tolist()).count(2)

        # occurrence 1 vertical
        oc1v = (board[:, x].tolist()).count(1)
        oc2v = (board[:, x].tolist()).count(2)

        if 3 in [oc1h, oc1v]:
            return 1
        elif 3 in [oc2h, oc2v]:
            return 2

    return 0


def diacheck(board):
    # create two diagonals to check
    check1 = [board[0, 0], board[1, 1], board[2, 2]]
    check2 = [board[0, 2], board[1, 1], board[2, 0]]

    # count occurrence
    dia1 = [check1.count(1), check2.count(1)]
    dia2 = [check1.count(2), check2.count(2)]
    if 3 in dia1:
        return 1
    elif 3 in dia2:
        return 2
    else:
        return 0


def wincheck(board):
    r1 = hnvcheck(board)
    r2 = diacheck(board)
    r3 = 0 in board

    winvec = [r1, r2]
    if (1 in winvec):
        # print("1 wins")
        return 1
    elif (2 in winvec):
        # print("2 wins")
        return 2
    elif (not r3):
        return 3
    else:
        return 0

def gamebus(board):
    # available squares
    avSqrs = 0 in board
    # did u win
    duw = wincheck(board)
    if duw in [1, 2, 3]:
        return False
    else:
        return True

if __name__ == "__main__":
    board = boards.board4
    board = np.array(board)
    # print(boards.board1)
    # print(board[0])
    # print(board[1])
    # print(board[2])
    print(type(board[:, 0]))
    winner = wincheck(board)
    if winner == 0:
        print("no winner")
    else:
        print("the winner is %d" % winner)