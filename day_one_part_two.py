#import regex as re
import re

pat = re.compile(r"(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))")

with open("dayoneinput.txt", "r") as fh:
  puzzle_input = fh.read().strip()

test_input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

ref = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

numerical = []
final = []

for line in puzzle_input.splitlines():
  for entry in list(pat.findall(line)):
    numerical.append(ref.get(entry, entry))
  final.append(str(numerical[0]) + str(numerical[-1]))
  numerical = []

total = sum(int(char) for char in final) 

print(total)


