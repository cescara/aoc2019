from interpreter import Interpreter
from util import get_input


def read_input():
    with open(get_input(__file__)) as file:
        return [int(x) for x in file.read().strip().split(",")]


def part1():
    print(Interpreter(read_input(), 1).run())


def part2():
    print(Interpreter(read_input(), 5).run())


def test_part1():
    assert Interpreter([1002, 4, 3, 4, 33], 1).run() == []
    assert Interpreter([1101, 100, -1, 4, 0], 1).run() == []


def test_part2():
    assert Interpreter([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                       1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                       999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99], 7).run()[-1] == 999
    assert Interpreter([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                       1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                       999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99], 8).run()[-1] == 1000
    assert Interpreter([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                       1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                       999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99], 9).run()[-1] == 1001


if __name__ == '__main__':
    part1()
    part2()
