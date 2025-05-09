def main():
    # Initialize game state
    game_state = ['', '', '', '', '', '', '', '', '']
    current_player = 'X'
    game_active = True
    
    # Winning combinations
    winning_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    
    def print_board():
        print(f"{game_state[0]} | {game_state[1]} | {game_state[2]}")
        print("---------")
        print(f"{game_state[3]} | {game_state[4]} | {game_state[5]}")
        print("---------")
        print(f"{game_state[6]} | {game_state[7]} | {game_state[8]}")
    
    def check_result():
        nonlocal game_active, current_player
        
        for condition in winning_conditions:
            a, b, c = condition
            if game_state[a] == game_state[b] == game_state[c] != '':
                print(f"Player {game_state[a]} wins!")
                game_active = False
                return
        
        if '' not in game_state:
            print("Game ended in a draw!")
            game_active = False
            return
        
        current_player = 'O' if current_player == 'X' else 'X'
        print(f"Now it's Player {current_player}'s turn")
    
    def reset_game():
        nonlocal game_state, current_player, game_active
        game_state = ['', '', '', '', '', '', '', '', '']
        game_active = True
        current_player = 'X'
        print(f"Player {current_player}'s turn")
    
    print("Welcome to Tic Tac Toe!")
    print("Enter a number (1-9) to make your move:")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")
    
    while game_active:
        print_board()
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Please enter a number between 1 and 9")
                continue
            if game_state[move] != '':
                print("That position is already taken!")
                continue
            
            game_state[move] = current_player
            check_result()
        except ValueError:
            print("Please enter a valid number")
    
    print("Game over!")
    if input("Play again? (y/n): ").lower() == 'y':
        reset_game()
        main()

if __name__ == "__main__":
    main()