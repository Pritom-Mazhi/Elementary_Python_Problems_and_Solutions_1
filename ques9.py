import numpy

def calculation(h,l):
    A = numpy.array([[1,1],[2,4]])
    B = numpy.array([h,l])
    C = numpy.linalg.solve(A,B)
    chicken = int(C[0])
    rabbit = int(C[1])
    print("chicken: {} rabbit: {}".format(chicken,rabbit))

print("please enter the number of heads and legs")
h = int(input())
l = int(input())
calculation(h,l)
