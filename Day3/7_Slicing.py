# SLicing oparator:
# strating index is 0
# ending index is from back and is 1

# exp1:
# str="welcome"
# print(str[1:3])     #el
# print(str[:6])      #welcom
# print(str[2:])      #lcome
# print(str[1:-1])       #elcom   last 1 char removed
# print(str[1:-2])        #elco       last 2 char removed

# EX 2:  max(), min(), len() functions of the string
# print(max("welcome"))   #w
# print(min("welcome"))   #c
# print(len("welcome"))   #7


# EX 3: in, not in operators:(it will return True or False)
# s="welcome"
# print("come" in s)      #True
#
# print("hi" in s)        #False
#
# print("hi" not in s)        #True

# EX 4: string comparision:
# print("tim"=="tie")   # false
# print("free" != "freedom")     #True
# print("arrow" > "aron")     #True compaire no. of alphabate
# print("right" >= "left")   #True
# print("teeth" < "tee")     # False
# print("yellow" <= "fellow")     # False
# print("abc" > " ")      #True


# # EX 5: Testing string  True/False
# s= "welcome to python"
# print(s.isalnum())  #False
#
# a="123"
# print(a.isalnum())      #True

# print("welcome".isalpha())  #True

# print("2012".isdigit()) #True

# print(s.islower())      #True

# print("WELCOME".isupper())  #True

# print("  ".isspace())       #True


# EX 6: Searching for substrings:
# s= "welcome to python"
# print(s.endswith("thon"))       #True
# print(s.startswith("welcome"))      #True
# print(s.startswith("good"))     #False
#
# print(s.find("come"))   # 3 Show the position of value
#
# print(s.find("god"))    # -1  (-1 show not found)
#
# print(s.count("t"))  #2 return the number of occurances of substring in string



# EX 7: Converting string
# s = "string in PYTHON"
#
# # capitalize starting substring
# print(s.capitalize())       #String in python
#
# # capitalize starting of all strings
# print(s.title())    #String In Python
#
# # Lowercase the all strings
# print(s.lower())    #string in python
#
# # Uppercase all the strings
# print(s.upper())        #STRING IN PYTHON
#
# # Upper to lower and lower to upper:
# print(s.swapcase())     #STRING IN python
#
# # Replace the string to old string:
# print(s.replace("in","on"))     #strong on PYTHON


# EX 8: Reverse a string
# method1:
s="welcome"
# rev_s=""
#
# for i in s:
#     rev_s=i+rev_s
# print(rev_s)


# method 2:
rev_str=s[::-1]
print(rev_str)      #emoclew