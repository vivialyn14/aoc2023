from collections import Counter
from pprint import pprint

with open("dayseveninput.txt", "r") as fh:
  puzzle_input = fh.read().strip()

test_input = """JK784 1
JJ986 2
QQ456 4
JJJJJ 10
"""

# JK784 becomes 13,13,784 (weakest (J = 1) one pair) - rank 1 * 1 = 1
# JJ986 becomes 9,9,9,86 (three of a kind) - rank 3 * 2 = 6
# QQ456 becomes 12,12,456 (strongest (Q = 12) one pair) - rank 2 * 4 = 8

card_values = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 1,
    "T": 10,
    9: 9,
    8: 8,
    7: 7,
    6: 6,
    5: 5,
    4: 4,
    3: 3,
    2: 2
}

hand_types = {  # in descending order of power 
    7: [],  # five of a kind: all cards the same (counter = 1 item)
    6: [],  # four of a kind: one card different (counter = 2 items)
    5: [],  # full house: 3 x same + 1 pair (counter = 2, all counts > 1)
    4:
    [],  # three of a kind: 3 x same + 2 randos (counter = 3, any counts > 2)
    3: [],  # two pair: 2 x pairs (counter = 3 items, all counts =< 2)
    2: [],  # one pair: 1 x pair (counter = 4 items)
    1: [],  # high card: all cards different (counter = 5 items)
}

list_of_cards = []
numeric_card = []
all_numeric_cards = []
sorted_cards = []
answer = 0

lines = test_input.splitlines()

for entry in lines:
  cards_and_bids = entry.split()
  card = (cards_and_bids[0], int(cards_and_bids[1]))
  list_of_cards.append(card)

for card in list_of_cards:  # go through each card
  for char in card[0]:  # look each card in hand
    numeric_card.append(card_values.get(char, char))  # convert cards to values
  numeric_card = [int(c) for c in numeric_card]  # int all values
  new_hand = [numeric_card, card[1],
              numeric_card]  # [numeric_card, bid, numeric_card]
  all_numeric_cards.append(new_hand)
  numeric_card = []  # reset numeric_card ready for next hand

#print(all_numeric_cards)

for entry in all_numeric_cards:  # using J as a wild card
  #print(entry[0])
  # if there is no most freq. value, change 1s to highest val.
  if all(count == 1 for count in Counter(entry[0]).values()):
    hand_hand = [x if x != 1 else max(entry[0]) for x in entry[0]]
  # if there is a most freq. value...
  else:
    # if the most freq. value is J (1)
    if Counter(entry[0]).most_common(1)[0][0] == 1:
      hand_hand = [x if x != 1 else max(entry[0])
                   for x in entry[0]]  # change J to max val.
    # if the most freq. value is not J
    else:  # change J to most freq. val
      hand_hand = [
          x if x != 1 else Counter(entry[0]).most_common(1)[0][0]
          for x in entry[0]
      ]
  entry[0] = hand_hand

#print(all_numeric_cards)

for card in all_numeric_cards:  # sort cards into hand_types dictionary
  if len(Counter(card[0])) == 1:  # five
    hand_types[1].append(card)
  if len(Counter(card[0])) == 2:  # full, else: four
    if all(count > 1 for count in Counter(card[0]).values()):
      hand_types[3].append(card)
    else:
      hand_types[2].append(card)
  if len(Counter(card[0])) == 3:  # three  else: two
    if any(count > 2 for count in Counter(card[0]).values()):
      hand_types[4].append(card)
    else:
      hand_types[5].append(card)
  if len(Counter(card[0])) == 4:  # one pair
    hand_types[6].append(card)
  if len(Counter(card[0])) == 5:  # high card
    hand_types[7].append(card)

#print(hand_types)

for item in hand_types:
  hand_types.get(item).sort(
      key=lambda x: x[2])  # sort values in dict from l -> h

for item in hand_types:  # add to a big list in order of power l -> h
  for card in hand_types.get(item):
    sorted_cards.append(card)

# print(sorted_cards)

for index, card_tuple in list(enumerate(sorted_cards,
                                        start=1)):  # index is rank
  answer += index * card_tuple[1]

#print("dict of types of hands: ", hand_types)
print(answer)
