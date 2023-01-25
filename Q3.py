singleword = input("Give a single word less than 50 chars long ")
newword=singleword.lower()
length = len(singleword)
numofrepeat = (30//length) + 1
print("num of repeat", numofrepeat)
print("the new word is ", newword*numofrepeat)

