import random
from Card import *



class Pile(): 
    # deck store all the Card Object
    def __init__(self, deck): 
        self.deck = deck

    def shuffle(self): 
        # for cardindex in range(len(self.deck)): 
        #     randindex = random.randint(0,len(self.deck)-1)
        #     self.deck[cardindex], self.deck[randindex] = self.deck[randindex],self.deck[cardindex]
        for i in range(len(self.deck)-1, 0, -1): #-1: 表示从(0,x)倒着取数(-)，且步长为1(-1)
            r = random.randint(0,i) # 以此保证洗牌顺序不会再换回去：i=51,r=50->i=50,r!=51; 若无此约束，则r又可换回r=51，导致i刚和r交换了顺序旧友换回去了；
            self.deck[i], self.deck[r] = self.deck[r], self.deck[i]        
        return self.deck
        
    
    # Opening deal and drawing cards each turn
    # desk(牌库)
    # At the beginning, each person get 7 cards, and the rest is used as draw_pile
    # (开局每人发7张牌 剩下的 作为draw_pile)
    # at begining number =7  each turn number =1 for others function card number =2 or 4

    def DrawCard(self,number): 
        cardsDrawn = []
        for _ in range(number): 
            cardsDrawn.append(self.deck.pop(0))# remove one element form the list
        return cardsDrawn

    def takecard_0(self):
        card=self.deck[0]
        return card


class draw_Pile(Pile): 

    # the cardlist accept the rest card after (each person get 7 cards from deck and give 1 card to discard pile)

    def __init__(self,deck): 
        super().__init__(deck)
    
    def show_card(self, number): 
        return self.deck

    
class discard_Pile(Pile): 

    def __init__(self,pile): 
        # a list to store discards
        # Pile accept a object of Pile
        self.discardlist = []

        # after player drawn 7card, put the fist card of deck to discard Pile
        self.discardlist.append(pile.deck.pop(0)) ####### ? - ? board
    
    def show_topCard(self): 
        # show the top card on discard pile  discardlist[-1] 
        return self.discardlist[-1] 
        






