# Tuple:A tuple is collection which is ordered and unchangable.
# tuple::: ()
# tuple is immutable.(Change, Append, Insert, remove is not possible)

# ex 1: create tuple:
# mylist1 = ("apple", "banana", "cherry")
# print(mylist1)

# ex 2: Access tuple items:
# mylist1 = ("apple", "banana", "cherry")
# print(mylist1[1])       #banana
# print(mylist1[-1])      #cherry

# ex 3: rang of indexs:
# mylist1 = ("apple", "banana", "cherry","orange","kiwi","mango","melon")
# print(mylist1[2:5])     #('cherry', 'orange', 'kiwi')
# print(mylist1[-4:-1])       #('orange', 'kiwi', 'mango')

# ex 4: Change the tuple values: It is not possible due it is immutable
# mylist1 = ("apple", "banana", "cherry","orange","kiwi","mango","melon")

# to change, Tuple>> List>> Tuple
# mytuple = ("apple", "banana", "cherry","orange","kiwi","mango","melon")
# mylist=list(mytuple)
# print(mylist)       #['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango', 'melon']
#
# mylist.append("Watermelon")
# print(mylist)       #['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango', 'melon', 'Watermelon']
#
# mytuple1=tuple(mylist)
# print(mytuple1)     #('apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango', 'melon', 'Watermelon')

# ex 5: reading tuple using loop:
# mytuple = ("apple", "banana", "cherry","orange","kiwi","mango","melon")
# for i in mytuple:
#     print(i)


# ex 6: Check item in tuple:
# mytuple = ("apple", "banana", "cherry","orange","kiwi","mango","melon")
#
# if "banana" in mytuple:
#     print("Yes")
# else:
#     print("NO")

# ex 7: tuple length:
# mytuple = ("apple", "banana", "cherry","orange","kiwi","mango","melon")
# print(len(mytuple))  # 7

# ex 8: Add items (Not possible)

# ex 9: Copy tuple
# mytuple = ("apple", "banana", "cherry","orange","kiwi","mango","melon")
# mytuple1=mytuple
# print(mytuple1)     #('apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango', 'melon')


# ex 10: Removing/Delete items from tuple is Not possible.

# ex 11: Joining of tuple:
# mytuple = ("apple", "banana", "cherry")
# mytuple1= ("orange","kiwi","mango")
# print(mytuple + mytuple1)       #('apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango')
