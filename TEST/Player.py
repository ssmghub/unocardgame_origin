from Pile import *
from Card import *


class Player():
    def __init__(self,Ordernum):
        self.Ordernum = Ordernum
        self.playerHand = [] # this is a list to store player hand card
    
    # add card from cardsDrawn to playerhand
    def get_Handcard(self,number,pile):
        self.playerHand.extend(pile.DrawCard(number)) # 用于在列表末尾一次性追加另一个序列中的多个值（用新列表list扩展原来的列表list）
        return self.playerHand
    def addcard(self,x): 
        self.playerHand.extend(x)  # ????????????????????? 
    # show cards in each player's hand
    # def showHand(self,screen,x,y): 
    #     i = 0
    #     for card in self.playerHand: 
    #         card.drawCard(screen,x+i*70,y)
    #         i += 1
    #     pass  
    def showHand(self,screen,x,y):
        i = 0
        j = 0
        if len(self.playerHand)<=10:
            for card in self.playerHand:
                card.drawCard(screen,x+i*70,y)
                i += 1
        else :
            part1 = self.playerHand[0,9]
            part2 = self.playerHand[10,len(self.playerHand)]
            for card in part1:
                card.drawCard(screen,x+i*70,y)
                i += 1
            for card in part2:
                card.drawCard(screen,x+j*70,y+150)
                j += 1

    # if someone play the reverse card each player's ordernum * -1 
    # so that the turn of play cards can be reverse
    def changeOrder(self):
        self.Ordernum = self.Ordernum * (-1)
        pass

    # Judging whether the card can be played
    # 只写了判断数字卡的功能
    def canPlay(self,dispile,handcard): 
        # get the top card on discard pile
        card = dispile.show_topCard()
        if isinstance(self, numCard): # self ??????
            if card.colour == handcard.colour or card.number == handcard.number: 
                return True
            else: 
                return False 
        elif isinstance(self, skipCard): 
            if card.colour == handcard.colour: 
                return True
            else: 
                return False
        elif isinstance(self, reverseCard): 
            if card.colour == handcard.colour: 
                return True
            else: 
                return False
        elif isinstance(self, take2Card): 
            if card.colour == handcard.colour: 
                return True
            else: 
                return False
        elif isinstance(self, wildCard): 
            return True
        elif isinstance(self, wild4Card): 
            return True
        else: 
            return False


    def playCard(self,position,discardPile): 
       for card in self.playerHand: 
           if card.click(position) and card.canPlay(discardPile): 
               discardPile.discardlist.append(card)
               self.playerHand.remove(card)
               print(self.playerHand)
    

        
        
