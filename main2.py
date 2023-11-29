from icecream import ic


def check_hamilton_availability():
    pass


def shortestpath_func():
    pass


def euler_func():
    pass


def numofpath_func(_src, _dst, _paths):
    current = _src
    check_point = _src
    while True:
        for c in _paths[current]:
            pass


cities_raw = input().split()
cities = {}  # list of cities along with their prices
paths = {}  # list of cities along with all the paths attached to them
relations = {}  # list of "_id"s along with their names (change id to city name)
_id = 1
for index, raw_city in enumerate(cities_raw):
    if index % 2 == 0:
        cities[raw_city] = int(cities_raw[index + 1])
        relations[_id] = raw_city
        _id += 1

ic(cities)
ic(relations)

num_of_paths = int(input())
# graph = {str(i + 1): [] for i in range(len(cities))}
for i in range(num_of_paths):
    inp = input().split()
    if inp[2] == '0':
        src = relations[int(inp[0])]
        dst = relations[int(inp[1])]
        if src not in paths:
            paths[src] = {}
        paths[src][dst] = int(inp[3])
    else:
        src = relations[int(inp[0])]
        dst = relations[int(inp[1])]
        if src not in paths:
            paths[src] = {}
        paths[src][dst] = int(inp[3])

        src = relations[int(inp[1])]
        dst = relations[int(inp[0])]
        if src not in paths:
            paths[src] = {}
        paths[src][dst] = int(inp[3])

ic(paths)

num_of_commands = int(input())
for i in range(num_of_commands):
    cmd = input()
    if cmd == "NUMOFPATH":
        c1, c2 = input().split()
        numofpath_func(
            relations[int(c1)],
            relations[int(c2)],
            paths
        )
        # use numofpath_func here
    elif cmd == "EULER":
        pass
        # use euler_func here
    elif cmd == "SHORTESTPATH":
        ct1, ct2 = input().split()
        # use shortestpath_func here
    elif cmd == "HAMILTON":
        pass
        # use check_hamilton_availability here
    elif cmd == "TOUR":
        pass
    elif cmd == "ECONOMIC_TOUR":
        pass
