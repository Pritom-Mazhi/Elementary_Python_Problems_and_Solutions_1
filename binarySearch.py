def binarySearch(someItem,someList) :
    index = None
    start = 0
    end= len(someList)-1
    while start <= end :
            midpoint     = (start+end)//2
            if someItem == someList[midpoint] :
                index = midpoint
                # end = midpoint - 1
            elif  someItem > someList[midpoint] :

                start = midpoint + 1
            else:

                end = midpoint - 1

    return index

list1 = [1,2,3,4,5,5,5,6,8,10,22]
someItem = int(input())
print(binarySearch(5,sorted(list1)))
