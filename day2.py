def compute_intcode(lst):
    for idx in range(0, len(lst), 4):
        opcode = lst[idx]
        if opcode == 99:
            return
        input1 = lst[idx + 1]
        input2 = lst[idx + 2]
        output = lst[idx + 3]
        if opcode == 1:
            lst[output] = lst[input1] + lst[input2]
        elif opcode == 2:
            lst[output] = lst[input1] * lst[input2]


def part1(lst):
    copy = lst.copy()
    copy[1] = 12
    copy[2] = 2
    compute_intcode(copy)

    return copy[0]


def part2(lst):
    for i in range(0, 99):
        for j in range(0, 99):
            copy = lst.copy()
            copy[1] = i
            copy[2] = j
            compute_intcode(copy)
            if copy[0] == 19690720:
                return 100 * i + j


test_data = """\
1,0,0,0,99:2,0,0,0,99
2,3,0,3,99:2,3,0,6,99
2,4,4,5,99,0:2,4,4,5,99,9801
1,1,1,4,99,5,6,0,99:30,1,1,4,2,5,6,0,99
"""

if __name__ == '__main__':
    for input_, expected_output in [[[1, 0, 0, 0, 99], [2, 0, 0, 0, 99]],
                                    [[2, 3, 0, 3, 99], [2, 3, 0, 6, 99]],
                                    [[2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]],
                                    [[1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]]]:
        compute_intcode(input_)
        print(f"expected output: {expected_output}\noutput:          {input_}")

    with open("input/day2") as file:
        lst_ = [int(x) for x in file.read().strip().split(",")]
    print(f"\nPart 1: {part1(lst_)}")
    print(f"\nPart 2: {part2(lst_)}")
