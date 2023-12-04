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

for x_sym, y_sym in symbols: 
  for x_check, y_check in checks:
    check_me = (x_sym + x_check, y_sym + y_check)
    if check_me in numbers:
      if int(numbers.get(check_me)) + x_sym not in check_set:
        answer += int(numbers.get(check_me))
        check_set.add(int(numbers.get(check_me)) + x_sym)
  check_set = set()


print(answer)



