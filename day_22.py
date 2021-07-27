TEST_INPUT = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""

PUZZLE_INPUT = """Player 1:
38
1
28
32
43
21
42
29
18
13
39
41
49
31
19
26
27
40
35
14
3
36
12
16
45

Player 2:
34
15
47
20
23
2
11
9
8
7
25
50
48
24
46
44
10
6
22
5
33
30
4
17
37"""


def solve(starting_decks):

    player1_deck = []
    player2_deck = []

    current_deck = None

    for line in starting_decks.split("\n"):
        if not line:
            continue
        if line == "Player 1:":
            current_deck = player1_deck
            continue
        if line == "Player 2:":
            current_deck = player2_deck
            continue

        current_deck.insert(0, int(line))

    # play
    while player2_deck and player1_deck:
        player1_card = player1_deck.pop()
        player2_card = player2_deck.pop()

        if player1_card > player2_card:
            player1_deck.insert(0, player1_card)
            player1_deck.insert(0, player2_card)
        else:
            player2_deck.insert(0, player2_card)
            player2_deck.insert(0, player1_card)

    print(f"{player1_deck=} {player2_deck=}")

    winning_deck = player1_deck or player2_deck

    score = 0
    for i, card in enumerate(winning_deck):
        score += (i+1) * card
    return score

if __name__ == "__main__":
    assert solve(TEST_INPUT) == 306
    print(solve(PUZZLE_INPUT))
