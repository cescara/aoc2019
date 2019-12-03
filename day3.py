def walk_coordinates(instructions):
    coordinates = {}
    x, y, steps = 0, 0, 1

    for instruction in instructions:
        direction, step_count = instruction[0], int(instruction[1:])
        points = range(1, step_count + 1)

        if direction == "R":
            for point in points:
                coordinates[(x + point, y)] = steps
                steps += 1
            x += step_count
        elif direction == "D":
            for point in points:
                coordinates[(x, y - point)] = steps
                steps += 1
            y -= step_count
        elif direction == "L":
            for point in points:
                coordinates[(x - point, y)] = steps
                steps += 1
            x -= step_count
        elif direction == "U":
            for point in points:
                coordinates[(x, y + point)] = steps
                steps += 1
            y += step_count

    return coordinates


def find_crosses(wire_1, wire_2):
    return set(wire_1).intersection(set(wire_2))


def manhattan_dist(crosses):
    for x, y in crosses:
        yield abs(x) + abs(y)


def part1(wires):
    coordinates = [walk_coordinates(wire) for wire in wires]
    crosses = find_crosses(*coordinates)

    return min(manhattan_dist(crosses))


def part2(wires):
    coordinates = [walk_coordinates(wire) for wire in wires]
    crosses = find_crosses(*coordinates)

    return min([coordinates[0][cross] + coordinates[1][cross] for cross in crosses])


test1 = '''R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83'''

result1_1 = 159
result1_2 = 610

test2 = '''R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'''

result2_1 = 135
result2_2 = 410


if __name__ == '__main__':
    wires_test1 = [wires_test1.strip().split(",") for wires_test1 in test1.split("\n")]
    wires_test2 = [wires_test2.strip().split(",") for wires_test2 in test2.split("\n")]

    with open("input/day3") as file:
        real_wires = [line.strip().split(",") for line in file]

    print(result1_1, part1(wires_test1))
    print(result2_1, part1(wires_test2))
    print(part1(real_wires))

    print(result1_2, part2(wires_test1))
    print(result2_2, part2(wires_test2))
    print(part2(real_wires))




