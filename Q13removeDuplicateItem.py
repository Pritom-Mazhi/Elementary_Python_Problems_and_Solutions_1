def removeDuplicate(someList):
    new_list=[]
	for i in someList:
		if i not in new_list:
			new_list.append(i)
    return new_list

a = list(map(str,input().split(",")))
print(removeDuplicate(a))
