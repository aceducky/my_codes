class Player:
    def __init__(self, name, isHuman=False):
        self.name = name
        self.isHuman = isHuman
        self.left = 1
        self.right = 1
        self.next = None
class Game:
    def __init__(self):
        self.game_mode = int(input("Choose a game mode:\n\
            1. Human vs Human\n\
            2. Human vs AI\n"))

        if self.game_mode == 1:
            self.p1 = Player(input("Enter player 1's name: "), isHuman=True)
            self.p2 = Player(input("Enter player 2's name: "), isHuman=True)
            self.p1.next = self.p2
            self.p2.next = self.p1
            self.play_with_human()
        elif self.game_mode == 2:
            self.p1 = Player(input("Enter your name: "), isHuman=True)
            self.p2 = Player("AI", isHuman=False)
            self.p1.next = self.p2
            self.p2.next = self.p1
            self.play_with_ai()
        else:
            print("Invalid Choice")
            exit()

    def display_board(self):
        print(f'''{"_"*10}

        {self.p1.name}      {self.p1.left}  {self.p1.right}

        {self.p2.name}      {self.p2.left}  {self.p2.right}

        {"_"*10}
        ''')
    def get_move_from_human(self,player):
        move = input("Enter your move (ll,rr,lr,rl) : ")
        #verifying move is valid
        while move not in ["ll","rr","lr","rl"]:
            move = input("Enter your move (ll,rr,lr,rl) : ")
        if (move == "ll"  and (player.left == 0 or player.next.left == 0))\
            or ( move == "rr" and (player.right == 0 or player.next.right == 0))\
            or (move == "lr" and (player.left == 0 or player.next.right == 0))\
            or (move == "rl" and (player.right == 0 or player.next.left == 0)):
                print("Invalid move")
                return self.get_move_from_human(player)  # Include 'return' to propagate the result

        return move

    def play_with_human(self):
        while True:
            self.display_board()
            p1_move = self.get_move_from_human(p1)
            if p1_move == "ll":
                pass
            #todo
            #check for lose condition
            if p2.left == 0 and p2.right == 0:
                print(f"Winner: {p1.name}")
                print("Congrats")
                self.display_board()
                exit()
            self.display_board()

            p2_move = self.get_move_from_human(p2)
            if p2_move == "ll":
                pass
            #todo
            #check for lose condition
            if p1.left == 0 and p1.right == 0:
                print(f"Winner: {p2.name}")
                print("Congrats")
                self.display_board()
                exit()
            self.display_board()


    def play_with_ai(self):
        pass
        #while True:
            #self.display_board()

            # Implement the game logic for Human vs AI here
            # For example, take turns, make moves, and check for the game's end condition
            # You can use self.p1 and self.p2 attributes to access player information

# Entry point
if __name__ == "__main__":
    game = Game()
