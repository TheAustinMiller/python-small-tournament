def printTourney(list):
  print("\n" +list[0])
  print("---------- " + list[4])
  space = ""
  difference = 10 - len(list[1])
  for i in range(difference):
    space += " "
  print(list[1] + space + "|----------")
  print("----------           |" + list[6])
  space = ""
  difference = 10 - len(list[2])
  for i in range(difference):
    space += " "
  print(list[2] + space + "           |----------")
  space = ""
  difference = 10 - len(list[5])
  for i in range(difference):
    space += " "
  print("---------- " + list[5] + space + "|")
  space = ""
  difference = 10 - len(list[3])
  for i in range(difference):
    space += " "
  print(list[3] + space + "|----------")
  print("----------\n")


list = ["", "", "", "", "", "", ""]
print("Welcome to AJ's Tournament Maker\n(4 teams/players needed)\n")
for i in range(4):
  player = input("Please enter player " + str((i + 1)) + ": ")
  while len(player) > 10:
    print("No names longer than 10 characters please!")
    player = input("Please enter player " + str((i + 1)) + ": ")
  list[i] = player

printTourney(list)
flag = False
print("ROUND 1")
print(f"{list[0]} vs. {list[1]}")
while not flag:
  winner = input("Please type a winner: ")
  if winner.upper() == list[0].upper():
    print(f"{list[0]} Wins!")
    flag = True
    list[4] = list[0]
  if winner.upper() == list[1].upper():
    print(f"{list[1]} Wins!")
    flag = True
    list[4] = list[1]
printTourney(list)

flag = False
print("ROUND 2")
print(f"{list[2]} vs. {list[3]}")
while not flag:
  winner = input("Please type a winner: ")
  if winner.upper() == list[2].upper():
    print(f"{list[2]} Wins!")
    flag = True
    list[5] = list[2]
  if winner.upper() == list[3].upper():
    print(f"{list[3]} Wins!")
    flag = True
    list[5] = list[3]
printTourney(list)

flag = False
print("ROUND 3")
print(f"{list[4]} vs. {list[5]}")
while not flag:
  winner = input("Please type a winner: ")
  if winner.upper() == list[4].upper():
    print(f"{list[4]} Wins!")
    flag = True
    list[6] = list[4]
  if winner.upper() == list[5].upper():
    print(f"{list[5]} Wins!")
    flag = True
    list[6] = list[5]
printTourney(list)

print("Congratulations to " + list[6] + " for winning this tournament!")
