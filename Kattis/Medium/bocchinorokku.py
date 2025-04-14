'''
Problem Name: Bocchi's Rocks
Link: https://open.kattis.com/problems/bocchinorokku
Memory Limit: 1024 MB
CPU Time Limit: 1 second
Difficulty: 1.4 - 2.9 (Medium)
'''

# current issues: tle'd in group 3 (n = ???)

n = int(input())
rocks = [int(x) for x in input().split()]
srocks = sorted(rocks)
out = ""

for rock in rocks:
    over = 0
    for i in srocks:
        if i == rock:
            break
        else:
            over += 1            
    out += str(over) + " "

print(out.strip())