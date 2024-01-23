import pygame
from pygame.locals import *
from Path import *
from PIL import Image
import torchvision.transforms as transforms


class Cxolor():
    def __init__(self,color):
        # self.colorList = ['yellow','blue','green','red']
        self.color = color
        self.image = pygame.image.load(f'images/Buttons/changeColor/{self.color}.png')
        # self.image = pygame.image.load(f'images/Buttons/changeColor/{self.color}_resize.png')
        self.rect = self.image.get_rect()

        self.img_path = f'images/Buttons/changeColor/{self.color}.png'
        self.img0 = Image.open(self.img_path)
        self.img  = self.img0.resize((50,50),Image.BILINEAR)
    
    def bt_Resize(self):
        self.resizePath = f"images/Buttons/changeColor/{self.color}_resize.png"
        self.img.save(self.resizePath, 'PNG')

    def drawColor(self,screen,x,y):
        self.bt_Resize()
        self.image = pygame.image.load(self.resizePath) # .convert():  # 别用“.convert()”！！！要不然有阴影！！！
        # screen.blit(self.bt_img ,self.pos)
        
        self.rect.left = x
        self.rect.top = y
        screen.blit(self.image,self.rect)



    # def drawColor(self,screen,x,y): #,color): 
    #     self.rect.left = x
    #     self.rect.top = y
    #     screen.blit(self.image,self.rect)
    #     screen.blit(self.image,(x,y))

    def click(self,position):
            if self.rect.collidepoint(position): #测试一个点是否在矩形内(bool)
                print("Change Color: Yes! ")
                return True
            else:
                return  False

class changeColor:
    def __init__(self,colorList):
        self.color_List = colorList

    def show(self,screen,x,y): 
        i = 0
        for c in self.color_List:
            c.drawColor(screen,x+i*66,y)
            i += 1
        pass

    


# class changeColor:
#     # def __init__(self,):
#     #     self.colorList = ['yellow','blue','green','red']
#     #     # self.rect = self.image.get_rect()

#     #     # self.image = pygame.image.load(f'images/Buttons/changeColor/{self.colour}.png')
#     def show(self,screen,x,y): 
#             i = 0
#             for c in self.colorList: 
#                 c.drawColor(screen,x+i*70,y, c)
#                 i += 1
#             pass  

#     # def drawColor(self,screen,x,y,color): 
#     #     # self.rect.left = x
#     #     # self.rect.top = y
#     #     self.image = pygame.image.load(f'images/Buttons/changeColor/{color}.png')
#     #     # self.rect = self.image.get_rect()
#     #     # screen.blit(self.image,self.rect)
#     #     screen.blit(self.image,(x,y))
    
#     def click(self,position):
#             if self.rect.collidepoint(position): #测试一个点是否在矩形内(bool)
#                 print("Change Color: Yes! ")
#                 return True
#             else:
#                 return  False

    # p = Player()
    # p.playerHand = []
    # p.showHand(x,y)


