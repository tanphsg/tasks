listofnames = []
firstname = input("firstname ")
secname = input("Secondname ")
thirdname = input("Thirdname ")
fourthname = input("Fourthname ")
fifthname = input("Fifthname ")
listofnames.append(firstname)
listofnames.append(secname)
listofnames.append(thirdname)
listofnames.append(fourthname)
listofnames.append(fifthname)
for i in range(len(listofnames)):
    name = listofnames[i]
    if name == 'Ellie':
        index = listofnames.index('Ellie')
        index+=1
        if index == 1:
           print("1st")
        elif index == 2:
            print("2nd")
        elif index == 3:
            print("3rd")
        elif index == 4:
            print("4th")
        elif index == 5:
            print("5th")
            
           
