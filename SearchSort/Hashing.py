# we can take ordinal values and use the remainder method to get a hash value
def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])
    return sum%tablesize

firstList = [None] * 4
hashValue1 = hash('cat', len(firstList))
print(hashValue1)


