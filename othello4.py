import sys; args=sys.argv[1:]
 
def setGlobals():
    global board,tokenToPlay,positionsToPlayDict,moveToPlay
    board = '.'*27 + "ox......xo" + '.'*27
    tokenToPlay = 'x'
    positionsToPlayDict = {}
    moveToPlay = []

lookUpChess = {
    "a":0, "b":1, "c":2, "d":3,
    "e":4, "f":5, "g":6
}
corner_idx = {0,7,56,63}
edge_idx = {1, 2, 3, 4, 5, 6, 8, #not include corners
15, 16, 23, 24, 31, 32, 39, 40, 
47, 48, 55, 57, 58, 59, 60, 61, 62}
corneradj_idx = {1,6,8,9,14,15,62,57,55,54,48,49}
 


def print_board(pzl):
    toret=""
    for i in range(0,64,8):
        toret+=pzl[i:i+8] + "\n"
    return toret
 
#idx//8 row
#idx%8 column
def findMoves(brd,tkn):
    global positionsToPlayDict
    positionsToPlay = set()
    positionsToPlayDict = {}
    if brd.find("x")==-1 or brd.find("o")==-1:
        return positionsToPlay
    tokenPositions = [idx for idx,ch in enumerate(brd) if ch ==tkn]
    if tkn=="x": notToken = "o"
    else: notToken="x"
    for idx in tokenPositions:
        rPoss,lPoss = True,True
        uPoss,dPoss = True,True
        rudPoss, lddPoss= True, True #right up diagonal, left down diagonal
        ludPoss, rddPoss= True, True #left up diagonal, right down diagonal
        r = idx+1
        if idx%8<6:
            while r>=0 and r<64 and brd[r]==notToken:
                if r%8==7:
                    rPoss = False
                    break
                r+=1
            if r>=0 and r<64 and r!= idx+1 and rPoss and brd[r]==".":
                if r in positionsToPlayDict: positionsToPlayDict[r].append("r")
                else: positionsToPlayDict[r] = ["r"]
                positionsToPlay.add(r)
 
        l = idx-1
        if idx%8>1:
            while l>=0 and l<64 and brd[l]==notToken:
                if l%8==0:
                    lPoss = False
                    break
                l-=1
            if l>=0 and l<64 and l!= idx-1 and lPoss and brd[l]==".":
                if l in positionsToPlayDict: positionsToPlayDict[l].append("l")
                else: positionsToPlayDict[l] = ["l"]
                positionsToPlay.add(l)
       
        u = idx-8
        if idx//8>1:
            while u>=0 and u<64 and brd[u]==notToken:
                if u//8==0:
                    uPoss = False
                    break
                u-=8
            if u>=0 and u<64 and u!= idx-8 and uPoss and brd[u]==".":
                if u in positionsToPlayDict: positionsToPlayDict[u].append("u")
                else: positionsToPlayDict[u] = ["u"]
                positionsToPlay.add(u)
 
        d = idx+8
        if idx//8<6:
            while d>=0 and d<64 and brd[d]==notToken:
                if d//8==0:
                    dPoss = False
                    break
                d+=8
            if d>=0 and d<64 and d!= idx+8 and dPoss and brd[d]==".":
                if d in positionsToPlayDict: positionsToPlayDict[d].append("d")
                else: positionsToPlayDict[d] = ["d"]
                positionsToPlay.add(d)
      
        rud = idx-7
        if idx%8<6:
            while rud>=0 and rud<64 and brd[rud]==notToken:
                if rud%8==7:
                    rudPoss = False
                    break
                rud-=7
            if rud>=0 and rud<64 and rud!= idx-7 and rudPoss and brd[rud]==".":
                if rud in positionsToPlayDict: positionsToPlayDict[rud].append("rud")
                else: positionsToPlayDict[rud] = ["rud"]
                positionsToPlay.add(rud)
 
        ldd = idx+7
        if idx%8>1:
            while ldd>=0 and ldd<64 and brd[ldd]==notToken:
                if ldd%8==0:
                    rudPoss = False
                    break
                ldd+=7
            if ldd>=0 and ldd<64 and ldd!= idx+7 and lddPoss and brd[ldd]==".":
                if ldd in positionsToPlayDict: positionsToPlayDict[ldd].append("ldd")
                else: positionsToPlayDict[ldd] = ["ldd"]
                positionsToPlay.add(ldd)
 
        lud = idx-9
        if idx%8>1:
            while lud>=0 and lud<64 and brd[lud]==notToken:
                if lud%8==0:
                    ludPoss = False
                    break
                lud-=9
            if lud>=0 and lud<64 and lud!= idx-9 and ludPoss and brd[lud]==".":
                if lud in positionsToPlayDict: positionsToPlayDict[lud].append("lud")
                else: positionsToPlayDict[lud] = ["lud"]
                positionsToPlay.add(lud)
 
        rdd = idx+9
        if idx%8<6:
            while rdd>=0 and rdd<64 and brd[rdd]==notToken:
                if rdd%8==7:
                    rudPoss = False
                    break
                rdd+=9
            if rdd>=0 and rdd<64 and rdd!= idx+9 and rddPoss and brd[rdd]==".":
                if rdd in positionsToPlayDict: positionsToPlayDict[rdd].append("rdd")
                else: positionsToPlayDict[rdd] = ["rdd"]
                positionsToPlay.add(rdd)
    return positionsToPlay
 
def makeMove(pzl,idx_r,directions,token):
    pzl = pzl[:idx_r] + token + pzl[idx_r+1:]
    for direc in directions:
        idx = idx_r
        if direc == "r": #went right so have to go left
            idx-=1
            while pzl[idx]!= token:
                pzl = pzl[:idx] + token + pzl[idx+1:]
                idx-=1
        if direc == "l":
            idx+=1
            while pzl[idx]!= token:
                pzl = pzl[:idx] + token + pzl[idx+1:]
                idx+=1
        if direc == "u":
            idx+=8
            while pzl[idx]!= token:
                pzl = pzl[:idx] + token + pzl[idx+1:]
                idx+=8
        if direc == "d":
            idx-=8
            while pzl[idx]!= token:
                pzl = pzl[:idx] + token + pzl[idx+1:]
                idx-=8
    
        if direc == "rud":
            idx+=7
            while pzl[idx]!= token:
                pzl = pzl[:idx] + token + pzl[idx+1:]
                idx+=7
        if direc == "lud":
            idx+=9
            while pzl[idx]!= token:
                pzl = pzl[:idx] + token + pzl[idx+1:]
                idx+=9
        if direc == "rdd":
            idx-=9
            while pzl[idx]!= token:
                pzl = pzl[:idx] + token + pzl[idx+1:]
                idx-=9
        if direc == "ldd":
            idx-=7
            while pzl[idx]!= token:
                pzl = pzl[:idx] + token + pzl[idx+1:]
                idx-=7
    return pzl
 
def switchToken(board):
    global tokenToPlay
    if tokenToPlay=="x": 
        tokenToPlay="o"
        if len(findMoves(board,tokenToPlay))==0:
            tokenToPlay="x"
            if len(findMoves(board,tokenToPlay))==0:
                tokenToPlay=""
    else: 
        tokenToPlay="x"
        if len(findMoves(board,tokenToPlay))==0:
            tokenToPlay="o"
            if len(findMoves(board,tokenToPlay))==0:
                tokenToPlay=""

def quickMove(brd,tkn): #find best move
    global positionsToPlayDict
    positionsToPlay = findMoves(brd,tkn)
    if tkn=="x": nottkn="o"
    else:nottkn="x"
    #return positionsToPlay.pop()
    toRet = -1
    #corner
    if len(corner_idx.intersection(positionsToPlay))>0:
        temp_count = -65
        scoreDiff = 0
        for idx in corner_idx.intersection(positionsToPlay):
            mademove = makeMove(brd,idx,positionsToPlayDict[idx],tkn)
            temp = findScore(mademove).split("/")
            if tkn == "x": scoreDiff == int(temp[0]) - int(temp[1])
            else: scoreDiff == int(temp[1]) - int(temp[0])
            if scoreDiff>temp_count: 
                temp_count = scoreDiff
                toRet = idx
        return toRet
    #limit mobility
    temp_count = 65
    for pos in positionsToPlay:
        findMoves(brd,tkn)
        other_tkn_moves = findMoves(makeMove(brd,pos,positionsToPlayDict[pos],tkn),nottkn)
        if len(other_tkn_moves)==0: return pos
        if len(corner_idx.intersection(other_tkn_moves))==0:
            if len(other_tkn_moves)<temp_count: 
                temp_count = len(other_tkn_moves)
                toRet=pos
    if temp_count!=65: return toRet
    
    if len(positionsToPlay - corneradj_idx)>0: positionsToPlay = positionsToPlay - corneradj_idx
    return positionsToPlay.pop()  

def findScore(pzl):
    xC = sum(1 for k,j in enumerate(pzl) if j == "x")
    oC = sum(1 for k,j in enumerate(pzl) if j == "o")
    if tokenToPlay == "x": scoreDiff = xC - oC
    else: scoreDiff = oC - xC
    return str(xC)+"/"+str(oC)
 
def snapshot(board):
    print(print_board(board))
    print("1D: "+board)
    print(findScore(board))
    print("Possible Moves For "+ tokenToPlay+": "+str(list(findMoves(board,tokenToPlay)))+"\n")

def main():
    global board,tokenToPlay,positionsToPlayDict
    lis = set()
    for arg in args:
        if len(arg)==64:
            lis.add(1)
            board = arg.lower()
        elif arg.lower()=="x" or arg.lower()=="o":
            lis.add(2)
            tokenToPlay = arg.lower()  
        elif arg.isdigit():
            lis.add(3)
            moveToPlay.append(int(arg))
        else:
            if arg[0].lower() in lookUpChess:
                lis.add(3)
                chess = arg.lower()
                moveToPlay.append(8*int(chess[1]) - 8 + lookUpChess[chess[0]])
    if 1 not in lis: board = '.'*27 + "ox......xo" + '.'*27
    elif 2 not in lis:
        x = sum(1 for k,j in enumerate(board) if j == "x")
        o = sum(1 for k,j in enumerate(board) if j == "o")
        if (x%2==0 and o%2==0) or (x%2==1 and o%2==1):tokenToPlay = "x"
        else: tokenToPlay= "o"

    if len(findMoves(board,tokenToPlay))==0:
        switchToken(board)
    
    snapshot(board) 
    for move in moveToPlay:
        if tokenToPlay: 
            print(tokenToPlay + " plays to " + str(move))  
            board = makeMove(board,move,positionsToPlayDict[move],tokenToPlay)
            switchToken(board) 
            snapshot(board)
            print(tokenToPlay + " plays to " +str(quickMove(board,tokenToPlay)))


    #if tokenToPlay: print("Possible Moves: "+str(list(find_positions(newboard))))
    #else: print("No moves possible")
setGlobals()
if __name__ == '__main__': main()

 
#Maggie Gao, pd.6, 2023
 


