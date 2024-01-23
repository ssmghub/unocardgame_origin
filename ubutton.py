# from pygame.locals import *
import pygame


# surface1 = pygame.display.set_mode((500,500))                                  #合并代码的时候可以删掉这两行
# surface1.fill((255,255,255))


class Check_uno_button:
    def __init__(self):
        #self.color = color
        self.x = 800
        self.y = 445
        #self.width = width
        #self.height = height
        #self.text = text

    def draw_button(self, screen):
        # pygame.draw.rect(surface1,"black",(self.x,self.y,self.width,self.height),0)
        # font = pygame.font.SysFont("Button",60)                                             #从系统中创造一个字体对象
        # text = font.render(self.text,1,"white","black")                                 #draw text on a new surface
        # picture = pygame.image.load('images/UNO_BUTTON.png')
        picture = pygame.image.load(f'images/MicrosoftTeams-image.png')
        screen.blit(picture, (self.x, self.y))
        # surface1.blit(picture,(self.x + (self.width / 2 - picture.get_width() / 2), \
        #     self.y + (self.height / 2 - picture.get_height() / 2)))

    def redrawwindow(self, screen):
        Check_uno_button.draw_button(screen, (0, 0, 0))

    # pos is the mouse position
    def press_button(self, pos):
        if pos[1] > self.x and pos[1] < (self.x + self.width):
            if pos[1] > self.y and pos[1] < (self.x + self.height):
                return True

                # 将是否按下按键这一动作集合，放在一个列表里
        # for event in pygame.event.get():
        #     pos1 = pygame.mouse.get_pos()
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         if button.press_button(pos1):
        #             print("clicked")
        #             clicked_list.append("clicked")
        #     else:  clicked_list.append("unclicked")
        #     if event.type == pygame.QUIT:                             #可以删掉
        #         run = False
        #         pygame.quit()
        #         quit()
        # return clicked_list


#run = True
#Whitebutton = Check_uno_button((0, 255, 0), 150, 225, 250, 100, 'Uno')
# while run:
#     Whitebutton.redrawwindow()
#     pygame.display.update()

    # for event in pygame.event.get():
    #         pos = pygame.mouse.get_pos()

    # if event.type == pygame.QUIT:                             #可以删掉
    #             run = False
    #             pygame.quit()
    #             quit()

    # if event.type == pygame.MOUSEBUTTONDOWN:
    #     if button.press_button(pos):
    #         print("clicked")
    #         clicked_list.append("clicked")
    # else:  clicked_list.append("unclicked")
    # #return clicked_list

    # 12月5日晚上 已经实现了基础AI功能 + 出wildcard后指定颜色 +检测玩家是否喊UNO ！
    # 下一步：
    # 1. 给朋友讲一下自己所写的代码的逻辑+函数+类
    # 2. 让朋友检查一下自己代码哪里有问题？
    # 3. 尝试运行代码，确保目前所写的部分无误

def unobuttonclick():
    flag1=True
    playerifuno=False
    while flag1:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                x,y = pygame.mouse.get_pos()
                if 890>=x>=800 and 485>=y >=445:
                    playerifuno=True
                    flag1=False
                else:
                    flag1=False
    return playerifuno

