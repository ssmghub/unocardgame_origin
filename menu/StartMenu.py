import pygame
from pygame.locals import *
from Path import *
import sys
from Board import *
from Button import *
# from menu.AI_Menu import *



pygame.init()
# pygame.display.set_caption("UNO Start Menu")

screen = pygame.display.set_mode((1280,740))
#bg_img_path=getPath("images","BGs","bg_start2.jpg")
bg = pygame.image.load(f'images/BGs/uno_snow.jpeg')
bg= pygame.transform.scale(bg,(1280,740))

class startMenuModule:
    def __init__(self):  
        pygame.display.set_caption("UNO Start Menu")
        # self.screen = pygame.display.set_mode((1280,740))
        # bg_img_path=getPath("UNO", "images","bg1.png")
        # bg_img_path=getPath("images","BGs","bg_start2.jpg")
        # bg = pygame.image.load(bg_img_path)
        # bg= pygame.transform.scale(bg,(1280,740))
        # self.screen.blit(bg,(0,0))
        # pygame.display.flip()
        # pygame.display.update()  



#Creating the Buttons 
PlayButton = Button("start", 490 ,521, 300, 100)

# Main loop of the game - checking for new events and rendering the window picture

def startMenu(ActMenu):
    while(True):

        # pygame.init()
        # pygame.display.set_caption("UNO Start Menu")

        # screen = pygame.display.set_mode((1280,740))
        # bg_img_path=getPath("images","BGs","bg_start2.jpg")
        # bg = pygame.image.load(bg_img_path)
        # bg= pygame.transform.scale(bg,(1280,740))

        # PlayButton = Button("start", 90 ,521, 300, 100)
        # AIButton = Button("AI", 490 ,521, 300, 100)
        # ExitButton =Button ("exit", 890 ,521, 300, 100)

        startMenuScreen = startMenuModule()
        # screen = startMenuScreen.screen

        screen.blit(bg,(0,0))

        PlayButton.draw_button(screen)

        ActMenu="MainMenu"
        
        # sprint(PlayButton.get_hover())

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            
            #check if the mouse is hovering over the buttons 
            #and changing a hovering color 
            if(event.type == pygame.MOUSEMOTION):
                if( PlayButton.rect.collidepoint(pygame.mouse.get_pos())):
                    # print("pygame.mouse.get_pos()): ", pygame.mouse.get_pos())
                    # print("PlayButton.rect: ", PlayButton.rect)
                    PlayButton.set_hover(True)
                    PlayButton.set_grey(screen)
                    
                else : 
                    PlayButton.set_hover(False)
                    PlayButton.set_grey(screen)
                
                # if( AIButton.rect.collidepoint(pygame.mouse.get_pos())):
                #     AIButton.set_hover(True)
                #     AIButton.set_grey(screen)
                # else :
                #     AIButton.set_hover(False)
                #     AIButton.set_grey(screen)
                #
                # if( ExitButton.rect.collidepoint(pygame.mouse.get_pos())):
                #     ExitButton.set_hover(True)
                #     ExitButton.set_grey(screen)
                # else :
                #     ExitButton.set_hover(False)
                #     ExitButton.set_grey(screen)
                #
        
            if( event.type == pygame.MOUSEBUTTONDOWN):
            
                if( PlayButton.rect.collidepoint(pygame.mouse.get_pos())and ActMenu=="MainMenu" ):
                    print ("Play")
                    ActMenu="PlayBoard"
                    board(ActMenu) 
                    ##################??????????????????????########################


                # if( AIButton.rect.collidepoint(pygame.mouse.get_pos()) and ActMenu=="MainMenu"):
                #         print ("AI Menu")
                #         ActMenu ="AIMenu"
                #         AIMenu(ActMenu)
                #         # if( AI1Button.rect.collidepoint(pygame.mouse.get_pos()) and ActMenu=="AIMenu"):
                #         #     Board().AI_num =
                #
                # if (ExitButton.rect.collidepoint(pygame.mouse.get_pos()) and ActMenu=="MainMenu" ):
                #         print ("Exit")
                #         # quiting the game with the exit button
                #         pygame.quit()
                #         sys.exit()

        
        # PlayButton.draw_text(screen ,(0,0,0),(250,550))  
        # AIButton.draw_text(screen ,(0,0,0),(650,550))
        # ExitButton.draw_text(screen,(0,0,0),(1050,550))
        
        # PlayButton.draw_button(screen)
        # AIButton.draw_button(screen)
        # ExitButton.draw_button(screen)
        
        
        # Render the picture on the screen
        pygame.display.flip()
        
        # Slow down the main loop
        # pygame.time.wait(20)
            
    # pygame.quit()