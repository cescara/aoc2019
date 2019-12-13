from util import get_input


def decode(layers):
    for i in range(0, len(layers[0])):
        for layer in layers:
            if layer[i] != "2":
                yield layer[i]
                break


def part1(layers):
    layers.sort(key=lambda layer: layer.count("0"))
    print(layers[0].count("1") * layers[0].count("2"))


def part2(layers):
    image = [*decode(layers)]
    for col in range(0, len(image), 25):
        print("".join(image[col : col + 25]))


def main():
    with open(get_input(__file__)) as file:
        file_input = file.read().strip()

    layers = [
        file_input[layer: layer + 25 * 6]
        for layer in range(0, len(file_input), 25 * 6)
    ]
    part1(layers.copy())
    part2(layers)


if __name__ == "__main__":
    main()
