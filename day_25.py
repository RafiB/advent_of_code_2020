TEST_INPUT = """5764801
17807724"""

PUZZLE_INPUT = """18499292
8790390"""

SUBJECT_NUMBER = 7


def determine_loop_size(public_key):
    loop_size = 1

    current = (SUBJECT_NUMBER * SUBJECT_NUMBER) % 20201227

    while current != public_key:
        loop_size += 1
        current = (current * SUBJECT_NUMBER) % 20201227

    return loop_size + 1


def solve(public_keys):
    card_public_key, door_public_key = tuple(map(int, public_keys.split("\n")))

    card_loop_size = determine_loop_size(card_public_key)
    door_loop_size = determine_loop_size(door_public_key)

    c_encryption_key = (door_public_key * door_public_key) % 20201227
    for _ in range(card_loop_size-2):
        c_encryption_key = (c_encryption_key * door_public_key) % 20201227

    d_encryption_key = (card_public_key * card_public_key) % 20201227
    for _ in range(door_loop_size-2):
        d_encryption_key = (d_encryption_key * card_public_key) % 20201227

    assert c_encryption_key == d_encryption_key
    return c_encryption_key

if __name__ == "__main__":
    assert solve(TEST_INPUT) == 14897079
    print(solve(PUZZLE_INPUT))
