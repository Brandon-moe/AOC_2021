#https://adventofcode.com/2021/day/7
import statistics
def solve(file):
    with open(f"./inputs/{file}",'r') as input:
        data = list(map(int,input.read().split(",")))
    median = int(statistics.median(data))
    mean = int(statistics.mean(data))
    return sum(abs(x-median) for x in data),sum(sum(range(abs(x-mean)+1)) for x in data)
