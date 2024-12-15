#Öppnar filen och tankar in den
file = open("D:/Repos/aoc2024/Day2/input.txt", "r")
content = file.readlines()
file.close()

#Skapar en lista med strängar utifrån inputfilen
inputList = []
while len(content) > 0:
    tempRow = (content.pop(0))
    inputList.append(tempRow.split())

print(inputList)

counter = 0
#Börjar med att ta fram första värdet ur arrayen som är en lista
while len(inputList) > 0:
    tempList = inputList.pop(0)
    tempListInt = []
    # Skapar en lista med ints istället
    while len(tempList) > 0:
            tempListInt.append(int(tempList.pop(0)))
    else:
        # Bearbetar en egen temporär lista samt plussar på countern med 1 om den är "säker"
        i = 0
        while len(tempListInt) > i+1:
            if (tempListInt[i] != tempListInt[i+1]) and (abs(tempListInt[i] - tempListInt[i+1]) < 4):
                if (tempListInt[0] > tempListInt[1]) and (tempListInt[i] > tempListInt[i+1]):
                    i+=1
                else:
                    if (tempListInt[0] < tempListInt[1]) and (tempListInt[i] < tempListInt[i+1]):
                        i+=1
                    else:
                        break
            else:
                break
        else:
            counter += 1
else:
    print(counter)
