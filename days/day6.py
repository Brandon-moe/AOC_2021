#https://adventofcode.com/2021/day/6
def solve(file,numdays):
    with open(f"./inputs/{file}",'r') as input:
        data = list(map(int,input.read().split(",")))
    age = [0]*9
    for fish in data:
        age[fish] += 1
    for day in range(numdays):
        age[(day+7)%9] += age[day%9]
    return sum(age)
