import random


def rock_paper_scissors():
    your_score = 0
    computer_score = 0
    Win = [
        ["rock(✊)", "scissors(scissors(✌️))"],
        ["paper(✋)", "rock(✊)"],
        ["scissors(scissors(✌️))", "paper(✋)"]]
    while True:
        computer_choice = random.choice(["rock(✊)", "paper(✋)", "scissors(scissors(✌️))"])
        user_choice = input('''Enter one of the choice:
        (r)rock(✊)
        (p)paper(✋)
        (s)scissors(scissors(✌️)): \t''').lower()
        if user_choice.strip() == '':
            print("Thanks for playing......")
            quit()
        elif user_choice == 'r':
            user_choice = "rock(✊)"
        elif user_choice == 'p':
            user_choice = "paper(✋)"
        elif user_choice == 's':
            user_choice = "scissors(scissors(✌️))"
        else:
            print("Invalid option")
            quit()
        choice_list = [user_choice, computer_choice]
        print(
            f'User choice: {user_choice},  Computer choice: {computer_choice}')
        if user_choice == computer_choice:
            print("\nTie")
            computer_score += 1
            your_score += 1
        elif choice_list in Win:
            print("You Win")
            your_score += 1
        else:
            print("Computer Wins")
            computer_score += 1
        print(f"Your score: {your_score}\nComputer score: {computer_score}")
        print("\n(Press Enter to exit)\n")


rock_paper_scissors()

#emoji credits: https://emojiclipboard.com/
