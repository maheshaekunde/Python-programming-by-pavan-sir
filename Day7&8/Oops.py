# ex 1: Instance method(we can call only through object)
# class Myclass:
#     def myfun(self):        #FUNCTION inside class is known as method.
#         pass
#     def display(self):
#         print("john")
#     def argument(self,name):
#         print(name)
#
# mc=Myclass()           #Object
#
# # calling methods:
# mc.myfun()
# mc.display()        #john
#
# # calling methods with argument.
# mc.argument("scott")        #scott


# Ex 2:
# class Myclass:
#     def method1(self):
#         print('This is instance method')
#
#     @staticmethod   # annotation(comman for every object)
#     def method2(self,num):
#         print(self,num)
#
# # Instance methode we can call through object only.
# # Static methode we can call through class itself and also by object by giving self and other arguments.
# #menas 'self' is also act as parameter.
#
# # instance method
# mc=Myclass()        #object
# mc.method1()
#
# # Static method
# mc.method2(100,200)     #100 200
#
# Myclass.method2(10,20)      #10 20


# Ex 3:
# Class Variables:
# class Myclass:
#     a,b=10,20       # class variables: these are created inside the class.
#     def add(self):
#         print(self.a+self.b)  # to access class variable, we have to use self.
#     def multi(self):
#         print(self.a*self.b)
#
# mc=Myclass()
# mc.add()        #30
# mc.multi()      #200


# Ex 4: global,class,local variable.
# i,j=15,25                   # i, j are Global variable.
#
# class Myclass:
#     a,b=10,20               # a, b are Class variables.
#     def addi(self,x,y):     # Method
#         print(x+y)          # x,y are Local variables.
#         print(self.a + self.b)    # to access class variables in method we have to use self.variable
#         print(i+j)  # global variables can access directly.
#
#
# mc=Myclass()
#
# mc.addi(100,200)    #300
# # 30 class variables
# # 40 global variables

# Ex 5: global,class,local variable with same variables.
# a,b=15,25                   # i, j are Global variable.
#
# class Myclass:
#     a,b=10,20               # a, b are Class variables.
#     def addi(self,a,b):     # Method
#         print(a+b)          # x,y are Local variables.
#         print(self.a + self.b)    # to access class variables in method we have to use self.variable
#         # print(a+b)  # We can not use global variables directly.
#         print(globals()['a']+globals()['b']) #access global variable
#
# mc=Myclass()
# mc.addi(100,200)    #300


# Ex 6: one class can have multiple objects
# class Myclass:
#     def display(self,name):
#         print('this is display method...')
#         print(name)
#
# object1=Myclass()
# object1.display("john")
#
# object2=Myclass()
# object2.display("scott")

# Ex 7:Constructor example:
# class Myclass():
#     def __init__(self):     # constructor.
#         print("this is constructor...")
#     def Method(self):       # Method
#         print("this is method....")
#
#     def method2(self,x,y):
#         return (x+y)
#
# object1=Myclass()       #his is constructor...(Invoke costructor automatically, No need call method# )
#
# object1.Method()     #this is method...(method we can call explicitely by using object.)
#
# print(object1.method2(10,20))   #30


# Ex 8:
# class Myclass:
#     name="john"     #class variable.
#     def __init__(self,name):
#         print(name)         # accessing local variable
#         print(self.name)    # accessing class variable
#
# object=Myclass("david")     #passing parameter in constructor.
# print(object)
# # david     (local variable)
# # john      (class variable)


# Ex 9: create employee class(Emp) inside create constructor which accept 3 parameter(Id, name, salary)
# and create methode(display()) which print id, name, salary

# class Emp():
#     def __init__(self,id,name,salary):
#         self.id=id      #creating class variable inside method(constructor)
#         self.name=name   #creating class variable inside method(constructor)
#         self.salary=salary   #creating class variable inside method(constructor)
#     def display(self):
#         print(self.id,self.name,self.salary)
#
# object=Emp(101,"john",50000)
# object.display()        #101 john 50000
#
# object2=Emp(102,"scott",60000)
# object2.display()       #102 scott 60000


# Ex 10: As constructor does not print, we need method to print(ex 9)
# to avoid method, we con also use constructor to print(__str__) but it only accept strint datatype value.
#create employee class(Emp) inside create constructor which accept 3 parameter(Id, name, salary)
# and create methode(display()) which print id, name, salary

class Emp():    #class
    def __init__(self,id,name,salary):      #constructor.
        self.id=id                          # creating class variable inside constructor by self argument
        self.name=name
        self.salary=salary
    def __str__(self):              # creating constructor to print string(return)
        return(self.name)

obj=Emp(101,"john",50000)
print(obj)      #john