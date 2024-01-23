import pygame
def choosecolor():
    colors=""
    flag1=True
    while flag1:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                x,y = pygame.mouse.get_pos()
                if x>=515 and x <=565 and y>=445 and y<=495:
                #if x<50 and y <50:
                    colors="yellow"
                    flag1=False
                if x>=581 and x<=631 and y>=445 and y<=495:
                    colors="blue"
                    flag1=False
                if x >= 647 and x <= 697 and y >= 445 and y <= 495:
                    colors="green"
                    flag1=False
                if x >= 713 and x <= 763 and y >= 445 and y <= 495:
                    colors="red"
                    flag1=False
    return colors
