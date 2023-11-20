"""
Create program, each line will be an address each offset by just 1 for simplicity.
Basically just line numbers
"""

from tokenizer import *


class Programifier:
    def __init__(self, tokens: list) -> None:
        self.tokens = tokens
        self.program = {}

    def dewIt(self) -> dict:
        while 1:
            pass
        return self.program

    def parseLine(self, line: str):
        pass


if __name__ == "__main__":
    t = Tokenizer()
    ts = t.tokenize("addi $bar1, 45")
    p = Programifier(ts)
    gram = p.dewIt()
    print(gram)
