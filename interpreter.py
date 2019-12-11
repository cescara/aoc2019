from typing import Iterator


def parse_instruction(instruction) -> Iterator[int]:
    tmp = str(instruction)
    if len(tmp) == 1:
        tmp = tmp.zfill(2)

    yield int(tmp[-2:])
    for mode in reversed(tmp[:-2]):
        yield int(mode)

    while True:
        yield 0


class Interpreter:
    def __init__(self, program, input_=(0,)):
        self.program = program.copy()
        self.input = iter(input_)
        self.idx: int = 0
        self.output = []
        self.halt = False
        self.opcodes = {
            1: self.add,
            2: self.mul,
            3: self.mov,
            4: self.out,
            5: self.jit,
            6: self.jif,
            7: self.lt,
            8: self.eq,
        }

    def add(self, params):
        self.program[params[2]] = params[0] + params[1]
        self.idx += 1

    def mul(self, params):
        self.program[params[2]] = params[0] * params[1]
        self.idx += 1

    def mov(self, params):
        try:
            self.program[params[0]] = next(self.input)
            self.idx += 1
        except StopIteration:
            self.idx -= 1
            self.halt = True

    def out(self, params):
        self.output.append(self.program[params[0]])
        self.idx += 1

    def jit(self, params):
        if params[0]:
            self.idx = params[1]
        else:
            self.idx += 1

    def jif(self, params):
        if not params[0]:
            self.idx = params[1]
        else:
            self.idx += 1

    def lt(self, params):
        self.program[params[2]] = int(params[0] < params[1])
        self.idx += 1

    def eq(self, params):
        self.program[params[2]] = int(params[0] == params[1])
        self.idx += 1

    def run(self):
        while not self.halt:
            self.step()
        return self.output

    def step(self):
        instruction = parse_instruction(self.program[self.idx])
        opcode = next(instruction)

        if opcode == 99:
            self.halt = True
            return self.output

        params = []
        if opcode == 3 or opcode == 4:
            params.append(self.get_idx(next(instruction)))
        elif opcode == 5 or opcode == 6:
            params.append(self.program[self.get_idx(next(instruction))])
            params.append(self.program[self.get_idx(next(instruction))])
        else:
            params.append(self.program[self.get_idx(next(instruction))])
            params.append(self.program[self.get_idx(next(instruction))])
            params.append(self.get_idx(next(instruction)))

        idx = self.idx
        self.opcodes[opcode](params)

    def get_idx(self, mode):
        self.idx += 1
        if mode == 0:
            return self.program[self.idx]
        if mode == 1:
            return self.idx

    def receive_input(self, input_):
        self.halt = False
        self.input = iter([*self.input, *input_])
