EMPTY = "."
color = True
board = [[EMPTY for _ in range(8)] for _ in range(8)]
board[0] = ["r", "n", "b", "q", "k", "b", "n", "r"]
board[1] = ["p"] * 8
board[6] = ["P"] * 8
board[7] = ["R", "N", "B", "Q", "K", "B", "N", "R"]


def print_board():
    for row in range(8):
        print(8 - row, end="   ")
        for col in range(8):
            print(board[row][col], end="  ")
        print()
    print("    a  b  c  d  e  f  g  h")


print_board()


def notation_to_position(move):
    file = move[0]
    rank = move[1]
    files = "abcdefgh"
    col = files.index(file)
    row = 8 - int(rank)

    return (row, col)


def move_white_pawn(from_pos, to_pos):
    valid_move = False
    from_row = from_pos[0]
    from_col = from_pos[1]
    to_row = to_pos[0]
    to_col = to_pos[1]
    destination = board[to_row][to_col]
    if to_col == from_col and to_row == from_row - 1 and destination == EMPTY:
        valid_move = True
    elif (
        to_col == from_col
        and from_row == 6
        and to_row == from_row - 2
        and board[from_row - 1][from_col] == EMPTY
        and destination == EMPTY
    ):
        valid_move = True
    elif (
        abs(to_col - from_col) == 1
        and to_row == from_row - 1
        and destination != EMPTY
        and destination.islower()
    ):
        valid_move = True
    else:
        print("Illegal pawn move!")
        valid_move = False
    return valid_move


def move_black_pawn(from_pos, to_pos):
    valid_move = False
    from_row = from_pos[0]
    from_col = from_pos[1]
    to_row = to_pos[0]
    to_col = to_pos[1]
    destination = board[to_row][to_col]
    if to_col == from_col and to_row == from_row + 1 and destination == EMPTY:
        valid_move = True
    elif (
        to_col == from_col
        and from_row == 1
        and to_row == from_row + 2
        and board[from_row + 1][from_col] == EMPTY
        and destination == EMPTY
    ):
        valid_move = True
    elif (
        abs(to_col - from_col) == 1
        and to_row == from_row + 1
        and destination != EMPTY
        and destination.isupper()
    ):
        valid_move = True
    else:
        print("Illegal pawn move!")
        valid_move = False
    return valid_move


def move_white_knight(from_pos, to_pos):
    valid_move = False
    from_row = from_pos[0]
    from_col = from_pos[1]
    to_row = to_pos[0]
    to_col = to_pos[1]
    destination = board[to_row][to_col]
    row_diff = abs(to_row - from_row)
    col_diff = abs(to_col - from_col)
    if (row_diff, col_diff) in [(2, 1), (1, 2)]:
        if destination == EMPTY or destination.islower():
            valid_move = True
    if (row_diff, col_diff) not in [(2, 1), (1, 2)]:
        print("Invalid Knight move!")
    return valid_move


def move_black_knight(from_pos, to_pos):
    valid_move = False
    from_row = from_pos[0]
    from_col = from_pos[1]
    to_row = to_pos[0]
    to_col = to_pos[1]
    destination = board[to_row][to_col]
    row_diff = abs(to_row - from_row)
    col_diff = abs(to_col - from_col)
    if (row_diff, col_diff) in [(2, 1), (1, 2)]:
        if destination == EMPTY or destination.isupper():
            valid_move = True
    if (row_diff, col_diff) not in [(2, 1), (1, 2)]:
        print("Invalid Knight move!")
    return valid_move


def move_white_rook(from_pos, to_pos):
    valid_move = False
    from_row = from_pos[0]
    from_col = from_pos[1]

    to_row = to_pos[0]
    to_col = to_pos[1]
    destination = board[to_row][to_col]
    if from_row == to_row:
        blocked = False
        start = min(from_col, to_col) + 1
        end = max(from_col, to_col)
        for col in range(start, end):
            if board[to_row][col] != EMPTY:
                blocked = True
                break
        if not blocked:
            if destination == EMPTY or destination.islower():
                valid_move = True
    elif from_col == to_col:
        blocked = False
        start = min(from_row, to_row) + 1
        end = max(from_row, to_row)
        for row in range(start, end):
            if board[row][to_col] != EMPTY:
                blocked = True
                break
        if not blocked:
            if destination == EMPTY or destination.islower():
                valid_move = True
    else:
        print("Invalid Rook move!")
    return valid_move


def move_black_rook(from_pos, to_pos):
    valid_move = False
    from_row = from_pos[0]
    from_col = from_pos[1]

    to_row = to_pos[0]
    to_col = to_pos[1]
    destination = board[to_row][to_col]
    if from_row == to_row:
        blocked = False
        start = min(from_col, to_col) + 1
        end = max(from_col, to_col)
        for col in range(start, end):
            if board[to_row][col] != EMPTY:
                blocked = True
                break
        if not blocked:
            if destination == EMPTY or destination.isupper():
                valid_move = True
    elif from_col == to_col:
        blocked = False
        start = min(from_row, to_row) + 1
        end = max(from_row, to_row)
        for row in range(start, end):
            if board[row][to_col] != EMPTY:
                blocked = True
                break
        if not blocked:
            if destination == EMPTY or destination.isupper():
                valid_move = True
    else:
        print("Invalid Rook move!")
    return valid_move


def move_white_bishop(from_pos, to_pos):
    valid_move = False
    from_row = from_pos[0]
    from_col = from_pos[1]

    to_row = to_pos[0]
    to_col = to_pos[1]
    destination = board[to_row][to_col]
    if abs(from_col - to_col) == abs(from_row - to_row):
        blocked = False
        row_step = 1 if to_row > from_row else -1
        col_step = 1 if to_col > from_col else -1

        current_row = from_row + row_step
        current_col = from_col + col_step

        while current_row != to_row:
            if board[current_row][current_col] != EMPTY:
                blocked = True
                break
            current_row += row_step
            current_col += col_step
        if not blocked:
            if destination == EMPTY or destination.islower():
                valid_move = True
    else:
        print("Invalid Bishop move!")
    return valid_move


def move_black_bishop(from_pos, to_pos):
    valid_move = False
    from_row = from_pos[0]
    from_col = from_pos[1]

    to_row = to_pos[0]
    to_col = to_pos[1]
    destination = board[to_row][to_col]
    if abs(from_col - to_col) == abs(from_row - to_row):
        blocked = False
        row_step = 1 if to_row > from_row else -1
        col_step = 1 if to_col > from_col else -1

        current_row = from_row + row_step
        current_col = from_col + col_step

        while current_row != to_row:
            if board[current_row][current_col] != EMPTY:
                blocked = True
                break
            current_row += row_step
            current_col += col_step
        if not blocked:
            if destination == EMPTY or destination.isupper():
                valid_move = True
    else:
        print("Invalid Bishop move!")
    return valid_move

def move_white_king(from_pos,to_pos):
    valid_move = False
    from_row = from_pos[0]
    from_col = from_pos[1]

    to_row = to_pos[0]
    to_col = to_pos[1]
    destination = board[to_row][to_col]
    
    row_diff = abs(from_row - to_row)
    col_diff = abs(from_col - to_col)
    
    if max(row_diff,col_diff) == 1:
        if destination == EMPTY or destination.islower():
            valid_move = True
    return valid_move

def move_black_king(from_pos,to_pos):
    valid_move = False
    from_row = from_pos[0]
    from_col = from_pos[1]

    to_row = to_pos[0]
    to_col = to_pos[1]
    destination = board[to_row][to_col]
    
    row_diff = abs(from_row - to_row)
    col_diff = abs(from_col - to_col)
    
    if max(row_diff,col_diff) == 1:
        if destination == EMPTY or destination.isupper():
            valid_move = True
    return valid_move
        
def move_piece(from_pos, to_pos, color):
    valid_move = False
    from_row = from_pos[0]
    from_col = from_pos[1]

    to_row = to_pos[0]
    to_col = to_pos[1]
    piece = board[from_row][from_col]
    if piece == EMPTY:
        print(
            "There's no piece present!",
        )
        return False
    if color and not piece.isupper():
        print("White can only move white pieces.")
        return False

    elif not color and not piece.islower():
        print("Black can only move black pieces.")
        return False
    if piece == "P":
        valid_move = move_white_pawn(from_pos, to_pos)
    elif piece == "N":
        valid_move = move_white_knight(from_pos, to_pos)
    elif piece == "R":
        valid_move = move_white_rook(from_pos, to_pos)
    elif piece == "B":
        valid_move = move_white_bishop(from_pos, to_pos)
    elif piece == "Q":
        valid_move = move_white_bishop(from_pos, to_pos) or move_white_rook(
            from_pos, to_pos
        )
    elif piece == "K":
        valid_move = move_white_king(from_pos,to_pos)
    elif piece == "p":
        valid_move = move_black_pawn(from_pos, to_pos)
    elif piece == "n":
        valid_move = move_black_knight(from_pos, to_pos)
    elif piece == "r":
        valid_move = move_black_rook(from_pos, to_pos)
    elif piece == "b":
        valid_move = move_black_bishop(from_pos, to_pos)
    elif piece == "q":
        valid_move = move_black_bishop(from_pos, to_pos) or move_black_rook(
            from_pos, to_pos
        )
    elif piece == "k":
        valid_move = move_black_king(from_pos,to_pos)
    if not valid_move:
        return False
    board[from_row][from_col] = EMPTY
    board[to_row][to_col] = piece
    return True


while True:
    player = "White" if color else "Black"

    your_move = input(f"{player} to move: ")

    if your_move == "exit":
        break
    if len(your_move) != 5:
        print("Enter a valid notation!")
        continue
    if your_move[0] not in "abcdefgh" or your_move[3] not in "abcdefgh":
        print("File invalid!")
        continue
    if your_move[1] not in "12345678" or your_move[4] not in "12345678":
        print("Rank invalid!")
        continue
    success = move_piece(
        notation_to_position(your_move[0:2]),
        notation_to_position(your_move[3:5]),
        color,
    )

    if success:
        color = not color
        print_board()
