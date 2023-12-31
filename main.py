from collections import deque

with open("daynineinput.txt", "r") as fh:
  puzzle_input = fh.read().strip()

test_input = """1 3 6 10 15 21
0 3 6 9 12 15
10 13 16 21 30 45"""

reports = puzzle_input.splitlines()

d = []
l = []
xindex = 1
yindex = 1
answer = 0

for report in reports: # report = "0 3 6 9 12 15"
  d.append([int(num) for num in report.split()]) # report = [0, 3, 5, 6, 9, 12, 15]
  for item in d: # go thru each list within top list
    if any(x for x in item): # if any of the numbers are not 0 
      for num in item[:-1]: # go thru each number (except the last one)
        l.append(item[xindex] - num) # y - x <- add this to a new list
        xindex += 1 # move index so that y value moves to next number
      d.append(l) # once you have all the differences, add l as item to big list
      l = [] # reset new list ready for next set of differences
      xindex = 1 # reset index
  d = d[::-1] 
  d[0].append(0)
  for item in d: # item = [0, 0, 0]#
    try: #if yindex is in range...
      deck = deque(d[yindex]) # deck = [2, 2, 2]
      num = item[0] # num = 0, d[yindex][0] = 2
      deck.appendleft(d[yindex][0] - num) # add 2 - 0 to the left of the [2, 2, 2] tier
      d[yindex] = list(deck) # turn it back into a list
      yindex += 1 # move the index along
    except IndexError:
      answer += d[-1][0]
      yindex = 1
  d = []

print(answer)
      
