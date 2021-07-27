import attr

TEST_INPUT = "389125467"
PUZZLE_INPUT = "318946572"


@attr.s()
class Cup(object):
    left = attr.ib()
    right = attr.ib()
    label = attr.ib()


def solve(cup_order):
    cup_map = {}
    first = None
    current = None

    previous_cup = None

    min_label = float("inf")
    max_label = float("-inf")

    for label in cup_order:
        label = int(label)
        cup = Cup(label=label, left=previous_cup, right=None)

        min_label = min(min_label, label)
        max_label = max(max_label, label)

        cup_map[label] = cup

        if previous_cup:
            previous_cup.right = cup

        if first is None:
            first = cup

        previous_cup = cup

    cup.right = first
    first.left = cup

    current = first

    for _ in range(100):
        extract_start = current.right
        extract_end = extract_start.right.right

        excluded = (extract_start.label, extract_start.right.label, extract_end.label)

        current.right = extract_end.right
        current.right.left = current

        destination_label = current.label - 1
        while destination_label in excluded or destination_label < min_label:
            if destination_label < min_label:
                destination_label = max_label
            else:
                destination_label -= 1

        destination_cup = cup_map[destination_label]

        destination_cup.right.left = extract_end
        extract_end.right = destination_cup.right
        extract_start.left = destination_cup
        destination_cup.right = extract_start

        current = current.right

    c = cup_map[1]
    state = ""
    c = c.right
    while c is not cup_map[1]:
        state += f"{c.label}"
        c = c.right
    return state

if __name__ == "__main__":
    assert solve(TEST_INPUT) == "67384529"
    print(solve(PUZZLE_INPUT))
