# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is unordered, changeable and do not allow duplicates.
#As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# product(key) : 100 (value)

# value can be duplicate but key can not duplicate.

# ex 1:
# mydic={101:"x",102:"y",103:"z"}
# print(mydic)        #{101: 'x', 102: 'y', 103: 'z'}

# ex 2:
# mydic={
#     "brand":"hyndai",
#     "model":"i10",
#     "year":2010
# }
#
# print(mydic["brand"])       #hyndai
# print(mydic["model"])       #i10
#
# # using get()
# print(mydic.get("brand"))       #hyndai

# Ex 3: change values in dictionary.
# mydic={
#     "brand":"hyndai",
#     "model":"i10",
#     "year":2010
# }
# mydic["year"]=2022
# print(mydic)        #{'brand': 'hyndai', 'model': 'i10', 'year': 2022}


# Ex 4: reading items from dictionary using loop.
# mydic={
#     "brand":"hyndai",
#     "model":"i10",
#     "year":2010
# }

# for i in mydic:
#     print(i)        #print only keys
#
# for i in mydic:
#     print(mydic[i])     # print only values.
#
# for i in mydic.values():
#     print(i)         # print only values.

# for x,y in mydic.items():
#     print(x,y)          #print key and value.


# ex 5: check key is exist in dictionary or not.
# mydic={
#     "brand":"hyndai",
#     "model":"i10",
#     "year":2010
# }
#
# if "model" in mydic:
#     print("exist")
# else:
#     print("Not exist")
#
# print("brand" in mydic)     #True


# ex 6: Find number of items in dictionary.
# mydic={
#     "brand":"hyndai",
#     "model":"i10",
#     "year":2010
# }
# print(len(mydic))           #3


# ex 7: Adding to dictionary.
# mydic={
#     "brand":"hyndai",
#     "model":"i10",
#     "year":2010
# }
#
# mydic["color"]="red"
# print(mydic)            #{'brand': 'hyndai', 'model': 'i10', 'year': 2010, 'color': 'red'}


# ex 8: Remove items from dictionary.-- pop()
# mydic={
#     "brand":"hyndai",
#     "model":"i10",
#     "year":2010
# }
# mydic.pop("year")
# print(mydic)        #{'brand': 'hyndai', 'model': 'i10'}
#
# del mydic["model"]
# print(mydic)        #{'brand': 'hyndai'}


# ex 9: deleting complete dictionary.
# mydic={
#     "brand":"hyndai",
#     "model":"i10",
#     "year":2010
# }
# del mydic
# print(mydic)


# ex 10:removing items not dictionary.
# mydic={
#     "brand":"hyndai",
#     "model":"i10",
#     "year":2010
# }
#
# mydic.clear()
# print(mydic)            #{}


# ex 11: copying dictionary.
# mydic={
#     "brand":"hyndai",
#     "model":"i10",
#     "year":2010
# }

# mydic1=mydic
# print(mydic1)       #{'brand': 'hyndai', 'model': 'i10', 'year': 2010}

# mydic1=mydic.copy()
# print(mydic1)       #{'brand': 'hyndai', 'model': 'i10', 'year': 2010}
