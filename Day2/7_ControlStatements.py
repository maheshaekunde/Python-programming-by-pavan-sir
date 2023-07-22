# 1) Conditional statements: if    if,else    elif

# ex:  print a person is eligible for vote or not

# Ex1:
# age should greater equal to 18

# age=16
#
# if age>= 18:
#     print("Eligible for vote")
# else:
#     print("Not eligible for vote")

# Ex 2:
# age=int(input("Age for voting:"))
# if age>=18:
#     print("Eligible")
# else:
#     print("Not eligible")


# Ex 3:
# if 1:
#     print("One")
# else:
#     print("Not one")

# Ex 4: find a number is even or odd  (num%2=0 then even   or num%2=1 then odd)
# num=10      # for even number
#
# if num%2==0:
#     print("even")
# else:
#     print("odd")
#
#
# num1=11      # for odd number
#
# if num1%2==1:
#     print("odd")
# else:
#     print("even")

# by using input statement:
# num = int(input("Enter the number:"))
#
# if num%2==0:
#     print("Even")
# else:
#     print("Odd")


# if else in single line(ternary operator)
# num=int(input("Enter number:"))
#
# print("Even number") if num%2==0 else print("Odd number")


#################### elif ################

# weeknum=int(input("Enter the Week number:"))
#
# if weeknum==1:
#     print("sunday")
# elif weeknum==2:
#     print("monday")
# elif weeknum==3:
#     print("Tuesday")
# elif weeknum == 4:
#     print("Wednesday")
# elif weeknum == 5:
#     print("Thursday")
# elif weeknum == 6:
#     print("Friday")
# elif weeknum == 7:
#     print("Saturday")
# else:
#     print("Holiday")


# Check the given number is positive or nagetive:
'''
num=float(input("Enter positive of negative number:"))

if num>=0:
    if num==0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")'''


# # Check the largest of 2 numbers
# a=150
# b=167
#
# if a>b:
#     print("a is greatest")
# else:
#     print("b is greatest")

# Check the largest of 3 numbers
# a=int(input("Enter a:"))
# b=int(input("Enter b:"))
# c=int(input("Enter c:"))
#
# if a>b:
#     print("a is greated")
# elif b>c:
#     print("b is greatest")
# else:
#     print("c is greatest")



# Print week no if we provide weekname as input
# a=input("Enter weekname:")
#
# if a=="sunday":
#     print("1")
# elif a=="monday":
#     print("2")
# elif a=="tuesday":
#     print("3")
# elif a=="wednesday":
#     print("4")
# elif a=="thursday":
#     print("5")
# elif a=="friday":
#     print("6")
# elif a=="saturday":
#     print("7")
# else:
#     print("No weekname")


#For Example: You have written an exam for a total score of 100 and if your score is above or equal to 60 then you will be considered as PASS in the exam.

marks=int(input("Enter Your Marks:"))

if marks>= 60:
    print("You are pass!!")
else:
    print("You are failed!!")
