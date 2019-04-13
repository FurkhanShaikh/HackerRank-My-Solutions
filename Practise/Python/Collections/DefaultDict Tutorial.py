#Problem Link: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem 
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n,m = map(int,raw_input().split())
A = defaultdict(list)
index =1
for i in range(n):
    word = raw_input()
    A[word].append(index)
    index+=1
B = list()
for i in range(m):
    word = raw_input()
    B.append(word)

for x in B:
    if(len(A[x])!=0):
        for i in range(len(A[x])):
            print A[x][i],
    else:
        print '-1',
    print


