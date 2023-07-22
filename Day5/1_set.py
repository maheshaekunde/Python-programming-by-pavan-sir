# Set(): sA Set in Python programming is an unordered collection data type that is iterable, mutable and has no duplicate elements. In python sers are written in curly brackets{}
# set is mutable(changeable)


# ex 1: creating set
# myset1={"apple","banana","cherry"}
# print(myset1)        #{'banana', 'apple', 'cherry'}  is unordered

# ex 2: accessing items from set.
# mylist={"apple","banana","cherry"}
# for i in mylist:
#     print(i)

# banana
# apple
# cherry

# ex 3: value exists in set or not.
# myset={"apple","banana","cherry"}
# print("banana" in myset)        #True

# ex 4: adding items in set.        add()(for single item) and update()(for multiple items) function.
# myset={"apple","banana","cherry"}
# # myset.add("orange")
# print(myset)        #{'banana', 'apple', 'cherry', 'orange'}
#
# myset.update(["chiku","pineapple","greps"])
# print(myset)    #{'chiku', 'apple', 'banana', 'greps', 'pineapple', 'cherry'}


# ex 5: find number of items in set:
# myset={"apple","banana","cherry"}
# print(len(myset))       #3


# ex 6: Remove items from set.   remove() and discard()

# myset={"apple","banana","cherry","chiku","pineapple","greps"}
# myset.remove("banana")
# print(myset)
#
# myset.discard("cherry")
# print(myset)

# difference between remove and discard is if we try to delete the item which is not available, remove will through error
# but discard will not through any error.


# ex 7: Clear all the items from set.
# myset={"apple","banana","cherry","chiku","pineapple","greps"}
# # myset.clear()
# print(myset)        #set()
#
# # delete variable also
# del myset
# print(myset)

# Ex 8: Joining 2 sets-  union()
set1={"a","b","c"}
set2={1,2,3}
# set3=set1.union(set2)
# print(set3)     #{1, 2, 3, 'a', 'c', 'b'}

# update():
set1.update(set2)
print(set1)     #{1, 'b', 2, 3, 'c', 'a'}

