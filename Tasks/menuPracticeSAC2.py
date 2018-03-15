
def EnterNewData():
    f = input("What file would you like to open: ")
    try:
        f = open(f,"a")
    except:
        f = open(f,"w")
    x = 0
    while x == 0:
        player = input('''  (To exit leave blank)
        Enter player name and scores seperated be spaces:''')
        if player == "":
            x = 1
        name = []
        scoreslist = []
        name.append(player[0])
        scores = player[1:].split(" ")
        scoreslist.append(scores)
        print(name)
        print(scoreslist)
    return

EnterNewData()


#Load previous data
#INPUT fileName
#OPEN ‘filename’ file for reading
#    FOR each line in fileName
#playerList <- playerName
#playerScores <-  gamescore1, gamescore2, gamescore3
#END FOR

#Search player
#position <- 0
#INPUT targetPlayer
#while position < length of playerList
#if playerList[position] >= targetValue then
#DISPLAY analyse(position)
#end if
#position <- position + 1
#end while

#Function to analyse
#gamesPlayed <- number of scores in playerScore list
#otalScore <- sum of playerScores
#ppg <- totalScore / numberofgames
#maxScore <- maximum of playerScores
#positionppg <- index(max(ppgList))
#DISPLAY player, ppg, totalScore, (listLength-1)
