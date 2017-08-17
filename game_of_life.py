def get_state(width, height):
    board = [[0 for i in range(0, width)] for i in range(0, height)]

    for i in range(0, height):
        board[i] = list(input("Enter state of row {0}: ".format(i+1)))

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
        num += int(board[cell[0]][cell[1]])

    return num

def get_neighbour_table(board):
    rows = len(board)
    cols = len(board[0])

    neighbours = [[0 for i in range(0, cols)] for i in range(0, rows)]

    for row in range(0, rows):
        for col in range(0, cols):
            neighbours[row][col] = get_num_neighbours(board, row, col)

    return neighbours
            
