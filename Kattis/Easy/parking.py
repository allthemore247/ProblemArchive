'''
Problem Name: Parking
Memory Limit: 1024 MB
CPU Time Limit: 1 second
Difficulty: 2.0 (Easy)
'''

rate = list(map(int, input().split()))
trucks = []
payment = 0

# first get the list of all three truck arival times
for i in range(3):
    trucks.append(list(map(int, input().split())))

latest = 0
# determine what is the latest departure time
for i in trucks:
    if i[1] > latest:
        latest = i[1]

# then loop through the available minutes and determine which truck is parked and when.
for i in range(1, latest+1):
    curr = 0 # trucks in lot
    for truck in trucks:
        # if curr time is within truck's arrv/depart
        if truck[0] <= i and truck[1] > i:
            curr += 1
    
    if curr != 0:
        payment += (rate[curr-1] * curr)
print(payment)