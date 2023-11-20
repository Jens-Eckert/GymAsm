import re

Whitespace = None

patterns = [
    [r"\s+", Whitespace],
    [r"\#.*", "Comment"],
    [r"[a-z]+\:", "Label"],
    [r"[a-z]+", "Operator"],
    [r"\.[a-z]+|\ \d+", "Modifer"],
    [r"\"([^\"]|\"\")*\"", "String"],
    [r"\d+(\.\d*)?", "Number"],
    [r"\$[a-z0-9]{2}", "Register"],
    [r"supbro", "Syscall"],
    [r".", "Error"],
]


def number(s: str):
    if "." in s:
        return float(s)
    else:
        return int(s)


def tokenize(characters: str):
    print('Tokenizing "', characters, '"')
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

        if token == Whitespace:
            continue

        assert token != "Error", "Syntax Error: illegal character at " + match.group(0)

        if token == "Number":
            tokens.append([token, number(match.group(0))])
            continue

        if token == "String" or token == "Label":
            tokens.append([token, match.group(0)])
            continue

        tokens.append(token)
    return tokens


def testSimple():
    pass


if __name__ == "__main__":
    testSimple()
