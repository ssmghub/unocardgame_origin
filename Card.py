import random
from Pile import *
import pygame

class Card():
    def __init__(self,  colour: str, number):
        self.colour = colour
        self.number = number
        self.image = pygame.image.load(f'images/cards/{self.colour}_{self.number}.png')
        self.back = pygame.image.load('images/cards/back.png')
        self.rect = self.image.get_rect()
        
    # this function for paint the front of card 
    # screen is the nuogame window 
    # x,y is the image position
    def drawCard(self,screen,x,y):
        self.rect.left = x
        self.rect.top = y
        screen.blit(self.image,self.rect)
        
    # this function for paint the back of card
    # cause other players donot have to show their card
    def drawBack(self,screen,x,y):
        self.rect.left = x
        self.rect.top = y
        screen.blit(self.back,(x, y))

    # this function for check if card was clicked
    # position is the position of mouse
    # collidepoint is built-in function for detects whether a point is contained within a rect object
    def click(self,position):
            if self.rect.collidepoint(position): #测试一个点是否在矩形内(bool)
                print("yes")
                return True
            else:
                return  False
        
    # def __str__(self):
    #    if isinstance(self, numCard):
    #        return self.colour+ " "+ str(self.number)
    #    elif isinstance(self, skipCard):
    #        return self.colour+ " "+ str(self.number)
    #    elif isinstance(self, reverseCard):
    #        return self.colour+ " "+ str(self.number)
    #    elif isinstance(self, take2Card):
    #        return self.colour+ " "+ str(self.number)
    #    elif isinstance(self, wildCard):
    #        return self.colour+ " "+ str(self.number)
    #    elif isinstance(self, wild4Card):
    #        return self.colour+ " "+ str(self.number)

    # def __repr__(self):
    #    if isinstance(self, numCard):
    #        return self.colour+ " "+ str(self.number)
    #    elif isinstance(self, skipCard):
    #        return self.colour+ " "+ str(self.number)
    #    elif isinstance(self, reverseCard):
    #        return self.colour+ " "+ str(self.number)
    #    elif isinstance(self, take2Card):
    #        return self.colour+ " "+ str(self.number)
    #    elif isinstance(self, wildCard):
    #        return self.colour+ " "+ str(self.number)
    #    elif isinstance(self, wild4Card):
    #        return self.colour+ " "+ str(self.number)
    
    # def canPlay(self,dispile):
    #     # get the top card on discard pile
    #     card = dispile.show_topCard()
        
    #     if isinstance(self, numCard) and isinstance(card,numCard):
    #        if card.colour == self.colour or card.number == self.number:
    #            return True
    #     elif isinstance(self, skipCard):
    #            if isinstance(card, skipCard) or card.colour == self.colour:
    #                return True
    #     elif isinstance(self, reverseCard):
    #        if isinstance(card, skipCard) or card.colour == self.colour:
    #                return True
    #     elif isinstance(self, take2Card):
    #        if isinstance(card, take2Card) or card.colour == self.colour:
    #                return True
    #     elif isinstance(self, wildCard):
    #        return True
    #     elif isinstance(self, wild4Card):
    #        return True
    #     else:
    #        return False
    
    # def isValid(self, card):
    #     if isinstance(card, WildCard):
    #         return True
    #     if isinstance(card, FourCard):
    #         return True
    #     elif isinstance(card, NumCard) and ((isinstance(self.face_card, NumCard) and card.number == self.face_card.number) or card.colour == self.face_card.colour):
    #         return True
    #     elif isinstance(card, AddCard) and ((isinstance(self.face_card, AddCard) and card.add == self.face_card.add) or card.colour == self.face_card.colour):
    #         return True
    #     elif isinstance(card, MissCard) and (isinstance(self.face_card, MissCard) or card.colour == self.face_card.colour):
    #         return True
    #     elif isinstance(card, ReverseCard) and (isinstance(self.face_card, ReverseCard) or card.colour == self.face_card.colour):
    #         return True
    #     return False
    
# class numCard(Card): 
#     def __init__(self, colour, number): 
#        super().__init__(colour)
#        self.number = number
#        self.image = pygame.image.load(f'images/{self.colour}_{self.number}.png')
        
#     def drawCard(self,screen,x,y): 
#        super().drawCard(screen, x, y)

#     def drawBack(self, screen, x, y): 
#        super().drawBack(screen, x, y)
     
#     def __repr__(self):
#        return self.colour+ " "+ str(self.number)

# class skipCard(Card):
#    def __init__(self, colour):
#        super().__init__(colour)
#        self.number = 100
#        self.image = pygame.image.load(f'images/{self.colour}_skip.png')
#        self.rect = self.image.get_rect()
    
#    def drawCard(self, screen, x, y):
#        super().drawCard(screen, x, y)
    
#    def drawBack(self, screen, x, y):
#        super().drawBack(screen, x, y)

# class reverseCard(Card):
#    def __init__(self, colour):
#        super().__init__(colour)
#        self.number = 200
#        self.image = pygame.image.load(f'images/{self.colour}_reverse.png')
#        self.rect = self.image.get_rect()
    
#    def drawCard(self, screen, x, y):
#        super().drawCard(screen, x, y)
    
#    def drawBack(self, screen, x, y):
#        super().drawBack(screen, x, y)
    


# class take2Card(Card):
#     def __init__(self, colour):
#         super().__init__(colour)
#         self.number = 300
#         self.image = pygame.image.load(f'images/{self.colour}_+2.png')
#         self.rect = self.image.get_rect()
    
#     def drawCard(self, screen, x, y): 
#         super().drawCard(screen, x, y) 
    
#     def drawBack(self, screen, x, y): 
#         super().drawBack(screen, x, y) 

# class wildCard(Card):
#     def __init__(self):
#         self.colour = "black"
#         self.number = 400 #??????????????????
#         self.image = pygame.image.load('images/black_14.png')
#         self.rect = self.image.get_rect()
        
#     def drawCard(self, screen, x, y):
#         super().drawCard(screen, x, y)
    
#     def drawBack(self, screen, x, y):
#         super().drawBack(screen, x, y)

# class wild4Card(Card): 
#     def __init__(self): 
#         self.colour = "black"
#         self.number = 500 #??????????????????
#         self.image = pygame.image.load('images/black_15.png')
#         self.rect = self.image.get_rect()
        
#     def drawCard(self, screen, x, y): 
#         super().drawCard(screen, x, y)
    
#     def drawBack(self, screen, x, y):
#         super().drawBack(screen, x, y)


# write a function to add all card into deck(牌库)

# def add_numCard(): 
#     cardlist1 = []
#     for colour in ['yellow','blue','green','red']: 
#         for i in range(2): # 两套牌
#             for i in range(1,10): 
#                 cardlist1.append(numCard(colour, i))
#         cardlist1.append(numCard(colour,0)) # 一套0牌
#     return cardlist1

# def add_skipCard(): 
#     cardlist2 = []
#     for colour in ['yellow','blue','green','red']:
#         for i in range(2):
#             cardlist2.append(skipCard(colour))
#     return cardlist2

# def add_reverseCard(): 
#     cardlist3 = []
#     for colour in ['yellow','blue','green','red']:
#         for i in range(2):
#             cardlist3.append(reverseCard(colour))
#     return cardlist3

# def add_take2Card():
#     cardlist4 = []
#     for colour in ['yellow','blue','green','red']:
#         for i in range(2):
#             cardlist4.append(take2Card(colour))
#     return cardlist4

# def add_wildCard():
#     cardlist5 = []
#     for colour in ['yellow','blue','green','red']:
#         cardlist5.append(wildCard())
#     return cardlist5

# def add_wild4Card():
#     cardlist6 = []
#     for colour in ['yellow','blue','green','red']:
#         cardlist6.append(wild4Card())
#     return cardlist6







