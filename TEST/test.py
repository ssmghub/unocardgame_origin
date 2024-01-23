from PIL import Image
# import PIL
import pygame
from pygame.locals import *
from Path import *
import torchvision.transforms as transforms
import sys

# path=getPath("images","Buttons","blue","AI.png")
# img = Image.open(path)
# img = img.resize((300,100))
# resizePath = getPath('./images/Buttons/blue/AI_resize.png')
# img.save(resizePath, 'PNG')
# img1=Image.open(resizePath)
# img1.show()
      
pygame.init()

pygame.display.set_caption("UNO")

screen = pygame.display.set_mode((1280,740))
bg_img_path=getPath("images","BGs","bg_start2.jpg")
bg = pygame.image.load(bg_img_path).convert()
print(bg.get_rect())

# bg0 = Image.open(bg_img_path)
# bg  = bg0.resize((1280,740))
# resizePath = getPath('./images/BGs/bg_resize.jpg')
# bg.save(resizePath, 'JPEG')
# bg = pygame.image.load(resizePath).convert()

while(True):
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()
    pygame.display.flip()

    # self.rect = self.bt_img.get_rect()