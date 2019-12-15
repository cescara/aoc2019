from util import get_input
from interpreter import Interpreter


dirs = {
    ((0, 1), 0): (-1, 0),
    ((0, 1), 1): (1, 0),
    ((1, 0), 0): (0, 1),
    ((1, 0), 1): (0, -1),
    ((0, -1), 0): (1, 0),
    ((0, -1), 1): (-1, 0),
    ((-1, 0), 0): (0, -1),
    ((-1, 0), 1): (0, 1)
}


def paint(program, start_input):
    result = None
    interpreter = Interpreter(program, [start_input])
    current = (0, 0)
    current_dir = (1, 0)
    panels = {current: [start_input]}

    while True:
        while not interpreter.halt:
            result = interpreter.step()
        if result is not None:
            break

        panels[current].append(interpreter.output[0])
        current_dir = dirs[(current_dir, interpreter.output[1])]
        current = (current[0] + current_dir[0], current[1] + current_dir[1])
        if current not in panels:
            panels[current] = [0]
        interpreter.receive_input([panels[current][-1]])
        interpreter.output = []

    return panels


def part1(program):
    panels = paint(program, 0)
    return len(panels)


def part2(program):
    panels = paint(program, 1)

    sorted_panels = sorted(panels, key=lambda x: x)
    for i in range(sorted_panels[0][0], sorted_panels[-1][0] + 1):
        for j in range(sorted_panels[0][1], sorted_panels[-1][1] + 1):
            if (i, j) not in panels:
                continue
            if panels[(i, j)][-1] == 0:
                print("░░", end="")
            else:
                print("██", end="")
        print("")


def main():
    with open(get_input(__file__)) as file:
        program = [int(x) for x in file.read().strip().split(",")]

    print(part1(program))
    part2(program)


if __name__ == "__main__":
    main()

