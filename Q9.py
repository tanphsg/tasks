dancestep = input("What's your first dance character ")
dancemoves = ["+", "&", ">", "<"]
dancedisplay = []
idx = -4
num_chars = 0
for i in range(len(dancemoves)):
    if dancemoves[i] == dancestep:  # to append the first char that user input into the list
        dancedisplay.append(dancemoves[i])
        num_chars +=1
        while i < 3:  # to cater for subsequent chars after the char that user input except "<" as the next while loop
            i += 1                 # will help to handle
            dancedisplay.append(dancemoves[i])
            num_chars +=1
        while idx < 0 or num_chars < 8 : # to append the char "+" by using index -4 if the user input "<"
            dancedisplay.append(dancemoves[idx])
            idx +=1
            num_chars +=1
# print(dancedisplay)
for n in range(8):
    print(dancedisplay[n], end='')

