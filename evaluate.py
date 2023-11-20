from typing import Callable


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


add: Callable[[str, str, Environment], int] = (
    lambda r1, r2, env: env.registers[r1] + env.registers[r2]
)
addi: Callable[[str, int, Environment], int] = lambda r1, i, env: env.registers[r1] + i

sub: Callable[[str, str, Environment], int] = (
    lambda r1, r2, env: env.registers[r1] - env.registers[r2]
)
subi: Callable[[str, int, Environment], int] = lambda r1, i, env: env.registers[r1] - i

mult: Callable[[str, str, Environment], int] = (
    lambda r1, r2, env: env.registers[r1] * env.registers[r2]
)
multi: Callable[[str, int, Environment], int] = lambda r1, i, env: env.registers[r1] * i

div: Callable[[str, str, Environment], int] = (
    lambda r1, r2, env: env.registers[r1] // env.registers[r2]
)
divi: Callable[[str, int, Environment], int] = lambda r1, i, env: env.registers[r1] // i


instructions = [add, addi, sub, subi]

if __name__ == "__main__":
    env = Environment()

    print(env.registers)
    # print(env.memory)
