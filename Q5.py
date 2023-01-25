firstinput = int(input("Input a num betw -100 and 100: "))
secinput = input("Input an operator * or + ")
thirdinput = int(input("Input another num betw -100 and 100: "))
if secinput == "*":
    result = firstinput * thirdinput
elif secinput == "+":
    result = firstinput + thirdinput
print("The result is ", result)
                
