from typing import Callable


Register = ["Register", str]
Immediate = int
Address = int


class Environment:
    def __init__(self):
        self.registers = {
            # Zeros
            "$0": 0,
            "$zero": 0,
            # Temporaries
            "$45": 0,
            "$90": 0,
            "$135": 0,
            "$180": 0,
            # Saved Temporaries
            "$bar1": 0,
            "$bar2": 0,
            "$bar3": 0,
            "$bar4": 0,
            # Function results and Syscall numbers
            "$pr1": 0,
            "$pr2": 0,
            # Arguments
            "$bnch": 0,
            "$sqat": 0,
            "$dlft": 0,
            "$curl": 0,
            "$rep": 0,  # return address
            "$rack": 0,  # stack pointer
        }

        self.memory = {}

        for x in range(0, 2**16):
            self.memory[x] = 0

    def run(self, program: list):
        pass


class Operation:
    def __init__(self, type: str, func: Callable):
        self.func = func
        self.type = type

    def __call__(self, *args):
        pass


instructions = {
    "add": Operation(
        "RType", lambda r1, r2, env: env.registers[r1] + env.registers[r2]
    ),
    "addi": Operation("IType", lambda r1, i, env: env.registers[r1] + i),
    "sub": Operation(
        "RType", lambda r1, r2, env: env.registers[r1] - env.registers[r2]
    ),
    "subi": Operation("IType", lambda r1, i, env: env.registers[r1] - i),
}

if __name__ == "__main__":
    env = Environment()

    print(env.registers)
    # print(env.memory)
