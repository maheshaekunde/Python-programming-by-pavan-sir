# Concatenation
# Concatenation: obtaining a new string that contains both of the original strings

print(10+10)        #20 valid
print(10.5 + 12.0)  #22.5 valid

print(10+10.5)      #20.5 valid

# this will concatenate two strings
print("welcome"+"python")       #welcomepython  valid

print(True+5)       #6  valid (True==1 and False==0)
print(False+5)      #5  valid
print(True+True)    #2  valid
print(False+False)  #0 valid
print(True+False)   #1 valid

print(10+"welcome")     #TypeError: unsupported operand type(s) for +: 'int' and 'str'

