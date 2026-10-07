# # Filter() filter kar ke ek list mai store kar leta hai.
# sequence = [2,3,4,5,6]
# odd = lambda num: True if num % 2 != 0 else False
# even = lambda num: True if num % 2 == 0 else False


# filted_output1 = filter(odd,sequence)
# filted_output2 = filter(even,sequence)


# print("Odd", list(filted_output1)) # yaha pr aagar ham list mai convert nahi karenge to output mai memory location type kuch aayega !
# print("Even", list(filted_output2))



# # Filter() (Short form: )

# filted_output1 = filter(lambda num: True if num % 2 != 0 else False, [2,3,4,5,6])
# filted_output2 = filter(lambda num: True if num % 2 == 0 else False, [2,3,4,5,6])

# print("Odd", list(filted_output1)) 
# print("Even", list(filted_output2))





# map(): 
filted_output1 = map(lambda num: True if num % 2 != 0 else False, [2,3,4,5,6])
print("Maped Value: ", list(filted_output1)) 



maped_fun1 = map(lambda num: num ** 2 , [1,2,3,4,5,6]) # maped function dose maped in to the expreesion
print(list(maped_fun1))


name = "bittu", "shivam", "piyush"
clean_name = list(map(lambda name :name.upper(),name))
print(clean_name)