def number_of_parity(data):
    m = len(data)
    r = 0
    while 2 ** r < m + r + 1:
        r += 1
    return r


def place_parity_bits(data, r):
    c = 0
    new_data = []
    for i in range(1, r + len(data) + 1):
        if i == 2 ** c:
            new_data.insert(0, 0)
            c += 1
        else:
            new_data.insert(0, int(data[-1]))
            data = data[:-1]
    return new_data


def hamming(data):
    r = number_of_parity(data)
    hamming_bits = place_parity_bits(data, r)
    for i in range(r + 1):
        for j in range(2 ** i + 1, len(hamming_bits) + 1):
            if j & 2 ** i == 2 ** i:
                hamming_bits[-1 * 2 ** i] ^= hamming_bits[-j]
    return hamming_bits


def decode(data):
    m = len(data)
    i = 0
    # res = 0
    arr = []
    while 2 ** i < m:
        val = 0
        for j in range(1, m + 1):
            if j & 2 ** i == 2 ** i:
                # print(val, data[-j], 2 ** i)
                val ^= data[-j]
        # res = res + val * (10 ** i)
        arr.append(val)
        i += 1
    print(arr[::-1])


msg = list("10110")
print(hamming("1011001"))
decode([1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0])
