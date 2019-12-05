from interpreter import Interpreter


def part1():
    with open("input/day05") as file:
        program = [int(x) for x in file.read().strip().split(",")]
    print(Interpreter([1002, 4, 3, 4, 33], 1).run())
    print(Interpreter([1101, 100, -1, 4, 0], 1).run())
    print(Interpreter(program, 1).run())


def part2():
    with open("input/day05") as file:
        program = [int(x) for x in file.read().strip().split(",")]
    print(Interpreter([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                       1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                       999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99], 7).run())
    print(Interpreter([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                       1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                       999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99], 8).run())
    print(Interpreter([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                       1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                       999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99], 9).run())
    print(Interpreter(program, 5).run())


def test_part01():
    ...
    # assert run([1002, 4, 3, 4, 33], 1) == []
    # assert run([1101, 100, -1, 4, 0], 1) == []


if __name__ == '__main__':
    part1()
    part2()
