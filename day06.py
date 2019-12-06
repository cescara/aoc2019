from util import get_input


class Node:
    nodes = {}

    def __init__(self, name, parent = None):
        self.name = name
        self.parent = parent
        self.children = []
        Node.nodes[name] = self

    def __repr__(self):
        return self.name


def parse(orbits):
    for parent, child in orbits:
        if parent not in Node.nodes:
            Node(parent)
        if child not in Node.nodes:
            Node(child, Node.nodes[parent])
        else:
            Node.nodes[child].parent = Node.nodes[parent]
        Node.nodes[parent].children.append(Node.nodes[child])


def count_orbits():
    def inner(child):
        if child.parent:
            yield 1
            yield from inner(child.parent)
    return sum([sum(inner(x)) for x in Node.nodes.values()])


def get_ancestors(node):
    ancestors = []
    while True:
        if node.parent is None:
            return ancestors
        node = node.parent
        ancestors.append(node)


def walk(source, target):
    source_ancestors = get_ancestors(source)
    target_ancestors = get_ancestors(target)
    for source_count, source_ancestor in enumerate(source_ancestors):
        for target_count, target_ancestor in enumerate(target_ancestors):
            if source_ancestor == target_ancestor:
                return source_count + target_count


def read_input(input_):
    return [tuple(line.strip().split(")")) for line in input_]


def test_part1():
    text = '''COM)B
    B)C
    C)D
    D)E
    E)F
    B)G
    G)H
    D)I
    E)J
    J)K
    K)L'''

    orbits = read_input(text.split("\n"))
    assert part1(orbits) == 42


def test_part2():
    text = '''COM)B
    B)C
    C)D
    D)E
    E)F
    B)G
    G)H
    D)I
    E)J
    J)K
    K)L
    K)YOU
    I)SAN'''
    orbits = read_input(text.split("\n"))
    assert part2(orbits) == 4


def part1(orbits):
    parse(orbits)
    return count_orbits()


def part2(orbits):
    parse(orbits)
    return walk(Node.nodes["YOU"], Node.nodes["SAN"])


def main():
    with open(get_input(__file__)) as file:
        orbits = read_input(file)

    print(part1(orbits))
    Node.nodes = {}
    print(part2(orbits))


if __name__ == '__main__':
    main()
