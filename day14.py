from typing import List
from math import ceil, floor
from util import get_input


def read_input(file):
    return {rule.result.name: rule for rule in [Rule.from_string(line.strip()) for line in file]}


class Component:
    def __init__(self, amount, name):
        self.amount = int(amount)
        self.name = name

    def __repr__(self):
        return f"{self.amount} {self.name}"

    @classmethod
    def from_string(cls, s):
        return cls(*s.split(" "))


class Rule:
    def __init__(self, components: List[Component], result: Component):
        self.components = components
        self.result = result

    def __repr__(self):
        return f"{self.components} => {self.result}"

    @classmethod
    def from_string(cls, s):
        components, result = s.split(" => ")
        return cls([Component.from_string(c) for c in components.split(", ")], Component.from_string(result))


def produce(rules, name, material):
    if name == "ORE":
        return
    if material[name] >= 0:
        return

    amount = rules[name].result.amount
    factor = ceil((-material[name]) / amount)
    material[name] += factor * amount
    for component in rules[name].components:
        material[component.name] -= factor * component.amount
        produce(rules, component.name, material)


def part1(rules):
    material = {rule: 0 for rule in rules.keys()}
    material["ORE"] = 0
    material["FUEL"] = -1
    produce(rules, "FUEL", material)
    return -material["ORE"]


def part2(rules):
    material = {rule: 0 for rule in rules.keys()}
    material["ORE"] = 0
    material["FUEL"] = -1
    fuel = 0
    while material["ORE"] > -1000000000000:
        if fuel == 5000:
            fraction = (1000000000000 + 100 * material["ORE"]) / -material["ORE"]
            # print(f"\n  Ore: {material['ORE']}")
            # print(f"  fraction: {fraction}")
            fuel = floor(fuel * fraction)
            for key in material:
                if key == "FUEL":
                    continue
                material[key] = floor(material[key] * fraction)
        material["FUEL"] = -1
        produce(rules, "FUEL", material)
        fuel += 1
    # print([*material.values()])
    # print(fuel-1)
    return fuel - 1


# def part2(rules):
#     material = {rule: 0 for rule in rules.keys()}
#     material["ORE"] = 0
#     material["FUEL"] = -1
#     fuel = 0
#     while material["ORE"] > -1000000000000:
#         if {v for k, v in material.items() if k not in ("FUEL", "ORE")} == {0} and fuel > 0:
#             fraction = 1000000000000 / -material["ORE"]
#             fuel = floor(fuel * fraction)
#             material["ORE"] = floor(material["ORE"] * fraction)
#         material["FUEL"] = -1
#         produce(rules, "FUEL", material)
#         fuel += 1
#     return fuel - 1


test_1_0 = """10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL""".split("\n")

test_1_1 = """9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL""".split("\n")

test_1_2 = """157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT""".split("\n")

test_1_3 = """2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
17 NVRVD, 3 JNWZP => 8 VPVL
53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
22 VJHF, 37 MNCFX => 5 FWMGM
139 ORE => 4 NVRVD
144 ORE => 7 JNWZP
5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
145 ORE => 6 MNCFX
1 NVRVD => 8 CXFTF
1 VJHF, 6 MNCFX => 4 RFSQX
176 ORE => 6 VJHF""".split("\n")

test_1_4 = """171 ORE => 8 CNZTR
7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
114 ORE => 4 BHXH
14 VRPVC => 6 BMBT
6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
5 BMBT => 4 WPTQ
189 ORE => 9 KTJDG
1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
12 VRPVC, 27 CNZTR => 2 XDBXC
15 KTJDG, 12 BHXH => 5 XCVML
3 BHXH, 2 VRPVC => 7 MZWV
121 ORE => 7 VRPVC
7 XCVML => 6 RJRHP
5 BHXH, 4 VRPVC => 5 LTCX""".split("\n")


def _test_part1():
    assert part1(read_input(test_1_0)) == 31
    assert part1(read_input(test_1_1)) == 165
    assert part1(read_input(test_1_2)) == 13312
    assert part1(read_input(test_1_3)) == 180697
    assert part1(read_input(test_1_4)) == 2210736


def test_part2_1():
    print(82892753)
    assert part2(read_input(test_1_2)) == 82892753


def test_part2_2():
    print(5586022)
    assert part2(read_input(test_1_3)) == 5586022


def test_part2_3():
    print(460664)
    assert part2(read_input(test_1_4)) == 460664


def main():
    with open(get_input(__file__)) as file:
        rules = read_input(file)
    print(part1(rules))
    print(part2(rules))


if __name__ == '__main__':
    main()
