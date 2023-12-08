"""
Creates list version of gasm program.
"""

import re
from sys import argv

Whitespace = None

patterns = [
    [r"\s+", Whitespace],
    [r"\#.*", "Comment"],
    [r"[a-zA-Z]+\:", "Label"],
    [r"[a-zA-Z]+", "Operator"],  # Operator or operand that is a label
    [r"\,\s", "Separator"],
    [r"\.[a-z]+|\ \d+", "Section"],
    [r"\"([^\"]|\"\")*\"", "String"],
    [r"\d+(\.\d*)?", "Number"],
    [r"\$[a-z0-9]{1,6}", "Register"],
    [r".", "Error"],
]


def tokenize(characters: str) -> list:
    # print('Tokenizing "' + characters + '"')

    tokens = []
    pos = 0

    while pos < len(characters):
        for regex, token in patterns:
            pattern = re.compile(regex)
            match = pattern.match(characters, pos)

            if match:
                break

        assert match
        pos = match.end()

        if token == Whitespace or token == "Separator":
            continue

        assert token != "Error", "Syntax Error: illegal character at " + match.group(0)

        tokens.append(match.group(0))
    return tokens


def number(s: str):
    if "." in s:
        return float(s)
    else:
        return int(s)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Please supply a .gasm input file.")
        print("USAGE: python3 tokenizer.py <FILE>.gasm")
        exit(69)

    if not argv[1].endswith(".gasm"):
        print("Not a .gasm file")
        exit(69)

    lines = ""

    with open(argv[1]) as f:
        lines = "".join(f.readlines())

    print(lines)

    tokens = tokenize(lines)

    intFileName = argv[1].removesuffix(".gasm") + ".gimp"

    with open(intFileName, "w") as f:
        f.write(tokens.__str__())
