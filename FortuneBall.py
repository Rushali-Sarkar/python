import random

AFFIRMATIVE  = ["It is certain", "It is decidedly so", "Without a doubt", "Yes- definitely", \
                        "You may rely on it", "As I see it, yes", "Most Likely", "Outlook good", "Yes", "Signs point to yes"]
NONCOMMITAL = ["Reply hazy, Try Again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again"]
NEGATIVE     = ["Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
CHOICE = [AFFIRMATIVE, AFFIRMATIVE, NONCOMMITAL, NEGATIVE]

def predictAnswer(question: str) -> str:
        return random.choice(random.choice(CHOICE))

TURN = True
while TURN:
    question = input("Please enter the question you wanna ask\n")
    print(predictAnswer(question))
    print("Do you want to ask another Question?")
    descion = input()
    if descion[0] in "Nn":
        TURN = False

