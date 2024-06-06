# Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
"-----------------------------------------------------------------------------------------"
def blackjack():
    import random  # imports "random" function
    from art import blacjack_logo
    
    print(blacjack_logo)
    
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # deck of cards
    
    
    def deal_card():  # selects a card from the deck randomly
        """
        Selects and returns a random card from a deck of cards.
    
        :return: A randomly selected card from the default deck.
        """
        card = random.choice(cards)
        return card
    
    
    # Deal the user and computer 2 cards each using deal_card() and append().
    # user_cards = []
    # computer_cards = []
    
    user_cards = []
    computer_cards = []
    
    def give_card_user():  # selects a card from the deck randomly
        user_cards.append((deal_card()))
    
    user_cards.append((deal_card()))  # gives de user his first card
    user_cards.append((deal_card()))  # gives de user his second card
    # print(f"Your cards: {user_cards}")
    
    def give_card_computer():  # selects a card from the deck randomly
        computer_cards.append((deal_card()))
        
    computer_cards.append((deal_card()))  # gives de computer his first card
    computer_cards.append((deal_card()))  # gives de computer his second card
    # print(computer_cards)
    
    
    # Create a function called calculate_score() that takes a List of cards as input
    # and returns the score.
    # Look up the sum() function to help you do this.
    def calculate_score(cards):
        """
        Calculates the total score of a list of cards.
    
        :param cards: List of integers representing the cards.
        :return: Integer representing the total score of the cards.
        """
        score = sum(cards)
    
        # Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
        if score == 21:
            return 0
    
    # Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
        for card in cards:
            if card == 11 and score > 21:
                cards.remove(11)  # removes the As (11)
                cards.append(1)  # appends an As value of 1
                score = sum(cards)  # Recalculates de score
        return score
    
    print(f"    Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
    print(f"    Computers first card: {computer_cards[0]}")
    
    
    # Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    def is_it_game_over():
        if calculate_score(user_cards) == 0 or calculate_score(computer_cards) == 0 or calculate_score(user_cards) > 21:  
            return True
        return False
    
    is_it_game_over()
    # If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
    # The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    
    game_over = is_it_game_over()
    while not game_over:
        other_card = input("Type 'y' to get another card, type ´n´ to pass: \n")
        if other_card == "y":
            give_card_user()
            print()
            print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
            print(f"Computers first card: {computer_cards[0]}")
            game_over = is_it_game_over()
        else:
            break
    
    # Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while calculate_score(computer_cards) < 17:
        give_card_computer()
    
    print()
    print(f"Your final hand: {user_cards}, final score:", calculate_score(user_cards))
    print(f"Computer´s final hand: {computer_cards}, final score:", calculate_score(computer_cards))
    
    # Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
    def compare():
        if calculate_score(user_cards) == calculate_score(computer_cards):
            print("draw")
        elif calculate_score(computer_cards) == 0:
            print("computer wins")
        elif calculate_score(user_cards) == 0:
            print("computer wins")
        elif calculate_score(user_cards) > 21:
            print("computer wins")
        elif calculate_score(computer_cards) > 21:
            print("user wins")
        else:
            if calculate_score(user_cards) > calculate_score(computer_cards):
                print("user wins")
            else:
                print("computer wins")
    
    compare()
    # Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
    def clear_console():
        print("\033c", end="")
    
    restart = input("do you want to restart? y/n \n")
    if restart == "y":
        clear_console()
        blackjack()
blackjack()
