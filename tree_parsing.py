from typing import List


# Tree parsing --------------------------------------------------------------------------------------------------------#

def get_node(id_str: str, level: List[dict]) -> dict:
    for node in level:
        if node["id"] == id_str:
            return node
    new_node = {"id": id_str, "yes": "bad", "no": "bad"}
    level.append(new_node)
    return new_node

def parse_level(level: List[dict], line: str, index: int) -> None:
    if line[index] == ' ':
        node = level[-1]
        index += len(node["id"])
        branch = ("no" if isinstance(node["no"], list) else "yes")
        return parse_level(node[branch], line, index + 3)
    id_len = line[index:].find(' ')
    node = get_node(line[index:index + id_len], level)
    index += len(node["id"])
    branch = ("no" if line[index + 1] == 'N' else "yes")
    if len(line) == index + 2:
        node[branch] = "good"
        return None
    if isinstance(node[branch], str):
        node[branch] = []
    return parse_level(node[branch], line, index + 3)

def parse_tree(lines: List[str]) -> List[dict]:
    root_level = []
    for line in lines:
        parse_level(root_level, line, 0)
    return root_level


# Tree printing -------------------------------------------------------------------------------------------------------#

def print_term_node(node: dict):
    print('{', end='')
    print(f' id: ', end='')
    print(f'\'{node["id"]}\',', end='')
    print(f' yes: ', end='')
    print(f'[{node["yes"]}],', end='')
    print(f' no: ', end='')
    print(f'[{node["no"]}] ', end='')

def print_level_node(node: dict, index: int):
    print('{')
    for key in node.keys():
        print(((index + 4) * ' '), end='')
        print(f"{key}: ", end='')
        if isinstance(node[key], list):
            print_tree(node[key], index + 4)
        else:
            print(f"'{node[key]}'", end='')
            print('' if key == 'no' else ',')
    print(((index + 2) * ' '), end='')

def print_tree(level: List[dict], index: int):
    print('[')
    last_index = len(level) - 1
    for i in range(len(level)):
        print(((index + 2) * ' '), end='')
        if isinstance(level[i]["yes"], list) \
                or isinstance(level[i]["no"], list):
            print_level_node(level[i], index)
        else:
            print_term_node(level[i])
        print('},' if i != last_index else '}')
    print((index * ' '), end='')
    print('],' if index else ']')


# Program start -------------------------------------------------------------------------------------------------------#

input_lines = [
    "Q1 N",
    "Q1 O Q2 O",
    "     Q3 N Q4 O",
    "          Q4 N",
    "Q5 N",
    "Q5 O Q6 N Q7 O",
    "     Q8 O",
    "     Q8 N Q9 N",
    "          Q9 O Q10 O",
    "          Q11 O",
    "     Q12 N",
    "Q13 0"
]

tree = parse_tree(input_lines)
print_tree(tree, 0)
