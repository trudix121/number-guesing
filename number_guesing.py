import random

# Create a random number
random_number = random.choice("123456789")
less_than_5 = 5
greater_than_5 = 5

if int(random_number) <= 5:
    x = input("This number is less than 5, choose a number: ")
if x == random_number:
    print("CONGRATULATIONS! YOU GUESSED THE NUMBER")
else:
    input("Try again! You have 2 more attempts:")
if x == random_number:
    print("CONGRATULATIONS! YOU GUESSED THE NUMBER")
else:
    x = input("Try again! You have one more attempt:")
if x == random_number:
    print("CONGRATULATIONS! YOU GUESSED THE NUMBER")
else:
    x = input("Try again! Last attempt:")
    print("YOU GOT IT WRONG, THE NUMBER WAS: " + random_number)

if int(random_number) >= 5:
    y = input("The number is greater than 5! : ")
if y == random_number:
    print("CONGRATULATIONS! YOU GUESSED THE NUMBER")
else:
    y = input("Try again! You have 3 more attempts:")
if y == random_number:
    print("CONGRATULATIONS! YOU GUESSED THE NUMBER")
else:
    y = input("Try again! You have 2 more attempts:")
if y == random_number:
    print("CONGRATULATIONS! YOU GUESSED THE NUMBER")
else:
    y = input("Try again! You have one more attempt:")
if y == random_number:
    print("CONGRATULATIONS! YOU GUESSED THE NUMBER")
else:
    print("WRONG, THE NUMBER WAS: " + random_number)
