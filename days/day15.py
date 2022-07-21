#https://adventofcode.com/2021/day/15
from numpy import Inf
import heapq

def solve(file,part):
    with open(f"./inputs/{file}",'r') as input:
        data = [[int(i) for i in j] for j in input.read().splitlines()]

    max_l = len(data[0])
    if part == "b":
        data, max_l = extend_data(data)
    start_node = (0, 0)
    end_node = (max_l - 1, max_l - 1)

    open_queue = []
    closed_queue = set()
    parents = {}
    g_score = {}

    for y in range(len(data)):
        for x in range(len(data)):
            g_score[(y, x)] = Inf

    g_score[start_node] = 0
    heapq.heappush(open_queue, (l1_norm(start_node, end_node), start_node))

    while open_queue:
        _, node = heapq.heappop(open_queue)
        if node == end_node:
            total = 0
            while node in parents:
                x = node[0]
                y = node[1]
                total += data[y][x]
                node = parents[node]
            return total
        elif node in closed_queue:
            continue
        else:
            neighbours = get_neighbours(data, node)
            for neighbour in neighbours:
                if neighbour in closed_queue:
                    continue
                x = neighbour[0]
                y = neighbour[1]
                added_g_score = data[y][x]
                candidate_g = g_score[node] + added_g_score
                if candidate_g <= g_score[neighbour]:
                    g_score[neighbour] = candidate_g
                    parents[neighbour] = node
                    f = l1_norm(neighbour, end_node) + candidate_g
                    heapq.heappush(open_queue, (f, neighbour))
            closed_queue.add(node)

def l1_norm(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbours(data, node):
    x = node[0]
    y = node[1]
    node_neighbours = []
    neighbours = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    for i in neighbours:
        if (0 <= i[0] <= len(data) - 1) and (0 <= i[1] <= len(data) - 1):
            node_neighbours.append(i)
    return node_neighbours

def extend_data(data):
    d = len(data)
    max_list_size = len(data) * 5
    extended_data = [[0 for _ in range(max_list_size)] for _ in range(max_list_size)]

    for y_index, y in enumerate(extended_data):
        for x_index, x in enumerate(y):
            n = data[y_index % d][x_index % d]
            extended_data[y_index][x_index] = (n + ((y_index // d) + (x_index // d)) - 1) % 9 + 1
    return extended_data, max_list_size
