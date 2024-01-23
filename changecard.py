def changecard(card,player,drawpail,discardpail):
    player.get_Handcard(1,drawpail)
    player.playerHand.remove(card)
    list1=[]
    list1.append(card)
    discardpail.discardlist=list1+discardpail.discardlist