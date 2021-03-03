#This is the title
print("Welcome to DoorDash Distand Tracker")
print("")

#This is the title for the travel log
print("Travel Log")
print("")

#These are the variables for the total distance, 
distance = 100
daynum = 0
drive = 0

#This calculated the distance travelled and the amount of days taken
while drive < distance:
  days = int(input("Enter the distance travelled for the day: "))
  daynum = daynum+1
  drive = days+drive

#This is the summary of the code
print("")
print("Summary")
print("It took "+str(daynum) + " days to surpass 100km driven")
print("The average distance driven per day is "+str(drive/daynum) + "km")