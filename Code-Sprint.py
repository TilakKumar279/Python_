#CODE SPRINT
#!/bin/python3

import sys

def solve(a):
    # Complete this function
    b=a[:int(len(a)/2)]
    c=a[int(len(a)/2):]
    if(sum(b) < sum(c)): dif = sum(c)-sum(b)
    if(sum(b) > sum(c)): dif = sum(b)-sum(c)
    if(sum(b) ==sum(c)): dif = 0
    return dif

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
result = solve(a)
print(result)


#!/bin/python3

import sys

def getMagicNumber(s, k, b, m):
    # Complete this function
    t=[]
    for i in range(len(s)-k+1):
        t.append(s[i:i+k])
        t[i]=int(t[i],b)
        t[i]= t[i]%m
        
    return sum(t)

s = input().strip()
k, b, m = input().strip().split(' ')
k, b, m = [int(k), int(b), int(m)]
result = getMagicNumber(s, k, b, m)
print(result)









import sys

def find_days(n,k,v):
    #v.sort()
    v = list(map(int, v))
    v = [v[i+1]-v[i] for i in range(len(v)-1)]
    v = [i for i in v if i!=0]
    v = [v[i] - k for i in range(len(v))]
    print (len(set(v)))
        
        


t = int(input())
for i in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    v = input().strip().split(' ')
    find_days(n,k,v)









crt=['phonebook', 'phonebook(0)', 'phonebook(1)', 'todo']
command = input().strip()
def name_check(name):
  for i in range(len(crt)):
    if any(name in s for s in crt):
      crt.append(name+'(%s)'%i)
    else:crt
      crt.append(name)
    if(name+'(%s)'%i == crt[i]):
      crt.append(name+'%s'%i+1)
print (set(crt))


name = command[4:len(command)]
if (command[0:3] == "crt"):
  a=name_check(name)
if (command[0:3] == "del"):
  s= crt.index(name)
  del crt[s]   
if (command[0:3] == "rnm"):
  s= crt.index(name)
  del crt[s]
  a=name_check(name)


# this is to exor love printing the values in the double summation within  the range
# there are two versions which is used to update along with the constraints
  import sys

def xorlove(k, p, r, a):
    # Complete this function
    kpr_sum=0
    for i in range(p-1,r-1):
        for j in range(i+1, r):
            kpr_sum = (k^(a[i]^a[j])) +kpr_sum  
    return kpr_sum

n = int(input())
a =list(map(int, input().strip().split(' ')))
m = int(input())

for i in range(m):
    k, p, r = input().strip().split(' ')
    k, p, r = [int(k), int(p), int(r)]
    print(xorlove(k,p,r,a))


 import sys
n = int(input())
if(n<=pow(10,5) or n>=1):
    a =list(map(int, input().strip().split(' ')))
m = int(input())
if(m<=pow(10,5) or m>=1 and len(a)<= pow(10,6)):
    for i in range(m):
        kpr_sum=0
        k, p, r = input().strip().split(' ')
        k, p, r = [int(k), int(p), int(r)]
        if(k<=pow(10,6) or k>=0 and (p>=1 or p<=r) and (r>=p or r<=n) and (n>=r) ):
            for i in range(p-1,r-1):
                for j in range(i+1, r):
                    kpr_sum = (k^(a[i]^a[j])) +kpr_sum
                    if(p==r):kpr_sum=0
            print(kpr_sum)


#!/bin/python3
# problem where the user stripes the card several times in a month where the
# values does not exceed 100

import sys

def getPoints(month1, month2, month3):
    # Complete this function
    m1,m2,m3=month1,month2,month3
    sum_m1 = 10*m1
    sum_m2 = 10*m2
    sum_m3 = 10*m3
    if(m1*10 > 100): sum_m1=100
    if(m2*10 > 100): sum_m2=100
    if(m3*10 > 100): sum_m3=100
    return(sum_m1+sum_m2+sum_m3)
    

month1,month2,month3 = input().strip().split(' ')
month1,month2,month3 = [int(month1),int(month2),int(month3)]
pointsEarned = getPoints(month1, month2, month3)
print(pointsEarned)

# Count the number of times the string appears  in the supplied element

n = int(input())
a,b=[],[]
for i in range(n):
    a.append(input().strip())
q=int(input())
for i in range(q):
    b.append(input().strip())
    print(a.count(b[i]))


 # Printing the maxim value of the sequence and with contraints
 n,m = input().strip().split(' ')
n,m = [ int(n), int(m)]
seql= [0 for  i in range(n)]
for i in range(m):
    a,b,k = input().strip().split(' ')
    a,b,k = [int(a), int(b), int(k)]
    for j in range(a-1,b,1):
        seql[j]=seql[j]+k
print(max(seql))

n,m = input().strip().split(' ')
n,m = [ int(n), int(m)]
if(n>=3 and n<=pow(10,7) and m>=1 and m<= 2*pow(10,5)):
    seql= [0 for i in range(n)]
    for i in range(m):
        a,b,k = input().strip().split(' ')
        a,b,k = [int(a), int(b), int(k)]
        if(a>=1 and a<=b and b>= a and b<=n and k>=0 and k<=pow(10,9)):
            for j in range(a-1,b,1):
                seql[j]=seql[j]+k
        else:
            print(max(seql))
    print(max(seql))
else:
    print(max(seql))


# printing the code for the with sequence for Dynamic Array
n, num_q = input().strip().split(' ')
n, num_q = [int(n), int(num_q)]
s=[[0 for i in range(n)] for j in range(n)]
trim =False
la = 0
for i in range(num_q):
    q,x,y = list(map(int, input().strip().split(' ')))
    if (q==1):
        s[(x^la)%n].append(y)
        
    if(q==2):
        if(trim==False):
            for k in range(n):
                for j in range(n):
                    s[k].remove(0)
            trim=True        
        la=s[(x^la)%n][y%len(s)]
        print(la)


