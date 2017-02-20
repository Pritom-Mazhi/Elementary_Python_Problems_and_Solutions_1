
def solution(someInput):

	for i in someInput:
		row=someInput[0]
		col=someInput[1]
	arr=[[x for x in range(col)] for y in range(row)]

	for i in range(row):
		for j in range(col):
			arr[i][j]=i*j

	return arr

someInput=list(map(int,input().split(",")))
print(solution(someInput))
