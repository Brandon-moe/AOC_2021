#https://adventofcode.com/2021/day/24
#Today's puzzle input is a program to be interpreted, but is computationally
#impossible to run. My solution involved analysing the input to reverse-engineer
#the program, and produce a puzzle solution without building and running an interpreter.
#Initially solved entirely by hand, but wrote some python code to have a complete git repo afterwards.

#reverse engineering notes:
#input program is composed of 14 blocks of code, near identical except for 3 lines
#1 line differs between mod z 26 and mod z 1. mod z 1 blocks are increasing z by
#factor of 26 regardless of input. mod z 26 lines either do nothing significant to z
#or decrease it depending on input. The other 2 lines that differ do so by integer
#values to be added to x and y. To get z=0 at end, pair mod z 1 and mod z 26 lines
#together using a stack, inputs for the 2 blocks have to differ by an amount determined
#by those 2 addition lines.

def solve(file,part):
    with open(f"./inputs/{file}",'r') as input:
        data = input.read().strip().split("\n")
    div1,div26 = [],[]
    for line in range(0,len(data),18):
        if data[line+4][-1] == "1":
            div1.append(int(data[line+15].split(" ")[-1]))
            div26.append(None)
        else:
            div1.append(None)
            div26.append(int(data[line+5].split(" ")[-1]))
    stack = []
    model_no = [0]*14
    for idx,(div1_val,div26_val) in enumerate(zip(div1, div26)):
        if not div1_val is None:
            stack.append((idx,div1_val))
        else:
            to_match = stack.pop()
            difference = div26_val + to_match[1]
            if part == "a":
                model_no[to_match[0]] = min(9,9-difference)
                model_no[idx] = min(9,9+difference)
            if part == "b":
                model_no[to_match[0]] = max(1,1-difference)
                model_no[idx] = max(1,1+difference)
    return "".join([str(x) for x in model_no])
