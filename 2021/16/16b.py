from operator import mul
from functools import reduce

def to_bin(hexa):
    as_bin = ""
    for char in hexa:
        as_bin += f'{int(char, 16):04b}'
    return as_bin

def parse_literal(packet):
    # print("checking", packet)
    groups = []
    last = False
    bit = 6
    while packet:
        # print("checking2", encoded_packet)
        group = packet[bit:bit+5]
        # leading bit is 0 - last group
        if group[0] == "0":
            # print(group)
            last = True
            last_bit_index = bit+5
            packet = packet[last_bit_index:]
        groups.append(group[1:])
        # print(last)
        bit += 5
        if last:
            break
    # print("returning bit", bit)
    literal_value = int("".join(groups), base=2)
    # print("encoded packet", packet)
    # return position where to start next lookup
    return bit, last_bit_index, literal_value

def parse_acc_to_length(encoded_packet):
    subpackets_total_length_in_bits = int(encoded_packet[7:7+15], base=2)
    encoded_packet = encoded_packet[:22]
    print("parsed out", len(encoded_packet))
    return 22, subpackets_total_length_in_bits

def parse_acc_to_subpacket_number(encoded_packet):
    number_of_subpackets_contained = int(encoded_packet[7:7+11], base=2)
    # print(number_of_subpackets_contained)
    encoded_packet = encoded_packet[:18]
    # print("parsed out", encoded_packet)
    return 18, number_of_subpackets_contained

# hexa = "020D708041258C0B4C683E61F674A1401595CC3DE669AC4FB7BEFEE840182CDF033401296F44367F938371802D2CC9801A980021304609C431007239C2C860400F7C36B005E446A44662A2805925FF96CBCE0033C5736D13D9CFCDC001C89BF57505799C0D1802D2639801A900021105A3A43C1007A1EC368A72D86130057401782F25B9054B94B003013EDF34133218A00D4A6F1985624B331FE359C354F7EB64A8524027D4DEB785CA00D540010D8E9132270803F1CA1D416200FDAC01697DCEB43D9DC5F6B7239CCA7557200986C013912598FF0BE4DFCC012C0091E7EFFA6E44123CE74624FBA01001328C01C8FF06E0A9803D1FA3343E3007A1641684C600B47DE009024ED7DD9564ED7DD940C017A00AF26654F76B5C62C65295B1B4ED8C1804DD979E2B13A97029CFCB3F1F96F28CE43318560F8400E2CAA5D80270FA1C90099D3D41BE00DD00010B893132108002131662342D91AFCA6330001073EA2E0054BC098804B5C00CC667B79727FF646267FA9E3971C96E71E8C00D911A9C738EC401A6CBEA33BC09B8015697BB7CD746E4A9FD4BB5613004BC01598EEE96EF755149B9A049D80480230C0041E514A51467D226E692801F049F73287F7AC29CB453E4B1FDE1F624100203368B3670200C46E93D13CAD11A6673B63A42600C00021119E304271006A30C3B844200E45F8A306C8037C9CA6FF850B004A459672B5C4E66A80090CC4F31E1D80193E60068801EC056498012804C58011BEC0414A00EF46005880162006800A3460073007B620070801E801073002B2C0055CEE9BC801DC9F5B913587D2C90600E4D93CE1A4DB51007E7399B066802339EEC65F519CF7632FAB900A45398C4A45B401AB8803506A2E4300004262AC13866401434D984CA4490ACA81CC0FB008B93764F9A8AE4F7ABED6B293330D46B7969998021C9EEF67C97BAC122822017C1C9FA0745B930D9C480"
# hexa = "9C0141080250320F1802104A08"
hexa = "880086C3E88112"
counter_of_subpackets = 0
versions = 0
packet = to_bin(hexa)
print(packet)

literal_values = []
all_values = []


def parse_all(packet, all_values, kontrola_zanoreni, sub_no=0, sub_len=0):
    kontrola_zanoreni += 1


    print(sub_no)
    print(sub_len)
    if not any([int(x) for x in packet]):
        print("breaking")
        all_values.append(len(packet))
        return all_values

    version = packet[:3]
    # versions += int(version, base=2)
    # print("version", int(version, base=2))
    type_ID = packet[3:6]
    type_in_dec = int(type_ID, base=2)
    print("type_ID", int(type_ID, base=2))
    # if type_in_dec != 4:
    #     all_values.append(type_in_dec)
    if type_ID == "100":
        print("continue: parse literal")
        if sub_no:
            sub_no -= 1
        next_starting_bit, last_bit_index, literal_value = parse_literal(packet)
        packet = packet[next_starting_bit:]
        if sub_len:
            sub_len -= last_bit_index
        all_values.append((type_in_dec, sub_no, sub_len, literal_value, last_bit_index))
        return parse_all(packet, all_values, kontrola_zanoreni, sub_no, sub_len)
    else:
        length_type_ID = packet[6]
        if length_type_ID == "0":
            if sub_no:
                sub_no -= 1
            print("continue: total length in bits")
            next_starting_bit, subpackets_total_length_in_bits = parse_acc_to_length(packet)
            # all_values.append((type_in_dec, subpackets_total_length_in_bits))
            packet = packet[next_starting_bit:]
            # parse_all(packet)
            all_values.append((type_in_dec, sub_no, subpackets_total_length_in_bits, next_starting_bit))
            return parse_all(packet, all_values, kontrola_zanoreni, sub_len=subpackets_total_length_in_bits, sub_no=sub_no)
        else:
            print("continue: number of subpackets")
            if sub_no:
                sub_no -= 1
            next_starting_bit, subpacket_number = parse_acc_to_subpacket_number(packet)
            # print("calculated number", subpacket_number)
            # print("packet", packet[:18], packet[18:])
            # all_values.append((type_in_dec, len(packet), subpacket_number, 0))
            packet = packet[next_starting_bit:]
            all_values.append((type_in_dec, subpacket_number, sub_len, next_starting_bit))
            return parse_all(packet, all_values, kontrola_zanoreni, sub_no=subpacket_number, sub_len=sub_len)
    kontrola_zanoreni -= 1


# def parse_all(packet, all_values, sub_no=0, sub_len=0):
#     print(sub_no)
#     print(sub_len)
#     if not any([int(x) for x in packet]):
#         print("breaking")
#         all_values.append(len(packet))
#         return all_values

#     version = packet[:3]
#     # versions += int(version, base=2)
#     # print("version", int(version, base=2))
#     type_ID = packet[3:6]
#     type_in_dec = int(type_ID, base=2)
#     print("type_ID", int(type_ID, base=2))
#     # if type_in_dec != 4:
#     #     all_values.append(type_in_dec)
#     if type_ID == "100":
#         print("continue: parse literal")
#         if sub_no:
#             sub_no -= 1
#         next_starting_bit, last_bit_index, literal_value = parse_literal(packet)
#         packet = packet[next_starting_bit:]
#         if sub_len:
#             sub_len -= last_bit_index
#         all_values.append((type_in_dec, sub_no, sub_len, literal_value, last_bit_index))
#         return parse_all(packet, all_values, sub_no, sub_len)
#     else:
#         length_type_ID = packet[6]
#         if length_type_ID == "0":
#             if sub_no:
#                 sub_no -= 1
#             print("continue: total length in bits")
#             next_starting_bit, subpackets_total_length_in_bits = parse_acc_to_length(packet)
#             # all_values.append((type_in_dec, subpackets_total_length_in_bits))
#             packet = packet[next_starting_bit:]
#             # parse_all(packet)
#             all_values.append((type_in_dec, sub_no, subpackets_total_length_in_bits, next_starting_bit))
#             return parse_all(packet, all_values, sub_len=subpackets_total_length_in_bits, sub_no=sub_no)
#         else:
#             print("continue: number of subpackets")
#             if sub_no:
#                 sub_no -= 1
#             next_starting_bit, subpacket_number = parse_acc_to_subpacket_number(packet)
#             # print("calculated number", subpacket_number)
#             # print("packet", packet[:18], packet[18:])
#             # all_values.append((type_in_dec, len(packet), subpacket_number, 0))
#             packet = packet[next_starting_bit:]
#             all_values.append((type_in_dec, subpacket_number, sub_len, next_starting_bit))
#             return parse_all(packet, all_values, sub_no=subpacket_number, sub_len=sub_len)
    # return parse_all(packet)


print(parse_all(packet, [], 0))

print(versions)


# print(versions)

# print(all_values)

