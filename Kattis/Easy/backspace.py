'''
Problem Name: Backspace
Link: https://open.kattis.com/problems/backspace
Memory Limit: 1024 MB
CPU Time Limit: 1 second
Difficulty: 1.1 - 1.7 (Easy)
'''

# current issues: tle on group 3 (n <= 100) even though group 4 (n <= 1000000) worked completely fine???

out = ""
x = input()

for i in x:
    if i == "<":
        out = out[:-1]
    else:
        out += i

print(out)