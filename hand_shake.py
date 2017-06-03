#!/bin/python3
import sys
import itertools

# your code goes here
def hand_s(N):
    a=[]
    f=[]
    d=[]
    for i in range(N):
	       a.append(i)
    
    f=list(itertools.permutations(a,2))
    
    for i in range (len(f)):
        e=list(f[i])
        e.sort()
        if (e not in d):
            d.append(e)
    return len(d)

num =0
T = int(input().strip())
for a0 in range(T):
    N = int(input().strip())
    num = int(N)
    b = hand_s(num)
    print(b)
    