def fact(f) :
    if  f == 1 :
        return 1
    else :
        r = f * fact((f-1))
        return r

v=8
print(fact(v))
