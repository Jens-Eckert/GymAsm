"""
Create program, each line will be an address each offset by just 1 for simplicity.
Basically just line numbers.
"""

from tokenizer import *
from evaluate import instructions


class Programifier:
    def __init__(self, tokens: list) -> None:
        self.tokens = tokens
        self.program = {}
        self.pos = 0
        self.line = 1

    def dewIt(self) -> dict:
        while self.pos < len(self.tokens):
            self.parseLine()
        return self.program

    def parseLine(self):
        token = self.tokens[self.pos]
        print(token)
        if type(token) is list:
            pass  # Label Register Number Or String
        elif type(token) is str and token in instructions.keys():
            typeo = instructions[self.tokens[self.pos]].type
            print(typeo)
            if typeo == "RType":
                line = [
                    token,
                    self.tokens[self.pos + 1],
                    self.tokens[self.pos + 2],
                    self.tokens[self.pos + 3],
                ]
                self.program[self.line] = line
                self.line += 1
                self.pos += 4
            elif typeo == "IType":
                line = [token, self.tokens[self.pos + 1], self.tokens[self.pos + 2]]
                self.program[self.line] = line
                self.line += 1
                self.pos += 3
            elif typeo == "JType":
                pass
        else:  # Comment
            pass


if __name__ == "__main__":
    t = Tokenizer()
    ts = t.tokenize("addi $bar1, 45\nsubi $45, 90")
    print(ts)
    p = Programifier(ts)
    gram = p.dewIt()
    print(gram)
