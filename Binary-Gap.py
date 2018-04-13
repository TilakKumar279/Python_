def solution(N):
    # write your code in Python 3.6
    c="{0:b}".format(N).replace('1','ab').split('a')
    for i in range (len(c)):
        if (c[i].startswith('b') and i!= (len(c)-1)):
            c[i]=c[i].count('0')
        else:
            c[i]=0
    return(max(c))