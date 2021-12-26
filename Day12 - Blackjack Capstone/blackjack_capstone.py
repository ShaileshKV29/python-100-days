import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_starter_cards = [5, 10]
total_user_score = sum(user_starter_cards)

computer_starter_deck = cards[random.randint(0, len(cards))]

print(f"Your cards: {user_starter_cards}, current score: {total_user_score}")
print(f"Computer's first card: {computer_starter_deck}")
resume = input("Type 'y' to get another card, type 'n to pass: '")

while(True):
    if(resume == "n"):
        break
    elif(resume == "y"):
        new_card = cards[random.randint(0, len(cards))]
        