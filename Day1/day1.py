listA = []
listB = []

file = open("D:/Repos/aoc2024/Day1/input.txt", "r")
content = file.readlines()
file.close()

while len(content) > 0:
   tempRow = (content.pop(0))
   tempList = tempRow.split()
   listA.append(int(tempList.pop(0)))
   listB.append(int(tempList.pop(0)))  

listA.sort()
listB.sort()

#print(listA)
#print(listB)

i = 0
while len(listA) > 0:
   i = i + abs(listA.pop(0) - listB.pop(0))
else:
    print(i)