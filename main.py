with open("daythreeinput.txt", "r") as fh:
  puzzle_input = fh.read().strip()

test_input = """467..114..
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
# go through the input and find co-ords of all numbers
# for multi-digit numbers i need the computer to save each co-ord as the whole number (e.g. (0,1), (0,2) and (0,3) are all saved as 576)

symbols = {}
# go through the input and find co-ords of all symbols

# now i'm going to go thru the input and add co-ordinates of numbers to my dictionary

lines = test_input.splitlines()

for line_no, line in enumerate(lines):
  str = ""
  for pos, char in enumerate(line):
    if char.isdigit():
      str += char
      numbers[(line_no, pos)] = ""
    if str != "" and char == ".":
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
#print(numbers)
#print(symbols)

checks = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
check_set = set()

answer = 0

for x_sym, y_sym in symbols:
  for x_check, y_check in checks:
    check_me = (x_sym + x_check, y_sym + y_check)
    if check_me in numbers:
      if int(numbers.get(check_me)) + check_me[0] not in check_set:
        answer += int(numbers.get(check_me))
        check_set.add(int(numbers.get(check_me)) + check_me[0])
      # print(check_set)


print(answer)



