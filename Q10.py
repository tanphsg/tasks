ingredient = input("Input your ingredient ")
counti = 0
countm = 0
countc = 0
countw = 0
for n in range(len(ingredient)):
    if ingredient[n]== "I":
        counti+=1
    elif ingredient[n]== "M":
        countm += 1
    elif ingredient[n] == "C":
        countc += 1
    elif ingredient[n] == "W":
        countw += 1
if counti != 2:
   print("I")
elif countm != 1:
   print("M")     
elif countc != 3:
    print("C")
elif countw != 1:
    print("W")
