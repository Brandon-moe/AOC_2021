#https://adventofcode.com/2021/day/11
def solve(file):
    with open(f"./inputs/{file}",'r') as input:
        data = input.read().splitlines()
    data = [list(map(int,list(x))) for x in data]
    counter = 0
    its = 0
    while True:
        its += 1
        lit = []
        resolved = []
        for i in range(len(data)):
            for j in range(len(data[i])):
                data[i][j] += 1
                if data[i][j] > 9:
                    lit.append((i,j))
        while lit:
            counter += 1
            x = lit.pop(0)
            i = [y for y in [x[0]-1,x[0],x[0]+1] if y>=0 and y<len(data)]
            j = [y for y in [x[1]-1,x[1],x[1]+1] if y>=0 and y<len(data[0])]
            for n in i:
                for m in j:
                    if (n,m) in resolved or (n==x[0] and m==x[1]):
                        continue
                    data[n][m] += 1
                    if data[n][m] > 9:
                        if not (n,m) in lit:
                            lit.append((n,m))
            resolved.append(x)
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] > 9:
                    data[i][j] = 0
        if its == 100:
            part_a_solution = counter
        if len(resolved) == 100:
            return(part_a_solution,its)
    return
