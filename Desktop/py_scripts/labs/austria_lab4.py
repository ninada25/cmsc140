# I was not in attendance on Thursday because I was in Missouri presenting at a Women in Statistics Data Science Conference, so I completed this assignment individually.

# Your goal is to make function, battleship(), which when called starts a game the user can play that:
# Lets one player select a location to place their battleship.
# Lets the second player guess locations of the battleship until it is found.
# At the end, output their number of guesses as a “score”.
# You’ll use dictionaries to do this.

### Part I: Build a Battleship Board

theBoard = {
    'A' : ['.','.','.'],
    'B' : ['.','.','.'],
    'C' : ['.','.','.']
}

def print_board(board):
    print("     A    B    C")
    for i in range(len(board.values())):
        print(str(i+1) + "    " + board["A"][i] + "    " +  board["B"][i] + "    " + board["C"][i])

print_board(theBoard) # call print_board() function on my battleship board

### Parts II: Select your Battleship, III: Take a Guess, and IV: Sink your Battleship (I put it all together since we're working within the same function for all parts):

def battleship(board):
    print("Welcome to Battleship!")

    num_guesses = 0 # initialize number of guesses to 0

    col = input("Player 1, select a column for your battleship: ") # ask user to input the col they want to put their battleship, store in variable called 'col'
    row = int(input("Player 1, select a row for your battleship: ")) # ask user to input the row they want to put their battleship, store in variable called 'row'
    print("Current Board: ")
    print_board(board)

    while True:
        col_guess = input("Player 2, select a column to check: ") # ask user to guess a col
        row_guess = int(input("Player 2, select a row to check: ")) # ask user to guess a row

        num_guesses += 1 # increment num_guesses by 1

        if col == col_guess and row == row_guess: # if the guess is correct
            board[col_guess][row_guess-1] = "!" # must subtract 1 from row_guess since our first row is called row 1, not row 0
            print("You won!")
            print("Current Board: ")
            print_board(board)
            print("Score: ", num_guesses, " Guesses") # print score
            exit()
        else:
            board[col_guess][row_guess-1] = "x" # must subtract 1 from row_guess since our first row is called row 1, not row 0
            print("Sorry, nothing there.")
            print("Current Board: ")
            print_board(board)

battleship(theBoard)
