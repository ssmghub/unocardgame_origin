import pygame
from pygame.locals import *
from Path import *
from PIL import Image
import torchvision.transforms as transforms

class Button() :  
    hover = False

    def __init__(self,name,x,y,w,h):
        self.name = name
        # self.font = pygame.font.SysFont("Chalkboard SE",self.size)
        self.x = x 
        self.y = y 
        self.w = w
        self.h = h
        self.rect = pygame.Rect((self.x,self.y),(self.w,self.h))   
        self.pos =(self.x, self.y)
        # self.rect = (0,0)

    # def draw_button(self,screen):
    #     self.resizePath = getPath("images","Buttons","blue",f"{self.name}_resize.png")
    #     self.bt_img = pygame.image.load(self.resizePath)
    #     # self.bt_img = pygame.image.load(self.resizePath).convert()
    #     screen.blit(self.bt_img ,self.pos)
   
    def bt_Resize(self):
        self.img_path = getPath("images","Buttons","blue",f"{self.name}.png")
        self.img0 = Image.open(self.img_path)
        self.img  = self.img0.resize((self.w,self.h),Image.BILINEAR)
        # self.img  = self.img0.resize((300,100),Image.BILINEAR)
        self.resizePath = getPath("images","Buttons","blue",f"{self.name}_resize.png")
        self.img.save(self.resizePath, 'PNG')

    def draw_button(self,screen):
        #drawinf the button 
        # if self.name == "start":
            # self.bt_img_path = getPath("images","Buttons","blue","start.png")
        # self.img_path = getPath("images","Buttons","blue",f"{self.name}.png")
        # self.img0 = Image.open(self.img_path)
        # self.img  = self.img0.resize((self.w,self.h),Image.BILINEAR)
        # # self.img  = self.img0.resize((300,100),Image.BILINEAR)
        # self.resizePath = getPath("images","Buttons","blue",f"{self.name}_resize.png")
        # self.img.save(self.resizePath, 'PNG')
        # elif self.name == "AI":
        #     self.img_path = getPath("images","Buttons","blue",f"{self.name}.png")
        #     self.img0 = Image.open(self.img_path)
        #     self.img  = self.img0.resize((300,100),Image.BILINEAR)
        #     self.resizePath = getPath("images","Buttons","blue",f"{self.name}_resize.png")
        #     self.img.save(self.resizePath, 'PNG')
        #     # self.bt_img_path = getPath("images","Buttons","blue","AI.png")
        # elif self.name == "exit":
        #     self.img_path = getPath("images","Buttons","blue",f"{self.name}.png")
        #     self.img0 = Image.open(self.img_path)
        #     self.img  = self.img0.resize((300,100),Image.BILINEAR)
        #     self.resizePath = getPath("images","Buttons","blue",f"{self.name}_resize.png")
        #     self.img.save(self.resizePath, 'PNG')
        #     # self.bt_img_path = getPath("images","Buttons","blue","exit.png")

        # bg_img_path=getPath("images","BGs","bg_start2.jpg")
        # bt0 = Image.open(self.bt_img_path)
        # bt  = bt0.resize((300,100))
        # resizePath = getPath('./images/BGs/bg_resize.jpg')
        # bg.save(resizePath, 'JPEG')
        # bt = pygame.image.load(resizePath).convert()
        
        self.bt_Resize()
        self.bt_img = pygame.image.load(self.resizePath) # DON'T USE "convert()", it will lead to SHADOW!!!
        # self.bt_img = pygame.image.load(self.resizePath).convert()
        # self.bt_img = pygame.image.load(self.bt_img_path).convert()
        # self.bt_img= pygame.transform.scale(self.bt_img,(300,100))
        # self.bt_img  = self.bt_img.resize((300,100),Image.BILINEAR)

        # self.rect = self.bt_img.get_rect()

        screen.blit(self.bt_img ,self.pos)

    
    
    #change color of the button when hovering over it 
    def set_grey(self,screen):
    # def set_color(self,screen):
        if Button.hover:
            # print("Hover")
            # self.color = (33, 236, 42)
            if self.name == "start":
                self.bt_img_path = getPath("images","Buttons","grey","start.png")
            elif self.name == "1_player":
                self.bt_img_path = getPath("images","Buttons","grey","1_player.png")
            elif self.name == "2_player":
                self.bt_img_path = getPath("images","Buttons","grey","2_player.png")
            elif self.name == "3_player":
                self.bt_img_path = getPath("images","Buttons","grey","3_player.png")
            elif self.name == "restart":
                self.bt_img_path = getPath("images", "Buttons", "grey", "restart.png")
            elif self.name == "menu":
                self.bt_img_path = getPath("images","Buttons","grey","menu.png")
            # elif self.name == "exit":
            else:
                self.bt_img_path = getPath("images","Buttons","grey","exit.png")
                
            self.bt_img = pygame.image.load(self.bt_img_path) # 别用“.convert()”！！！要不然有阴影！！！ 
            # self.bt_img = pygame.image.load(self.bt_img_path).convert() 
            self.bt_img= pygame.transform.scale(self.bt_img,(self.w,self.h))
            # self.bt_img= pygame.transform.scale(self.bt_img,(300,100))

            # self.rect = self.bt_img.get_rect()

            screen.blit(self.bt_img ,self.pos)
        else :
            # self.color=(255, 196, 0)
            self.draw_button(screen)

    
    def set_hover(self,bool):
        Button.hover = bool
    
    def get_hover(self):
        return Button.hover

