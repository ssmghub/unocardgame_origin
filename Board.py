import time

import pygame
from pygame.locals import *
import random
import sys
from Card import *
from Player import *
from Pile import *
from Path import *
import globals
from changeColor import *
from Label import *
from AI_class import *
from playeract import *
from whosturn import *
from changecard import *
from ubutton import *
from menu import WinEndMenu
from menu import LoseEndMenu
from menu import StartMenu
from clocktime import *
from Button import *

# 三原色
bg_color1 = (0,128,128)
bg_color2 = (60,60,60)
bg_color3 = (255,0,0)


def add_All():
    cardlist = []
    for colour in ['yellow','blue','green','red']:
        for _ in range(2): ###
            for i in range(1,10):
                cardlist.append(Card(colour, i))
            cardlist.append(Card(colour,11)) #reverseCard
            cardlist.append(Card(colour,12)) #take2Card
            cardlist.append(Card(colour,13)) #skipcard
            cardlist.append(Card(colour,0))
    for i in range(4): 
        cardlist.append(Card("black",14)) #wildCard
        cardlist.append(Card("black",15)) #wild4Card
    return cardlist

# 初始化 pygame
pygame.init()
screen = pygame.display.set_mode((1280,740))
bg = pygame.image.load(f'images/BGs/play_bg.jpg') #.convert()
bg= pygame.transform.scale(bg,(1280,740))

# pygame.draw.rect(bg, (255, 255, 255), (150, 350, 50, 50))#left
# pygame.draw.rect(bg, (255, 255, 255), (600, 200, 50, 50))#top
# pygame.draw.rect(bg, (255, 255, 255), (900, 350, 50, 50))#right
pygame.draw.rect(bg, (255, 255, 255), (400, 450, 50, 50))#human


class boardModule():
    def __init__(self):
        # self.screen_image = pygame.display.set_mode((1280,740))
        # 窗口标题
        pygame.display.set_caption('UNO Play Board')


def board(actmenu):
    ActMenu = actmenu
    
    ActMenu=="PlayBoard"

    current_screen = boardModule()

    MenuButton = Button("home_left", 25, 13, 66, 66)
    ExitButton = Button("exit_small", 1189, 13, 66, 66)

    pile = Pile(add_All())
    pile.shuffle() 
    AI_num=globals.AI_num
    player1 = Player(1,100)
    playerlist = ["player1"]
    for i in range(AI_num):
        playerlist.append("ai" + str(i + 1))
    ai1 = AI_player(100)
    ai2 = AI_player(100)
    ai3 = AI_player(100)
    discard = discard_Pile(pile)
    for p in playerlist:
        if p == "player1":
            player1.get_Handcard(8, pile)
            #player1.showHand(bg, 20, 400)
        if p == "ai1":
            ai1.get_card(7, pile)
            #ai1.show_left_AI_hand_card(bg,50,300)
        if p == "ai2":
            ai2.get_card(7, pile)
            #ai2.show_top_AI_hand_card(bg,470,50)
            # ai2.showHand(current_screen.screen_image, 20, 100)
        if p == "ai3":
            ai3.get_card(7, pile)
            #ai3.show_right_AI_hand_card(bg,1000,300)

    discardpicture= Card("discard","pile")#需改成玩家出牌类似的图片
    # discardpicture= Card("black",15)#需改成玩家出牌类似的图片
    discardpicture.image= pygame.transform.scale(discardpicture.image,(72,108))

    drawpile = draw_Pile(pile.deck)

    colors = ['yellow','blue','green','red']
    color_List = []
    for c in colors:
        color_List.append(Cxolor(c))
    unobutton=Check_uno_button()
    x = changeColor(color_List)
    x.show(bg, 515, 445)

    # changecolor.show(screen,0,0)

    def repage():
        discardpicture.drawCard(screen, 680, 300)
        drawpile.deck[0].drawBack(screen, 530, 300)
        player1.showHand(screen, 383, 510)
        # player1.showHand(screen, 395, 545)
        ai1.show_AI_hand_card(screen, 80, 184)
        # ai1.show_AI_hand_card(screen, 50, 300)
        ai2.show_top_AI_hand_card(screen, 383, 35)
        # ai2.show_top_AI_hand_card(screen, 395, 70)
        ai3.show_AI_hand_card(screen, 1128, 184)
#        changecolor.show(screen, 515, 445)

    needtakecardnumber=1 #下家累计需要摸牌数
    clockwise=1#出牌顺序方向
    whichplayer=0 #直接代表ordernum
    #unobotton=Check_uno_button()
    lastcolor=""
    lastnumber=999
    canputflag = True
    humancanputflag = False
    changecardflag=True
    choosecolorflag=True
    # lable1=Label("1111", (535,250),25,"black")
    # lable2=Label("22222", (535,250),25,"black")
    while True:
        if ActMenu=="PlayBoard":
            screen.blit(bg, (0,0))

            MenuButton.draw_button(screen)
            ExitButton.draw_button(screen)
            if len(pile.deck)==0:
                globals.score = len(player1.playerHand)
                globals.ai1score = len(ai1.hand_list)
                globals.ai2score = len(ai2.hand_list)
                globals.ai3score = len(ai3.hand_list)
                LoseEndMenu.loseEndMenu("Lose")
            else:
                if playerlist[whichplayer] == "player1":
                    pygame.draw.rect(bg, (0, 255, 255), (400, 450, 50, 50))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                        if lastcolor == "" and lastnumber == 999:
                            # lable1.draw(screen)
                            if event.type == pygame.MOUSEBUTTONUP:
                                spot = pygame.mouse.get_pos()
                                mpositionx, mpositiony = pygame.mouse.get_pos()
                                for card in player1.playerHand:
                                    if card.click(spot):
                                        lastcolor, lastnumber, discard, whichplayer,needtakecardnumber = playeractstep1(player1, lastcolor,
                                                                                                     lastnumber, card, pile,
                                                                                                     discard, whichplayer,needtakecardnumber)
                                        pygame.draw.rect(bg, (255, 255, 255), (400, 450, 50, 50))
                                if 25 <= mpositionx <= 91 and 13 <= mpositiony <= 79:
                                    ActMenu = "MainMenu"
                                    StartMenu.startMenu(ActMenu)
                                if 1189 <= mpositionx <= 1255 and 13 <= mpositiony <= 79:
                                    print("Exit")
                                    pygame.quit()
                                    sys.exit()
                        elif lastnumber==12 or lastnumber==15:
                            needtakecardnumber,clockwise,whichplayer=specialcardturn(player1,pile,needtakecardnumber,clockwise,whichplayer)
                            lastnumber=99
                            pygame.draw.rect(bg, (255, 255, 255), (400, 450, 50, 50))
                        else:
                            if changecardflag:
                                # lable2.draw(screen)
                                if event.type==pygame.MOUSEBUTTONUP:
                                    spot = pygame.mouse.get_pos()
                                    mpositionx, mpositiony = pygame.mouse.get_pos()
                                    for card in player1.playerHand:
                                        if card.click(spot):
                                            changecard(card,player1,pile,discard)
                                            changecardflag=False
                                    if 25 <= mpositionx <= 91 and 13 <= mpositiony <= 79:
                                        ActMenu = "MainMenu"
                                        StartMenu.startMenu(ActMenu)
                                    if 1189 <= mpositionx <= 1255 and 13 <= mpositiony <= 79:
                                        print("Exit")
                                        pygame.quit()
                                        sys.exit()
                            if not changecardflag:
                                # lable1.draw(screen)
                                if event.type == pygame.MOUSEBUTTONUP:
                                    spot = pygame.mouse.get_pos()
                                    mpositionx, mpositiony = pygame.mouse.get_pos()
                                    if len(player1.playerHand)>2 or len(player1.playerHand)==1:
                                        for card in player1.playerHand:
                                            if card.click(spot):
                                                print(card.number, card.colour)
                                                lastcolor, lastnumber, discard, whichplayer, clockwise, needtakecardnumber,humancanputflag = playeractstep2(
                                                    player1, lastcolor, lastnumber, card, pile, discard, whichplayer, clockwise,
                                                    needtakecardnumber,humancanputflag)
                                                player1.ifuno=False
                                                pygame.draw.rect(bg, (255, 255, 255), (400, 450, 50, 50))
                                        if 25 <= mpositionx <= 91 and 13 <= mpositiony <= 79:
                                            ActMenu = "MainMenu"
                                            StartMenu.startMenu(ActMenu)
                                        if 1189 <= mpositionx <= 1255 and 13 <= mpositiony <= 79:
                                            print("Exit")
                                            pygame.quit()
                                            sys.exit()
                                        if humancanputflag:
                                            changecardflag = True
                                        if mpositionx <= 602 and mpositionx>=530 and mpositiony <= 402 and mpositiony>=300:  # 摸牌区域（数值还需调整）
                                            #card_0=pile.takecard_0()
                                            if len(player1.playerHand)==1:
                                                needtakecardnumber = 1
                                                if clockwise==1:
                                                    whichplayer = 1
                                                else:
                                                    whichplayer=(-1)
                                                humancanputflag = True
                                                player1.ifuno = False
                                            else:
                                                player1.get_Handcard(needtakecardnumber, pile)
                                                needtakecardnumber = 1
                                                if clockwise == 1:
                                                    whichplayer = 1
                                                else:
                                                    whichplayer = (-1)
                                                humancanputflag=True
                                                player1.ifuno=False
                                    if len(player1.playerHand)==2:
                                        for card in player1.playerHand:
                                            if card.click(spot):
                                                print(card.number, card.colour)
                                                player1.ifuno = unobuttonclick()
                                                lastcolor, lastnumber, discard, whichplayer, clockwise, needtakecardnumber,humancanputflag = playeractstep2(
                                                    player1, lastcolor, lastnumber, card, pile, discard, whichplayer, clockwise,
                                                    needtakecardnumber,humancanputflag)
                                                pygame.draw.rect(bg, (255, 255, 255), (400, 450, 50, 50))
                                        if 25 <= mpositionx <= 91 and 13 <= mpositiony <= 79:
                                            ActMenu = "MainMenu"
                                            StartMenu.startMenu(ActMenu)
                                        if 1189 <= mpositionx <= 1255 and 13 <= mpositiony <= 79:
                                            print("Exit")
                                            pygame.quit()
                                            sys.exit()
                                        if mpositionx <= 602 and mpositionx>=530 and mpositiony <= 402 and mpositiony>=300:  # 摸牌区域（数值还需调整）
                                            #card_0=pile.takecard_0()
                                            player1.get_Handcard(needtakecardnumber, pile)
                                            needtakecardnumber = 1
                                            whichplayer = 1
                                            humancanputflag=True
                                            player1.ifuno=False
                                            pygame.draw.rect(bg, (255, 255, 255), (400, 450, 50, 50))

                                if humancanputflag:
                                    changecardflag = True
                                    humancanputflag=False
                    #repage()
                    #pygame.display.flip()

                elif (playerlist[whichplayer] == "ai1"):

                    #second_1()# left
                    #time.sleep(1)
                    pygame.time.wait(1000)
                    ai1.Check_Uno_button(player1,pile)
                    if lastnumber==12 or lastnumber==15:
                        needtakecardnumber,clockwise,whichplayer=ai1.specialplay(ai1,pile,needtakecardnumber,clockwise,whichplayer,AI_num)
                        lastnumber=99
                    else:
                        lastnumber, lastcolor, canputflag, discard, pile = ai1.PlayCard(discard, ai1, lastnumber, lastcolor,needtakecardnumber, pile)
                        whichplayer, clockwise, needtakecardnumber = whosturn(lastnumber, whichplayer, clockwise,canputflag, AI_num, needtakecardnumber)
                        discardpicture = discard.show_topCard()
                    #repage()
                    #pygame.display.flip()
                    #pygame.display.flip()
                    #ai1.show_left_AI_hand_card(screen, 50, 300)

                elif (playerlist[whichplayer] == "ai2"):

                    ai2.Check_Uno_button(player1, pile)
                    #time.sleep(1)
                    #second_1()
                    pygame.time.wait(1000)
                    if lastnumber==12 or lastnumber==15:
                        needtakecardnumber,clockwise,whichplayer=ai2.specialplay(ai2,pile,needtakecardnumber,clockwise,whichplayer,AI_num)
                        lastnumber=99

                    else:
                        lastnumber, lastcolor, canputflag, discard, pile = ai2.PlayCard(discard, ai2, lastnumber, lastcolor,needtakecardnumber, pile)
                        whichplayer, clockwise, needtakecardnumber = whosturn(lastnumber, whichplayer, clockwise,
                                                                              canputflag, AI_num, needtakecardnumber)
                        discardpicture = discard.show_topCard()
                    #repage()
                    #pygame.display.flip()
                    #pygame.display.flip()
                    #ai2.show_top_AI_hand_card(screen, 395, 70)

                elif (playerlist[whichplayer] == "ai3"):

                    ai3.Check_Uno_button(player1, pile)
                    #time.sleep(1)
                    #second_1()
                    pygame.time.wait(1000)
                    if lastnumber==12 or lastnumber==15:
                        needtakecardnumber,clockwise,whichplayer=ai3.specialplay(ai3,pile,needtakecardnumber,clockwise,whichplayer,AI_num)
                        lastnumber=99
                    else:
                        lastnumber, lastcolor, canputflag, discard, pile = ai3.PlayCard(discard, ai3, lastnumber, lastcolor,
                                                                                        needtakecardnumber, pile)
                        whichplayer, clockwise, needtakecardnumber = whosturn(lastnumber, whichplayer, clockwise,
                                                                              canputflag, AI_num, needtakecardnumber)
                        discardpicture = discard.show_topCard()
                    #repage()
                    #pygame.display.flip()
                    #pygame.display.flip()
                    #ai3.show_right_AI_hand_card(screen, 1000, 300)

            repage()
            if changecardflag == True:
                # time.sleep(3)
                changeCard_flag_L1 = ""
                changeCard_flag_L2 = ""
                # changeCard_flag_L = "Please Change Your Card"
            else:
                changeCard_flag_L1 = "You have changed"
                changeCard_flag_L2 = "    your card"
                # changeCard_flag_L = ""

            # changeCard_flag_LabelTXT = changeCard_flag_L1
            changeCardLabel1 = Label(changeCard_flag_L1, (55, 596), 45, "black")
            changeCardLabel1.draw(screen)
            changeCardLabel2 = Label(changeCard_flag_L2, (55, 646), 45, "black")
            changeCardLabel2.draw(screen)

            unobutton.draw_button(screen)
            colorLabelTxt = "Current color is: "+ lastcolor
            colorLabel = Label(colorLabelTxt, (535,250),25,"black")
            colorLabel.draw(screen)
            # changecolor.show(screen, 515, 445)

            if len(player1.playerHand)==0:
                globals.score = len(player1.playerHand)
                globals.ai1score = len(ai1.hand_list)
                globals.ai2score = len(ai2.hand_list)
                globals.ai3score = len(ai3.hand_list)
                WinEndMenu.winEndMenu("Win",globals.score,globals.ai1score,globals.ai2score,globals.ai3score)
            if len(ai1.hand_list)==0 or len(ai2.hand_list)==0 or len(ai3.hand_list)==0:
                globals.score = len(player1.playerHand)
                globals.ai1score = len(ai1.hand_list)
                globals.ai2score = len(ai2.hand_list)
                globals.ai3score = len(ai3.hand_list)
                LoseEndMenu.loseEndMenu("Lose",globals.score,globals.ai1score,globals.ai2score,globals.ai3score)
        # changecolor.show(screen, 515, 445)

            # globals.score = player1.score
            # globals.score -= len(player1.playerHand)

        pygame.display.flip()