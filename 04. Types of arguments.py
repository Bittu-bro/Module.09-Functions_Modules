# def add(num1,num2):
#     return num1 + num2

# Positional Argument- passing the arguments in order of their position.

# result = add(2,3)




# Defult Arguments

# def add(num1,num2 = 3):
#     return num1 + num2

# result = add(2,4)

# print(result)



# def add(num1,num2=6 ,num3=3):
#     return num1 + num2 + num3

# result = add(8)

# print(result)


# Keyword Argument

def add(num1,num2=6 ,num3=3):
    return num1 + num2 + num3

result = add(3,3,num3 = 3) # In Python, 1.positional arguments(Primary) and 2.keyword arguments(Secondry) follow this order.

print(result)