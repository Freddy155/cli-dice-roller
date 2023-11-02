import random

def roll_dice(sides):
    """Roll a dice with a specified number of sides."""
    return random.randint(1, sides)

if __name__ == "__main__":
    while True:
        try:
            sides = int(input("Enter the number of sides for the dice (or 0 to quit): "))
            if sides == 0:
                print("Goodbye!")
                break
            if sides < 2:
                print("A dice must have at least 2 sides.")
            else:
                result = roll_dice(sides)
                print(f"You rolled a {sides}-sided dice and got: {result}")
        except ValueError:
            print("Please enter a valid number of sides.")
