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


def test_part1():
    assert part1([line.strip().split(",") for line in
                  ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]]) == 159
    assert part1([line.strip().split(",") for line in
                  ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]]) == 135


def test_part2():
    assert part2([line.strip().split(",") for line in
                  ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]]) == 610
    assert part2([line.strip().split(",") for line in
                  ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]]) == 410


if __name__ == '__main__':
    with open("input/day03") as file:
        real_wires = [line.strip().split(",") for line in file]

    print(part1(real_wires))
    print(part2(real_wires))




