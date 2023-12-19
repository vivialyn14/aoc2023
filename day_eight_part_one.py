from pprint import pprint

with open("dayeightinput.txt", "r") as fh:
  puzzle_input = fh.read().strip()

test_input = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

# save LLR as guide
# ref: [l, r] = {"AAA": ["BBB", "BBB"]}
# start instruction as guide[0] (index = 0) <- if index == 4, index = 0
# start ref as "AAA"
# while ref != "ZZZ"
# look up "ref"
# ref = dict.get(index)
# steps += 1
# if ref = "ZZZ": break
# print(steps)

guide = puzzle_input.splitlines()[0]
block = puzzle_input.splitlines()[2:]
index = 0
steps = 0
ref = "AAA"

map = {}

for line in block: # create dictionary AAA: BBB, BBB
  key, value_str = line.split(" = ")
  values = value_str[1:-1].split(", ")
  map[key] = values

while ref != "ZZZ": # if we're not at the end
  if index > len(guide) - 1: # text wrap for guide LLR = LLRLLRLLRLLR... etc
    index = 0
  if ref in map: # if the current ref is in the dict
    if guide[index] == "L": # if we're looking at the left instruction
      ref = map[ref][0] # re-write ref to left value
      index += 1 # add to index to change the instruction 
      steps += 1 # add to answer
    else: # if we're looking at the right instruction
      ref = map[ref][1] # re-write ref to right value
      index += 1 # add to index to change the instruction
      steps += 1 # add to answer


print("steps taken: ", steps)
    