with open("dayoneinput.txt", "r") as fh:
  puzzle_input = fh.read().strip()

test_input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

lines = test_input.splitlines()
number = ""
numbers = []

for line in lines:
  for char in line:
    if char.isdigit():
      number += char
  numbers.append(int(number[0] + (number[-1])))
  number = ""

total = sum(numbers)

print(total)