import sys; args = sys.argv[1:]
import math
transformation = set()
rect = args[0]
length=len(rect)
width=0
height=0
if len(args)>1:
    width = int(args[1])
    height = len(rect)//width
else:
    if math.sqrt(length)%1==0: width=int(math.sqrt(length))
    else: 
        x = int(math.sqrt(length) - math.sqrt(length)%1 + 1)
        while (length/x)%1!=0: x+=1
        width = x
    height = int(length/width)

def horizontal():
    #horizontal
    temp = []
    for i in range(0,length,width):
        temp += [rect[i:i+width]]
    temp = temp[::-1]
    horiz=""
    for item in temp:
        horiz += item
    # transformation.add(horiz)
    return horiz
def vertical():
    #vertical
    temp = []
    for i in range(0,length,width):
        r = rect[i:i+width]
        temp += [r[::-1]]
    vert=""
    for item in temp:
        vert += item
    return vert
    # transformation.add(vert)

def ninety(rect,width,height):
    #90 degrees
    ninetytransformstring=""
    for i in range(width):
        for j in range(i+width*(height-1),-1,-width):
            ninetytransformstring+=rect[j]
    return ninetytransformstring

def oneeighty():
    #180 degrees
    newrect=ninety(rect,width,height)
    return ninety(newrect,height,width)

def backninety(rect,width,height):
    #back 90 degrees
    ninetytransformstring=""
    for i in range(width-1,-1,-1):
        smallstr=""
        for j in range(i+width*(height-1),-1,-width):
            smallstr+=rect[j]
        smallstr=smallstr[::-1]
        ninetytransformstring+=smallstr
    return ninetytransformstring

def forwardslash():
    temp = []
    for i in range(0,length,width):
        temp += [rect[i:i+width]]
    temp = temp[::-1]
    currentRect=""
    for item in temp:
        currentRect += item
    return backninety(currentRect,width,height)
    #change to backwards ninety

def backwardslash():
    temp = []
    for i in range(0,length,width):
        temp += [rect[i:i+width]]
    temp = temp[::-1]
    currentRect=""
    for item in temp:
        currentRect += item
    return ninety(currentRect,width,height)


transformation.add(rect)
transformation.add(horizontal())
transformation.add(vertical())
transformation.add(ninety(rect,width,height))
transformation.add(oneeighty())
transformation.add(backninety(rect,width,height))
transformation.add(forwardslash())
transformation.add(backwardslash())

for trans in transformation:
    print(trans)

#Maggie Gao, pd.6, 2023
