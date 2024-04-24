from p1_random import P1Random

rng = P1Random()

game_continue = True
game_num = 0
player_wins = 0
dealer_wins = 0
tie_games = 0

# Control the number of games the player will play
while game_continue:
    game_num += 1
    print(f"\nSTART GAME #{game_num}")

    player_hand = 0
    card = rng.next_int(13) + 1

    if card == 1:
        print("\nYour card is a ACE!")
        card = 1
    elif 2 <= card <= 10:
        print(f"\nYour card is a {card}!")
    elif card == 11:
        print("\nYour card is a JACK!")
        card = 10
    elif card == 12:
        print("\nYour card is a QUEEN!")
        card = 10
    elif card == 13:
        print("\nYour card is a KING!")
        card = 10

    player_hand += card
    print(f"Your hand is: {player_hand}")

    # Game options
    while True:
        print("\n1. Get another card")
        print("2. Hold hand")
        print("3. Print statistics")
        print("4. Exit")

        # Prompt player for an input to choose a menu option
        option = input("\nChoose an option: ")

        if option == '1':
            card = rng.next_int(13) + 1
            if card == 1:
                print("\nYour card is a ACE!")
                card = 1
            elif 2 <= card <= 10:
                print(f"\nYour card is a {card}!")
            elif card == 11:
                print("\nYour card is a JACK!")
                card = 10
            elif card == 12:
                print("\nYour card is a QUEEN!")
                card = 10
            elif card == 13:
                print("\nYour card is a KING!")
                card = 10

            player_hand += card
            print(f"Your hand is: {player_hand}")

            if player_hand == 21:
                print("\nBLACKJACK! You win!")
                player_wins += 1
                break
            elif player_hand > 21:
                print("\nYou exceeded 21! You lose.")
                dealer_wins += 1
                break
        elif option == '2':
            dealer_hand = rng.next_int(11) + 16
            print(f"\nDealer's hand: {dealer_hand}")
            print(f"Your hand is: {player_hand}")
            if dealer_hand > 21 or player_hand > dealer_hand:
                print("\nYou win!")
                player_wins += 1
            elif dealer_hand > player_hand:
                print("\nDealer wins!")
                dealer_wins += 1
            else:
                print("\nIt's a tie! No one wins!")
                tie_games += 1
            break
        elif option == '3':
            print(f"\nNumber of Player wins: {player_wins}")
            print(f"Number of Dealer wins: {dealer_wins}")
            print(f"Number of tie games: {tie_games}")
            print(f"Total # of games played is: {game_num - 1}")
            if game_num > 0:
                print(f"Percentage of Player wins: {round(player_wins / (game_num - 1) * 100, 1)}%")
            game_continue = False
        elif option == '4':
            game_continue = False
            break
        else:
            print("\nInvalid input! \nPlease enter an integer value between 1 and 4.")
