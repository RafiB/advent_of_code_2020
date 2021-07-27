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

    winning_deck = play(player1_deck, player2_deck)

    score = 0
    for i, card in enumerate(winning_deck):
        score += (i+1) * card
    return score

def play(player1_deck, player2_deck):
    previous_decks = tuple()

    while player1_deck and player2_deck:
        game_state = (tuple(player1_deck), tuple(player2_deck))
        if game_state in previous_decks:
            """
            if there was a previous round in this game that had exactly the same cards in the same order
            in the same players' decks, the game instantly ends in a win for player 1.
            """
            return player1_deck

        previous_decks = previous_decks + (game_state,)

        player1_card = player1_deck.pop()
        player2_card = player2_deck.pop()

        if len(player1_deck) >= player1_card and len(player2_deck) >= player2_card:
            p1_sub_deck = player1_deck[-player1_card:]
            p2_sub_deck = player2_deck[-player2_card:]
            winning_deck = play(
                p1_sub_deck,
                p2_sub_deck,
            )
            winning_deck = player1_deck if winning_deck is p1_sub_deck else player2_deck
        else:
            winning_deck = player1_deck if player1_card > player2_card else player2_deck

        winning_deck.insert(0, player1_card if winning_deck is player1_deck else player2_card)
        winning_deck.insert(0, player2_card if winning_deck is player1_deck else player1_card)

    return player1_deck or player2_deck

if __name__ == "__main__":
    assert solve(TEST_INPUT) == 291
    print(solve(PUZZLE_INPUT))
