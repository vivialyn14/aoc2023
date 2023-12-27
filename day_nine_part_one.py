with open("daynineinput.txt", "r") as fh:
  puzzle_input = fh.read().strip()

test_input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

reports = puzzle_input.splitlines()

d = []
l = []
answer = 0
xindex = 1
yindex = 1

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
  for item in d:
    try:
      num = item[-1]
      d[yindex].append(num + d[yindex][-1]) # add num to last num in next item, append to final item
      yindex += 1
    except IndexError: # if yindex is out of range then we're at the end of the list
      answer += d[-1][-1]
      yindex = 1
  d = []

print(answer)
