import sys; args=sys.argv[1:]

board = ""
tokenToPlay = ""
positionsToPlay = set()

#print(len(args[0]))
if len(args)==1:
    if len(args[0])==0:
        board = '.'*27 + "ox......xo" + '.'*27
        tokenToPlay = "x"
    elif len(args[0]) ==1:
        board = '.'*27 + "ox......xo" + '.'*27
        tokenToPlay = args[0].lower()
    else:
        board = args[0].lower()
        x = sum(1 for k,j in enumerate(board) if j == "x")
        o = sum(1 for k,j in enumerate(board) if j == "o")
        if (x%2==0 and o%2==0) or (x%2==1 and o%2==1):tokenToPlay = "x"
        else: tokenToPlay= "o"

if len(args)==2:
    board, tokenToPlay= args[0].lower(),args[1].lower()

def print_board(pzl):
    toret=""
    for i in range(0,64,8):
        toret+=pzl[i:i+8] + "\n"
    return toret

#idx//8 row
#idx%8 column
def find_positions():
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
                #print(r)
                #print("r")
                positionsToPlay.add(r)

        l = idx-1
        if idx%8>1:
            while l>=0 and l<64 and board[l]==notToken:
                if l%8==0: 
                    lPoss = False
                    break
                l-=1
            if l>=0 and l<64 and l!= idx-1 and lPoss and board[l]==".": 
                #print(l)
                #print("l")
                positionsToPlay.add(l)
        
        u = idx-8
        if idx//8>1:
            while u>=0 and u<64 and board[u]==notToken:
                if u//8==0: 
                    uPoss = False
                    break
                u-=8
            if u>=0 and u<64 and u!= idx-8 and uPoss and board[u]==".": 
                #print(u)
                #print("u")
                positionsToPlay.add(u)

        d = idx+8
        if idx//8<6:
            while d>=0 and d<64 and board[d]==notToken:
                if d//8==0: 
                    dPoss = False
                    break
                d+=8
            if d>=0 and d<64 and d!= idx+8 and dPoss and board[d]==".": 
                #print(d)
                #print("d")
                positionsToPlay.add(d)

        
        rud = idx-7
        if idx%8<6:
            while rud>=0 and rud<64 and board[rud]==notToken:
                if rud%8==7: 
                    rudPoss = False
                    break
                rud-=7
            if rud>=0 and rud<64 and rud!= idx-7 and rudPoss and board[rud]==".": 
                #print(rud)
                #print("rud")
                positionsToPlay.add(rud)

        ldd = idx+7
        if idx%8>1:
            while ldd>=0 and ldd<64 and board[ldd]==notToken:
                if ldd%8==0: 
                    rudPoss = False
                    break
                ldd+=7
            if ldd>=0 and ldd<64 and ldd!= idx+7 and lddPoss and board[ldd]==".": 
                #print(ldd)
                #print("ldd")
                positionsToPlay.add(ldd)

        lud = idx-9
        if idx%8>1:
            while lud>=0 and lud<64 and board[lud]==notToken:
                if lud%8==0: 
                    ludPoss = False
                    break
                lud-=9
            if lud>=0 and lud<64 and lud!= idx-9 and ludPoss and board[lud]==".": 
                #print(lud)
                #print("lud")
                positionsToPlay.add(lud)

        rdd = idx+9
        if idx%8<6:
            while rdd>=0 and rdd<64 and board[rdd]==notToken:
                if rdd%8==7: 
                    rudPoss = False
                    break
                rdd+=9
            if rdd>=0 and rdd<64 and rdd!= idx+9 and rddPoss and board[rdd]==".": 
                #print(rdd)
                #print("rdd")
                positionsToPlay.add(rdd)

find_positions()

#print(print_board(board))

newboard = board
for k,j in enumerate(newboard):
    if k in positionsToPlay: newboard = newboard[:k] + "*" + newboard[k+1:]

print(print_board(newboard))
if len(positionsToPlay)==0: print("No moves possible")
else: print(positionsToPlay)


#Maggie Gao, pd.6, 2023