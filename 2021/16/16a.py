def to_bin(hexa):
    as_bin = ""
    for char in hexa:
        as_bin += f'{int(char, 16):04b}'
    return as_bin

def parse_literal(encoded_packet):
    # the binary number is padded with leading zeroes
    # until its length is a multiple of four bits
    # while len(as_bin) % 4 != 0:
    #     as_bin += "0"
    print("checking", encoded_packet)
    groups = []
    last = False
    bit = 6
    while encoded_packet:
        # print("checking2", encoded_packet)
        print("starting bit", bit)
        print(last)
        group = encoded_packet[bit:bit+5]
        # leading bit is 0 - last group
        if group[0] == "0":
            print(group)
            last = True
            last_bit_index = bit+5
            print("last_bit_index", last_bit_index)
            encoded_packet = encoded_packet[last_bit_index:]
        groups.append(group[1:])
        if last:
            break
        bit += 5
    print("literal value", int("".join(groups), base=2))
    print("encoded packet", encoded_packet)
    return encoded_packet

def parse_acc_to_length(encoded_packet):
    subpackets_total_length_in_bits = int(encoded_packet[7:7+15], base=2)
    # encoded_packet = encoded_packet[22:22+subpackets_total_length_in_bits]
    return subpackets_total_length_in_bits

def parse_acc_to_subpacket_number(encoded_packet):
    number_of_subpackets_contained = int(encoded_packet[7:7+11], base=2)
    print(number_of_subpackets_contained)
    # encoded_packet = encoded_packet[18:]
    return number_of_subpackets_contained

hexa = "620080001611562C8802118E34"
counter_of_subpackets = 0
versions = 0
as_bin = to_bin(hexa)
print(as_bin)


# version = as_bin[:3]
# versions += int(version, base=2)
# print("version", int(version, base=2))
# type_ID = as_bin[3:6]


def parse(packet, versions, subpacket):
    # subpacket_number = 100
    subpacket -= 1
    print("subpacket", subpacket)

    print("checking in parse", packet)
    # counter_to_check =1
    # print("counter", counter_to_check)
    if not packet or subpacket < 0:
        return versions
    version = packet[:3]
    versions += int(version, base=2)
    print("version", int(version, base=2))
    type_ID = packet[3:6]
    print("type_ID", type_ID)
    if type_ID == "100":
        print("continue: parse literal")
        packet = parse_literal(packet)
        return parse(packet, versions, subpacket)
    else:
        length_type_ID = packet[6]
        if length_type_ID == "0":
            print("continue: total length in bits")
            total_length = parse_acc_to_length(packet)
            subpacket +=1
            return parse(packet[22:22+total_length], versions, subpacket)
        else:
            print("continue: number of subpackets")
            subpacket_number = parse_acc_to_subpacket_number(packet)
            print("calculated number", subpacket_number)
            print("packet", packet[:18], packet[18:])
            return parse(packet[18:], versions, subpacket_number)

print("tu", parse(as_bin, versions, 100))
# number_of_subpackets_contained = 1000

# for i in range(4):
# while True:
#     # if counter_of_subpackets == number_of_subpackets_contained:
#     #     print("subpackets exhausted")
#     #     break
#     if not as_bin:
#         print("no more binary")
#         break
#     print("check", as_bin)
#     version = as_bin[:3]
#     versions += int(version, base=2)
#     print("version", int(version, base=2))
#     type_ID = as_bin[3:6]

#     # literal packet type
#     if type_ID == "100":
#         print("literal")
#         as_bin = parse_literal(as_bin)
#     # operator packet
#     else:
#         as_bin = parse_operator(as_bin)
#     counter_of_subpackets += 1

# print(versions)