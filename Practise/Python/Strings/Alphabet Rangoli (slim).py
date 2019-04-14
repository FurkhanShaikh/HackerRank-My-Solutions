import string
def print_rangoli(size):
    if(size==1):
        print "a"
        return
    alphas= list(string.ascii_lowercase)
    maxalpha = size-1
    rows=size*2 - 1
    midrow=rows//2
    cols = size + 3*(size-1)
    midcol = (cols -1)//2
    for i in range(midrow):
        al=maxalpha
        midstr=alphas[al]
        al-=1
        for j in range(0,i):
            midstr+='-'+alphas[al]
            al-=1
        al+=2
        for j in range(0,i):
            midstr+='-'+alphas[al]
            al+=1
        print midstr.center(cols,'-')
    for i in range(midrow,-1,-1):
        al=maxalpha
        midstr=alphas[al]
        al-=1
        for j in range(0,i):
            midstr+='-'+alphas[al]
            al-=1
        al+=2
        for j in range(0,i):
            midstr+='-'+alphas[al]
            al+=1
        print midstr.center(cols,'-')
    return
if __name__ == '__main__':
    n = int(raw_input())
    print_rangoli(n)
