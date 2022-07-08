def dijkstra(Distance, nPoint, sp, dp):

    INFTY = 1 << 32

    sDist = INFTY
    sRoute = [-1] * nPoint

    pDist = [INFTY] * nPoint
    pFixed = [False] * nPoint
    pRoute = [0] * nPoint
    
    pDist[sp] = 0

    while True:

        i = 0
        while i < nPoint:
            if not pFixed[i]:
                break
            i += 1
        if i == nPoint:
            break

        for j in range(i+1, nPoint):
            if not pFixed[j] and pDist[j] < pDist[i]:
                i = j
        
        sPoint = i
        pFixed[sPoint] = True

        for j in range(nPoint):
            if Distance[sPoint][j] > 0 and not pFixed[j]:
                newDist = pDist[sPoint] + Distance[sPoint][j]
                if newDist < pDist[j]:
                    pDist[j] = newDist
                    pRoute[j] = sPoint
    
    sDist = pDist[dp]
    i, j = dp, 0
    while i != sp:
        sRoute[j] = i
        i = pRoute[i]
        j = j + 1
    sRoute[j] = sp

    return sDist, sRoute

if __name__ == "__main__":

    Distance = [
        [ 0, 2, 8, 4,-1,-1,-1],
        [ 2, 0,-1,-1, 3,-1,-1],
        [ 8,-1, 0,-1, 2, 3,-1],
        [ 4,-1,-1, 0,-1, 8,-1],
        [-1, 3, 2,-1, 0,-1, 9],
        [-1,-1, 3, 8,-1, 0, 3],
        [-1,-1,-1,-1, 9, 3, 0]
    ]

    nPoint = 7
    sp, dp = 0, 6
    sDist, sRoute = dijkstra(Distance, nPoint, sp, dp)
    print(sDist)
    print(sRoute)   

