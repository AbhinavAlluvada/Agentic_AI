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

    if not color and not piece.islower():
        print("Black can only move black pieces.")
        return False
    if piece == "P":
        if to_col == from_col and to_row == from_row - 1:
            valid_move = True
        elif to_col == from_col and from_row == 6 and to_row == from_row - 2:
            valid_move = True
        else:
            print("Illegal pawn move!")
            valid_move = False
    if piece == "p":
        if to_col == from_col and to_row == from_row + 1:
            valid_move = True
        elif to_col == from_col and from_row == 1 and to_row == from_row + 2:
            valid_move = True
        else:
            print("Illegal pawn move!")
            valid_move = False
    if not valid_move:
        return False
    board[from_row][from_col] = EMPTY
    board[to_row][to_col] = piece
    return True


while True:
    if color:
        your_move = str(input("White to move: "))

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

    else:
        your_move = str(input("Black to move: "))

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
