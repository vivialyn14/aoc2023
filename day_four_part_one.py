with open("dayfourinput.txt", "r") as fh:
  puzzle_input = fh.read().strip()

test_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

cards = test_input.splitlines()
matches = [] # list of matches in a single card
card_points = 0 # total points per card (2 to power of len(check_list))
answer = 0 # sum of all cards

for line in cards: # line is one big string
  winnings, my_numbers = map(str.split, line.split(":")[1].split("|")) # 2 lists
  for number in my_numbers: # go through each of my numbers
    if number in winnings: # check if my number is in winnings list
      matches.append(number) # if yes, add number to check_list
    if len(matches) >= 1: # 1+ matches = ready to start doubling
      card_points = 1
  for i in range(len(matches)-1): # skip first match, then start doubling
      card_points *= 2
  answer += card_points # add card_points to running total
  card_points = 0 # reset to 0 for next card
  matches = [] # reset to 0 for next card
print(answer) # sum of all cards
    





