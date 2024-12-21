#program to find if a number is Armstrong Number

#Take input from the user
number = int(input("Input Your Number: "))

#Calculate number of digits 
digits = len(str(number))

#Intialize result variable 
resultNumber = 0

#Find the sum of the a^digits of each digit
temp = number
while temp > 0:
    digit = temp % 10
    resultNumber += digit ** digits 
    temp //= 10
    
#Display the result
if number == resultNumber:
    print(number,"is an armstrong number")
else:
    print(number,"is not an armstrong number")
