# list: it is collection which is ordered(in sequence) and changable(mutable).
# in python list are written with square bracket [ ]
# List is mutable.

# mylist1=[10,20,30,40]
# mylist2=["apple","banana","cherry"]
# mylist3=list()      #empty list
#
# # ex1: Accessing items from list
# print(mylist2[0])       #apple
# print(mylist2[2])       #cherry
# print(mylist2[-1])      #cherry:  count from the end

# ex 2: Range of indexes
# mylist=["apple","banana","cherry","orange","kiwi","mango","melon"]
# print(mylist[2:5])      #['cherry', 'orange', 'kiwi']
# print(mylist[-4:-1])       #['orange', 'kiwi', 'mango']


# ex 3: replace the items value
# mylist=["apple","banana","cherry"]
# mylist[0]="orange"
# print(mylist)       #['orange', 'banana', 'cherry']

# ex 4: read the list by using loop:
# mylist=["apple","banana","cherry"]
#
# for i in mylist:
#     print(i)

# Ex 5: Check if the item is exist in the list or not:
# mylist=["apple","banana","cherry"]
#
# if "apple" in mylist:
#     print("apple is available")
# else:
#     print("apple is not avaiable")

# ex 6: List length
# mylist=["apple","banana","cherry","orange","kiwi","mango","melon"]
# print(len(mylist))      #7

# ex 7: Add items in list:  By 'append()' and 'insert()'
# mylist=["apple","banana","cherry"]
# # mylist.append("orange")  # append class adds item at end of the list
# # print(mylist)       #['apple', 'banana', 'cherry', 'orange']
#
# mylist.insert(2,"orange") # to insert at specific place
# print(mylist)       #['apple', 'banana', 'orange', 'cherry']

# ex 8: Remove item from list: pop(), del(keyword), clear()
mylist=["apple","banana","cherry","orange","kiwi","mango","melon"]

# mylist.pop(3) # item will be remove according to index
# print(mylist)       #['apple', 'banana', 'cherry', 'kiwi', 'mango', 'melon'

# del mylist[2]
# print(mylist)       #['apple', 'banana', 'orange', 'kiwi', 'mango', 'melon']


# mylist.clear()
# print(mylist)       #[], delete all item, but do not delete variable

# ex 9: Copy list:
# mylist=["apple","banana","cherry","orange","kiwi","mango","melon"]
# mylist1=list(mylist)
# print(mylist1)      #['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango', 'melon']

# ex 10:
# mylist=["apple","banana","cherry","orange","kiwi","mango","melon"]
# mylist1=mylist.copy()
# print(mylist1)   #['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango', 'melon']

# ex 11: Joing of list
mylist1 = ["apple", "banana", "cherry"]
mylist2 = ["orange","kiwi","mango","melon"]

# Using + operator.
# print(mylist1+mylist2)      #['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango', 'melon']

# by using loop statement:
# for i in mylist2:
#     mylist1.append(i)
# print(mylist1)      #['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango', 'melon']

# By using extend() function:
# mylist1.extend(mylist2)
# print(mylist1)      #['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango', 'melon']
