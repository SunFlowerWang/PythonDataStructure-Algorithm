# def SbinarySearch(alist,item):
#     #base case of recursive call
#     if len(alist) == 0:
#         return False
#     else: 
#         midPoint = len(alist)//2
#         if (alist[midPoint] == item):
#             return True
#         else:
#             if (item < alist[midPoint]):
#                 SbinarySearch(alist[:midPoint],item)
#             else:
#                 SbinarySearch(alist[midPoint+1:], item)

# def binarySearch2(alist, item):
#     if len(alist) == 0:        
#         return False
# 	else:
# 	    midpoint = len(alist)//2
# 	    if alist[midpoint]==item:
# 	        return True
# 	    else:
# 	        if item<alist[midpoint]:
# 	            return binarySearch2(alist[:midpoint],item)
# 	        else:	           
#                 return binarySearch2(alist[midpoint+1:],item)
def binarySearch(alist,item):
    first = 0
    last = len(alist) - 1
    found = False

    while first<=last and not found:
        midPoint = (first + last) // 2
        if alist[midPoint] == item:
            found = True
        elif item < alist[midPoint]:
            last = midPoint - 1
        elif item > alist[midPoint]:
            first = midPoint + 1
    return found

testList = [0,1,2,3,8,9,17,19,32,43]
print(binarySearch(testList, 3))
print(binarySearch(testList, 11))
# print(SbinarySearch(testList,3))
# print(SbinarySearch(testList,11))
