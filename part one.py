with open("dayoneinput.txt", "r") as fh:
  puzzle_input = fh.read().strip()

test_input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

lines = puzzle_input.splitlines()
number = ""
list = []
total = 0

for line in lines:
  for char in line:
    if char.isdigit():
      number += char
  list.append(int(number[0] + (number[-1])))
  number = ""

for entry in list:
  total += int(entry)

print(total)