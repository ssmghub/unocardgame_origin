import pygame
from pygame.locals import *
from Path import *
from PIL import Image
import torchvision.transforms as transforms
class Resize:
    def __init__(self,name,x,y,w,h):
            self.name = name
            self.x = x 
            self.y = y 
            self.w = w
            self.h = h
            self.rect = pygame.Rect((self.x,self.y),(self.w,self.h))   
            self.pos =(self.x, self.y)
            # self.rect = (0,0)

    def bt_Resize(self,path1,path2,path3):
            self.img_path = getPath(path1,path2,path3, f"{self.name}.png")
            # self.img_path = getPath("images","Buttons","blue",f"{self.name}.png")
            self.img0 = Image.open(self.img_path)
            self.img  = self.img0.resize((self.w,self.h),Image.BILINEAR)
            self.resizePath = getPath(path1,path2,path3, f"{self.name}_resize.png")
            # self.resizePath = getPath("images","Buttons","blue",f"{self.name}_resize.png")
            self.img.save(self.resizePath, 'PNG')

    def draw_button(self,screen):
        self.bt_Resize()
        self.bt_img = pygame.image.load(self.resizePath).convert()
        screen.blit(self.bt_img ,self.pos)