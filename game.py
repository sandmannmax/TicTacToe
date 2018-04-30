def getPos(pos):
    posList = [-1,-1]
    if pos > 9 or pos < 1:
        raise Exception('Position not possible')
    elif pos == 1:
        posList = [0,0]
    elif pos == 2:
        posList = [0,1]
    elif pos == 3:
        posList = [0,2]
    elif pos == 4:
        posList = [1,0]
    elif pos == 5:
        posList = [1,1]
    elif pos == 6:
        posList = [1,2]
    elif pos == 7:
        posList = [2,0]
    elif pos == 8:
        posList = [2,1]
    else:
        posList = [2,2]
    return posList

def test(testTable):
    win = -1
    for row in testTable:
        add = 0
        li = []
        for x in row:
            if x > 0:
                add += x
                li.append(x)
        if add == 3 or add == 6:
            if len(li) == 3:
                win = row[0]
                break
    add1 = 0
    add2 = 0
    add3 = 0
    li1 = []
    li2 = []
    li3 = []
    for row in testTable:
        if row[0] > 0:
            add1 += row[0]
            li1.append(x)
        if row[1] > 0:
            add2 += row[1]
            li2.append(x)
        if row[2] > 0:
            add3 += row[2]
            li3.append(x)
    if add1 == 3 or add1 == 6:
        if len(li1) == 3:
            win = testTable[0][0]
    elif add2 == 3 or add2 == 6:
        if len(li2) == 3:
            win = testTable[0][1]
    elif add3 == 3 or add3 == 6:
        if len(li3) == 3:
            win = testTable[0][2]
    add = 0
    li = []
    for x in range(3):
        if testTable[x][x] > 0:
            add += testTable[x][x]
            li.append(x)
    if add == 3 or add == 6:
        if len(li) == 3:
             win = testTable[0][0]
    add = 0
    li = []
    for x in range(3):
        if testTable[x][(2-x)] > 0:
            add += testTable[x][(2-x)]
            li.append(x)
    if add == 3 or add == 6:
        if len(li) == 3:
             win = testTable[0][2]
    return win

def insert(pos, player, testTable):
    table = testTable
    table[getPos(pos)[0]][getPos(pos)[1]] = int(player)
    return table

def getPosHelp(pos, testTable):
    table = testTable
    return table[getPos(pos)[0]][getPos(pos)[1]]

def reset():
    table = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
    count = 0
    return table

def getPosXY(posXY):
    pos = 0
    if posXY[0] > 9 and posXY[0] < 133 and posXY[1] > 9 and posXY[1] < 133:
        pos = 1
    elif posXY[0] > 142 and posXY[0] < 264 and posXY[1] > 9 and posXY[1] < 133:
        pos = 2
    elif posXY[0] > 273 and posXY[0] < 391 and posXY[1] > 9 and posXY[1] < 133:
        pos = 3
    elif posXY[0] > 9 and posXY[0] < 133 and posXY[1] > 142 and posXY[1] < 264:
        pos = 4
    elif posXY[0] > 142 and posXY[0] < 264 and posXY[1] > 142 and posXY[1] < 264:
        pos = 5
    elif posXY[0] > 273 and posXY[0] < 391 and posXY[1] > 142 and posXY[1] < 264:
        pos = 6
    elif posXY[0] > 9 and posXY[0] < 133 and posXY[1] > 273 and posXY[1] < 391:
        pos = 7
    elif posXY[0] > 142 and posXY[0] < 264 and posXY[1] > 273 and posXY[1] < 391:
        pos = 8
    elif posXY[0] > 273 and posXY[0] < 391 and posXY[1] > 273 and posXY[1] < 391:
        pos = 9
    return pos    

#def init():
#    table = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
#    count = 0
