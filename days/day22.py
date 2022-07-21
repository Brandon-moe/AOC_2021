#https://adventofcode.com/2021/day/22
def solve(file,part):
    with open(f"./inputs/{file}",'r') as input:
        data = input.read().strip().split("\n")
    for idx,val in enumerate(data):
        instruction = 0 if val[1] == "f" else 1 #on or off
        val = val.split("=")
        x1 = int(val[1].split("..")[0])
        x2 = int(val[1].split("..")[1].split(",")[0])
        y1 = int(val[2].split("..")[0])
        y2 = int(val[2].split("..")[1].split(",")[0])
        z1 = int(val[3].split("..")[0])
        z2 = int(val[3].split("..")[1])
        data[idx] = [instruction,x1,x2,y1,y2,z1,z2]

    #solution uses inclusion-exclusion principle
    cubes = []
    for instruction in data:
        if part == "a":
            if not all([abs(x)<=50 for x in instruction]):
                continue
        if instruction[0]:
            to_add = [instruction]
        else:
            to_add = []
        for cube in cubes:
            intersection = get_intersection(instruction,cube)
            if intersection:
                to_add += [intersection]
        cubes += to_add

    count = 0
    for c in cubes:
        count += c[0]*(c[2]-c[1]+1)*(c[4]-c[3]+1)*(c[6]-c[5]+1)
    return(count)

def get_intersection(cube1,cube2):
    mapping = [lambda a,b:-b,max,min,max,min,max,min]
    n = [mapping[i](cube1[i],cube2[i]) for i in range(7)]
    return None if n[1] > n[2] or n[3] > n[4] or n[5] > n[6] else n
