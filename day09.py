from util import get_input
from interpreter import Interpreter


def part1(program):
    return Interpreter(program, [1]).run()


def part2(program):
    return Interpreter(program, [2]).run()


def test_part1():
    assert Interpreter([109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]).run() == \
           [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    assert len(str(Interpreter([1102, 34915192, 34915192, 7, 4, 7, 99, 0]).run()[0])) == 16
    assert Interpreter([104, 1125899906842624, 99]).run()[0] == 1125899906842624
    assert Interpreter([109, -1, 4, 1, 99]).run()[0] == -1
    assert Interpreter([109, -1, 104, 1, 99]).run()[0] == 1
    assert Interpreter([109, -1, 204, 1, 99]).run()[0] == 109
    assert Interpreter([109, 1, 9, 2, 204, -6, 99]).run()[0] == 204
    assert Interpreter([109, 1, 109, 9, 204, -6, 99]).run()[0] == 204
    assert Interpreter([109, 1, 209, -1, 204, -106, 99]).run()[0] == 204
    assert Interpreter([109, 1, 3, 3, 204, 2, 99]).run()[0] == 0
    assert Interpreter([109, 1, 203, 2, 204, 2, 99]).run()[0] == 0


def main():
    with open(get_input(__file__)) as file:
        program = [int(x) for x in file.read().strip().split(",")]

    print(part1(program))
    print(part2(program))


if __name__ == '__main__':
    main()
