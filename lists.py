myList = [1, 4, 9]
temp = myList[0]
for i in range(len(myList) - 1):
    myList[i] = myList[i + 1]
myList[len(myList) - 1] = temp
print(myList)