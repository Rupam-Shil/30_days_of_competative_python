  """
 During the last week track of training,
 Shoshanna achieves the following times in sec
 rounds - 66, 57, 54, 53, 64, 52, 59
 Found her best score using bubble sort
"""

herTime = [66, 57, 54, 53, 64, 52, 59]
for i in range(0,len(herTime)-1):
  for j in range(0,len(herTime)-i-1):
    if(herTime[j]>herTime[j+1]):
      temp = herTime[j]
      herTime[j] = herTime[j+1]
      herTime[j+1] = temp
print(f"Her Best score is {herTime[0]} sec")
