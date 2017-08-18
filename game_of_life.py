import time

def get_state(width, height):
    board = [[0 for i in range(0, width)] for i in range(0, height)]

    for i in range(0, height):
        board[i] = list(map(int, list(input("Enter state of row {0}: ".format(i+1)))))

    return board

def get_num_neighbours(board, row, col):
    MAX_ROW = len(board) - 1
    MAX_COL = len(board[0]) - 1

    i = 0
    num = 0

    cells = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1), (row, col - 1), (row, col + 1), (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]

    while i < len(cells):
        if (cells[i][0] < 0) or (cells[i][0] > MAX_ROW) or (cells[i][1] < 0) or (cells[i][1] > MAX_COL):
            cells.pop(i)
            i = 0
        else:
            i += 1

    for cell in cells:
        num += board[cell[0]][cell[1]]

    return num

def get_next_gen(board):
    WIDTH = len(board)
    HEIGHT = len(board[0]) 

    next_gen = [[0 for i in range(0, WIDTH)] for i in range(0, HEIGHT)]
    neighbour_board = get_neighbour_board(board)
    
    for row in range(0, WIDTH):
        for col in range(0, HEIGHT):
            state = board[row][col]
            neighbours = neighbour_board[row][col]

            if state == 0 and neighbours == 3:
                next_gen[row][col] = 1
            elif state == 1 and (neighbours > 3 or neighbours < 2):
                next_gen[row][col] = 0
            elif state == 1:
                next_gen[row][col] = 1
            
    return next_gen

def get_neighbour_board(board):
    return [[get_num_neighbours(board, row, col) for col in range(0, len(board[0]))] for row in range(0, len(board))]
