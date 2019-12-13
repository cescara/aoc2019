from math import atan2

from util import get_input
from collections import defaultdict, deque


def observe(asteroids, current):
    buckets = defaultdict(list)
    for row in range(0, len(asteroids)):
        for col in range(0, len(asteroids[row])):
            if not asteroids[row][col]:
                continue
            if (row, col) == current:
                continue

            row_, col_ = row - current[0], col - current[1]
            buckets[atan2(col_, row_)].append({"relative": (row_, col_), "original": (row, col)})
    return buckets


def obliterate(targets):
    destroyed = []
    for bucket in targets:
        targets[bucket] = deque(sorted(targets[bucket], key=lambda x: (abs(x["relative"][0]), abs(x["relative"][1]))))

    while sum([len(asteroids) for asteroids in targets.values()]):
        for bucket in sorted(targets, key=lambda x: -x):
            if not targets[bucket]:
                continue

            destroyed.append(targets[bucket].popleft())
    return destroyed


def part1(asteroids):
    result, coords = 0, None
    for row in range(0, len(asteroids)):
        for col in range(0, len(asteroids[row])):
            if not asteroids[row][col]:
                continue
            observation = len(observe(asteroids, (row, col)))
            if observation > result:
                result = observation
                coords = col, row
    return result, coords


def part2(asteroids, origin):
    targets = observe(asteroids, origin)
    nr_200 = obliterate(targets)[199]
    return (nr_200["original"][1] * 100) + nr_200["original"][0]


test_1_0 = """###
###
###"""

test_1_1 = """.#..#
.....
#####
....#
...##"""

test_1_2 = """......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####"""

test_1_3 = """#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###."""

test_1_4 = """.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#.."""

test_1_5 = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
"""


def test_part1():
    assert part1(read_input(test_1_0.split("\n"))) == (8, (1, 1))
    assert part1(read_input(test_1_1.split("\n"))) == (8, (3, 4))
    assert part1(read_input(test_1_2.split("\n"))) == (33, (5, 8))
    assert part1(read_input(test_1_3.split("\n"))) == (35, (1, 2))
    assert part1(read_input(test_1_4.split("\n"))) == (41, (6, 3))
    assert part1(read_input(test_1_5.split("\n"))) == (210, (11, 13))


def test_part2():
    assert part2(read_input(test_1_5.split("\n")), (13, 11)) == 802


def read_input(file):
    return [list(0 if c == "." else 1 for c in line.strip()) for line in file]


def main():
    with open(get_input(__file__)) as file:
        asteroids = read_input(file)
    print(part1(asteroids))
    print(part2(asteroids, (25, 22)))


if __name__ == "__main__":
    main()
