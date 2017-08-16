def get_state():
    width = int(input("Enter board width: "))
    height = int(input("Enter board height: "))

    board = [[0 for i in range(0, width)] for i in range(0, height)]

    for i in range(0, height):
        board[i] = list(input("Enter state of row {0}: ".format(i+1)))

    return board
