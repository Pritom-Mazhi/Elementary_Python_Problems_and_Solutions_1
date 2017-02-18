def revLi(li):
    if li:
        return [li[-1]] + rev(li[:-1])
    else :
        return []
c=[1,2,3,4,5]
print(revLi(c))
