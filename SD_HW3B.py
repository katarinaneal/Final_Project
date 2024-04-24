def to_hex_string(data):
    strg = ""
    for i in data:
        h = hex(i)
        strg += h[2:]

    return strg


def count_runs(flat_data):
    runs = 0
    if len(flat_data) == 0:
        return runs

    elem = flat_data[0]
    count = 1
    runs = 1

    for i in range(1, len(flat_data)):
        if count == 15:
            runs += 1
            elem = flat_data[i]
            count = 1
        elif elem != flat_data[i]:
            runs += 1
            elem = flat_data[i]
            count = 1
        else:
            count += 1

    return runs


def encode_rle(flat_data):
    n = len(flat_data)
    i = 0
    result = []

    while i < n:
        count = 1
        while (i + 1 < n and flat_data[i] == flat_data[i + 1]):
            count += 1
            if count == 15:
                # result.extend([int(count),flat_data[i]])
                i += 1
                break;
            i += 1
        if (i == n):
            result.extend([int(count), flat_data[i - 1]])
        else:
            result.extend([int(count), flat_data[i]])
        i += 1

    return result


def get_decoded_length(rle_data):
    length = 0
    for i in range(0, len(rle_data), 2):
        length += rle_data[i]
    return length

def decode_rle(rle_data):
    flat_data = []
    for i in range(0, len(rle_data), 2):
        count = rle_data[i]
        value = rle_data[i+1]
        flat_data.extend([value]*count)
    return flat_data

def string_to_data(data_string):
    byte_data = []

    for char in data_string:
        byte = int(char, 16)
        byte_data.append(byte)

    return byte_data


def to_rle_string(rle_data):
    rle_string = ""

    for i in range(0, len(rle_data), 2):
        rle_string += str(rle_data[i])

        rle_string += hex(rle_data[i + 1])[-1]

        if i != len(rle_data) - 2:
            rle_string += ":"

    return rle_string


def string_to_rle(rle_string):
    rle_data = []

    lst = rle_string.split(":")

    for element in lst:
        run_length = int(element[0:-1])

        run_value = int(element[-1], 16)

        rle_data.append(run_length)
        rle_data.append(run_value)

    return rle_data




