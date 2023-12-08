import json
import icecream


def check_hamilton_availability(_graph):
    for v in _graph:
        pass



    return True


def shortestpath_func(_ct1, _ct2, _graph, _cities):
    def choose_shortest_option(_options: [(str, str, int)]) -> (str, str, int):
        """
        options_example = [
            ('city1', 'city2', 200),
            ('city2', 'city4', 400),
            ...
            (src, dst, cost)
        ]
        """
        best_option = _options[0]  # the default value will be the first option
        for opt in _options:  # inside this loop, we update the res if it was not the cheapest option
            if opt[2] < best_option[2]:
                best_option = opt

        _options.remove(best_option)
        _options += [(best_option[0], x, _cities[int(x)]['dist'] + best_option[2]) for x in _graph[best_option[0]]]
        # for x in _graph[best_option[0]]:
        #     print("______________________________")
        #     print(best_option[1])
        #     print(x)
        #     print(_cities)
        #     # print(_cities[x] + best_option[2])
        #     print("______________________________")
        #     _options.append((best_option[1], x, _cities[int(x)]['dist'] + best_option[2]))

        return best_option, _options

    options = [(_ct1, x, _cities[int(x)]['dist']) for x in _graph[_ct1]]
    best_opt, options = choose_shortest_option(options)
    while best_opt[0] != _ct1:
        best_opt, options = choose_shortest_option(options)


def euler_func(_graph):
    def is_eulerian_directed():
        odd_in_degree_counter = 0
        odd_out_degree_counter = 0
        start_node_out = None
        start_node_in = None

        out_degree_counter = {x: 0 for x in _graph}
        in_degree_counter = {x: 0 for x in _graph}

        for node in _graph:
            out_degree_counter[node] = len(_graph[node])
            for n in _graph[node]:
                in_degree_counter[n] += 1

        for node in _graph:
            in_degree = in_degree_counter[node]
            out_degree = out_degree_counter[node]

            if in_degree - out_degree > 1 or out_degree - in_degree > 1:
                return False, None

            if in_degree - out_degree == 1:
                odd_out_degree_counter += 1
                start_node_out = node

            if out_degree - in_degree == 1:
                odd_in_degree_counter += 1
                start_node_in = node

        if odd_out_degree_counter == 0 and odd_in_degree_counter == 0:
            return True, list(graph.keys())[0]
        elif odd_out_degree_counter == 1 and odd_in_degree_counter == 1:
            return True, start_node_out
        else:
            return False, None


def numofpath_func(_graph, start, end):
    simple_paths = []
    visited = set()

    def dfs(current, path):
        visited.add(current)
        path.append(current)

        if current == end:
            simple_paths.append(path[:])  # Found a path from start to end
        else:
            for neighbor in _graph[current]:
                if neighbor not in visited:
                    dfs(neighbor, path)

        # Backtrack
        visited.remove(current)
        path.pop()

    dfs(start, [])

    return simple_paths


def numeric_path_to_string(_graph, _cities):
    new_graph = {}
    for c in _cities:
        new_graph[c] = _graph[str(_cities[c]['id'])]

    return new_graph


cities_raw = input().split()
cities = {}
_id = 1
for index, raw_city in enumerate(cities_raw):
    if index % 2 == 0:
        cities[raw_city] = {
            "name": raw_city,
            "price": cities_raw[index + 1],
            "id": _id
        }
        _id += 1

print(cities)

num_of_paths = int(input())
paths = []
graph = {str(i + 1): [] for i in range(len(cities))}
for i in range(num_of_paths):
    inp = input().split()
    if inp[2] == '0':
        p = {
            "src": inp[0],
            "dst": inp[1],
            "dist": int(inp[3])
        }
        paths.append(p)
        graph[inp[0]].append(inp[1])
    else:
        p1 = {
            "src": inp[0],
            "dst": inp[1],
            "dist": int(inp[3])
        }
        p2 = {
            "src": inp[1],
            "dst": inp[0],
            "dist": int(inp[3])
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
        print(euler_func(graph))
    elif cmd == "SHORTESTPATH":
        ct1, ct2 = input().split()
        print(shortestpath_func(ct1, ct2, numeric_path_to_string(graph, cities), paths))
    elif cmd == "HAMILTON":
        is_hamilton_available = check_hamilton_availability(graph)
        if is_hamilton_available:
            pass
    elif cmd == "ECONOMIC_TOUR":
        pass
