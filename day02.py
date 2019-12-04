def run_program(instructions):
    for idx in range(0, len(instructions), 4):
        opcode = instructions[idx]
        if opcode == 99:
            return instructions
        noun = instructions[idx + 1]
        verb = instructions[idx + 2]
        output = instructions[idx + 3]
        if opcode == 1:
            instructions[output] = instructions[noun] + instructions[verb]
        elif opcode == 2:
            instructions[output] = instructions[noun] * instructions[verb]

    raise ValueError("Format not as expected.")


def part1(instructions):
    instructions_ = instructions.copy()
    instructions_[1] = 12
    instructions_[2] = 2
    run_program(instructions_)

    return instructions_[0]


def part2(instructions):
    for i in range(0, 99):
        for j in range(0, 99):
            instructions_ = instructions.copy()
            instructions_[1] = i
            instructions_[2] = j
            run_program(instructions_)
            if instructions_[0] == 19690720:
                return 100 * i + j


def test_part1():
    assert run_program([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert run_program([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert run_program([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert run_program([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]


if __name__ == '__main__':
    with open("input/day02") as file:
        program = [int(x) for x in file.read().strip().split(",")]
    print(f"\nPart 1: {part1(program)}")
    print(f"\nPart 2: {part2(program)}")
