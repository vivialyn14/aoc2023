import math

with open("daythreeinput.txt", "r") as fh:
  puzzle_input = fh.read().strip()

test_input = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

numbers = {}
symbols = {}

lines = puzzle_input.splitlines()

for line_no, line in enumerate(lines):
  str = ""
  for pos, char in enumerate(line):
    if char.isdigit():
      str += char
      numbers[(line_no, pos)] = ""
    if str != "" and not char.isdigit():
      for key, value in numbers.items():
        if value == "":
          numbers[key] = str
      str = ""
    if not char.isdigit() and char != ".":
      symbols[(line_no, pos)] = char
  if str != "":
    for key, value in numbers.items():
      if value == "":
        numbers[key] = str


checks = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
check_set = set()

answer = 0
gear_ratios = set()

for x_sym, y_sym in symbols: # look thru every entry in symbols dict (looks like this -> (0,3): *), 
  if symbols.get((x_sym, y_sym)) == "*": # if we find a gear in the dictionary,
    for x_check, y_check in checks: # check surrounding co-ordinates for adjacent numbers
      check_me = (x_sym + x_check, y_sym + y_check) # check_me = the coordinate we want to check
      if check_me in numbers: # if check_me is in the numbers dictionary
        gear_ratios.add(int(numbers.get(check_me))) # add adjacent number to gear_ratios
        print(gear_ratios)
  if len(gear_ratios) == 2:
    answer += math.prod(gear_ratios) # multiply numbers together and add to 'answer'
    print(answer)
    gear_ratios = set() # reset the set ready for next gear
  else:
    gear_ratios = set()

print(answer)




