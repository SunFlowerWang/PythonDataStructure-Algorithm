def orderedSequentialSearch(alist,item):
    pos = 0 # pointer to keep track the positon
    found = False
    stop = False

    while (pos < len(alist) and not found and not stop):
        # if alist[pos] == item:
        #     found = True
        # else:
        #     if (alist[pos] > item):
        #         stop = True
        #     else:
        #         pos = pos + 1
        if alist[pos] == item:
            found == True
        elif alist[pos] > item:
            stop = True
        else:
            pos = pos + 1
    return found



def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found

testList = [1,2,3,4,5,6,7,8]
print(sequentialSearch(testList, 9))
print(sequentialSearch(testList,5))
alist = [17,20,34,15,39,35]
alist.sort()
print(alist)
print(orderedSequentialSearch(alist, 30))
