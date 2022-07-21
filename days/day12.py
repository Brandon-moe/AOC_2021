#https://adventofcode.com/2021/day/12
def solve(file):
    with open(f"./inputs/{file}",'r') as input:
        data = input.read().splitlines()
    data = list(map(lambda x: (x.split("-")[0],x.split("-")[1]),data))
    return(solve_rec(data,False),solve_rec(data,True))

def solve_rec(data,restep_allowed,current_location="start",previous_location="",already_visited_small_caves=[]):
    counter = 0
    if previous_location.islower() and not restep_allowed:
        data = list(filter(lambda x:previous_location not in x,data))
    elif previous_location.islower() and restep_allowed:
        already_visited_small_caves.append(previous_location)
    if current_location == "end":
        return 1
    possible_paths = list(filter(lambda x:current_location in x,data))
    if possible_paths == []:
        return 0
    for path in possible_paths:
        next_location = [x for x in path if not x == current_location][0]
        if next_location == "start":
            continue
        if next_location in already_visited_small_caves and not restep_allowed:
            continue
        if next_location in already_visited_small_caves:
            counter += solve_rec(data,False,next_location,current_location,already_visited_small_caves.copy())
        else:
            counter += solve_rec(data.copy(),restep_allowed,next_location,current_location,already_visited_small_caves.copy())
    return counter
