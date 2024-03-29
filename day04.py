from util import get_input


def part1(password):
    if len(password) != 6:
        return False

    same_digits = False
    last_digit = "0"
    for digit in password:
        if last_digit > digit:
            return False
        if last_digit == digit:
            same_digits = True
        last_digit = digit

    return same_digits


def part2(password):
    chk = {str(dg): 0 for dg in range(1, 10)}

    if len(password) != 6:
        return False

    last_digit = "0"
    for digit in password:
        if last_digit > digit:
            return False
        chk[digit] += 1
        last_digit = digit

    return 2 in chk.values()


def test_part1():
    assert part1("111111")
    assert part1("223450") is False
    assert part1("123789") is False


def test_part2():
    assert part2("112233")
    assert part2("123444") is False
    assert part2("111122")


def main():
    with open(get_input(__file__)) as file:
        pw_range = list(map(int, file.read().strip().split("-")))

    candidates_part1 = [password for password in range(pw_range[0], pw_range[1]) if part1(str(password))]
    print(len(candidates_part1))

    candidates_part2 = [password for password in range(pw_range[0], pw_range[1]) if part2(str(password))]
    print(len(candidates_part2))


if __name__ == "__main__":
    main()
