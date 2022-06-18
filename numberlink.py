from pprint import pprint
from random import choice

WIDTH = 6
HEIGHT = 6
MAX = 4

DIRECTION = {(-1,0), (0,1), (1,0), (0,-1)}

LEFTEND = 0
RIGHTEND = WIDTH-1
UPPEREND = 0
LOWEREND = HEIGHT-1

class Stone:

    def __init__(self,num,x,y):
        self.num = num
        self.x = x
        self.y = y

    def check(self):
        L = []
        for direction in DIRECTION:
            movable = 1
            xtemp, ytemp = self.x + direction[0], self.y + direction[1]
            if xtemp < UPPEREND or xtemp > LOWEREND or ytemp < LEFTEND or ytemp > RIGHTEND:
                movable = 0
            elif not MAP[xtemp][ytemp] == 0:
                movable = 0
            if movable:
                L.append(direction)
        return L

    def move(self, direction):
        if direction not in self.check():
            return 0
        else:
            self.x += direction[0]
            self.y += direction[1]
            MAP[self.x][self.y] = self.num
            return 1

    def search(self):
        # self.num + 4 is the goal.
        for direction in DIRECTION:
            xtemp, ytemp = self.x + direction[0], self.y + direction[1]
            if UPPEREND <= xtemp and xtemp <= LOWEREND and LEFTEND <= ytemp and ytemp <= RIGHTEND:
                if MAP[xtemp][ytemp] == self.num + 4:
                    return 1
        return 0

    def random(self):
        # If self.check = [], the Stone cannot move any more.
        movable = self.check()
        if not movable:
            return 0
        else:
            direction = choice(movable)
            self.move(direction)
            return 1

    def findroute(self):

        while True:
            movable = self.random()
            if self.search():
                return 1
            elif not movable:
                return 0


def findloc():

    loc = []
    for i in range(MAX):
        for j in range(HEIGHT):
            for k in range(WIDTH):
                if MAP[j][k] == i+1:
                    loc.append([j, k])
    return loc


def numberlink():

    loc = findloc()

    for i in range(MAX):
        stone = Stone(i+1,loc[i][0],loc[i][1])
        if not stone.findroute():
            return 0
    return 1


if __name__ == "__main__":
    solved = 0
    count = 0
    for i in range(10000):
        count += 1

        MAP=[[1,0,0,0,0,6],
             [0,0,0,0,0,5],
             [0,0,0,7,0,0],
             [0,0,4,0,0,0],
             [0,2,3,0,8,0],
             [0,0,0,0,0,0]]

        x = numberlink()
        if x:
            solved = 1
            print(f"{count}th trial: Cleared!")
            pprint(MAP)

    if not solved:
        print("Not cleared...")
