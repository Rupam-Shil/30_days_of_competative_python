'''
Dan Rented two movies to watch last night.
The first was 100 minutes long, the second 110 minutes long.
How many hours did it take for Dan to watch the two movies'''

firstMovie = 100   #min
secondMovie = 110  #min
minToHour = (1 / 60) #hour
TotalHour = (firstMovie + secondMovie) * minToHour
print("Total time took {:.2f} hour".format(TotalHour))
