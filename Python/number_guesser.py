import random
import time

print("Hi! Welcome to the guessing game. I am going to pick a number between 1 and 100.")
time.sleep(3)
print("Picking a number...")
time.sleep(2)
guess = int(input("What is your guess?: "))
correct_number = random.randint(1, 100)
guess_count = 1

while guess != correct_number:
        time.sleep(1)
        guess_count += 1
        if guess < correct_number:
                guess = int(input("Wrong. You need to guess higher. What is your guess?: "))
        elif guess > correct_number:
                guess = int(input("Wrong. You need to guess lower. What is your guess?: "))

print("You got the right answer :)")
print(f"Congrats! The right answer was {correct_number}. It took you {guess_count} guesses.")
