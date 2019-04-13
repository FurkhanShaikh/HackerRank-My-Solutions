#problem link : https://www.hackerrank.com/challenges/itertools-permutations/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
data = raw_input().split()
string = data[0]
k = int(data[1])
strlist= list(string)
strlist.sort()
perms= list(permutations(strlist,k))
for item in perms:
    res=''
    for i in range(len(item)):
        res+=str(item[i])
    print res
