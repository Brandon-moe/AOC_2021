#https://adventofcode.com/2021/day/25
import copy
def solve(file):
    with open(f"./inputs/{file}",'r') as input:
        data = input.read().strip().split("\n")
    grid = [[x for x in data[i]] for i in range(len(data))]
    still_moving = True
    counter = 0
    while still_moving:
        counter+=1
        still_moving = False
        updated_grid = copy.deepcopy(grid)
        #horizontal movement
        for idx,val in enumerate(grid):
            for idx2,val2 in enumerate(grid[idx]):
                if idx2 == len(grid[idx])-1:
                    target = 0
                else:
                    target = idx2+1
                if val2 == ">":
                    if grid[idx][target] == ".":
                        updated_grid[idx][target] = ">"
                        updated_grid[idx][idx2] = "."
                        still_moving = True
                    else:
                        updated_grid[idx][idx2] = ">"
        #vertical movement
        for idx,val in enumerate(grid):
            for idx2,val2 in enumerate(grid[idx]):
                if idx == len(grid)-1:
                    target = 0
                else:
                    target = idx+1
                if val2 == "v":
                    if(grid[target][idx2] == "." and not updated_grid[target][idx2] == ">" or
                        grid[target][idx2] == ">" and updated_grid[target][idx2] == "."):
                        updated_grid[target][idx2] = "v"
                        updated_grid[idx][idx2] = "."
                        still_moving = True
                    else:
                        updated_grid[idx][idx2] = "v"


        grid = copy.deepcopy(updated_grid)
    return counter
