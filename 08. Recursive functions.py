# def factorial(num):
#     fact = 1
#     while num >1:
#         fact = num * fact
#         num -=1
#     return fact


# print(factorial(5))



def factorial(num):
    if num == 1:
        return 1
    else:
        fact = num * factorial(num-1)
        return fact
print(factorial(5))    