#Problem Link: https://www.hackerrank.com/challenges/designer-door-mat/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
N,M = map(int,raw_input().split())
midrow = N//2
for i in range(0,midrow):
    print (".|."*(1+2*i)).center(M,'-')
print "WELCOME".center(M,'-')
for i in range(midrow-1,-1,-1):
    print (".|."*(1+2*i)).center(M,'-')

