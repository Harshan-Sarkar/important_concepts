import random
num = random.randint(1, 100)
guess = None
while guess != num :
    guess = int(input("Enter your guess "))
    if guess == num:
        print("You guessed it right !")
    else :
        if guess < num:
            print(f"Guess a greater number than {guess}")
        else :
            print(f"Guess a lesser number than {guess}")

