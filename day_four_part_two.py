with open("dayfourinput.txt", "r") as fh:
  puzzle_input = fh.read().strip()

test_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1"""
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

handful = test_input.splitlines()
cards = {}
matches = [] # list of matches in a single card
duplicate_cards = []
total_cards = 0 # how many cards do I have

for card_id, all_numbers in enumerate(handful, 1):
  card_nums = all_numbers[all_numbers.find(":") + 1:] 
  winnings = card_nums.split("|")[0]
  my_numbers = card_nums.split("|")[1]
  cards[card_id] = list(map(int, winnings.split())), list(map(int, my_numbers.split()))

# So now I have the cards saved to a dictionary {card_id: ([winnings], [my_numbers])}


# Now I need to go through the first card and check how many matches I have...

for key, value in cards.items():
  matching_numbers = value[0]
  my_numbers = value[1] # now I have saved the numbers to the right variables
  for number in my_numbers:
    if number in matching_numbers:
      matches.append(number)
  for i in range(len(matches)):
    duplicate_cards.append(i + key + 1) # now I have a list of cards I need to duplicate...?
  print(duplicate_cards) # but what do i do with them lol
  duplicate_cards = [] # dead

  





  



    





