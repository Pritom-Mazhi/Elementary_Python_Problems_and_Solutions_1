def remove_duplicate(aList):

    new_list = []
    for i in aList:
        if i not in new_list:
            new_list.append(i)
    return new_list


def reverse_list(blist):

	if len(blist) != 1:
		return [blist[-1]]+reverse_list(blist[:-1])
	return blist


cList = list(map(str,input().split(",")))
print("List After Removing Duplicate : {} ".format(remove_duplicate(cList)))
print("Original Order Reversed List  : {} ".format(reverse_list(remove_duplicate(cList))))
