from util import get_input
from itertools import count
from math import gcd
import re


def read_input(file):
    return [Vector.from_string(x.strip()) for x in file]


def cmp(i, j):
    return (i < j) - (i > j)


def lcm(x, y, z):
    gcd_yz = gcd(y, z)
    lcm_yz = y * z // gcd_yz
    lcm_xyz = x * lcm_yz // gcd(x, lcm_yz)
    return lcm_xyz


class Vector:
    __slots__ = ("x", "y", "z")
    pattern = re.compile(r".*<x=(?P<x> *-?\d+), y=(?P<y> *-?\d+), z=(?P<z> *-?\d+)>")

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __repr__(self):
        return f"Vector <x={self.x}, y={self.y}, z={self.z}>"

    def state_code(self):
        return hash((self.x, self.y, self.z))

    def gravitate(self, others):
        result = Vector()
        for other in others:
            if other == self:
                continue
            result += Vector(cmp(self.x, other.x), cmp(self.y, other.y), cmp(self.z, other.z))
        return result

    def abs_sum(self):
        return sum(map(abs, (self.x, self.y, self.z)))

    @classmethod
    def from_string(cls, s):
        match = cls.pattern.match(s)
        if match is None:
            raise ValueError
        return cls(int(match.group("x")), int(match.group("y")), int(match.group("z")))


def get_states(moons):
    return {attr: tuple(getattr(moon, attr) for moon in moons) for attr in "xyz"}


def part1(moons: list, steps):
    velocities, energy = {moon: Vector() for moon in moons}, []
    for step in range(steps + 1):
        energy = []
        print(f"After {step} steps:")
        for moon, vel in velocities.items():
            moon += vel
            moon_energy = moon.abs_sum() * vel.abs_sum()
            energy.append(moon_energy)
            print(f"pos={moon}, vel={vel}, total_energy={moon_energy}")
        for moon in moons:
            velocities[moon] += moon.gravitate(moons)
        print(f"Sum of total energy: {energy} => {sum(energy)}\n")
    return sum(energy)


def part2(moons: list):
    velocities = {moon: Vector() for moon in moons}
    first_loops = dict.fromkeys("xyz")
    initial_states = get_states(moons)
    for steps in count():
        for moon, vel in velocities.items():
            moon += vel
        for attr, state in get_states(moons).items():
            if steps and not first_loops[attr] and state == initial_states[attr]:
                first_loops[attr] = steps + 1
        for moon in moons:
            velocities[moon] += moon.gravitate(moons)
        if all(first_loops.values()):
            break
    return lcm(*first_loops.values())


test_1_0 = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""

test_1_1 = """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>"""


def test_part1():
    assert part1(read_input(test_1_0.split("\n")), 10) == 179
    assert part1(read_input(test_1_1.split("\n")), 100) == 1940


def test_part2():
    assert part2(read_input(test_1_0.split("\n"))) == 2772
    assert part2(read_input(test_1_1.split("\n"))) == 4686774924


def main():
    with open(get_input(__file__)) as file:
        moons = read_input(file)
    print(part1(moons.copy(), 1000))
    print(part2(moons))


if __name__ == '__main__':
    main()
