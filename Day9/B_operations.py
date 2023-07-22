## accessing calculator module in this file.

#approch 1:need to call module name.
# import A_calculator

# A_calculator.add(100,200)
# A_calculator.mul(20,25)

# approach 2: no need to call module name
from A_calculator import add,mul
add(10,20)      #30
mul(3,5)        #15

from A_calculator import *    # * represent all functions.
add(10,20)      #30
mul(3,5)        #15

