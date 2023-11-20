"""
Creates list version of gasm program.
"""

import re

Whitespace = None

patterns = [
    [r"\s+", Whitespace],
    [r"\#.*", "Comment"],
    [r"[a-zA-Z]+\:", "Label"],
    [r"[a-zA-Z]+", "Operator"],  # Operator or operand that is a label
    [r"\,\s", "Separator"],
    [r"\.[a-z]+|\ \d+", "Modifer"],
    [r"\"([^\"]|\"\")*\"", "String"],
    [r"\d+(\.\d*)?", "Number"],
    [r"\$[a-z0-9]{1,6}", "Register"],
    [r".", "Error"],
]


class Tokenizer:
    def tokenize(self, characters: str) -> list:
        print('Tokenizing "' + characters + '"')

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

            assert (
                token != "Error"
            ), "Syntax Error: illegal character at " + match.group(0)

            if token == "Number":
                tokens.append([token, self.number(match.group(0))])
                continue

            if (
                token == "String"
                or token == "Label"
                or token == "Modifier"
                or token == "Register"
            ):
                tokens.append([token, match.group(0)])
                continue

            tokens.append(match.group(0))
        return tokens

    def number(self, s: str):
        if "." in s:
            return float(s)
        else:
            return int(s)


def testSimple():
    t = Tokenizer()
    tokens = t.tokenize("main:\n\taddi $bar1, 45\nsubi $bar1, 90")
    print(tokens)
    print(t.tokenize("# This comment is cool\nsub $bar1, 90"))


if __name__ == "__main__":
    testSimple()
