from Pile import *
from Card import *
from Player import *
#from UNO_button import *
import pygame
from Label import *
import globals


class AI_player():
    def __init__(self,score):
        self.hand_list = []  ##怎么获取当前AI手牌信息
        self.score=score

    # AI玩家回合开始 判断上一名玩家手牌数，如果手牌数=1 并且 没有报UNO，该AI玩家则喊UNO，上一名玩家多摸牌
    # 1. 首先要画出一个UNO键呈现在人类玩家桌面上。
    # 2. 当人类玩家没有按UNO键时返回no, 按了返回yes
    # 3. 每一轮AI玩家开始都要检测人类玩家手牌数，当人类玩家手牌数=1 而且 没有按UNO键的记录时，返回UNO警告，令人类玩家摸牌

    def Check_Uno_button(self, player, pile):  # 检查玩家是否按UNO键，没按就使其摸牌！
        if len(player.playerHand) == 1:
            if not player.ifuno:
                # 下一步：当人类玩家每按UNO按键时，屏幕显示警告并让玩家摸一张牌
                print("You don't shout UNO, please get 1 card from draw pile to you hand!")
                player.get_Handcard(4,pile)

    # AI player draw cards from the drawpile
    def get_card(self, number, pile):
        self.hand_list.extend(pile.DrawCard(number))
        return self.hand_list

    # judge AI whther has the same number/color card in his hand
    def Judge(self, discard_Pile, card, num, color):
        # Topcard = discard_Pile.show_topCard()

        # 判断AI是否能出牌
        if card.colour == color or card.number == num:
            return True

    # AI player play card
    def PlayCard(self, discardpile, ai, ltnumber, ltcolour, takenumber, pile_):
        eligible_card = []
        next_color = []
        canputflag = False
        color_list = ["red", "yellow", "blue", "green"]
        for card in self.hand_list:
            if ai.Judge(discardpile, card, ltnumber, ltcolour):
                print(card.number,card.colour,"yes")
                eligible_card.append(card)
                print(eligible_card)
                canputflag = True
        if canputflag:
            output_card = random.choice(eligible_card)
            print(output_card.colour,output_card.number)
            discardpile.discardlist.append(output_card)
            self.hand_list.remove(output_card)
            if output_card.number == 14 or output_card.number == 15:
                output_card.colour=random.choice(color_list)
            return output_card.number, output_card.colour, canputflag,discardpile,pile_

        else:
            ai.get_card(takenumber, pile_)


            return ltnumber, ltcolour, canputflag,discardpile,pile_

            # if isinstance(output_card, wildCard) or \
            #         isinstance(output_card, wild4Card):  # AI 打完wildcard之后要指定下一个玩家要出的颜色
            #     {
            #         next_color.append(random.choice(color_list))
            #     }

            # AI 打完wildcard之后要指定下一个玩家要出的颜色
            # 剩1张牌时 检查是否含UNO
            # 高级AI

    # ai1_score_label = Label(f'AI1 score: {globals.ai1score}', (495, 490), 60, 'black')

    # def show_left_AI_hand_card(self, screen, x, y):  # 这里在后面主流程函数调用这几个函数时，再给这几个函数的x y赋具体值
    #     i = 0
    #     j = 70
    #     if len(self.hand_list) < 14:
    #         for card in self.hand_list:
    #             card.drawBack(screen, x, y + i * 10)
    #             i += 1
    #     else:
    #         # part1 = self.playerHand[0,9]
    #         # part2 = self.playerHand[10,len(self.hand_list)]
    #         for m in range(7):
    #             self.hand_list[m].drawBack(screen, x - 50, y + i * 10)
    #             # card.drawCard(screen,x-50,y+j*70)
    #             i += 1
    #         j = 0
    #         for m in range(7, len(self.hand_list)):
    #             self.hand_list[m].drawBack(screen, x , y + j * 10)
    #             j += 1
    #
    # def show_top_AI_hand_card(self, screen, x, y):
    #     i = 0
    #     j = 0
    #     if len(self.hand_list) <= 7:
    #         for card in self.hand_list:
    #             card.drawBack(screen, x + i * 74, y)
    #             i += 1
    #     else:
    #         for m in range(7):
    #             self.hand_list[m].drawBack(screen, x + i * 74, y)
    #             i += 1
    #         for n in range(7, len(self.hand_list)):
    #             self.hand_list[n].drawBack(screen, x + j * 74, y + 30)
    #             j += 1
    #     # i = 0
    #     # j = 0
    #     # if len(self.hand_list) < 14:
    #     #     for card in self.hand_list:
    #     #         card.drawCard(screen, x + i * 70, y)
    #     #         i += 1
    #     # else:
    #     #     # part1 = self.playerHand[0,9]
    #     #     # part2 = self.playerHand[10,len(self.hand_list)]
    #     #     for m in range(7):
    #     #         self.hand_list[m].drawCard(screen, x + i * 70, y)
    #     #         # card.drawCard(screen,x+i*70,y+700)
    #     #         i += 1
    #     #     i = 0
    #     #     for m in range(7, len(self.hand_list)):
    #     #         self.hand_list[m].drawCard(screen, x + i * 70, y + 50)
    #     #         # card.drawCard(screen,x+i*70,y+750)
    #     #         i += 1
    #
    # def show_right_AI_hand_card(self, screen, x, y):
    #     i = 0
    #     j = 70
    #     if len(self.hand_list) < 14:
    #         for card in self.hand_list:
    #             card.drawBack(screen, x, y + i * 10)
    #             i -= 1
    #     else:
    #         # part1 = self.playerHand[0,9]
    #         # part2 = self.playerHand[10,len(self.hand_list)]
    #         for m in range(7):
    #             self.hand_list[m].drawBack(screen, x , y + i * 10)
    #             # card.drawCard(screen,x+700,y+j*10)
    #             i -= 1
    #         j = 70
    #         for m in range(7, len(self.hand_list)):
    #             self.hand_list[m].drawBack(screen, x, y + i * 10)
    #             i -= 1
    def show_AI_hand_card(self, screen, x, y):  # 这里在后面主流程函数调用这几个函数时，再给这几个函数的x y赋具体值
        i = 0
        j = 70
        if len(self.hand_list) <= 7:
            for card in self.hand_list:
                card.drawBack(screen, x, y + i * 50)
                # card.drawCard(screen, x+50, y-200 + i * 70)
                i += 1
        else:
            # part1 = self.playerHand[0,9]
            # part2 = self.playerHand[10,len(self.hand_list)]
            for m in range(7):
                # self.hand_list[m].drawCard(screen, x + 50, y-200 + i * 20)
                self.hand_list[m].drawBack(screen, x, y + i * 25)

                # card.drawCard(screen,x-50,y+j*70)
                i += 1
            j = 0
            for m in range(7, len(self.hand_list)):
                self.hand_list[m].drawBack(screen, x, y + 175 + j * 25)
                # self.hand_list[m].drawCard(screen, x + 50, y-200 + j * 20)
                j += 1

    def show_top_AI_hand_card(self, screen, x, y):
        i = 0
        j = 0
        if len(self.hand_list) <=7:
            for card in self.hand_list:
                card.drawBack(screen, x + i * 74, y)
                i += 1
        else:
            # part1 = self.playerHand[0,9]
            # part2 = self.playerHand[10,len(self.hand_list)]
            for m in range(7):
                self.hand_list[m].drawBack(screen, x + i * 74, y)
                # card.drawCard(screen,x+i*70,y+700)
                i += 1
            i = 0
            for m in range(7, len(self.hand_list)):
                self.hand_list[m].drawBack(screen, x + i * 74, y + 50)
                # card.drawCard(screen,x+i*70,y+750)
                i += 1

    # def show_right_AI_hand_card(self, screen, x, y):
    #     i = 0
    #     j = 70
    #     if len(self.hand_list) <=7:
    #         for card in self.hand_list:
    #             card.drawCard(screen, x, y + i * 70)
    #             i -= 1
    #     else:
    #         # part1 = self.playerHand[0,9]
    #         # part2 = self.playerHand[10,len(self.hand_list)]
    #         for m in range(7):
    #             self.hand_list[m].drawCard(screen, x, y + i * 35)
    #             # card.drawCard(screen,x+700,y+j*10)
    #             i -= 1
    #         j = 0
    #         for m in range(7, len(self.hand_list)):
    #             self.hand_list[m].drawCard(screen, x, y+245 + j * 35)
    #             i -= 1

    def specialplay(self,ai,pile,needtakenumber,clockwise1,whichplayer1,AI_num1):
        ai.get_card(needtakenumber,pile)
        needtakenumber=1
        if clockwise1 == 1:
            if whichplayer1 != AI_num1:
                whichplayer1 += 1
            else:
                whichplayer1 = 0
        else:
            if whichplayer1 != AI_num1 * (-1):
                whichplayer1 -= 1
            else:
                whichplayer1 = 0

        return needtakenumber,clockwise1,whichplayer1

    def finalscol(self,ai):
        return ai.score-len(ai.hand_list)



