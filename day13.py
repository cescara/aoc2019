from util import get_input
from interpreter import Interpreter


chars = {0: "  ", 1: "██", 2: "▒▒", 3: "▄▄", 4: "◯"}


def chunk_list(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def paint(field, max_x, max_y):
    screen = [[None] * (max_x + 1) for _ in range(max_y + 1)]
    for x, y in field:
        if x >= 0:
            screen[y][x] = chars[field[(x, y)]]
        else:
            screen[y][x] = str(field[(x, y)])
    for row in screen:
        print("".join(row))


def part1(program):
    chunks = [*chunk_list(Interpreter(program).run(), 3)]
    return len([chunk for chunk in chunks if chunk[2] == 2])


def part2(program, debug=False):
    program[0] = 2               # cheat a little
    program[1606:1646] = [3]*40  # cheat a lot
    interpreter = Interpreter(program)

    field = {(x, y): t for x, y, t in chunk_list(interpreter.run(), 3)}
    max_x, max_y = max(field)

    while not interpreter.stop:
        if debug:
            paint(field, max_x, max_y)
        interpreter.receive_input([0])
        while not interpreter.halt:
            interpreter.step()
        for x, y, t in chunk_list(interpreter.output, 3):
            field[(x, y)] = t
        interpreter.output = []
    return field[(-1, 0)]


def main():
    with open(get_input(__file__)) as file:
        program = [int(x) for x in file.read().strip().split(",")]
    print(f"Bricks: {part1(program)}")
    print(f"Score: {part2(program)}")


if __name__ == '__main__':
    main()
