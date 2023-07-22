## approach 1:
# import f_class
# import g_class1
#
# object1=f_class.Animal()     #creating object.
# object1.display()       #I like cow..
#
# object2=g_class1.Bird()
# object2.display()       #I like parrot..


## approach2:
from f_class import Animal
from g_class1 import Bird

obj1=Animal()       #creating object
obj1.display()      #I like cow..

obj2=Bird()         #creating object
obj2.display()      #I like parrot..