#https://adventofcode.com/2021/day/2
def solve(file,part):
    with open(f"./inputs/{file}",'r') as input:
        data = input.read().splitlines()
    xpos = 0
    ypos = 0
    aim = 0
    for line in data:
        if part =="b":
            if line.split(" ")[0] == "forward":
                xpos += int(line.split(" ")[1])
                ypos += int(line.split(" ")[1])*aim
            elif line.split(" ")[0] == "up":
                aim -= int(line.split(" ")[1])
            elif line.split(" ")[0] == "down":
                aim += int(line.split(" ")[1])
        elif part =="a":
            if line.split(" ")[0] == "forward":
                xpos += int(line.split(" ")[1])
            elif line.split(" ")[0] == "up":
                ypos -= int(line.split(" ")[1])
            elif line.split(" ")[0] == "down":
                ypos += int(line.split(" ")[1])
    return(xpos*ypos)
