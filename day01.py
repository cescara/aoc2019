def read_input(file_path):
    with open(file_path) as file:
        return [int(line.strip()) for line in file]


def calculate_fuel(mass):
    return (mass // 3) - 2


def calculate_additional_fuel(mass):
    total = 0
    while True:
        fuel = calculate_fuel(mass)
        if fuel < 0:
            return total
        total += fuel
        mass = fuel


def part1(values):
    return sum(calculate_fuel(mass) for mass in values)


def part2(values):
    return sum(calculate_additional_fuel(mass) for mass in values)


def test_part1():
    assert part1([12]) == 2
    assert part1([14]) == 2
    assert part1([1969]) == 654
    assert part1([100756]) == 33583


def test_part2():
    assert part2([12]) == 2
    assert part2([14]) == 2
    assert part2([1969]) == 966
    assert part2([100756]) == 50346


if __name__ == '__main__':
    values_ = read_input("input/day01")

    print(f"\nResult Part 1: {part1(values_)}\n\n")
    print(f"\nResult Part 2: {part2(values_)}")

