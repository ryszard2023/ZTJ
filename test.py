import numpy as np

# board = ["1","2","3", "4","5","6", "7","8","9"]
board = ['X',"X","X", "4","X","6", "7","8","X"]

def disp_board(board, space=0):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print('-' * 10)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print('-' * 10)
    print(board[6] + " | " + board[7] + " | " + board[8])
    print('\n' * space)

disp_board(board, space=0)

np_board = np.reshape(board, (3, 3))

diag1 = [ np_board[i][i] for i in range(len(np_board)) ]
print(diag1)

diag2 = [ row[-i-1] for i,row in enumerate(np_board) ]
print(diag2)

diag3 = [np_board[i][i] for i in range(0, len(np_board))]
print(diag3)

diag4 = [np_board[i][~i] for i in range(0, len(np_board))]
print(diag4)

for i in range(0, len(np_board)):
    print(len(np_board), i, ~i)

for i in range(0, 3):
    print( i, ~i)

for i in range(0, 3):
    print( i, -i-1)


