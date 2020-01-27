import random
num = random.randint(1, 10)
tries = 1
user = input("Hello, What is your username? ")
print("Hello",user)
question = input("Do you want to play a game? y/n: ")
if question == "n":
    print("oops!...Thank you.")
if question == "y":
    print("I'm thinking of a number between 1 & 10")
    guess = int(input("Have a guess: "))
    if guess > num:
        print("Guess lower...")
    if guess < num:
        print("Guess higher...")
    while guess != num:
        tries += 1
        guess = int(input("Try again: "))
    if guess == num:
        print("You're right! you win! The number was", num,"and it only took",tries, "trial")