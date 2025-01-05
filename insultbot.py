import random
import time

def generate_insult():
    adjectives = ["artless", "bawdy", "beslubbering", "bootless", "churlish", "cockered", "clouted", "craven", "currish", "dankish", "dissembling", "droning", "errant", "fawning", "fobbing"]
    nouns = ["flap-dragon", "hedge-pig", "lewdster", "lout", "malt-worm", "miscreant", "mumble-news", "nut-hook", "scullion", "scurvy-knave", "varlet", "vassal", "wagtail", "minnow"]

    insult = f"Thou art a {random.choice(adjectives)} {random.choice(nouns)}!"
    return insult

def generate_compliment():
    adjectives = ["glorious", "peerless", "radiant", "gracious", "stellar", "magnificent", "angelic", "beauteous", "resplendent", "true-hearted", "noble", "upright"]
    nouns = ["wonder", "star", "delight", "jewel", "hero", "paragon", "ideal", "companion", "virtuoso", "champion", "treasure"]

    compliment = f"Thou art a {random.choice(adjectives)} {random.choice(nouns)}!"
    return compliment

def main():
    print("Welcome to InsultBot 3000!")
    time.sleep(1)

    while True:
        print("\nChoose an option:")
        print("1. Generate a Shakespearean Insult")
        print("2. Generate a Shakespearean Compliment")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("\n" + generate_insult())
            elif choice == 2:
                print("\n" + generate_compliment())
            elif choice == 3:
                print("\nFare thee well!")
                break
            else:
                print("\nInvalid choice! Please try again.")
        except ValueError:
            print("\nPlease enter a valid number.")

        time.sleep(1)

if __name__ == "__main__":
    main()
