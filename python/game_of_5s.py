import random
class Player:
    def __init__(self,name,isHuman = False):
        self.name = name
        self.turn = False
        self.left = 0
        self.right = 0
        self.isHuman = isHuman
        if cp.isHuman:
            inp = input("Your move: ").split()
            #todo
class Game:
    def __init__(self):
        self.p1 = Player("You",True)
        self.p2 = Player("Opponent")
        self.start()
    def drawBoard(self):
        print(f"""
        {"_"*10}

         {self.p2.name} {"<-" if self.p2.turn else ""}
            {self.p2.left}      {self.p2.right}

         {self.p1.name} {"<-" if self.p1.turn else ""}
            {self.p1.left}      {self.p1.right}

        current player: {self.p1.name if self.p1.turn else self.p2.name}
        {"_"*10}
        """)

    def play(self,cp,np):
        """
        Contains logic
        Based on the turn calculate the values and update them
        if player1 then take input
        else computer(random choice) or player2
        #important
        use self.drawBoard in the end of this to update values
        and show the board again after every move
        """

        while (self.first_move) or (cp.left != 0 and cp.right != 0) or (np.left != 0 and np.right != 0) :
            if(self.first_move): self.first_move = Falsc
            cp.getValue()
            cp,np = np,cp
            if (cp.left == 0 and cp.right % 2 == 0) or (cp.left % 2 == 0 and cp.right == 0):
                split_choice = input("Do you want to divide: ")
                if split_choice.lower() == "y" or "yes":
                    print("Values are divided now")
                    self.right = (self.right+self.left)/2
                    self.left = (self.left+self.right)/2
                    self.drawBoard()




    def start(self):
        print("_"*20)
        print("Game starts")
        self.p1.turn = random.choice([True,False])
        self.p2.turn = not self.p1.turn
        #current player - cp
        #next player - np
        if self.p1.turn:
            cp = self.p1
            np = self.p2
        else:
            cp = self.p2
            np = self.p1
        self.first_move = True
        self.drawBoard()
        self.play(cp,np)
        pass

game = Game()
