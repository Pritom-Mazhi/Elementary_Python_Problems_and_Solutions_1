def toh(n,start,mid,end) :
    if n==1 :
        print ("{} to {}".format(start,end))
    if n>1 :
        toh(n-1,start,end,mid)
        print ("{} to {}".format(start,end))
        toh(n-1,mid,start,end)

toh(3,'a','b','c')
