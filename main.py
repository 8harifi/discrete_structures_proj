from icecream import ic


def check_hamilton(_paths):
    ret = {
        "has_path": False,
        "has_circuit": False
    }  # (hamilton_path, hamilton_circuit)

    def goto(p: str):
        nonlocal cur_choices

        visited_cts_in_p = p.split()
        all_cts = list(_paths.keys())
        cur_choices += [
            f"{p} {x}" for x in list(_paths[p.split()[-1]].keys()) if x not in p.split()
        ]
        cur_choices.remove(p)
        # ic(cur_choices)
        if p.split()[-1] == _src and set(all_cts) == set(visited_cts_in_p):
            return "has_circuit"
        elif set(all_cts) == set(visited_cts_in_p):
            return "has_path"
        return None

    # ic(cur_choices)
    # cur_position = _src
    for _src in _paths:
        cur_choices = [f"{_src} {x}" for x in list(_paths[_src].keys())]
        while True:
            if not cur_choices:
                return ret["has_path"], ret["has_circuit"]
            # ic(cur_choices)
            # ic(ret)
            cur_choice = cur_choices[0]
            # for ch in cur_choices:
            #     if cur_choices[ch] < cur_choices[cur_choice]:
            #         cur_choice = ch
            res = goto(cur_choice)
            if res:
                if res == "has_path":
                    ret["has_path"] = True
                elif res == "has_circuit":
                    ret["has_circuit"] = True
                    return ret["has_path"], ret["has_circuit"]


def tour_func(_src: str, _paths: {dict}):
    def goto(p: str):
        """
        check if the last parameter of the given path is the dst
        if yes: return True
        if no: remove that path from cur_choices and add new available paths AND RETURN FALSE
        also avoid that paths that lead to an already-visited vertex
        """
        nonlocal cur_choices

        visited_cts_in_p = p.split()
        all_cts = list(_paths.keys())
        if p.split()[-1] == _src and set(all_cts) == set(visited_cts_in_p):
            return p, cur_choices[p]
        cur_choices = cur_choices | {
            f"{p} {x}": cur_choices[p] + _paths[p.split()[-1]][x] for x in list(_paths[p.split()[-1]].keys())
        }
        cur_choices.pop(p)
        # ic(cur_choices)
        return None, None

    cur_choices = {f"{_src} {x}": _paths[_src][x] for x in list(_paths[_src].keys())}
    # ic(cur_choices)
    # cur_position = _src
    while True:
        # ic(cur_choices)
        cheapest = list(cur_choices.keys())[0]
        for ch in cur_choices:
            if cur_choices[ch] < cur_choices[cheapest]:
                cheapest = ch
        found_path, weight = goto(cheapest)
        if found_path:
            # ic(found_path)
            return found_path, weight


def shortestpath_func(_src: str, _dst: str, _paths: {dict}):
    def goto(p: str):
        """
        check if the last parameter of the given path is the dst
        if yes: return True
        if no: remove that path from cur_choices and add new available paths AND RETURN FALSE
        also avoid that paths that lead to a already-visited vertex
        """
        nonlocal cur_choices

        if p.split()[-1] == _dst:
            return p, cur_choices[p]
        cur_choices = cur_choices | {
            f"{p} {x}": cur_choices[p] + _paths[p.split()[-1]][x] for x in list(_paths[p.split()[-1]].keys()) if
            x not in p.split()
        }
        cur_choices.pop(p)
        # ic(cur_choices)
        return None, None

    cur_choices = {f"{_src} {x}": _paths[_src][x] for x in list(_paths[_src].keys())}
    # ic(cur_choices)
    # cur_position = _src
    while True:
        cheapest = list(cur_choices.keys())[0]
        for ch in cur_choices:
            if cur_choices[ch] < cur_choices[cheapest]:
                cheapest = ch
        found_path, weight = goto(cheapest)
        if found_path:
            # ic(found_path)
            return found_path, weight


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

    # ic(all_edges)

    found_path = []
    for _src in _paths:
        cur_vertex = _src
        cur_path = []
        visited = []

        while True:
            # ic(cur_path)
            # ic(visited)
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

    # ic(found_path)
    if found_path:
        for v in found_path[0]:
            if v not in found_path[1] and v in found_path[-1]:
                return True, found_path
        return False, found_path
    else:
        return False, None


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
    # ic(found_paths)
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
    rev_relations = {relations[x]: x for x in relations}

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
            print("NUMOFPATH")
            c1, c2 = input().split()
            print(
                numofpath_func(
                    relations[int(c1)],
                    relations[int(c2)],
                    paths
                )
            )
        elif cmd == "EULER":
            print("EULER")
            is_circuit, res = euler_func(paths)
            if not res:
                print("NO NO")
            else:
                starting_point = [v for v in res[0] if v not in res[1]][0]
                p = [starting_point]
                for index, e in enumerate(res):
                    if index == 0:
                        pass
                    elif index == len(res) - 1:
                        p += [x for x in e]
                    else:
                        p.append([x for x in e if x in res[index - 1]][0])
                if is_circuit:
                    print("YES YES")
                    print("".join([str(rev_relations[x]) for x in p]))
                    print("".join([str(rev_relations[x]) for x in p]))
                else:
                    print("YES NO")
                    print(" ".join([str(rev_relations[x]) for x in p]))

        elif cmd == "SHORTESTPATH":
            print("SHORTESTPATH")
            ct1, ct2 = input().split()
            res, weight = shortestpath_func(ct1, ct2, paths)
            print(weight)
            print(" ".join([str(rev_relations[x]) for x in res.split()]))
        elif cmd == "HAMILTON":
            print("HAMILTON")
            has_path, has_circuit = check_hamilton(paths)
            res = f"{'Yes' if has_path else 'No'} {'Yes' if has_circuit else 'No'}"
            print(res)
        elif cmd == "TOUR":
            print("TOUR")
            ct = relations[int(input())]
            res, weight = tour_func(ct, paths)
            print(weight)
            print(" ".join([str(rev_relations[x]) for x in res.split()]))
        elif cmd == "ECONOMIC_TOUR":
            print("ECONOMIC_TOUR")


if __name__ == "__main__":
    main()
