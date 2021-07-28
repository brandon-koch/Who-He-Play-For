import requests
from bs4 import BeautifulSoup
import re
import random
import time

URL = "https://basketball.realgm.com/nba/players"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all(class_ = "nowrap")
names = re.findall('"Player" rel="(.*?)">', str(results))
name_list = []
for i in names:
  n = i.split(", ")
  if len(n) == 2:
    name = (n[1], n[0])
  else:
    name = (n[2], n[0], n[1])
  name_list.append(name)
teams = re.findall('"Current Team" rel="(.*?)">', str(results))
teams2 = []
for t in teams:
  new_t = t.replace("Sixers", "76ers")
  teams2.append(new_t)
all = {name_list[i]: teams2[i] for i in range(len(name_list))}
all2 = list(all.items())
print("Who He Play For?\n")
print("Instructions: A random NBA player will be selected, and you must")
print("provide the team they play for. You should respond with the team's")
print('nickname (Ex: "Bulls"). To end the game, submit a blank response.\n')
input("Press ENTER to begin. ")
playing = True
while playing:
  try:
    rand = random.choice(all2)
    if len(rand[0]) == 2:
      print("\n" + str(rand[0][0]), str(rand[0][1]) + "\n")
    else:
      print("\n" + str(rand[0][0]), str(rand[0][1]), str(rand[0][2]) + "\n")
    answer = input("Who he play for? ")
    team = rand[1].split()[-1]
    if answer.lower() == team.lower():
      print("Correct!")
      time.sleep(1.5)
    elif answer == "":
      print("Game ended. Thanks for playing!")
      playing = False
      break
    else:
      if len(rand[0]) == 2:
        raise ValueError(f"Incorrect. {rand[0][0]} {rand[0][1]} plays for the {rand[1]}.")
      else:
        raise ValueError(f"Incorrect. {rand[0][0]} {rand[0][1]} {rand[0][2]} plays for the {rand[1]}.")
  except ValueError as e:
    print(e)
    time.sleep(1.5)
