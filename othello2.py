import sys; args=sys.argv[1:]
 
board = ""
tokenToPlay = ""
positionsToPlay = set()
positionsToPlayDict = {}
moveToPlay = ""
 
lookUpChess = {
    "a":0, "b":1, "c":2, "d":3,
    "e":4, "f":5, "g":6
}
 
#print(len(args[0]))
if len(args)==1:
    if len(args[0])==0:
        board = '.'*27 + "ox......xo" + '.'*27
        tokenToPlay = "x"
    elif args[0].lower()=="x" or args[0].lower()=="o":
        board = '.'*27 + "ox......xo" + '.'*27
        tokenToPlay = args[0].lower()
       
    elif len(args[0])==64:
        board = args[0].lower()
        x = sum(1 for k,j in enumerate(board) if j == "x")
        o = sum(1 for k,j in enumerate(board) if j == "o")
        if (x%2==0 and o%2==0) or (x%2==1 and o%2==1):tokenToPlay = "x"
        else: tokenToPlay= "o"
    else:
        board = '.'*27 + "ox......xo" + '.'*27
        tokenToPlay = "x"
        if args[0].isnumeric(): moveToPlay = int(args[0])
        else:
            chess = args[0].lower()
            moveToPlay = 8*int(chess[1]) - 8 + lookUpChess[chess[0]]
 
if len(args)==2:
    lis = []
    for arg in args:
        if len(arg)==64:
            lis.append(1)
            board = arg.lower()
        elif arg.lower()=="x" or arg.lower()=="o":
            lis.append(2)
            tokenToPlay = arg.lower()  
        elif arg.isnumeric():
            lis.append(3)
            moveToPlay = int(arg)
        else:
            lis.append(3)
            chess = arg.lower()
            moveToPlay = 8*int(chess[1]) - 8 + lookUpChess[chess[0]]
    if 1 not in lis: board = '.'*27 + "ox......xo" + '.'*27
    elif 2 not in lis:
        x = sum(1 for k,j in enumerate(board) if j == "x")
        o = sum(1 for k,j in enumerate(board) if j == "o")
        if (x%2==0 and o%2==0) or (x%2==1 and o%2==1):tokenToPlay = "x"
        else: tokenToPlay= "o"
 
if len(args)==3:
    board, tokenToPlay= args[0].lower(),args[1].lower()
    if args[2].isnumeric(): moveToPlay = int(args[2])
    else:
        chess = args[2].lower()
        moveToPlay = 8*int(chess[1]) - 8 + lookUpChess[chess[0]]
 
def print_board(pzl):
    toret=""
    for i in range(0,64,8):
        toret+=pzl[i:i+8] + "\n"
    return toret
 
#idx//8 row
#idx%8 column
def find_positions(board):
    global positionsToPlay, positionsToPlayDict
    positionsToPlay = set()
    positionsToPlayDict = {}
    if board.find("x")==-1 or board.find("o")==-1:
        return positionsToPlay
    tokenPositions = [idx for idx,ch in enumerate(board) if ch ==tokenToPlay]
    if tokenToPlay=="x": notToken = "o"
    else: notToken="x"
    for idx in tokenPositions:
        rPoss,lPoss = True,True
        uPoss,dPoss = True,True
        rudPoss, lddPoss= True, True #right up diagonal, left down diagonal
        ludPoss, rddPoss= True, True #left up diagonal, right down diagonal
        r = idx+1
        if idx%8<6:
            while r>=0 and r<64 and board[r]==notToken:
                if r%8==7:
                    rPoss = False
                    break
                r+=1
            if r>=0 and r<64 and r!= idx+1 and rPoss and board[r]==".":
                if r in positionsToPlayDict: positionsToPlayDict[r].append("r")
                else: positionsToPlayDict[r] = ["r"]
                positionsToPlay.add(r)
 
        l = idx-1
        if idx%8>1:
            while l>=0 and l<64 and board[l]==notToken:
                if l%8==0:
                    lPoss = False
                    break
                l-=1
            if l>=0 and l<64 and l!= idx-1 and lPoss and board[l]==".":
                if l in positionsToPlayDict: positionsToPlayDict[l].append("l")
                else: positionsToPlayDict[l] = ["l"]
                positionsToPlay.add(l)
       
        u = idx-8
        if idx//8>1:
            while u>=0 and u<64 and board[u]==notToken:
                if u//8==0:
                    uPoss = False
                    break
                u-=8
            if u>=0 and u<64 and u!= idx-8 and uPoss and board[u]==".":
                if u in positionsToPlayDict: positionsToPlayDict[u].append("u")
                else: positionsToPlayDict[u] = ["u"]
                positionsToPlay.add(u)
 
        d = idx+8
        if idx//8<6:
            while d>=0 and d<64 and board[d]==notToken:
                if d//8==0:
                    dPoss = False
                    break
                d+=8
            if d>=0 and d<64 and d!= idx+8 and dPoss and board[d]==".":
                if d in positionsToPlayDict: positionsToPlayDict[d].append("d")
                else: positionsToPlayDict[d] = ["d"]
                positionsToPlay.add(d)
 
       
        rud = idx-7
        if idx%8<6:
            while rud>=0 and rud<64 and board[rud]==notToken:
                if rud%8==7:
                    rudPoss = False
                    break
                rud-=7
            if rud>=0 and rud<64 and rud!= idx-7 and rudPoss and board[rud]==".":
                if rud in positionsToPlayDict: positionsToPlayDict[rud].append("rud")
                else: positionsToPlayDict[rud] = ["rud"]
                positionsToPlay.add(rud)
 
        ldd = idx+7
        if idx%8>1:
            while ldd>=0 and ldd<64 and board[ldd]==notToken:
                if ldd%8==0:
                    rudPoss = False
                    break
                ldd+=7
            if ldd>=0 and ldd<64 and ldd!= idx+7 and lddPoss and board[ldd]==".":
                if ldd in positionsToPlayDict: positionsToPlayDict[ldd].append("ldd")
                else: positionsToPlayDict[ldd] = ["ldd"]
                positionsToPlay.add(ldd)
 
        lud = idx-9
        if idx%8>1:
            while lud>=0 and lud<64 and board[lud]==notToken:
                if lud%8==0:
                    ludPoss = False
                    break
                lud-=9
            if lud>=0 and lud<64 and lud!= idx-9 and ludPoss and board[lud]==".":
                if lud in positionsToPlayDict: positionsToPlayDict[lud].append("lud")
                else: positionsToPlayDict[lud] = ["lud"]
                positionsToPlay.add(lud)
 
        rdd = idx+9
        if idx%8<6:
            while rdd>=0 and rdd<64 and board[rdd]==notToken:
                if rdd%8==7:
                    rudPoss = False
                    break
                rdd+=9
            if rdd>=0 and rdd<64 and rdd!= idx+9 and rddPoss and board[rdd]==".":
                if rdd in positionsToPlayDict: positionsToPlayDict[rdd].append("rdd")
                else: positionsToPlayDict[rdd] = ["rdd"]
                positionsToPlay.add(rdd)
    return positionsToPlay
 
def make_move(pzl,idx,direc,token):
    pzl = pzl[:idx] + token + pzl[idx+1:]
    if direc == "r": #went right so have to left
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
        if len(find_positions(board))==0:
            tokenToPlay="x"
            if len(find_positions(board))==0:
                tokenToPlay=""
    else: 
        tokenToPlay="x"
        if len(find_positions(board))==0:
            tokenToPlay="o"
            if len(find_positions(board))==0:
                tokenToPlay=""
 
def findScore(pzl):
    return str(sum(1 for k,j in enumerate(pzl) if j == "x"))+"/"+str(sum(1 for k,j in enumerate(pzl) if j == "o"))
 
if len(find_positions(board))==0:
    switchToken(board)
 
print(print_board(board) + "\n")
print("1D: "+board)
print(findScore(board))
print("Possible Moves: "+str(list(find_positions(board))))
 
if type(moveToPlay) == int:
    print(tokenToPlay + " plays to " + str(moveToPlay))
    #print(positionsToPlayDict[moveToPlay])
    #print(positionsToPlayDict)
    newboard=board
    for direction in positionsToPlayDict[moveToPlay]:
        #print(print_board(newboard))
        newboard = make_move(newboard,moveToPlay,direction,tokenToPlay)
        #print(print_board(newboard))
    print(print_board(newboard)+"\n")
    #for k,j in enumerate(newboard):
     #   if k in positionsToPlay: newboard = newboard[:k] + "*" + newboard[k+1:]
    print("1D: "+ newboard)
    print(findScore(newboard))
    switchToken(newboard) 
    #print(tokenToPlay)
    if tokenToPlay: print("Possible Moves: "+str(list(find_positions(newboard))))
    else: print("No moves possible")
 
 
#Maggie Gao, pd.6, 2023
 

