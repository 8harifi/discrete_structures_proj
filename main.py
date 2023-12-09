from icecream import ic


def check_hamilton_availability():
    pass


def shortestpath_func():
    pass


# def euler_func(_paths):
#     def goto(vertex):
#         nonlocal cur_vertex
#         nonlocal cur_path
#         nonlocal visited
#
#         cur_path.append(vertex)
#         visited.append(vertex)
#         cur_vertex = cur_path[-1]
#
#     def backtrack():
#         nonlocal cur_vertex
#         nonlocal cur_path
#
#         cur_path.pop(-1)
#         cur_vertex = cur_path[-1]
#
#     # numofpath = 0
#     for _src in _paths:
#     cur_vertex = _src
#     cur_path = [_src]
#     visited = [_src]
#
#     while True:
#         # ic(cur_path)
#         choices = [x for x in _paths[cur_vertex].keys() if x not in visited]
#         if cur_vertex == _dst:
#             numofpath += 1
#         if not choices and cur_vertex == _src:
#             break
#         elif not choices and cur_vertex == _dst:
#             backtrack()
#         elif not choices:
#             backtrack()
#         else:
#             goto(choices[0])
#
#     return numofpath


def numofpath_func(_src, _dst, _paths):
    # numofpath = 0
    found_paths = []
    cur_vertex = _src
    cur_path = [_src]
    visited = []

    def goto(vertex):
        nonlocal cur_vertex
        nonlocal cur_path
        nonlocal visited

        cur_path.append(vertex)
        visited.append({cur_vertex, vertex})
        cur_vertex = cur_path[-1]

    def backtrack():
        nonlocal cur_vertex
        nonlocal cur_path

        cur_path.pop(-1)
        cur_vertex = cur_path[-1]

    while True:
        choices = [x for x in _paths[cur_vertex].keys() if {cur_vertex, x} not in visited]
        if cur_vertex == _dst and cur_path not in found_paths:
            # numofpath += 1
            found_paths.append([x for x in cur_path])
            backtrack()
        if not choices and cur_vertex == _src:
            break
        elif not choices and cur_vertex == _dst:
            backtrack()
        elif not choices:
            backtrack()
        else:
            goto(choices[0])

    # ic(numofpath)
    # return numofpath
    ic(found_paths)
    return len(found_paths)


def main():
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
            print(
                numofpath_func(
                    relations[int(c1)],
                    relations[int(c2)],
                    paths
                )
            )
            # paths = {
            #     'Isfahan': {'Tehran': 200, 'Yazd': 500},
            #     'Kerman': {'Yazd': 300},
            #     'Tehran': {'Isfahan': 200, 'Yazd': 100},
            #     'Yazd': {'Isfahan': 500, 'Kerman': 300, 'Tehran': 100}
            # }
            # src = "Kerman"
            # dst = "Isfahan"
            # res = numofpath_func(src, dst, paths)
            # print(res)
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


if __name__ == "__main__":
    main()
