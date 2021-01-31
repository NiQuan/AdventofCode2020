with open("inputs/input22.txt", "r") as f:
    starting_hands = f.read().split("\n\n")

starting_hands = [s.splitlines()[1:] for s in starting_hands]

p1_hand = [int(x) for x in starting_hands[0]]
p2_hand = [int(x) for x in starting_hands[1]]


def game(hand_1, hand_2):
    def round(hand_1, hand_2):

        card_1 = hand_1.pop(0)
        card_2 = hand_2.pop(0)

        if (len(hand_1) >= card_1) and (len(hand_2) >= card_2):

            if game(hand_1[:card_1], hand_2[:card_2])[0] == 1:
                hand_1 += [card_1, card_2]
            else:
                hand_2 += [card_2, card_1]
        else:
            if card_1 > card_2:
                hand_1 += [card_1, card_2]
            else:
                hand_2 += [card_2, card_1]

        return (hand_1, hand_2)

    previous_states = []

    while True:
        if (hand_1, hand_2) in previous_states:
            return (1, hand_1)
        else:
            previous_states.append((hand_1[:], hand_2[:]))

        (hand_1, hand_2) = round(hand_1, hand_2)

        if not hand_1:
            return (2, hand_2)
        elif not hand_2:
            return (1, hand_1)


winner_hand = game(p1_hand, p2_hand)[1]


total = 0
i = 1
for card in winner_hand[::-1]:
    total += card * i
    i += 1

print(f"Part 2: {total}")