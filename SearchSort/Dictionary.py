thisDict = {
    "brand": "Ford",
    "model": "muestang",
    "year": 1964
}
print(thisDict)

newDict = dict()
print(newDict)

x = thisDict["model"]
print(x)

#Get the value of "model" key
y = thisDict.get("model")
print(y)

print("change the value of a specific key")
thisDict["year"] = 2018
print(thisDict)

print("loop through the dictionary, print all the key names")
for x in thisDict:
    print(x,thisDict[x])

print("print the values() in the dict")
for x in thisDict.values():
    print(x)

print("print the both keys and items using items()")
for x, y, in thisDict.items():
    print(x,y)

print("check if the model is present in the dictionary")
if "model" in thisDict:
    print("yes, 'model' is one of the keys")

print(len(thisDict))
print("adding items into the dictionary")
thisDict['color'] = 'red'
print(thisDict)

print("remove the item from a dictionary")
print(" the pop() methods removes the item with the specified key name")
thisDict.pop('model')
print(thisDict)

print("the popitem() remove the last inserted item")
thisDict.popitem()
print(thisDict)