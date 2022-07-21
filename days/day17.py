#https://adventofcode.com/2021/day/17
def solve(file,part):
    with open(f"./inputs/{file}",'r') as input:
        data = input.read().split(", ")
    x = list(map(int,data[0].split("=")[1].split("..")))
    x.sort()
    y = list(map(int,data[1].split("=")[1].split("..")))
    y.sort()
    ymax = max([abs(x) for x in y])
    if part == "a":
        return triangular(ymax-1)
    counter = 0
    for i in range(0,x[1]+1):
        for j in range(y[0],-y[0]+1):
            xvel = i
            yvel = j
            xpos = 0
            ypos = 0
            while ypos > y[0] and xpos < x[1]:
                xpos +=  xvel
                if not xvel == 0:
                    xvel -= 1
                ypos += yvel
                yvel -= 1
                if (x[0] <= xpos <= x[1]) and (y[0] <= ypos <= y[1]):
                    counter += 1
                    break
    return counter
def triangular(n):
    return int(n*(n+1)/2)
