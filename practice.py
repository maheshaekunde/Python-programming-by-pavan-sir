# 1) A = 10, 20, 30 In the above assignment operation, what is the data type of ‘A’ that Python appreciates as?
# A= 10,20,30
# print(type(A))      #<class 'tuple'>

# Tuple:A tuple is collection which is ordered and unchangable.
# tuple::: ()
# tuple is immutable.(Change, Append, Insert, remove is not possible)

# 2)
# A = 1,2,3,4
# a,b,c,d = A
# # In the above assignment operations, what is the value assigned to the variable ‘d’?
# print(d)        #4
# This type of assignment is called ‘Tuple Unpacking’.

#3) Swap these two Variables without using the third temporary variable?
# a = 10
# b = 20
# a,b=b,a
# print(a,b)      #20 10  This kind of assignment is called a parallel assignment.

#4)What is the output? print b
# a = 10
# b = a
# a = 20
#
# print(b)    #10

#6) How do you find the type and identification number of an object in Python?
# a="python"
# print(type(a))      #<class 'str'>
# print(id(a))        #2033191440368

# 7) What is the Value of c?
# a = 0101
# b = 2
# c = a+b
# print(c)
#
# In Python2, any number with leading 0 is interpreted as an octal number. So, variable a points to 65(Equalent in Decimal) then the variable c will be pointing to the value 67 i.e 65+2. In Python3, a=0101 (Doesn’t support syntax)



# 11) How do you check whether the two variables are pointing to the same object in Python?
# In Python, we have an operation called ‘is’ operator, which returns true if the two variables are pointing to the same object.
# a="python"
# b=a
#
# print(a is b)   #True
# print(type(a))  #<class 'str'>
# print(id(a))    #2087144542192
# print(id(b))    #2087144542192


# 12) What is for-else and while-else in Python?
# Python provides an interesting way of handling loops by providing a function to write else block in case the loop is not satisfying the condition.
#
# a = [10,20,30]
#
# for i in a:
#     print("in for loop")
# else:
#     print("in else block")

# while True:
#     print("in while loop")
# else:
#     print("in else block")
# print()

# 13) How do you programmatically know the version of Python you are using?
# import sys
# print(sys.version)  #3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)]


# 15) How do you dispose a variable in Python?
# x="mahesh"
#
# del x
# print(x)

# 16) What is the difference between range() and xrange() functions in Python?
# range() and xrange() are two functions that could be used to iterate a certain number of times in for loops in Python.
# In Python 3, there is no xrange , but the range function behaves like xrange in Python 2.
# If you want to write code that will run on both Python 2 and Python 3, you should use range().

# for i in range(1,1001):
#     print(i)


# 17) What are the ideal naming conventions in Python?
'''
All variables and functions follow lowercase and underscore naming convention.
Examples: is_prime(), test_var = 10 etc
Constants are all either uppercase or camel case.
Example: MAX_VAL = 50, PI = 3.14
None, True, False are predefined constants follow camel case, etc.
Class names are also treated as constants and follow camel case.
Example: UserNames
'''


# 18) What happens in the background when you run a Python file?
'''
When we run a .py file, it undergoes two phases. In the first phase it checks the syntax
in the second phase it compiles to bytecode (.pyc file is generated) using Python virtual machine, loads the bytecode into memory and runs.'''


# 19) What is a module in Python?
# A module is a .py file in Python in which variables, functions, and classes can be defined. It can also have a runnable code.

# 20) How do you include a module in your Python file?
'''The keyword “import” is used to import a module into the current file.
Example: import sys #here sys is a predefined Python module'''

# 21) How do you reload a Python module?
# There is a function called reload() in Python, which takes module name as an argument and reloads the module.

# 22) What is List in Python?
'''The List is one of the built-in data structures in Python. 
Lists are used to store an ordered collection of items, which can be of different type.
List is mutable
Elements in a list are separated by a comma and enclosed in square brackets. 
Examples of List are: 
A = [1,2,3,4] 
B = [‘a’,’b’,’c’] 
C = [1,’a’,’2’,’b’] 
List in Python is sequence type as it stores ordered collection of objects/items. 
In Python String and tuple are also sequence types.'''

# 23) When do you choose a list over a tuple?
'''When there is an immutable, ordered list of elements, we choose tuple. 
Because we cannot add/remove an element from the tuple. 
On the other hand, we can add elements to a list using append() or extend() or insert(), etc., 
and delete elements from a list using remove() or pop(). Simple tuples are immutable, and lists are not. 
Based on these properties one can decide what to choose in their programming context.'''

# 24) How do you get the last value in a list or a tuple?
# a = [1,2,3,4] #List
# print(a[-1])
#
# b=(1,2,3,4) #tuple
# print(b[-1])

# 25) What is Index Out Of Range Error?
'''
When the value passed to the index operator is greater than the actual size of the tuple or list,
Index Out of Range error is thrown by Python.'''

# lst=[2,3,4,5]   #index start from 0
# print(lst[4])   #IndexError: list index out of range

# tpl=(4,5,6,7)
# print(tpl[5])   #IndexError: tuple index out of range

# 26) What is slice notation in Python to access elements in an iterator?
'''In Python, to access more than one element from a list or a tuple we can use ‘:’ operator. 
Here is the syntax. Say ‘a’ is list 
a[startindex:EndIndex:Step]'''

# lst=[11,12,13,14,15,16,17,18,19,20]      # print no 15 to 18
# print(lst[4:8])     #[15, 16, 17, 18]

# lst=[11,12,13,14,15,16,17,18,19,20]     #print no 13, 15, 17....
# print(lst[2::2])        #[13, 15, 17, 19]

# lst=[11,12,13,14,15,16,17,18,19,20]     #reverse list
# print(lst[::-1])        #[20, 19, 18, 17, 16, 15, 14, 13, 12, 11]

# tpl=(11,12,13,14,15,16,17,18,19,20)         # 13 to 20
# print(tpl[2:])          #(13, 14, 15, 16, 17, 18, 19, 20)
# #reverse
# print(tpl[::-1])        #(20, 19, 18, 17, 16, 15, 14, 13, 12, 11)

# 27) How do you convert a list of integers to a comma separated string?
# a = [1,2,3,4,5,6,7,8]
#
# number=','.join(str(i) for i in a)
# print(number)
# print(type(number)) #<class 'str'>

#  How do you convert a tuple of integers to a dot separated string?
# a = (1,2,3,4,5,6,7,8)
# num='.'.join(str(i) for i in a)
# print(num)      #1.2.3.4.5.6.7.8

# 28) What is the difference between Python append () and extend () functions?
'''The extend() function takes an iterable (list or tuple or set) and adds 'each element' of the iterable to the list. 
Whereas append() takes a value and adds to the list as a 'single' object.'''

# a=[1,2,3,4]   #list
# b=[5,6,7,8]
# # a.append(b)
# # print(a)        #[1, 2, 3, 4, [5, 6, 7, 8]]  , [5,6,7,8] considered as single object.
#
# a.extend(b)
# print(a)        #[1, 2, 3, 4, 5, 6, 7, 8]  adding single single element.


# 29) Tell me about a few string operations in Python?
'''
name = "John" # a string 
mychar = 'S' # a character
name1 = str() # this will create empty string object 
name2 = str("newstring") # string object containing 'newstring'''

#========Strings are mutable=========================
# str1="wel"
# str2="come"
# str3=str1+str2
# print(str3)     #welcome

#========== + and * with string========================
# str1="wel"
# str2="come"
# str3=str1+str2
# print(str3)     #welcome

# str4="welcome"*3
# print(str4)     #welcomewelcomewelcome

#============Slicing==============
# str="welcome"
# print(str[1:3]) #el
# print(str[1:-3])    #elc
# print(str[::-1])    #emoclew(reverse)

#=============String Functions in Python==========
# print(len("mahesh"))    #6
# print(max("mahesh"))    #s
# print(min("mahesh"))    #a

#==================='in' and 'not in' operators=====
# a="welcome"
# print("come" in a)  #True
# print("hello" in a) #False
# print("hello" not in a) #True
# print("come" not in a)  #False

#==============Strings comparison================
# a=50
# b=100
#
# print(a==b) #False
# print(a>b)  #False
# print(a<b)  #True
# print(a>=b) #False
# print(a<=b) #True
# print(a!=b) #True
# print("abc">"") #True

#===============Testing strings====================
# s = "welcome to python"
#
# print(s.isnumeric())    #False
# print(s.isspace())  #False
# print(s.isupper())  #False
# print(s.islower())  #True
# print(s.isidentifier()) #False


#===========Searching for Substrings==================
# s = "welcome to python"
# print(s.endswith("n"))  #True
# print(s.startswith("t"))    #False
# print(s.find("come"))   #3
# print(s.find("hi")) #-1 if fail returns -1
# print(s.count("o")) #3

#===============Converting Strings================
# s = "String in PYTHON"
# print(s.upper())    #STRING IN PYTHON
# print(s.lower())    #string in python
# print(s.capitalize())   #String in python
# print(s.title())    #String In Python
# print(s.swapcase())     #sTRING IN python
# print(s.replace("in","on")) #Strong on PYTHON

# 30) How do you create a list which is a reverse version on another list in Python?
#Python provides a function called reversed(), which will return a reversed iterator.
# Then, one can use a list constructor over it to get a list.
# a=[10,20,30,40,50]
# b=a.reverse()
# print(a)    #[50, 40, 30, 20, 10]

# 31) What is a dictionary in Python?
'''In Python, dictionaries are kind of hash or maps in another language. Dictionary consists of a key and a value. 
Keys are unique, and values are accessed using keys. Here are a few examples of creating and accessing dictionaries.'''
# a={"name":"john","job":"QA","company":"TCS","salary":"60000"}
# print(type(a))  #<class 'dict'>
# print(a["name"])    #john
# print(a["job"])     #QA
#
# ## adding key and value
# a["city"]="pune"
# print(a)    #{'name': 'john', 'job': 'QA', 'company': 'TCS', 'salary': '60000', 'city': 'pune'}
# a["phone"]="98698987686"
# print(a)    #{'name': 'john', 'job': 'QA', 'company': 'TCS', 'salary': '60000', 'city': 'pune', 'phone': '98698987686'}
#
# ###Modify elements into the dictionary
# a["phone"]="1234566788"
# print(a)    #{'name': 'john', 'job': 'QA', 'company': 'TCS', 'salary': '60000', 'city': 'pune', 'phone': '1234566788'}
#
# a["name"]="scott"
# print(a)    #{'name': 'scott', 'job': 'QA', 'company': 'TCS', 'salary': '60000', 'city': 'pune', 'phone': '1234566788'}

###Delete element from the dictionary
# del a['phone']
# print(a)


# 32) How do you merge one dictionary with the other?
''' we can use update() to merge one dictionary to another dictionary'''
# a={'fistname':'john'}
# b={'lastname':'cena'}
# a.update(b)
# print(a)    #{'fistname': 'john', 'lastname': 'cena'}

# x={'city':'pune'}
# y={'state':'Mh'}
# x.update(y)
# print(x)    #{'city': 'pune', 'state': 'Mh'}

# 33) How to walk through a list in a sorted order without sorting the actual list?
# in python we have sort() which sort the list, without sorting or changing actual list.
# a=[500,400,100,600,200,300]
# print(a)     #[500, 400, 100, 600, 200, 300]  without sort
# a.sort()
# print(a)    #[100, 200, 300, 400, 500, 600] with sort


# 34) names = [‘john’, ‘fan’, ‘sam’, ‘megha’, ‘popoye’, ’tom’, ‘jane’, ‘james’,’tony’]
# Write one line of code to get a list of names that start with character ‘j’?
# names = ['john','fan', 'sam', 'megha', 'popoye', 'tom', 'jane', 'james','tony']
#
# jname=[i for i in names if i[0]=="j"]
# print(jname)    #['john', 'jane', 'james']
# '''
# for i in names:
#     if i[0]=="j":
#         print(i)'''


# 35) What is a set?
# set it unordered collection of unique objects, {}

# set={10,20,30,40,50}
# print(set)      #{50, 20, 40, 10, 30} unordered

# set={10,20,30,30,40,40}
# print(set)  #{40, 10, 20, 30}  reflect only unique values


# 36) a = “this is a sample string with many characters”
# Write a Python code to find how many different characters are present in this string?
# a="this is a sample string with many characters"
# print(len(a))       #44 all charecter
# print(len(set(a)))  #16 unique charecter

# 37) Name some standard Python errors you know?
'''
TypeError: Occurs when the expected type doesn’t match with the given type of a variable. 
ValueError: When an expected value is not given- if you are expecting 4 elements in a list and you gave 2. 
NameError: When trying to access a variable or a function that is not defined. 
IOError: When trying to access a file that does not exist. 
IndexError: Accessing an invalid index of a sequence will throw an IndexError. 
KeyError: When an invalid key is used to access a value in the dictionary.'''

# 38) How Python supports encapsulation with respect to functions?
'''
Python supports inner functions. 
A function defined inside a function is called an inner function, whose behavior is not hidden. 
This is how Python supports encapsulation with respect to functions.
'''

# 39) What are the built-in type does python provides?
'''
There are mutable and Immutable types of Pythons built in types. 
Mutable(Changable) built-in types:
List 
Sets 
Dictionaries 
Immutable(Non-changable) built-in types:
Strings 
Tuples
Numbers
'''


# 40) What is module and package in Python?
'''In Python, module is the way to structure program. 
Each Python program file is a module, which imports other modules like objects and attributes.
The folder of Python program is a package of modules. A package can have modules or subfolders
'''

# 41) Explain how can you generate random numbers in Python?
# import random
# print(random.random())


# 43) How to connect to the Microsoft Excel and read write data in to excel using python script?
# import openpyxl
#
# path="D:\OpenCart_Test_cases.xlsx"
#
# workbook=openpyxl.load_workbook(path)
#
# sheet=workbook["Register"]
#
# row=sheet.max_row
# column=sheet.max_column
#
# print(row)  #15
# print(column) #12
#
# for r in range(1,row+1):
#     for c in range(1,column+1):
#         print(sheet.cell(row=r,column=c).value)
#     print()

# 44) What is the difference between list and tuples?
'''
list- list is mutable,list is slower than tuple,[]
tuple-tuple is immutable, is faster than list,()'''

# 45). Explain Inheritance in Python with an example.
'''Inheritance allows one class to gain all members(attribute and methods) from other class.
Inheritance provide code reusability, make it easier to create and maintain the application.
the class from which we are inheriting is called super class. or parent class.
the class which inherited is called as derived class or child class.
1. Single Inheritance:- where derived class(child class) occured from the member of super class(parent class).
2. Multi-level Inheritance:- the chain of the class
3. Hierarchical Inheritance:- from one super class or parent class we can inherit multiple derived or child class.
4. Multiple Inheritance:- a derived class or child class is inherited from the multiple parent class or super class.
'''

# 46). How can you randomize the items of a list in place in Python?
# from random import shuffle
# x=["mango","apple","pineapple","kiwi","cherry"]
# shuffle(x)
# print(x)    #['pineapple', 'kiwi', 'mango', 'apple', 'cherry']

# 47). Write a sorting algorithm for a numerical dataset in Python.
# list = ["1", "4", "0", "6", "9"]
# a=[int(i) for i in list]
# a.sort()
# print(a)


# 48) How to print current date & time?
# # TO IMPORT DATE AND TIME,  time module is available.
import time
# print(time.asctime())   #Wed Jul 26 22:36:29 2023
