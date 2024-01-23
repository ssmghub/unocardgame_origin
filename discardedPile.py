import pygame
from pygame.locals import *


class discardedPile:
    def __init__(self):  # ,x,y):
        # self.x = x
        # self.y = y
        self.dsP_img = pygame.image.load("images/discard_pile.png")
        self.dsP_img= pygame.transform.scale(self.dsP_img,(72,108))

        # self.rect = self.image.get_rect()
        # self.pos = (self.x, self.y)

    def drawDiscardPile(self,screen,x,y):
        # self.rect.left = self.x
        # self.rect.top = self.y
        # screen.blit(self.image,self.rect)
        screen.blit(self.dsP_img,(x,y))


#初始化丢弃牌堆 initialize discarded pile
    # dsP_img = pygame.image.load('images/discardPile.jpg')
    # dsP_img= pygame.transform.scale(dsP_img,(72,108))

    # current_screen.screen_image.blit(dsP_img,(680,300))
