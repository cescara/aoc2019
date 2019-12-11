from util import get_input
from interpreter import Interpreter


def generate(idx, params):
    if idx == 1:
        yield params
    else:
        yield from generate(idx - 1, params)

        for i in range(0, idx - 1):
            if idx % 2 == 0:
                params[i], params[idx - 1] = params[idx - 1], params[i]
            else:
                params[0], params[idx - 1] = params[idx - 1], params[0]
            yield from generate(idx - 1, params)


def run_amplifiers(program, settings):
    input_ = 0
    for setting in settings:
        input_ = Interpreter(program, [setting, input_]).run()[0]
    return input_


def run_feedback_loop(program, settings):
    result = None
    output = [0]
    interpreters = [Interpreter(program, [setting]) for setting in settings]
    while result is None:
        for count, interpreter in enumerate(interpreters):
            interpreter.receive_input(output)

            while not interpreter.halt:
                result = interpreter.step()
            output = interpreter.output.copy()
            interpreter.output = []
    return result[0]


def part1(program):
    print(max([run_amplifiers(program, settings) for settings in generate(5, [0, 1, 2, 3, 4])]))


def part2(program):
    print(max([run_feedback_loop(program, settings) for settings in generate(5, [5, 6, 7, 8, 9])]))


def test_part1():
    assert run_amplifiers(
            [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0], [4, 3, 2, 1, 0]) == 43210

    assert run_amplifiers(
            [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0],
            [0, 1, 2, 3, 4]) == 54321

    assert run_amplifiers(
            [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33, 1002, 33, 7, 33,
             1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99, 0, 0, 0], [1, 0, 4, 3, 2]) == 65210


def test_part2():
    assert run_feedback_loop([3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1,
                              28, 1005, 28, 6, 99, 0, 0, 5], [9, 8, 7, 6, 5])[0] == 139629729
    assert run_feedback_loop([3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54,
                              -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4,
                              53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10], [9, 7, 8, 5, 6])[0] == 18216


def main():
    with open(get_input(__file__)) as file:
        program = [int(x) for x in file.read().strip().split(",")]
    part1(program)
    part2(program)


if __name__ == "__main__":
    main()
