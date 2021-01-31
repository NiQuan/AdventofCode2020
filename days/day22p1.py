with open("inputs/input22.txt", "r") as f:
    starting_hands = f.read().split("\n\n")

starting_hands = [s.splitlines()[1:] for s in starting_hands]

p1_hand = [int(x) for x in starting_hands[0]]
p2_hand = [int(x) for x in starting_hands[1]]


def play_round(hand_1, hand_2):
    card_1 = hand_1.pop(0)
    card_2 = hand_2.pop(0)

    if card_1 > card_2:
        hand_1 += [card_1, card_2]
    else:
        hand_2 += [card_2, card_1]

    return (hand_1, hand_2)


done = False
while not done:
    if not (p1_hand and p2_hand):
        done = True
        if p1_hand:
            winner = p1_hand
        else:
            winner = p2_hand
    else:
        (p1_hand, p2_hand) = play_round(p1_hand, p2_hand)


total = 0
i = 1
for card in winner[::-1]:
    total += card * i
    i += 1

print(total)