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
    def __init__(self, program, input_ = 0):
        self.program = program
        self.input = input_
        self.idx: int = 0
        self.codes = []
        self.opcodes = {1: self.add, 2: self.mul, 3: self.mov, 4: self.out,
                        5: self.jit, 6: self.jif, 7: self.lt, 8: self.eq}

    def add(self, params):
        self.program[params[2]] = params[0] + params[1]

    def mul(self, params):
        self.program[params[2]] = params[0] * params[1]

    def mov(self, params):
        self.program[params[0]] = self.input

    def out(self, params):
        self.codes.append(self.program[params[0]])

    def jit(self, params):
        if params[0]:
            self.idx = params[1]

    def jif(self, params):
        if not params[0]:
            self.idx = params[1]

    def lt(self, params):
        self.program[params[2]] = int(params[0] < params[1])

    def eq(self, params):
        self.program[params[2]] = int(params[0] == params[1])

    def run(self):
        while True:
            instruction = parse_instruction(self.program[self.idx])
            opcode = next(instruction)

            if opcode == 99:
                return self.codes

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

            if idx == self.idx:
                self.idx += 1

    def get_idx(self, mode):
        self.idx += 1
        if mode == 0:
            return self.program[self.idx]
        if mode == 1:
            return self.idx
