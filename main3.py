def romanToInt(romanInput):
    
    #All roman units with integer equivalent values
    roman = {'M':1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    
    #result
    resultInteger = 0
    
    #Go from 0 to len-1 if integer equivalent is greater than next element then add it else subtract it 
    
    for i in range(0)