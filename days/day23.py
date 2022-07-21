#https://adventofcode.com/2021/day/23
import heapq
from copy import deepcopy
from ast import literal_eval
def solve(file,part):
    #load data
    with open(f"./inputs/{file}",'r') as input:
        data = input.read().strip().split("\n")
    data = "".join(data[-3:-1]).replace("#","").replace(" ","")
    depth = 2
    if part == "b":
        depth = 4
        data = data[:4]+"DCBADBAC"+data[4:]
    xidx = 2
    yidx = -1
    amphipods = [[],[],[],[]]
    #map data to easy to work with format
    while data:
        amphipod,data = data[0],data[1:]
        if amphipod == "A":
            amphipods[0].append((xidx,yidx))
        if amphipod == "B":
            amphipods[1].append((xidx,yidx))
        if amphipod == "C":
            amphipods[2].append((xidx,yidx))
        if amphipod == "D":
            amphipods[3].append((xidx,yidx))
        xidx += 2
        if xidx == 10:
            xidx = 2
            yidx += -1
    stateandval = literal_eval("".join("".join(str(x)) for x in amphipods).replace("][",",").replace("[","(0,").replace("]",")"))
    #A* traversal algorithm
    dests=[x for x in [(x,0) for x in range(11)]+[(a,b) for a in range(2,9,2) for b in range(-depth,0)] if not((x[0] in [2,4,6,8]) and x[1]==0)]
    dist={(x,y):int(int(abs(x[0]-y[0])+abs(x[1]-y[1]))) for x in dests for y in dests  if not((x[1]<0 and y[1]<0)) and not (x[1]==0 and y[1]==0)}
    blocks={w:[z for z in dests if z[0] in range(min(w[0][0],w[1][0])+1,max(w[0][0],w[1][0])) and z[1]==0]+list(set([w[1]]+[(z[0],z[1]+j) for j in range(1,depth) for z in w if z[1]+j<0  ])) for w in dist}
    hall=[x for x in dests if x[1]==0]
    rooms=[x for x in dests if x[1]<0]
    goals={k:sorted([(2*(k+1),-j) for j in range(1,depth+1)]) for k in range(4)}

    goal=[set(goals[k]) for k in range(4)]
    def flatten(state):
        state=[sorted(y) for y in state]
        return(tuple([x for y in state for x in y]))

    def expand(state):
        size=len(state)//4
        return([list(state[i*size:(i+1)*size]) for i in range(4)])

    def heuristic(exp):
        return(sum([abs(z[0]-2*(i+1)) for i in range(4) for z in exp[i] ]))

    def neighbors(cur):
        occupied=[x for y in cur for x in y]
        newstates=[]
        plusen=[]

        ready=[len([ y for j in range(4) for y in cur[j] if j!=k and y in goals[k]])==0 for k in range(4)]
        for k,let in enumerate(cur):
            if not len([x for x in let if x in goals[k]])==depth:
                for j,l in enumerate(let):
                        if l in rooms and (j!=k or (j==k and not(ready[k]))):
                            for h in hall:
                                if len([x for x in occupied if x in blocks[(l,h)]])==0:
                                    tmp=deepcopy(cur)
                                    tmp[k][j]=h
                                    newstates.append(deepcopy(tmp))
                                    plusen.append(dist[(l,h)]*(10**k))
                        elif l in hall:#l is in the hall
                            if len([ y for x in range(4) for y in cur[x] if x!=k and y in goals[k] ])==0:
                                gs=[x for x in goals[k] if x not in cur[k]]
                                if len(gs)>0 and len([x for x in occupied if x in blocks[(l,gs[0])]])==0:
                                    tmp=deepcopy(cur)
                                    tmp[k][j]=gs[0]
                                    newstates.append(deepcopy(tmp))
                                    plusen.append(dist[(l,gs[0])]*(10**k))
        return(newstates,plusen)
    frontier=[]
    heapq.heappush(frontier,stateandval)
    seen={stateandval[1:]:stateandval[0]}
    while True:
        stuff=heapq.heappop(frontier)
        state=stuff[1:]
        exp=expand(state)
        if len([j for j in range(4) if set(exp[j])==goal[j]])==4:
            return seen[state]
        e=seen[state]
        neighs,energies=neighbors(exp)
        for i in range(len(neighs)):
            etot=e+energies[i]
            new=flatten(neighs[i])
            if new not in seen or seen[new]>etot:
                seen[new]=etot
                priority=etot+heuristic(neighs[i])
                heapq.heappush(frontier,tuple([priority]+[x for x in new]))
