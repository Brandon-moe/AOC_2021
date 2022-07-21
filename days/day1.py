#https://adventofcode.com/2021/day/1
def solve(file,offset):
    with open(f"./inputs/{file}",'r') as input:
        data = list(map(int,input.read().splitlines()))
    return sum(list(map(lambda x,y: x>y,data[offset:],data)))
