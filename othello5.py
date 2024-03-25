import sys; args=sys.argv[1:]

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
 
def switchToken(board,tkn):
    if tkn=="x":
        if len(findMoves(board,"o")[0])==0:return "x"
        return "o"  
    if len(findMoves(board,"x")[0])==0:return "o"
    return "x"
 
def negScore(brd,tkn):
    xC = sum(1 for k,j in enumerate(brd) if j == "x")
    oC = sum(1 for k,j in enumerate(brd) if j == "o")
    if tkn=="x":return xC-oC
    return oC-xC
 
def negamax(brd,tkn,path,dotC): #dotC = dot count
    movesList = findMoves(brd,tkn)
    positionsToPlay = movesList[0]
    positionsToPlayDict = movesList[1]

    #nottkn ="xo"[tkn=="x"]
     
    if len(positionsToPlay)==0:
        #if len(brd,nottkn)[0]==0:
        return (negScore(brd,tkn),path)
    
    score = -70
    sequence = []
    for idx in positionsToPlay: #going through each available position
        newBrd = makeMove(brd,idx,positionsToPlayDict[idx],tkn)#makes new board
        newTkn = switchToken(newBrd,tkn) #changes token
        if tkn==newTkn:
            curr = negamax(newBrd,newTkn,path+[idx,-1],dotC-1)
            currScore = curr[0]
        else:
            curr = negamax(newBrd,newTkn,path+[idx],dotC-1)
            currScore = -curr[0]
        if currScore>score:
            sequence=curr[1]
            score = currScore
    return (score,sequence)
 
print(negamax("oooooooooooooxoxoooooo.ooooxxx.xoooox..oooooxx.xooooo...oooox...","x",[],10))

board = args[0]
tokenToPlay = args[1]
 

print("Possible Moves For "+ tokenToPlay+": "+str(list(findMoves(board,tokenToPlay)[0])[::-1]))
 
dotC = sum(1 for k,j in enumerate(board) if j==".")
if dotC==1:
    movesList = findMoves(board,tokenToPlay)
    pos = movesList[0].pop()
    positionsToPlayDict = movesList[1]
    score = negScore(makeMove(board,pos,positionsToPlayDict[pos],tokenToPlay),tokenToPlay)
    print("Min score: "+ str(score) + "; move sequence: ["+str(pos)+ "]")
else:
    neg = negamax(board,tokenToPlay,[],dotC)
    moveSequence = neg[1][::-1]###
    if moveSequence[0]==-1: moveSequence=moveSequence[1:]###
    print("Min score: "+ str(neg[0]) + "; move sequence: "+ str(moveSequence))###
 
#Maggie Gao, pd.6, 2023
 

