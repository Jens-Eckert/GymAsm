"""
Create program, each line will be an address each offset by just 1 for simplicity.
Basically just line numbers
"""

from tokenizer import *
from evaluate import validInstructionNames, instructionTypes


class Programifier:
    def __init__(self, tokens: list) -> None:
        self.tokens = tokens
        self.program = {}
        self.pos = 0

    def dewIt(self) -> dict:
        self.parseLine()
        return self.program

    def parseLine(self):
        token = self.tokens[self.pos]
        print(token)
        if type(token) is list:
            pass  # Label Register Number Or String
        elif type(token) is str and token in validInstructionNames.keys():
            typeo = validInstructionNames[self.tokens[self.pos]]
            print(typeo)
            if typeo == "RType":
                line = [
                    token,
                    self.tokens[self.pos + 1],
                    self.tokens[self.pos + 2],
                    self.tokens[self.pos + 3],
                ]
                print(line)
            elif typeo == "IType":
                line = [token, self.tokens[self.pos + 1], self.tokens[self.pos + 2]]
                print(line)
            elif typeo == "JType":
                pass
        else:  # Comment
            pass


if __name__ == "__main__":
    t = Tokenizer()
    ts = t.tokenize("addi $bar1, 45")
    print(ts)
    p = Programifier(ts)
    gram = p.dewIt()
    print(gram)
