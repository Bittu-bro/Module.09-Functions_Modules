n = 1 # Global value
def fun():
    #global n # this function apply local value globaly
    #n = 5 # local value ## if it is missing, global value apply locally
    print(f"in {n}")

fun()  
print("out", n)
  