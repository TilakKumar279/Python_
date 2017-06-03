#!/bin/python3

n = int(input())
lines = ""
for i in range(n):
    lines+=input()+"\n"
lines=list(filter(lambda lines: lines!='\n' and lines!=' ',lines))  
result =[]
for i in range(0,len(lines),4):
  for j in range(0,2,1):
      result.append(int(lines[i+j+2])*2 -int(lines[i+j]))

for i in range(0,len(result),2):
  print(result[i], result[i+1]) 


  10
1 1 2 2
4 3 5 2
2 4 5 6
1 2 2 2
1 1 1 1
1 2 2 1
1 8 7 8
9 1 1 1
8 4 3 2
7 8 9 1

3 3
6 1
8 8
3 2
1 1
3 0
13 8
-7 1
-2 0
11 -6