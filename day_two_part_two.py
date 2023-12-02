with open("daytwoinput.txt", "r") as fh:
  puzzle_input = fh.read().strip()
import math

test_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

games = puzzle_input.splitlines()

games = enumerate(games, start=1) 

total = 0

for line_num, line_txt in games:
  game_id = line_num
  sessions = line_txt.split(":")[1]
  possible_max = {
    "red": 0,
    "green": 0,
    "blue": 0
  }

  for session in sessions.split(";"):
    colours = session.split(",")
    for handful in colours:
      cubes, colour = handful.strip().split(" ") 
      if int(cubes) > possible_max.get(colour):
        possible_max[colour] = int(cubes)
  total += math.prod(possible_max.values())

print(total)

