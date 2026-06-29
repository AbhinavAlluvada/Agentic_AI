EMPTY = "."
board = [[EMPTY for _ in range(8)] for _ in range(8)]
board[0] = ['r','n','b','q','k','b','n','r']
board[1] = ['p']*8
board[6] = ['P']*8
board[7] = ['R','N','B','Q','K','B','N','R']

def print_board():
    for row in range(8):
        print(8-row, end="   ")
        for col in range(8):
                print(board[row][col], end ="  ")
        print()
    print("    a  b  c  d  e  f  g  h")
print_board()

def notation_to_position(move):
    file = move[0]
    rank = move[1]
    files ="abcdefgh"
    col = files.index(file)
    row = 8 - int(rank)
    
    return (row,col)

def move_piece(from_pos,to_pos):
    from_row = from_pos[0]
    from_col = from_pos[1]
    
    to_row = to_pos[0]
    to_col = to_pos[1]
    
    piece = board[from_row][from_col]
    if piece == EMPTY:
        print("There's no piece present!",)
        return
    board[from_row][from_col] = EMPTY
    board[to_row][to_col] = piece
    
while(True):
    your_move = str(input("Enter your move (e2 e4) or 'exit': "))
    if(your_move == "exit"):
        break
    if(your_move[0].isalpha() and your_move[1].isdigit() and your_move[2] == " " and your_move[3].isalpha() and your_move[4].isdigit()):
        move_piece(notation_to_position(your_move[0:2]),notation_to_position(your_move[3:5]))

        print_board()    
    else:
        print("Enter a valid notation!")
    


