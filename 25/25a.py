SUBJECT_NUMBER = 7


def loop(val, subj_number):
    val *= subj_number
    val = val % 20201227
    return val


card_pub_key = 9232416
val = 1
for i in range(100000000):
    val = loop(val, SUBJECT_NUMBER)
    if val == card_pub_key:
        card_loop_size = i + 1
        break

door_pub_key = 14144084
val = 1
for i in range(100000000):
    val = loop(val, SUBJECT_NUMBER)
    if val == door_pub_key:
        door_loop_size = i + 1
        break

val = 1
for i in range(card_loop_size):
    val = loop(val, door_pub_key)
print(val)

val = 1
for i in range(door_loop_size):
    val = loop(val, card_pub_key)
print(val)
