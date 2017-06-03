def palindrome(name):
  if(name[::-1] == name):
    return True
  
if(palindrome(input("Enter:"))):
  print('Yeah!')
else: print('Nope')  


#!/bin/python3
# reverse the elements in the array

import sys
n = int(input())
arr = input().strip().split()
arr =arr[::-1]
print(*arr)

# Left rotate the elements in the array

n,d=input().strip().split()
n,d=[int(n), int(d)]
a = input().strip().split()
print(*(a[d:] + a[:d]))
