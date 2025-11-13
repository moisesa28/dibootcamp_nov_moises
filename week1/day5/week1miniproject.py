#Tic-tac-toe
# Goal: Create a Tic Tac Toe game in Python where two players can play against each other.

#instructions:
# Tic Tac Toe is played on a 3x3 grid. Players take turns marking empty squares
# with their symbol (‘O’ or ‘X’). The first player to get three of their symbols 
# in a row (horizontally, vertically, or diagonally) wins. If all squares are filled 
# and no player has three in a row, the game is a tie.

board = [
  [' ', ' ', ' '],
  [' ', ' ', ' '],
  [' ', ' ', ' ']
]   

def print_board(board):
    # """Displays the current state of the board in a 3x3 grid format."""
    print("\n")
    # Format each row with vertical separators
    print('*' * 13)
    print(f"* {board[0][0]} | {board[0][1]} | {board[0][2]} *")
    print("-------------")
    print(f"* {board[1][0]} | {board[1][1]} | {board[1][2]} *")
    print("-------------")
    print(f"* {board[2][0]} | {board[2][1]} | {board[2][2]} *")
    print("-------------")
    
    print("\n")


#player input
player1 = 'X'
player2 = 'O'

def player_input(player):
    while True:
        row = int(input(f"Player {player}, enter the row (1, 2, or 3) to place your '{player}': "))-1
        col = int(input(f"Player {player}, enter the column (1, 2 or 3) to place your '{player}': "))-1
        if board[row][col] != ' ':
            print(f"Position full, choose another one.")
            
        else:
            board[row][col] = player
            print_board(board)
            break
   

def check_winner(board, player):
    #check rows
    for row in board:
        if all([cell == player for cell in row]):
            print(f"Player {player} wins!")
            return True
    #check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            print(f"Player {player} wins!")
            return True
    #check diagonals
    if all([board[i][i] == player for i in range(3)]):
        print(f"Player {player} wins!")
        return True
        
    if all([board[i][2 - i] == player for i in range(3)]):
      print(f"Player {player} wins!")
      return True
    
    elif all([board[i][j] != ' ' for i in range(3) for j in range(3)]):
        print("It's a tie!")
        return True  
    return False


def play():
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    while True:
       player_input(player1)
       if check_winner(board, player1):
          break
       player_input(player2)
       if check_winner(board, player2):
          break

  
      
play()