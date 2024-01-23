from choosecolor import *
def playeractstep1(player,lastcolor,lastnumber,chosecard,pile,discardpile,whichplayer,needtakecardnumber):
    discardpile.discardlist.append(chosecard)
    player.playerHand.remove(chosecard)
    lastcolor=chosecard.colour
    lastnumber=chosecard.number
    if chosecard.number == 12:
        needtakecardnumber = 2
    if chosecard.number == 15:
        needtakecardnumber = 4
        lastcolor = choosecolor()
    whichplayer=1
    return lastcolor,lastnumber,discardpile,whichplayer,needtakecardnumber

def playeractstep2(player,lastcolor,lastnumber,chosecard,pile,discardpile,whichplayer,clockwise,needtakecardnumber,humancanput):
    if (lastnumber in range(10)) or lastnumber==99:
        if chosecard.colour==lastcolor or chosecard.number==lastnumber or chosecard.colour=="black":
            humancanput=True
            discardpile.discardlist.append(chosecard)
            player.playerHand.remove(chosecard)
            lastcolor=chosecard.colour
            lastnumber=chosecard.number
            if chosecard.number != 13:
                if chosecard.number==11:
                    clockwise=clockwise*(-1)
                if chosecard.number==12:
                    needtakecardnumber=2
                if chosecard.number==14:
                    lastcolor=choosecolor()
                if chosecard.number==15:
                    needtakecardnumber=4
                    lastcolor=choosecolor()
                if clockwise==1:
                    whichplayer=1
                else:
                    whichplayer=(-1)
            else:
                if clockwise==1:
                    whichplayer+=2
                else:
                    whichplayer-=2
    else:
        if lastnumber==11 or lastnumber==13:
            if chosecard.colour == lastcolor or chosecard.number == lastnumber or chosecard.number==14 or chosecard.number==15:
                humancanput = True
                discardpile.discardlist.append(chosecard)
                player.playerHand.remove(chosecard)
                lastcolor = chosecard.colour
                lastnumber = chosecard.number
                if chosecard.number != 13:
                    if chosecard.number == 11:
                        clockwise = clockwise * (-1)
                    if chosecard.number == 12:
                        needtakecardnumber = 2
                    if chosecard.number == 14:
                        lastcolor = choosecolor()
                    if chosecard.number == 15:
                        needtakecardnumber = 4
                        lastcolor = choosecolor()
                    if clockwise == 1:
                        whichplayer = 1
                    else:
                        whichplayer = (-1)
                else:
                    if clockwise == 1:
                        whichplayer += 2
                    else:
                        whichplayer -= 2
        if lastnumber==12:
            if chosecard.number==12:
                humancanput = True
                discardpile.discardlist.append(chosecard)
                player.playerHand.remove(chosecard)
                lastcolor = chosecard.colour
                lastnumber = chosecard.number
                needtakecardnumber=2
                if clockwise == 1:
                    whichplayer = 1
                else:
                    whichplayer = (-1)
            if chosecard.number==14:
                humancanput = True
                discardpile.discardlist.append(chosecard)
                player.playerHand.remove(chosecard)
                lastcolor = choosecolor()
                lastnumber = chosecard.number
                if clockwise == 1:
                    whichplayer = 1
                else:
                    whichplayer = (-1)
            if chosecard.number==15:
                humancanput = True
                discardpile.discardlist.append(chosecard)
                player.playerHand.remove(chosecard)
                needtakecardnumber=4
                lastcolor = choosecolor()
                lastnumber = chosecard.number
                if clockwise == 1:
                    whichplayer = 1
                else:
                    whichplayer = (-1)

        if lastnumber==14:
            if chosecard.colour==lastcolor:
                humancanput = True
                discardpile.discardlist.append(chosecard)
                player.playerHand.remove(chosecard)
                lastcolor = chosecard.colour
                lastnumber = chosecard.number
                if chosecard.number != 13:
                    if chosecard.number == 11:
                        clockwise = clockwise * (-1)
                    if chosecard.number == 12:
                        needtakecardnumber = 2
                    if chosecard.number == 14:
                        lastcolor = choosecolor()
                    if chosecard.number == 15:
                        needtakecardnumber = 4
                        lastcolor = choosecolor()
                    if clockwise == 1:
                        whichplayer = 1
                    else:
                        whichplayer = (-1)
                else:
                    if clockwise == 1:
                        whichplayer += 2
                    else:
                        whichplayer -= 2
        if lastnumber==15:
            if chosecard.number==14:
                humancanput = True
                discardpile.discardlist.append(chosecard)
                player.playerHand.remove(chosecard)
                lastcolor = choosecolor()
                lastnumber = chosecard.number
                if clockwise == 1:
                    whichplayer = 1
                else:
                    whichplayer = (-1)
            if chosecard.number==15:
                humancanput = True
                discardpile.discardlist.append(chosecard)
                player.playerHand.remove(chosecard)
                lastnumber = chosecard.number
                needtakecardnumber = 4
                lastcolor = choosecolor()
            if clockwise == 1:
                whichplayer = 1
            else:
                whichplayer = (-1)

    return lastcolor,lastnumber,discardpile,whichplayer,clockwise,needtakecardnumber,humancanput


def specialcardturn(player,pile,needtakenumber,clockwise1,whichplayer1):
    player.get_Handcard(needtakenumber,pile)
    needtakenumber=1
    if clockwise1 == 1:
        whichplayer1 = 1
    else:
        whichplayer1 = (-1)
    return needtakenumber,clockwise1,whichplayer1



