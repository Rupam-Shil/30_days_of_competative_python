'''write a python program to takes the user
 for a distance(in meters) and the time was 
 taken(as three numbers: hours, minutes and seconds)
  and display the speed in miles per hour.'''

distance = float(input("Please inter the distance in meter:"))
hour, min, sec = [int(i) for i in input("Please enter the time taken in hh/mm/ss order:").split()]
hour = hour + (min /60) + (sec/3600)
mile = distance * 0.000621371
speed = mile / hour
print("THe speed of the car is {:.5f}m/hr".format(speed))
