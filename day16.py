with open("day16.in") as f:
    INPUT = f.read()

# INPUT = "D2FE28"
# INPUT = "38006F45291200"
# INPUT = "8A004A801A8002F478"

bin_input = ""
for byte in bytearray.fromhex(INPUT):
    sbyte = str(bin(byte))[2:]
    if len(sbyte) < 8:
        sbyte = "0" * (8 - len(sbyte)) + sbyte
    bin_input += sbyte

# print(bin_input)
# assert(len(bin_input) == len(INPUT) * 4)

def val(b_in, index, l):
    return int(b_in[index:index + l], base=2)


def parse_literal(bin_input):
    literal = ""
    index = 0
    for i in range(0, len(bin_input), 5):
        chunk = bin_input[i:i + 5]
        literal += chunk[1:]
        index += 5
        if chunk[0] == "0":
            break

    return int(literal, base=2), index


def parse_packet(bin_input):
    print("parse packet")
    if len(bin_input) < 6:
        return 0, 0, 0

    index = 0
    version_sum = 0

    version = val(bin_input, index, 3)
    version_sum += version
    type_id = val(bin_input, index + 3, 3)
    index += 6
    print(version, type_id)

    if type_id == 4:
        # literal
        print("parse literal")
        lit, sub_index = parse_literal(bin_input[index:])
        print("literal", lit)
        return index + sub_index, version_sum, lit

    print("parse operator")
    length_type_id = bin_input[index]
    index += 1

    values = []
    if length_type_id == "0":
        subpacket_len = val(bin_input, index, 15)
        index += 15
        total_parsed = 0
        print("parse subpacket len", subpacket_len)
        while total_parsed < subpacket_len:
            sub_index, sub_version_sum, value = parse_packet(bin_input[index:])
            index += sub_index
            total_parsed += sub_index
            version_sum += sub_version_sum
            values.append(value)
    else:
        subpacket_count = val(bin_input, index, 11)
        index += 11
        print("parse subpacket count", subpacket_count)
        for c in range(subpacket_count):
            sub_index, sub_version_sum, value = parse_packet(bin_input[index:])
            index += sub_index
            version_sum += sub_version_sum
            values.append(value)

    if type_id == 0:
        res = sum(values)
    elif type_id == 1:
        # product
        res = 1
        for p in values:
            res *= p
    elif type_id == 2:
        res = min(values)
    elif type_id == 3:
        res = max(values)
    elif type_id == 5:
        # gt
        assert(len(values) == 2)
        res = 1 if values[0] > values[1] else 0
    elif type_id == 6:
        # lt
        assert(len(values) == 2)
        res = 1 if values[0] < values[1] else 0
    elif type_id == 7:
        # eq
        assert(len(values) == 2)
        res = 1 if values[0] == values[1] else 0


    print("version sum", version_sum)
    return index, version_sum, res


print(parse_packet(bin_input))
