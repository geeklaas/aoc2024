listA = [3,3,87,5,4,3,7,8,9,455,645,3,345]
listB = [234,345,66,8,465,456,8,465,2,45,23,52,345]



listA.sort()
listB.sort()

#print(listA)
#print(listB)

i = 0
while len(listA) > 0:
   i = i + abs(listA.pop(0) - listB.pop(0))
else:
    print(i)