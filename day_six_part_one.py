import math

with open("daysixinput.txt", "r") as fh:
  puzzle_input = fh.read().strip()

test_input = """Time:      7  15   30
Distance:  9  40  200"""

input = puzzle_input.splitlines()

time = input[0]
distance = input[1]

time = time[time.find(":") + 1:].strip().split()
distance = distance[distance.find(":") + 1:].strip().split()

for i in range(len(time)): # convert time and distance to integers
  time[i] = int(time[i])
  distance[i] = int(distance[i])

record_breakers = 0
multiply_list = []

for i in range(len(time)): # go thru each race
  race = ((int(time[i]), int(distance[i])))
  t, d = race[0], race[1]
  for charge in range(t): # go thru each charge time (e.g. holding button for 0ms - 7ms)
    time_remaining = t - charge
    travelled = charge * time_remaining
    if travelled > d:
      record_breakers += 1
  multiply_list.append(record_breakers)
  record_breakers = 0

answer = math.prod(multiply_list)
print(answer)

  
  