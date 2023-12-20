import math

with open("dayeightinput.txt", "r") as fh:
  puzzle_input = fh.read().strip()

test_input = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX"""

guide = puzzle_input.splitlines()[0]
block = puzzle_input.splitlines()[2:]
index = 0
steps = 0
list_of_steps = []
beginning_list = []
map = {}

for line in block: # create dictionary AAA: BBB, BBB
  key, value_str = line.split(" = ")
  values = value_str[1:-1].split(", ")
  map[key] = values

for key in map: 
  if key.endswith("A"):
    beginning_list.append(key) # add XXAs to a list
for i in beginning_list: # for each XXA, follow instructions to find XXZ
  if i in map:
    while i[-1] != "Z":
      if index > len(guide) - 1: # text wrap for guide
        index = 0
      if guide[index] == "L": # if instruction is L
        i = map[i][0] # change i to new ref
        index += 1 # move to next guide letter
        steps += 1 
      else: # if instruction is R
        i = map[i][1] # change i to new ref
        index += 1 # move to next guide letter 
        steps += 1
    list_of_steps.append(steps) # add num of steps to list
    steps = 0 # reset steps

answer = 1

for num in list_of_steps:
  answer = math.lcm(answer, num) # get lowest common multiple of steps

print(answer)