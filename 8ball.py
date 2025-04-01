import random

def get_magic_8ball_answer():
    responses = {
        1: "Yes - definitely",
        2: "It is decidedly so",
        3: "Without a doubt",
        4: "Reply hazy, try again",
        5: "Ask again later",
        6: "Better not tell you now",
        7: "My sources say no",
        8: "Outlook not so good",
        9: "Very doubtful"
    }
    return responses.get(random.randint(1, 9), "Error")

name = input("What is your name? ")
question = input(f"Hello {name}, what's your question? ")

print(f"\n{name} asks: {question}")
print(f"Magic 8-Ball's answer: {get_magic_8ball_answer()}")

play_again = "yes"
while play_again.lower() in ["yes", "y"]:
    play_again = input("\nDo you want to ask another question? (yes/no): ")
    if play_again.lower() in ["yes", "y"]:
        question = input("What's your question? ")
        print(f"\n{name} asks: {question}")
        print(f"Magic 8-Ball's answer: {get_magic_8ball_answer()}")
