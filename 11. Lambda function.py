# #lambda

# in general: 
def even_odd(num):
    if num % 2 ==0:
        return "Even"
    else:
        return "Odd"
 
number = int(input("Enter your number: "))
result = even_odd(number)    
print(f"Your number is {result}.")
print(f"{(even_odd(number))}")





# # But in lambda
# fun = lambda num1: "Odd" if num1 % 2 != 00 else "Even" 
# # Yaha pr function ka naam fun hai, aap yah bhi keh sakte hai ki fun variable Mein assign hai.
# # And function ko print karne ke liye "fun(arguments)" likhna parta hai.
# num1 = int(input("Enter your number: "))
# print(fun(num1))



# But in lambda (function as a argument)
fun1 = lambda num1: num1 + 1
fun2= lambda fun1: "Odd" if (fun1(num1)) % 2 != 00 else "Even" 
num1 = int(input("Enter your number: "))



print((fun1(num1)))
print((fun2(fun1)))
