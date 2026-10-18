import random
def roll_dice():
    num_dice = int(input("Enter the number of dice to roll: "))
    if num_dice <= 0:
        print("Number of dice must be greater than 0.")
        return
    total = 0
    for i in range(num_dice):
        result = random.randint(1, 6)
        print("Die", i + 1, ":", result)
        total += result
    print("Total Score:", total)
roll_dice()