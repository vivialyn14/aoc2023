with open("daytwoinput.txt", "r") as fh:
  puzzle_input = fh.read().strip()

test_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

games = puzzle_input.splitlines()
#print(games)

games = enumerate(games, start=1) #this gives tuples: [0] is the game_id
#print(list(game_id))

total = 0 # game_id will be added to this if the game is impossible
total_games = len(puzzle_input.splitlines())
print(total_games)
check = 0

possible_max = { # these are the maximum cubes per colour in each game
  "red": 12,
  "green": 13,
  "blue": 14
}

for game in games:
#  print(game)
  game_id = game[0]
  sessions = game[1].split(":")[1]
  check = 0
#  print(sessions)
  for session in sessions.split(";"):
#    print(session)
    colours = session.split(",")
#    print(colours)
    for handful in colours:
      info = handful.strip().split(" ")
#      print(info)
      if int(info[0]) > possible_max.get(info[-1]) and check == 0:
        total_games -= 1
        check += 1
  if check == 0:
    total += game_id
    
print(total)
    
