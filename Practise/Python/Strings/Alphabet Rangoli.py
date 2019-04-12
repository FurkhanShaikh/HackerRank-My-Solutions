#Problem Statement: https://www.hackerrank.com/challenges/alphabet-rangoli/problem
import sys
import string
def print_rangoli(size):
    if(size==1):
        print "a"
        return
    # alphas= list("abcdefghijklmnopqrstuvwxyz")
    alphas= list(string.ascii_lowercase)
    maxalpha = size-1
    rows=size*2 - 1
    midrow=rows//2
    cols = size + 3*(size-1)
    mid = (cols -1)//2
    k=2
    #first row
    for j in range(cols):
        if(j==mid):
            sys.stdout.write(alphas[maxalpha])
        else:
            sys.stdout.write('-')
    print
    #middle
    for i in range(1,midrow):
        al=maxalpha
        h=k
        for j in range(0,mid):
            if(j==(mid-k)):
                sys.stdout.write(alphas[al])
                al-=1
                h-=2
            elif(j==(mid-h)):
                sys.stdout.write(alphas[al])
                al-=1
                h-=2
            else:
                sys.stdout.write('-')
        for j in range(mid,cols):
            if(i!=midrow):
                if(j==(mid-h) and j<=(mid+(2*i))):
                    sys.stdout.write(alphas[al])
                    al+=1
                    h-=2
                else:
                    sys.stdout.write('-')
            else:
                if(j==(mid-h)):
                    sys.stdout.write(alphas[al])
                    al+=1
                    h-=2
                else:
                    sys.stdout.write('-')
        k+=2
        print 
    temp=0
    for i in range(midrow,rows-1):
        al=maxalpha
        h=k
        for j in range(0,mid):
            if(j==(mid-k)):
                sys.stdout.write(alphas[al])
                al-=1
                h-=2
            elif(j==(mid-h)):
                sys.stdout.write(alphas[al])
                al-=1
                h-=2
            else:
                sys.stdout.write('-')
        for j in range(mid,cols):
            if(i!=midrow):
                if(j==(mid-h) and j<=(cols-(2*temp))):
                    sys.stdout.write(alphas[al])
                    al+=1
                    h-=2
                else:
                    sys.stdout.write('-')
            else:
                if(j==(mid-h)):
                    sys.stdout.write(alphas[al])
                    al+=1
                    h-=2
                else:
                    sys.stdout.write('-')
        k-=2
        temp+=1
        print 
    #last row
    for j in range(cols):
        if(j==mid):
            sys.stdout.write(alphas[maxalpha])
        else:
            sys.stdout.write('-')
    return
if __name__ == '__main__':
    n = int(raw_input())
    print_rangoli(n)
