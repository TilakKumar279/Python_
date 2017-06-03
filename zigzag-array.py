#!/bin/python3

import sys

def minimumDeletions(a):
    # Complete this function
    count =0
    for i in range(len(a)-2):
        if (a[i] < a[i+1] and a[i] < a[i+2] and  a[i+1] < a[i+2]):
            count +=1
        if (a[i] > a[i+1] and a[i] > a[i+2] and  a[i+1] > a[i+2]):
            count +=1
    return count
    
    

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Return the minimum number of elements to delete to make the array zigzag
result = minimumDeletions(a)
print(result)