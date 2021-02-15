'''  
SalesPerson Rita Drives 2052 miles in 6 days
stopping at 2 towns each day. How many Kilometers
does she average between stops?
'''

noOfMiles = 2052
noOfDays = 6
noOfTowns = 2
mileToKm = 1.60934
avgStops = ((noOfMiles / noOfDays) / noOfTowns) * mileToKm
print(avgStops)
