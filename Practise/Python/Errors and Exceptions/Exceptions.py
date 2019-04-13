#problem link : hackerrank.com/challenges/exceptions/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
T =int(raw_input())
for i in range(T):
    a,b = raw_input().split()
    try:
        a = int(a)
        b = int(b)
        x=a//b
        print x
    except ZeroDivisionError as e:
        print "Error Code:",e
    except ValueError as e:
        print "Error Code:",e

