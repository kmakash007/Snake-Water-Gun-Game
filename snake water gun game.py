import random


def game_check(computer, user):
    if computer == user:
        return 0
    if computer == 0 and user == 1:
        return -1
    if computer == 1 and user == 2:
        return -1
    if computer == 2 and user == 0:
        return -1
    return 1


def main():

    options = ["Snake", "Water", "Gun"]

    computer = random.randint(0, 2)
    user = int(input("0==Snake, 1==Water, and 2==Gun:\n"))

    if user < 0 or user > 2:
        print("Invalid choice. Please select 0, 1, or 2.")
        return

    score = game_check(computer, user)

    print("You:", options[user])
    print("Computer:", options[computer])

    if score == 0:
        print("Match draw!")
    elif score == -1:
        print("You lose!")
    else:
        print("You won!")


if __name__ == "__main__":
    main()
