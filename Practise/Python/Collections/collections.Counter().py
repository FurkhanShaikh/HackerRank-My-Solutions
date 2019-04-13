#problem link : https://www.hackerrank.com/challenges/collections-counter/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

X = int(raw_input())
sizes = map(int,raw_input().split())
cust = int(raw_input())
desired =[]
for i in range(cust):
    temp = map(int,raw_input().split())
    desired.append(temp)
count = Counter(sizes)
money = 0
for dlist in desired:
    if(dlist[0] in sizes):
        if(count[dlist[0]]!=0):
            count[dlist[0]]-=1
            money+=dlist[1]
print money

