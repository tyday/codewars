sudoku_board = [
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

sudoku_board2 = [
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[2, 3, 4, 5, 6, 7, 8, 9, 1], 
[3, 4, 5, 6, 7, 8, 9, 1, 2], 
[4, 5, 6, 7, 8, 9, 1, 2, 3], 
[5, 6, 7, 8, 9, 1, 2, 3, 4],
[6, 7, 8, 9, 1, 2, 3, 4, 5],
[7, 8, 9, 1, 2, 3, 4, 5, 6],
[8, 9, 1, 2, 3, 4, 5, 6, 7], 
[9, 1, 2, 3, 4, 5, 6, 7, 8]
]

def check_ninth(x,y,board):
    sum_total = 0
    dict_originals = {}
    for i in range(x, x+3):
        for j in range(y,y+3):
            a = board[i][j]
            sum_total += a
            if a in dict_originals:
                print('failed originality in ninth ' +str(x)+','+str(y))
                return False
            else:
                dict_originals[a] = 1
    if sum_total == 45:
        return True
    else: 
        return False

def validSolution(board):
    #determine if each row consists of unique numbers from 1-9
    for row in board:
        # if sum(row) != 45:
        #     # print("Failed to sum to 45" + str(row))
        #     return False
        for i in range(1,10):
            if row.count(i) != 1:
                # print(str(i) + " failed in " + str(row))
                return False
    for row in list(zip(*board)):
        if sum(row) != 45:
            # print("Column failed to sum to 45" +str(row))
            return False
        for i in range(1,10):
            if row.count(i) !=1:
                # print(str(i) + " failed in column " + str(row))
                return False
    # print('Passed')

    #divide the board into 9 sections. Make sure each section is made up of unique values
    # Row One
    for x in range(0,7,3):
        if check_ninth(x,0,board) == False:
            return False
    #Row Two
    for x in range(0,7,3):
        if check_ninth(x,3,board) == False:
            return False
    #Row Three
    for x in range(0,7,3):
        if check_ninth(x,6,board) == False:
            return False
    return True       

print(validSolution(sudoku_board))
print(validSolution(sudoku_board2))