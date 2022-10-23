# OOPS Approach and while loop out of the class
import random


class rock_paper_scissors:
    your_score = 0
    computer_score = 0

    def __init__(self):
        try:
            self.computer_choice = random.choice(["rock", "paper", "scissors"])
            user_choice = input('''Enter one of the choice:
            (r)rock
            (p)paper
            (s)scissors:\t''').lower()
            if user_choice.strip() == '':
                print("thanks for playing")
                quit()
            elif user_choice == 'r':
                self.user_choice = 'rock'
            elif user_choice == 'p':
                self.user_choice = 'paper'
            elif user_choice == 's':
                self.user_choice = 'scissors'
            else:
                print("Invalid option")
                quit()
            choice_list = [self.user_choice, self.computer_choice]
            # print(choice_list)  # ---->Checker#
            Win = [
                ["rock", "scissors"],
                ["paper", "rock"],
                ["scissors", "paper"]]
            if self.user_choice == self.computer_choice:
                print("\nTie")
                self.computer_score += 1
                self.your_score += 1
            elif choice_list in Win:
                print("You Win")
                self.your_score += 1
            else:
                print("Computer Wins")
                self.computer_score += 1
            print(
                f"Your score: {self.your_score}\nComputer score: {self.computer_score}")
            print("\n(Press Enter to exit)\n")
        except Exception as error:
            print(f"Error occured: {error}")


while True:
    rock_paper_scissors()
