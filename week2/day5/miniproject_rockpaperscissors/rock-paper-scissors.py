from game import Game

def get_user_menu_choice():
    # ... code to display menu and get user choice ...
    options = {
        '1': 'Play a new game',
        '2': 'Show scores',
        '3': 'Quit'
    }
    while True:
        print("\n--- Game Menu ---")
        for key, value in options.items():
            print(f"{key}. {value}")
        
        choice = input("Enter your choice: ").strip()
        
        if choice in options:
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    
# def game_results():
#     results = {'win': 0, 'loss': 0, 'draw': 0}
#     while True:
#         if game_results == str('You win!'):
#             results.update({"win": + 1})
#         elif game_results == str('You lose!'):
#             results.update({"loss": + 1})
#         else:
#             results.update({"draw": + 1})
            

def print_results(results):
    # ... code to print results in a user-friendly way ...
    wins = results.get('win', 0)
    losses = results.get('loss', 0)
    draws = results.get('draw', 0)
    
    print("\n--- Game Summary ---")
    print(f"Wins: {wins}, Losses: {losses}, Draws: {draws}")
    print("Thank you for playing!")
    

def main():
    # ... code to call all the related functions depending on the user's choice.
    game_results = {'win': 0, 'loss': 0, 'draw': 0}
    
    
    while True:
        choice = get_user_menu_choice()
        
        if choice == '1':  # Play a new game
            print("Starting a new game...")
            game = Game()  # Instantiate your Game object here
            result = game.play() # Call the play method
            game_results[result] = game_results.get(result, 0)
            
            #to update the results
            if result == "You win!":
                game_results['win'] += 1
            elif result == "You lose!":
                game_results['loss'] += 1
            else:
                game_results['draw'] += 1

        elif choice == '2':  # Show scores
            print("\nCurrent Scores:")
            print(f"Wins: {game_results['win']}, Losses: {game_results['loss']}, Draws: {game_results['draw']}")
        elif choice == '3':  # Quit
            print_results(game_results)
            break

    
if __name__ == "__main__":
    main()