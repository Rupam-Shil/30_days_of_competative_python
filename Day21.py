'''
Write a program that for a given hour and
minutes values calculates an angle in degree
between the hour and the minute hands.
Check whether the minute hand overlapping the hour hand at a given time.
'''

def calcAngle(h, m):
        
        if (h < 0 or m < 0 or h > 12 or m > 60):
            print('Wrong input')
         
        if (h == 12):
            h = 0

        if (m == 60):
            m = 0
            h += 1;
            if(h>12):
                   h = h-12;
         
        hour_angle = 0.5 * (h * 60 + m)
        minute_angle = 6 * m
         
        angle = abs(hour_angle - minute_angle)
         
        angle = min(360 - angle, angle)
         
        return angle
 
h = int(input("Enter the hour(1-12):"))
m = int(input("ENter the min(0-59):"))
print('Angle ', calcAngle(h,m))
