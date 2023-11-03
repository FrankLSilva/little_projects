import random

values = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
player_total = []
user_cards = []
pc_cards = []
game = ""
new_game = "y"
pc_total = 0
game_round = True

while new_game == "y":

    def deal_card(game):
        random_card = int(values[random.randint(0, 12)])
        return random_card


    game = input("Start Blackjack?: Y or N:\n")

    for _ in range(2):
        user_cards.append(deal_card(game))
        pc_cards.append(deal_card(game))

    print(f"Your first two cards is: {user_cards}")


    def deal_card2(check):
        random_card = int(values[random.randint(0, 12)])
        return random_card


    def calculate_score(check):
        for each in user_cards:
            total = 0
            total = int(sum(user_cards))
            if total == 21:
                return 21
            else:
                return total


    def pc_score(check):
        for each in pc_cards:
            total3 = 0
            total3 = int(sum(pc_cards))
            if total3 == 21:
                return 21
            else:
                return total3


    print(f"You score is : {calculate_score(game)}\n")
    print(f"The computer first card is: {user_cards[0]}\n")

    while game_round:
        check = input("Want another card? Y or N:\n")

        if check == "y":
            user_cards.append(deal_card2(check))
            pc_cards.append(deal_card2(check))
            total4 = pc_score(check)
            total2 = calculate_score(check)

            print(f"Your cards are : {user_cards}")
            print(f"You score is : {total2}\n")
            print(f"PC score is : {total4}\n")

            if total2 == 21:
                print("You Win")
                game_round = False

            elif total2 > 21 > total4:
                print("You lose!")
                game_round = False

            elif total4 > 21:
                print("You Win")
                game_round = False

            elif total2 == total4:
                print("Draw")
                game_round = False

            elif 21 < total2 < total4:
                print("You Win")
                game_round = False

            elif total4 == 21:
                print("You lose!")
                game_round = False

        elif check == "n":
            pc_cards.append(deal_card2(check))
            total4 = pc_score(check)
            total2 = calculate_score(check)

            print(f"Your cards are : {user_cards}")
            print(f"You score is : {total2}\n")
            print(f"PC score is : {total4}\n")

            if total4 == 21:
                print("You lose!")
                game_round = False

            elif total4 > 21:
                print("You Win!")
                game_round = False

            print("Game ended")

        else:
            print("Invalid")
            game_round = False

    new_game = input("Want to go another round? Y or N:\n")

print("Bye!")













