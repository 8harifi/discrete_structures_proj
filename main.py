from icecream import ic


def check_hamilton_availability():
    pass


def shortestpath_func():
    pass


def euler_func(_paths):
    def goto(vertex):
        nonlocal cur_vertex
        nonlocal cur_path
        nonlocal visited

        cur_path.append({cur_vertex, vertex})
        visited.append({cur_vertex, vertex})
        cur_vertex = vertex

    def backtrack():
        nonlocal cur_vertex
        nonlocal cur_path
        nonlocal visited

        x_vertex = cur_vertex
        cur_vertex = [sth for sth in cur_path[-1] if sth != cur_vertex][0]
        for e in _paths[x_vertex]:
            if cur_vertex != e:
                visited.remove({x_vertex, e})
        cur_path.pop(-1)

    all_edges = []
    for x in _paths:
        for y in _paths[x].keys():
            if {x, y} not in all_edges:
                all_edges.append({x, y})

    ic(all_edges)

    found_path = []
    for _src in _paths:
        cur_vertex = _src
        cur_path = []
        visited = []

        while True:
            ic(cur_path)
            ic(visited)
            # ic([x for x in all_edges if x not in cur_path])
            choices = [x for x in _paths[cur_vertex].keys() if {cur_vertex, x} not in visited]
            if [x for x in all_edges if x not in cur_path]:  # no path/circuit found yet
                if not choices:  # no valid choice to choose
                    if visited and cur_vertex == _src:  # cursor is at the start point but there are some visited edges (not the first round of the while loop)
                        break
                    else:  # no valid choice but cursor can still backtrack
                        backtrack()
                else:  # if we DO have a choice and we haven't visited all the edges, we should move forward
                    goto(choices[0])
            else:  # found a path/circuit
                if cur_vertex == _src:
                    return cur_path
                else:
                    found_path = cur_path
                    break

    if found_path:
        return found_path
    else:
        return None


def numofpath_func(_src, _dst, _paths):
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
        elif cmd == "EULER":
            res = euler_func(paths)
            # TODO: change res using relations (turn into numbers and then check if its a path or circuit)
            if not res:
                print("NO NO")

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
