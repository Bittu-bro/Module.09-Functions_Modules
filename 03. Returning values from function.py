# def even_odd(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
# result = even_odd(3)
# print(result)


# def greating_function(name):
#     print(f"Hello, {name}")
#     print("I am learing Python")
 
# print(f"{greating_function("Bittu")} Created a Function.\n We are just printing it in our terminal.")


# # when we printing upper function we got "None"
# #let's solve it


# def even_odd(num):
#     if num % 2 == 0:
#         return("Even")
#     else:
#         return("Odd")
# result = even_odd(3)
# print(result)


# def add(num1, num2):
#     result = num1 + num2
#     return result

# num1 = int(input("Enter 1st your Number: "))
# num2 = int(input("Enter your 2nd Number: "))

# addition = add(num1,num2)

# print(f"Your Addition is {addition}.")  




def add(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    return addition, subtraction, multiplication
    

num1 = int(input("Enter your 1st Number: "))
num2 = int(input("Enter your 2nd Number: "))

fun1, fun2, fun3 = add(num1,num2)


print(f"Your Addition is {fun1}.")  
print(f"Your Subtraction is {fun2}.")  
print(f"Your Multiplication is {fun3}.")  