with open("daysixinput.txt", "r") as fh:
  puzzle_input = fh.read().strip()

test_input = """Time:      7  15   30
Distance:  9  40  200"""

input = puzzle_input.splitlines()

time = input[0]
distance = input[1]

t = time[time.find(":") + 1:].strip().split() # this is a list with 1 str item
d = distance[distance.find(":") + 1:].strip().split() # this is a list with 1 str item

t = "".join(t) # concatenate 
d = "".join(d) # concatenate

t, d = int(t), int(d) # turn values into ints

rbreak = 0

for charge in range(t): # go thru each charge time (e.g. holding button for 0ms - 7ms)
  time_remaining = t - charge
  travelled = charge * time_remaining
  if travelled > d:
    rbreak += 1
print(rbreak)
  

  