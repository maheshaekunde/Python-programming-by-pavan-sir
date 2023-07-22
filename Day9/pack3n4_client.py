# from package2 import module1
# from package3 import module2
#
# obj1=module1.Employee()     #creating object
# obj1.dispemp()              #calling method      #this is employee from module 1..
#
#
# obj2=module2.Student()     #creating object
# obj2.dispstu()             #calling method     #this is student from module2..


##################### or ##############################
from package2 import module1
from package3 import module2

obj1=module1.Employee(101,"john",50000)
obj1.display()  #101 john 50000     #method

obj2=module2.Student(201,"scott",60000)
obj2.display()  #201 scott 60000        #method

