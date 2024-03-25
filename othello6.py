import sys; args=sys.argv[1:]
#Maggie Gao
LIMIT_AB=13
 
import random
import time
corner_idx = {0,7,56,63}
edge_idx = {1, 2, 3, 4, 5, 6, 8, #not include corners
15, 16, 23, 24, 31, 32, 39, 40,
47, 48, 55, 57, 58, 59, 60, 61, 62}
corneradj_idx = {1,6,8,9,14,15,62,57,55,54,48,49}
 
def setGlobals():
    global board,tokenToPlay,movesToPlay
    board = '.'*27 + "ox......xo" + '.'*27
    tokenToPlay = ''
    movesToPlay = []
 
def print_board(pzl):
    toret=""
    for i in range(0,64,8):
        toret+=pzl[i:i+8] + "\n"
    return toret

def print_boardast(pzl,tkn):
    toret=""
    for i in findMoves(pzl,tkn)[0]:
        pzl = pzl[0:i]+"*"+pzl[i+1:]

    for i in range(0,64,8):
        toret+=pzl[i:i+8] + "\n"
    return toret
 
def movesCondenseVer(moves):
    toret=""
    for move in moves:
        if move>=0:
            if move<10: toret+="_"+str(move)
            else:toret+=str(move)
    return toret
 
def playMoves(brd,tkn,moves):
    for move in moves:
        newbrd = makeMovePos(brd,move,tkn)
        tkn = "xo" [tkn=="x"]
        if newbrd==brd:
            newbrd = makeMovePos(brd,move,tkn)
            tkn = "xo" [tkn=="x"]
        brd = newbrd
    return brd
 
#idx//8 row
#idx%8 column
def findMoves(brd,tkn):
    positionsToPlay = set()
    positionsToPlayDict = {}
    if brd.find("x")==-1 or brd.find("o")==-1:
        return [positionsToPlay,positionsToPlayDict]
    tokenPositions = [idx for idx,ch in enumerate(brd) if ch =="."]
    if tkn=="x": notToken = "o"
    else: notToken="x"
    for idx in tokenPositions:
        rPoss,lPoss,uPoss,dPoss = True, True,True, True
        rudPoss, lddPoss,ludPoss, rddPoss = True,True,True,True
        if idx%8<6:
            r = idx+1
            while r>=0 and r<64 and brd[r]==notToken:
                if r%8==7:
                    rPoss = False
                    break
                r+=1
            if r>=0 and r<64 and r!= idx+1 and rPoss and brd[r]==tkn:
                if idx in positionsToPlayDict: positionsToPlayDict[idx].append("r")
                else: positionsToPlayDict[idx] = ["r"]
                positionsToPlay.add(idx)
        if idx%8>1:
            l = idx-1
            while l>=0 and l<64 and brd[l]==notToken:
                if l%8==0:
                    lPoss = False
                    break
                l-=1
            if l>=0 and l<64 and l!= idx-1 and lPoss and brd[l]==tkn:
                if idx in positionsToPlayDict: positionsToPlayDict[idx].append("l")
                else: positionsToPlayDict[idx] = ["l"]
                positionsToPlay.add(idx)
        if idx//8>1:
            u = idx-8
            while u>=0 and u<64 and brd[u]==notToken:
                if u//8==0:
                    uPoss = False
                    break
                u-=8
            if u>=0 and u<64 and u!= idx-8 and uPoss and brd[u]==tkn:
                if idx in positionsToPlayDict: positionsToPlayDict[idx].append("u")
                else: positionsToPlayDict[idx] = ["u"]
                positionsToPlay.add(idx)
        if idx//8<6:
            d = idx+8
            while d>=0 and d<64 and brd[d]==notToken:
                if d//8==0:
                    dPoss = False
                    break
                d+=8
            if d>=0 and d<64 and d!= idx+8 and dPoss and brd[d]==tkn:
                if idx in positionsToPlayDict: positionsToPlayDict[idx].append("d")
                else: positionsToPlayDict[idx] = ["d"]
                positionsToPlay.add(idx)
        if idx%8<6:
            rud = idx-7
            while rud>=0 and rud<64 and brd[rud]==notToken:
                if rud%8==7:
                    rudPoss = False
                    break
                rud-=7
            if rud>=0 and rud<64 and rud!= idx-7 and rudPoss and brd[rud]==tkn:
                if idx in positionsToPlayDict: positionsToPlayDict[idx].append("rud")
                else: positionsToPlayDict[idx] = ["rud"]
                positionsToPlay.add(idx)
        if idx%8>1:
            ldd = idx+7
            while ldd>=0 and ldd<64 and brd[ldd]==notToken:
                if ldd%8==0:
                    rudPoss = False
                    break
                ldd+=7
            if ldd>=0 and ldd<64 and ldd!= idx+7 and lddPoss and brd[ldd]==tkn:
                if idx in positionsToPlayDict: positionsToPlayDict[idx].append("ldd")
                else: positionsToPlayDict[idx] = ["ldd"]
                positionsToPlay.add(idx)
        if idx%8>1:
            lud = idx-9
            while lud>=0 and lud<64 and brd[lud]==notToken:
                if lud%8==0:
                    ludPoss = False
                    break
                lud-=9
            if lud>=0 and lud<64 and lud!= idx-9 and ludPoss and brd[lud]==tkn:
                if idx in positionsToPlayDict: positionsToPlayDict[idx].append("lud")
                else: positionsToPlayDict[idx] = ["lud"]
                positionsToPlay.add(idx)
        if idx%8<6:
            rdd = idx+9
            while rdd>=0 and rdd<64 and brd[rdd]==notToken:
                if rdd%8==7:
                    rudPoss = False
                    break
                rdd+=9
            if rdd>=0 and rdd<64 and rdd!= idx+9 and rddPoss and brd[rdd]==tkn:
                if idx in positionsToPlayDict: positionsToPlayDict[idx].append("rdd")
                else: positionsToPlayDict[idx] = ["rdd"]
                positionsToPlay.add(idx)
    return [positionsToPlay,positionsToPlayDict]
 
def makeMove(pzl,idx_r,directions,token):
    pzl = pzl[:idx_r] + token + pzl[idx_r+1:]
    for direc in directions:
        idx = idx_r
        if direc == "l": #went right so have to go left
            idx-=1
            while pzl[idx]!= token:
                pzl = pzl[:idx] + token + pzl[idx+1:]
                idx-=1
        if direc == "r":
            idx+=1
            while pzl[idx]!= token:
                pzl = pzl[:idx] + token + pzl[idx+1:]
                idx+=1
        if direc == "d":
            idx+=8
            while pzl[idx]!= token:
                pzl = pzl[:idx] + token + pzl[idx+1:]
                idx+=8
        if direc == "u":
            idx-=8
            while pzl[idx]!= token:
                pzl = pzl[:idx] + token + pzl[idx+1:]
                idx-=8
        if direc == "ldd":
            idx+=7
            while pzl[idx]!= token:
                pzl = pzl[:idx] + token + pzl[idx+1:]
                idx+=7
        if direc == "rdd":
            idx+=9
            while pzl[idx]!= token:
                pzl = pzl[:idx] + token + pzl[idx+1:]
                idx+=9
        if direc == "lud":
            idx-=9
            while pzl[idx]!= token:
                pzl = pzl[:idx] + token + pzl[idx+1:]
                idx-=9
        if direc == "rud":
            idx-=7
            while pzl[idx]!= token:
                pzl = pzl[:idx] + token + pzl[idx+1:]
                idx-=7
    return pzl
 
def quickMove(brd,tkn): #find best move    
    movesList = findMoves(brd,tkn)
    positionsToPlay = movesList[0]
    positionsToPlayDict = movesList[1]
    nottkn = "xo"[tkn=="x"]
    if len(positionsToPlay)==0: return -1
    toRet=-1
    #corner
    if len(corner_idx.intersection(positionsToPlay))>0:
        temp_count = -65
        scoreDiff = 0
        for idx in corner_idx.intersection(positionsToPlay):
            mademove = makeMove(brd,idx,positionsToPlayDict[idx],tkn)
            scoreDiff = negScore(mademove,tkn)
            if scoreDiff>temp_count:
                temp_count = scoreDiff
                toRet = idx
        return toRet
    #limit mobility
    temp_count = 65
    for pos in positionsToPlay:
        other_tkn_moves = findMoves(makeMove(brd,pos,positionsToPlayDict[pos],tkn),nottkn)[0]
        if len(other_tkn_moves)==0: return pos
        if len(corner_idx.intersection(other_tkn_moves))==0:
            if len(other_tkn_moves)<temp_count:
                temp_count = len(other_tkn_moves)
                toRet=pos
    if temp_count!=65: return toRet
   
    if len(positionsToPlay - corneradj_idx)>0: positionsToPlay = positionsToPlay - corneradj_idx
    return positionsToPlay.pop()  
 
def switchToken(board,tkn):
    if tkn=="x":
        if len(findMoves(board,"o")[0])==0:return "x"
        return "o"  
    if len(findMoves(board,"x")[0])==0:return "o"
    return "x"
 
def negScore(brd,tkn):
    xC = brd.count("x")
    oC = brd.count("o")
    if tkn=="x":return xC-oC
    return oC-xC
 
def alphabeta(brd,tkn,path,alpha,beta): #dotC = dot count
    movesList = findMoves(brd,tkn)
    positionsToPlay = movesList[0]
    positionsToPlayDict = movesList[1]
   
    if len(positionsToPlay)==0:
        if len(path)==0:
            return (negScore(brd,tkn),[-1])
        return (negScore(brd,tkn),path)
 
    score = alpha-1
    sequence = []
    for idx in positionsToPlay: #going through each available position
        newBrd = makeMove(brd,idx,positionsToPlayDict[idx],tkn)#makes new board
        newTkn = switchToken(newBrd,tkn) #changes token
        if tkn==newTkn:
            curr = alphabeta(newBrd,newTkn,path+[idx,-1],alpha,beta)
            currScore = curr[0]
        else:
            curr = alphabeta(newBrd,newTkn,path+[idx],-beta,-alpha)
            currScore = -curr[0]
        if score>beta: return (score,path)
        if currScore>score:
            sequence=curr[1]
            score = currScore
        alpha = score+1
    return (score,sequence)
 
def playGame(brd,tkn):
    gamePlay = [0,0]
    ogtkn = tkn
    nottkn = "xo"[tkn=="x"]
    dotCount = brd.count(".")
    tkn = "x"
    while gamePlay[-1]!=-1 or gamePlay[-2]!=-1:
        if tkn==ogtkn:
            dotCount = brd.count(".")
            if dotCount<LIMIT_AB:
                move = alphabeta(brd,tkn,[],-64,64)[1]
                move = move[0]
            else: move = quickMove(brd,tkn)
        else:
            move = findMoves(brd,tkn)[0]
            if move: move = random.choice(list(move))
            else: move = -1
        if move!=-1:
            brd = makeMovePos(brd,move,tkn)
        gamePlay += [move]
        #print(tkn + "\n"+print_board(brd))
        tkn = "xo"[tkn=="x"]
    tknC = brd.count(ogtkn)
    tknN = brd.count(nottkn)
    return [tknC-tknN,tknC,tknN,gamePlay]
 
def makeMovePos(pzl,idx,tkn): #make move w/ just position
    pzl = pzl[:idx] + tkn + pzl[idx+1:]
    if tkn=="x": notToken = "o"
    else: notToken="x"
    rPoss,lPoss,uPoss,dPoss = True, True,True, True
    rudPoss, lddPoss,ludPoss, rddPoss = True,True,True,True
    if idx%8<6:
        r = idx+1
        while r>=0 and r<64 and pzl[r]==notToken:
            if r%8==7:
                rPoss = False
                break
            r+=1
        if r>=0 and r<64 and r!= idx+1 and rPoss and pzl[r]==tkn:
            idxt = idx
            idxt+=1
            while pzl[idxt]!= tkn:
                pzl = pzl[:idxt] + tkn + pzl[idxt+1:]
                idxt+=1
    if idx%8>1:
        l = idx-1
        while l>=0 and l<64 and pzl[l]==notToken:
            if l%8==0:
                lPoss = False
                break
            l-=1
        if l>=0 and l<64 and l!= idx-1 and lPoss and pzl[l]==tkn:
            idxt = idx
            idxt-=1
            while pzl[idxt]!= tkn:
                pzl = pzl[:idxt] + tkn + pzl[idxt+1:]
                idxt-=1
    if idx//8>1:
        u = idx-8
        while u>=0 and u<64 and pzl[u]==notToken:
            if u//8==0:
                uPoss = False
                break
            u-=8
        if u>=0 and u<64 and u!= idx-8 and uPoss and pzl[u]==tkn:
            idxt = idx
            idxt-=8
            while pzl[idxt]!= tkn:
                pzl = pzl[:idxt] + tkn + pzl[idxt+1:]
                idxt-=8
    if idx//8<6:
        d = idx+8
        while d>=0 and d<64 and pzl[d]==notToken:
            if d//8==0:
                dPoss = False
                break
            d+=8
        if d>=0 and d<64 and d!= idx+8 and dPoss and pzl[d]==tkn:
            idxt = idx
            idxt+=8
            while pzl[idxt]!= tkn:
                pzl = pzl[:idxt] + tkn + pzl[idxt+1:]
                idxt+=8
    if idx%8<6:
        rud = idx-7
        while rud>=0 and rud<64 and pzl[rud]==notToken:
            if rud%8==7:
                rudPoss = False
                break
            rud-=7
        if rud>=0 and rud<64 and rud!= idx-7 and rudPoss and pzl[rud]==tkn:
            idxt = idx
            idxt-=7
            while pzl[idxt]!= tkn:
                pzl = pzl[:idxt] + tkn + pzl[idxt+1:]
                idxt-=7
    if idx%8>1:
        ldd = idx+7
        while ldd>=0 and ldd<64 and pzl[ldd]==notToken:
            if ldd%8==0:
                rudPoss = False
                break
            ldd+=7
        if ldd>=0 and ldd<64 and ldd!= idx+7 and lddPoss and pzl[ldd]==tkn:
            idxt = idx
            idxt+=7
            while pzl[idxt]!= tkn:
                pzl = pzl[:idxt] + tkn + pzl[idxt+1:]
                idxt+=7
    if idx%8>1:
        lud = idx-9
        while lud>=0 and lud<64 and pzl[lud]==notToken:
            if lud%8==0:
                ludPoss = False
                break
            lud-=9
        if lud>=0 and lud<64 and lud!= idx-9 and ludPoss and pzl[lud]==tkn:
            idxt = idx
            idxt-=9
            while pzl[idxt]!= tkn:
                pzl = pzl[:idxt] + tkn + pzl[idxt+1:]
                idxt-=9
    if idx%8<6:
        rdd = idx+9
        while rdd>=0 and rdd<64 and pzl[rdd]==notToken:
            if rdd%8==7:
                rudPoss = False
                break
            rdd+=9
        if rdd>=0 and rdd<64 and rdd!= idx+9 and rddPoss and pzl[rdd]==tkn:
            idxt = idx
            idxt+=9
            while pzl[idxt]!= tkn:
                pzl = pzl[:idxt] + tkn + pzl[idxt+1:]
                idxt+=9
    return pzl
 
def main():
    global board,tokenToPlay,movesToPlay
    movesToDecom = ""
    if args:
        for arg in args:
            if len(arg)==64 and "."in arg: board = arg #re.search(r'^[oxOX.]{64}$',arg)
            elif arg=="x" or arg=="o": tokenToPlay = arg
            elif arg.isnumeric() and int(arg)<64: movesToPlay.append(int(arg))
            else: movesToDecom = arg  #(r'^[-_1-5\d|6[0-3]])+$',arg)
            #moves+=[int(arg[i:i+2].replace(".","")) for i in range(0,len(arg),2)
            #tkn="xo"[brd.count(".")&1] 
            # #cache the moves in negamax
            #find moves dictionary values isn't dir but all pos
        if movesToDecom:
            for i in range(0,len(movesToDecom),2):
                temp = movesToDecom[i:i+2]
                if temp[0]=="_": movesToPlay.append(int(temp[1]))
                elif temp.isnumeric(): movesToPlay.append(int(temp))
        if not tokenToPlay:
            x = board.count("x")
            o = board.count("o")
            if (x%2==0 and o%2==0) or (x%2==1 and o%2==1):tokenToPlay = "x"
            else: tokenToPlay= "o"
        if movesToPlay:
            board = playMoves(board,tokenToPlay,movesToPlay)
            x = board.count("x")
            o = board.count("o")
            if (x%2==0 and o%2==0) or (x%2==1 and o%2==1):tokenToPlay = "x"
            else: tokenToPlay= "o"
            if len(findMoves(board,tokenToPlay)[0])==0: tokenToPlay="xo" [tokenToPlay=="x"]
 
        print(print_boardast(board,tokenToPlay))
        print(board + " "+str(board.count("x"))+"/"+str(board.count("o")))
        print("Possible moves for "+tokenToPlay+": "+str(list(findMoves(board,tokenToPlay)[0])))
        print("My prefered move is "+str(quickMove(board,tokenToPlay)))
       
        dotC = board.count(".")
        if dotC<LIMIT_AB:
            neg = alphabeta(board,tokenToPlay,[],-64,64)
            moveSequence = neg[1][::-1]
            if moveSequence[0]==-1: moveSequence=moveSequence[1:]
            print("Min score: "+ str(neg[0]) + "; move sequence: "+ str(moveSequence))
       
    else:
        startTime = time.time()
        myTkn, yourTkn =0,0
        twoLow = [[70,70,70,70],[70,70,70,70]]
        twoLowGame = [0,0]
        allGames = ""
        for i in range(1,101):
            if i%2==0:
                curr = playGame(board,"x")
            else:
                curr = playGame(board,"o")
            myTkn+=curr[1]
            yourTkn+=curr[2]
            if curr[0]<10 and curr[0]>=0: allGames = allGames + " "+str(curr[0])+"  "
            else: allGames=allGames+str(curr[0])+"  "
            if i%10==0: allGames+="\n"
            if curr<twoLow[0] or curr<twoLow[1]:
                if twoLow[0]<twoLow[1]:
                    twoLow[1] = curr
                    twoLowGame[1] = i
                else:
                    twoLow[0] = curr
                    twoLowGame[0] = i
        print(allGames)
        totTkn = myTkn+yourTkn
        print("My tokens: "+str(myTkn)+"; Total tokens: "+str(totTkn))
        print("Score: "+str(myTkn/totTkn*100)[:4]+"%")
        print("AB LIMIT: "+str(LIMIT_AB))
        print("Game "+str(twoLowGame[0])+" as "+"ox"[twoLowGame[0]%2==0]+" => "+str(twoLow[0][0])+":")
        print(movesCondenseVer(twoLow[0][3][2:]))
        print("Game "+str(twoLowGame[1])+" as "+"ox"[twoLowGame[1]%2==0]+" => "+str(twoLow[1][0])+":")
        print(movesCondenseVer(twoLow[1][3][2:]))
        print("Elapsed time: "+str(time.time()-startTime)[:5]+"s")#'''
 
setGlobals()
if __name__ == '__main__': main()
#Maggie Gao, pd.6, 2023