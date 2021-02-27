  '''
 Dave is 13, 772, 160 minutes old in age,
 can you calculate his age in year'''

def min_to_year(m):
    return int(((m/60)/24)/365)


print(f"Dave is {min_to_year(13772160)} years old.")
