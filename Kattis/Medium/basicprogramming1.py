'''
Problem Name: Basic Programming 1
Link: https://open.kattis.com/problems/basicprogramming1
Memory Limit: 1024 MB
CPU Time Limit: 1 second
Difficulty: 1.2 - 4.5 (Medium)
'''

# current issues: tle on some later problems, likely due to t == 7

import statistics

n, t = map(int, input().split())
a = list(map(int, input().split()))

if (t == 1):
    print(7)
elif (t == 2):
    if a[0] > a[1]:
        print("Bigger")
    elif a[0] == a[1]:
        print("Equal")
    else:
        print("Smaller")
elif (t == 3):
    # median
    print(statistics.median(a[0:3]))
elif (t == 4):
    print(sum(a))
elif (t == 5):
    b = []
    for i in a:
        if i % 2 == 0: #even
            b.append(i)
    
    print(sum(b))
elif (t == 6):
    out = ""
    for i in a:
        x = i % 26
        out += chr(x + 97)
    
    print(out)
elif (t == 7):
    ind = [0]
    i = 0
    while True:
        try:
            i = a[i]
        except:
            print("Out")
            quit()
        
        if (i == n-1):
            print("Done")
            quit()
        elif (i in ind):
            print("Cyclic")
            quit()
        else:
            ind.append(i)