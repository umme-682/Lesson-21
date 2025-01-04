def binaryToDecimal(binary):
    
    # variable set as 0
    decimal, i = 0, 0
    
    # while there is a digit multiply with 2 power i
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        
        #increment 1
        i += 1
        print("Decimal: ", decimal)
        
binary = int(input("Enter your binary: "))
binaryToDecimal(binary)