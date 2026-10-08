#1. .py file is a module
#2. built in module
#2.=> math, random, datetime, ...., etc.
# 
# 
# How to import a module in python 
#=> syntex - 'import module name'

# syntex for only few functon importing from one module/variable- 'from module_name import function_name'

import math
# calculate square root -
num = 100
output = math.sqrt(num) # module.function name (argument)
print(f"Square root of {num} is {output}")


# calculate area of circle
r = 22/21
area_of_circle =round(math.pi*(r**2),2)
print(f"Area of circle is {area_of_circle}")

# Trough a die
from random import randint  
print(f"Your die face is {randint(1,6)}.")

# from datetime import daytime as alias
import datetime as dt
print((dt.time(7,17,30)))

