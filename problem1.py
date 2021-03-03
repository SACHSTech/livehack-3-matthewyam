'''
Filename: problem1.py
Description: This program will calculate the wins and losses for your team while assigning you to your group based on that information
Author:Yam.M
Created On:03/03/2021

'''

#This is the title and the blank space
print("Tournament Tracker")
print("")

#This is the win and loss variable while indicating the user to input the wins or losses for the team
print("Enter wins and losses for your team: ")
wins = 0
loss = 0

#This is the forloop to ask the user if the game wasa win or loss.  It also calculates the total wins and losses
for i in range(0,6):
  game = input("W or L: ")
  if game == "w":
    wins = wins + 1
  if game == "l":
    loss = loss +1

#This calculaes the wins and losses to determine what group you are in
if wins>=5 or loss<=1:
  print("Your team is in Group 1")

elif wins>=3 and wins<=4 or loss<=2:
  print("Your team is in Group 2")

elif wins>=1 and wins<=2 or loss<=4:
  print("Your team is in Group 3")

elif wins<=0 or loss==6:
  print("Your team is eliminated")