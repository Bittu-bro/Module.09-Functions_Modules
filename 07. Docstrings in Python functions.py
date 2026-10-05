def arethematics(num1,num2):
    '''
    We are doing some arethematics calculation.
    like:
            addition
            subtraction
            multiplication
            division
    num1 & num2 taking as a intiger 

    and
         we are returing value of calculation as a
         return result1
         return result2
         return result3      
         return result4
    '''
    result1 = num1 + num2
    result2 = num1 - num2
    result3 = num1 * num2
    result4 = num1 / num2
    return result1, result2, result3, result4
num1 = int(input("Enter ypur 1st Number: "))
num2 = int(input("Enter ypur 2nd Number: "))
add, sub, mult, div = arethematics(1,1)
print(f"Your addition is {add}.")   
print(f"Your subtraction is {sub}.")   
print(f"Your multiplication is {mult}.")   
print(f"Your division is {div}.")   


help(len)
help(print)