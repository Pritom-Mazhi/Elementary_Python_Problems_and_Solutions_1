from math import sqrt


def calculation(someInput):
	C=50
	H=30
	Result=[]

	for i in someInput:
		Result.append(str(round(sqrt((2*C*i)/H))))
	return ",".join(Result)

D=map(float,input().split(","))
print(calculation(D))
