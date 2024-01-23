def whosturn(lastnumber1,whichplayer1,clockwise1,canputflag1,AI_num1,needtakecardnumber1):
    if canputflag1:
        if lastnumber1 == 11:
            clockwise1 = clockwise1 * -1
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
        if lastnumber1 == 12:
            needtakecardnumber1 = 2
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
        if lastnumber1 == 13:
            if clockwise1 == 1:
                for i in range(2):
                    if whichplayer1 != AI_num1:
                        whichplayer1 += 1
                    else:
                        whichplayer1 = 0
            else:
                for i in range(2):
                    if whichplayer1 != AI_num1 * (-1):
                        whichplayer1 -= 1
                    else:
                        whichplayer1 = 0
        if lastnumber1 == 15:
            needtakecardnumber1=4
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
        if (lastnumber1 in range(10)) or (lastnumber1==14):
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
    else:
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
        needtakecardnumber1=1
    return whichplayer1,clockwise1,needtakecardnumber1