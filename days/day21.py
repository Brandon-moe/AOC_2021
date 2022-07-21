#https://adventofcode.com/2021/day/21
def solve(file,part):
    with open(f"./inputs/{file}",'r') as input:
        data = input.read().split("\n")
    #remapping positions from 1-10 to 0-9 makes some of the calculations less verbose
    p1_pos,p2_pos = int(data[0].split(" ")[-1])-1,int(data[1].split(" ")[-1])-1
    if part == "a":
        return deterministic(p1_pos,p2_pos)
    elif part == "b":
        return max(dirac(p1_pos,0,p2_pos,0))
        
def deterministic(p1_pos,p2_pos):
    die_value = 1
    total_rolls = 0
    scores = [0,0]
    positions = [p1_pos,p2_pos]
    player = 1
    while scores[player] < 1000:
        player = 1 - player
        positions[player] = (positions[player] + 3*die_value + 3)%10
        scores[player] += positions[player] + 1
        total_rolls += 3
        die_value = ((die_value+2)%100)+1
    return total_rolls * min(scores)

def dirac(p1_pos,p1_score,p2_pos,p2_score):
    #number of new universes in which die value was rolled
    roll_to_universes = [(3,1),(4,3),(5,6),(6,7),(7,6),(8,3),(9,1)]
    #recursive call swaps player labels so p1 is always referring to next player to roll
    if p2_score >= 21: return (0,1)

    p1_wins,p2_wins = 0,0
    for (roll,universes) in roll_to_universes:
        count_2,count_1 = dirac(p2_pos,p2_score,(p1_pos+roll)%10,p1_score + 1 + (p1_pos+roll)%10)
        p1_wins,p2_wins = p1_wins + universes*count_1, p2_wins + universes*count_2

    return p1_wins,p2_wins
