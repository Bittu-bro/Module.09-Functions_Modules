# # Traditional method
# def add(num1):
#     return num1 + 1
# def square(num2):
#     return num2 ** 2

# number = int(input("Enter your number: "))

# result = add(number)
# final_result = square(result)


# print(f" Here is the Upgraded Result: {result}.")
# print(f"Here is the Final Result: {final_result}")



# Modern method -
def add(num1):
    return num1 + 1
def square(num2):
    return num2 ** 2

number = int(input("Enter your number: "))
final_result = square(add(number)) # yaha pr ham ek function ke aandar dushre function ko call kar rahe hai

print(f" Here is the Upgraded Result: {add(number)}.")
print(f"Here is the Final Result: {final_result}")