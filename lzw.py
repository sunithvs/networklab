def setup(reverse=False):
    table = {}
    for i in range(256):
        if reverse:
            table[i] = chr(i)
        else:
            table[chr(i)] = i
    return table


def encode(msg, table):
    output = []
    p = msg[0]
    for i in range(1, len(msg)):
        c = msg[i]
        # print(f"checking {p+c =}")
        if p + c in table:
            p = p + c
        else:
            # print(f'adding {p+c=}', len(table))
            output.append(table[p])
            table[p + c] = len(table)
            p = c
    output.append(table[p])
    print(table)
    return output


def decode(op, table):
    old = op[0]
    output = table[old]
    for n in op[1:]:
        if n not in table:
            table[n] = table[old] + table[old][0]
        else:
            table[len(table)] = table[old] + table[n][0]
        output += table[n]

        old = n
    return output


msg = "aaaabbbccccddddeeeeff"

encoded = encode(msg, setup())
decoded = decode(encoded, setup(True))
print(encoded)
print(decoded)
