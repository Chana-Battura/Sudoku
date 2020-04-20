#Python Project: Quarantine #1: Sudoku

#First Creating a Board

board = [[[' '] for in range(9)] for in range(9)]

print(board)

#I researched and decided to first make a solving algorithm
#For this, I will use a crosshatching technique ('https://www.bigfishgames.com/blog/how-to-solve-sudoku-puzzles-quickly-and-reliably/')

for hori in range(3):
    for vert in range(3):
        for num in range(1, 10):
            spot = []
            for j in range(3):
                for k in range(3):
                    if board[(3*horiz)+j][(3*vert)+k] == ' ':
                        if board[(3*horiz)+j].find(num) == -1:
                            row = []
                            for rows in range(9):
                                row.append(board[rows][[(3*vert)+k]])
                            if row.find(num) == -1:
                                spot.append([(3*horiz)+j, (3*vert)+k])
                            else:
                                continue
                        else:
                            continue

            if len(spot) == 1:
                board[spot[0], spot[1]] == num
