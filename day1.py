def calculate_fuel(mass):
    return (mass // 3) - 2


def read_input(file_path):
    with open(file_path) as file:
        return [int(line.strip()) for line in file]


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


if __name__ == '__main__':
    values_ = read_input("input/day1")

    for input_, expected_output in [[12, 2], [14, 2], [1969, 654], [100756, 33583]]:
        print(f"{input_}: (expected {expected_output}) {calculate_fuel(input_)}")
    print(f"\nResult Part 1: {part1(values_)}\n\n")

    for input_, expected_output in [[12, 2], [14, 2], [1969, 966], [100756, 50346]]:
        print(f"{input_}: (expected {expected_output}) {calculate_additional_fuel(input_)}")
    print(f"\nResult Part 2: {part2(values_)}")

