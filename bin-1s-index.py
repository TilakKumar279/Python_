#!/bin/python3

import sys

def duplication(x):
  s ='0'
  t ='1'
  for i in range(10):
    r = s  
    r = s.replace('1','a')
    t = r.replace('0','1')
    t = t.replace('a','0')
    s= s+t  
  return s[x] 

q = int(input().strip())
for a0 in range(q):
    x = int(input().strip())
    result = duplication(x)
    print(result)