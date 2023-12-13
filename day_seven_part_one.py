from collections import Counter

with open("dayseveninput.txt", "r") as fh:
  puzzle_input = fh.read().strip()

test_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

card_values = { 
  "A": 14,
  "K": 13,
  "Q": 12,
  "J": 11,
  "T": 10,
  9: 9,
  8: 8,
  7: 7,
  6: 6,
  5: 5,
  4: 4,
  3: 3,
  2: 2,
  1: 1
}

hand_types = { # in descending order of power 
  1: [], # five of a kind: all cards the same (counter = 1 item)
  2: [], # four of a kind: one card different (counter = 2 items)
  3: [], # full house: 3 x same + 1 pair (counter = 2, all counts > 1)
  4: [], # three of a kind: 3 x same + 2 randos (counter = 3, any counts > 2)
  5: [], # two pair: 2 x pairs (counter = 3 items, all counts =< 2)
  6: [], # one pair: 1 x pair (counter = 4 items)
  7: [], # high card: all cards different (counter = 5 items)
}

list_of_cards = []
numeric_card = []
all_numeric_cards = []
sorted_cards = []
answer = 0

lines = puzzle_input.splitlines()

for entry in lines:
  cards_and_bids = entry.split()
  card = (cards_and_bids[0], int(cards_and_bids[1]))
  list_of_cards.append(card)
  
for card in list_of_cards: # go through each card
  for char in card[0]: # look each card in hand
    numeric_card.append(card_values.get(char, char)) # convert cards to values
  numeric_card = [int(c) for c in numeric_card] # int all values
  new_hand = (numeric_card, card[1]) # create tuples: (numeric_card, bid)
  all_numeric_cards.append(new_hand)
  numeric_card = [] # reset numeric_card ready for next hand

for card in all_numeric_cards: # sort cards into hand_types dictionary
  if len(Counter(card[0])) == 1: 
    hand_types[7].append(card)
  if len(Counter(card[0])) == 2: 
    if all(count > 1 for count in Counter(card[0]).values()):
      hand_types[5].append(card)
    else:
      hand_types[6].append(card)
  if len(Counter(card[0])) == 3:
    if any(count > 2 for count in Counter(card[0]).values()):
      hand_types[4].append(card)
    else:
      hand_types[3].append(card)
  if len(Counter(card[0])) == 4:
    hand_types[2].append(card)
  if len(Counter(card[0])) == 5:
    hand_types[1].append(card)

for item in hand_types:
  hand_types.get(item).sort(key=lambda x: x[0]) # sort values in dict from l -> h

for item in hand_types: # add to a big list in order of power l -> h
  for card in hand_types.get(item):
    sorted_cards.append(card)

for index, card_tuple in list(enumerate(sorted_cards, start=1)): # index is rank
  answer += index * card_tuple[1]

print(answer)


    
      
  