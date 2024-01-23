import pygame
from pygame.locals import *
from Path import *
from Board import *
from Button import *
import sys
import globals

class ai_Menu:
    def __init__(self, AI_num):
        pygame.display.set_caption("UNO AI Menu")



# globals.AI_num = 0

pygame.init()

# pygame.display.set_caption("UNO AI Menu")

screen = pygame.display.set_mode((1280,740))
#bg_img_path=getPath("images","BGs","bg_start1.png")
bg = pygame.image.load(f'images/BGs/ai_menu.jpeg')
bg= pygame.transform.scale(bg,(1280,740))

pygame.display.update()

ai1Button = Button("3_player", 490,270, 300, 100)
ai2Button = Button("2_player", 490,420, 300, 100)
ai3Button = Button("1_player", 490,570, 300, 100)
# ai1Button = Button("AI1", 490,270, 300, 100)
# ai2Button = Button("AI2", 490,420, 300, 100)
# ai3Button =Button ("AI3", 490,570, 300, 100)

# aiMenu = AI_Menu() \\


# Main loop of the game - checking for new events and rendering the window picture

def AIMenu(ActMenu):
    aiMenu = ai_Menu()

    while(True):
            screen.blit(bg,(0,0))
            
            ai1Button.draw_button(screen)
            ai2Button.draw_button(screen)
            ai3Button.draw_button(screen)

            # ActMenu="AIMenu"
            

            for event in pygame.event.get(): 
                if(event.type == pygame.QUIT): 
                    pygame.quit()
                    sys.exit()
                
                #check if the mouse is hovering over the buttons 
                #and adding a  hovering color 
                if(event.type == pygame.MOUSEMOTION):
                    if( ai1Button.rect.collidepoint(pygame.mouse.get_pos())):
                        print("pygame.mouse.get_pos()): ", pygame.mouse.get_pos())
                        print("PlayButton.rect: ", ai1Button.rect)
                        ai1Button.set_hover(True)
                        ai1Button.set_grey(screen)
                        
                    else : 
                        ai1Button.set_hover(False)
                        ai1Button.set_grey(screen)
                    
                    if( ai2Button.rect.collidepoint(pygame.mouse.get_pos())):
                        ai2Button.set_hover(True)
                        ai2Button.set_grey(screen)
                    else : 
                        ai2Button.set_hover(False)
                        ai2Button.set_grey(screen)
                    
                    if( ai3Button.rect.collidepoint(pygame.mouse.get_pos())):
                        ai3Button.set_hover(True)
                        ai3Button.set_grey(screen)
                    else : 
                        ai3Button.set_hover(False)
                        ai3Button.set_grey(screen) 
                
            
                if( event.type == pygame.MOUSEBUTTONDOWN):
                
                    if( ai1Button.rect.collidepoint(pygame.mouse.get_pos())and ActMenu=="AIMenu" ):
                        print ("AI1")
                        ActMenu="PlayBoard"
                        # Board().AI_num = 1
                        globals.AI_num = 1
                        board(ActMenu) 
                        ##################??????????????????????########################


                    if( ai2Button.rect.collidepoint(pygame.mouse.get_pos()) and ActMenu=="AIMenu"):
                        print ("AI2")
                        ActMenu="PlayBoard"
                        globals.AI_num = 2
                        board(ActMenu) 
                        # Board().AI_num = 2
                        # GameRules(ActMenu)
                        # AImenu()
                        # if( ai1Button.rect.collidepoint(pygame.mouse.get_pos()) and ActMenu=="AIMenu"):
                        #     Board().AI_num = 
                        
                    if (ai3Button.rect.collidepoint(pygame.mouse.get_pos()) and ActMenu=="AIMenu" ):
                        print ("AI3")
                        ActMenu="PlayBoard"
                        globals.AI_num = 3
                        board(ActMenu) 
                        # Board().AI_num = 3
           
            
            # Render the picture on the screen
            pygame.display.flip()
            
            # Slow down the main loop
            # pygame.time.wait(20)
                
    # pygame.quit()