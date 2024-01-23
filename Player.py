class Player():
    def __init__(self, Ordernum,score):
        self.Ordernum = Ordernum
        self.playerHand = []  # this is a list to store player hand card
        self.score = score
        self.ifuno=False

    # add card from cardsDrawn to playerhand
    def get_Handcard(self, number, pile):
        if len(self.playerHand)<14:
            self.playerHand.extend(pile.DrawCard(number))
        return self.playerHand

    def addcard(self, x):
        self.playerHand.extend(x)

    # show cards in each player's hand
    def showHand(self, screen, x, y):
        i = 0
        j = 0
        if len(self.playerHand)<=7:
            for card in self.playerHand:
                card.drawCard(screen, x + i * 74, y)
                i += 1
        else:
            for m in range(7):
                self.playerHand[m].drawCard(screen,x+i*74,y)
                i += 1
            for n in range(7,len(self.playerHand)):
                self.playerHand[n].drawCard(screen,x+j*74,y+108)
                # self.playerHand[n].drawCard(screen,x+j*74,y+30)
                j += 1

        # if someone play the reverse card each player's ordernum * -1

    # so that the turn of play cards can be reverse
    def changeOrder(self):
        self.Ordernum = self.Ordernum * (-1)
        pass