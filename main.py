import json
import icecream


def euler_func():
    pass


def numofpath_func(gr, start, end):
    simple_paths = []
    visited = set()

    def dfs(current, path):
        visited.add(current)
        path.append(current)

        if current == end:
            simple_paths.append(path[:])  # Found a path from start to end
        else:
            for neighbor in gr[current]:
                if neighbor not in visited:
                    dfs(neighbor, path)

        # Backtrack
        visited.remove(current)
        path.pop()

    dfs(start, [])

    return simple_paths


cities_raw = input().split()
cities = []
for index, raw_city in enumerate(cities_raw):
    if index % 2 == 0:
        cities.append(
            {
                "name": raw_city,
                "price": cities_raw[index + 1]
            }
        )

num_of_paths = int(input())
paths = []
graph = {str(i + 1): [] for i in range(len(cities))}
for i in range(num_of_paths):
    inp = input().split()
    if inp[2] == '0':
        p = {
            "src": inp[0],
            "dst": inp[1],
            "dist": inp[3]
        }
        paths.append(p)
        graph[inp[0]].append(inp[1])
    else:
        p1 = {
            "src": inp[0],
            "dst": inp[1],
            "dist": inp[3]
        }
        p2 = {
            "src": inp[1],
            "dst": inp[0],
            "dist": inp[3]
        }
        paths.append(p1)
        paths.append(p2)
        graph[inp[0]].append(inp[1])
        graph[inp[1]].append(inp[0])

num_of_commands = int(input())
for i in range(num_of_commands):
    cmd = input()
    if cmd == "NUMOFPATH":
        c1, c2 = input().split()
        numofpath = len(numofpath_func(graph, c1, c2))
        print(numofpath)
    elif cmd == "EULER":
        print(euler_func())
    elif cmd == "SHORTESTPATH":
        pass
    elif cmd == "HAMILTON":
        pass
    elif cmd == "TOUR":
        pass
    elif cmd == "ECONOMIC_TOUR":
        pass
