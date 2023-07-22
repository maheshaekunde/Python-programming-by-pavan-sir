# # ex 1:
# print("this is starting point of program..")
# print("this is starting point of program..")
# print("this is starting point of program..")
# print(x)        #NameError: name 'x' is not defined
# print("this is end of the program..")
# print("this is end of the program..")
# print("this is end of the program..")

# ex 2:
# print("this is starting point of program..")
# print("this is starting point of program..")
# print("this is starting point of program..")
# try:
#     print(x)
# except:
#     print("exception occured...")
#
# print("this is end of the program..")
# print("this is end of the program..")
# print("this is end of the program..")


# ex 3:
# print("this is starting point of program..")
# print("program is progress..")
# print(10/0)     #ZeroDivisionError: division by zero
# print("program completed..")

## handled:
# print("this is starting point of program..")
# print("program is progress..")
#
# try:
#     print(10/0)     #ZeroDivisionError: division by zero
# except ZeroDivisionError:
#     print("expception handled..")
#
# print("program completed..")



## ex 3: Multiple except bocks- try,except else,finally
# try:
#     num1,num2=10,0
#     result=num1/num2
#     print("result is:",result)
# except ZeroDivisionError:
#     print("this is ZeroDivisionError exception")
# else:                       # if there is no any exception the else execute.
#     print("no exception")

####### else handled ###############
# if there is no any exception the else execute.
# try:
#     num1,num2=10,5
#     result=num1/num2
#     print("result is:",result)
# except ZeroDivisionError:
#     print("this is ZeroDivisionError exception")
# else:                       # if there is no any exception the else execute.
#     print("no exception")
#


#################### finally ####################
# if there is exception or no exception finally is always execute.
try:
    num1,num2=10,0
    result=num1/num2
    print("result is:",result)
except ZeroDivisionError:
    print("this is ZeroDivisionError exception")
else:                       # if there is no any exception the else execute.
    print("no exception")
finally:                    # if there is exception or no exception finally is always execute.
    print("always execute..")