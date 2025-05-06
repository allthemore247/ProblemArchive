'''
Problem Name: BizzFuzz
Link: https://open.kattis.com/problems/bizzfuzz
Memory Limit: 1024 MB
CPU Time Limit: 1 second
Difficulty: 1.9 - 4.4 (Medium)
'''

# current issues: tle in groups 2-4, need more efficient solution

count = 0
all = list(map(int, input().split()))
max = all[2] if (all[2] > all[3]) else all[3]

# find our starting location for the next loop
current = all[0]
for i in range(all[2] * all[3]):
    if current % all[2] == 0:
        if current % all[3] == 0:
            break
    current += 1

# loop through the entire range, stepping based on max(C, D) for efficiency
for i in range(current, all[1]+1, max):
    if i % all[2] == 0:
        if i % all[3] == 0:
            count += 1

print(count)