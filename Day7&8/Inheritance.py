# ex 1: Single Inheritance: single parent single child
# class A:
#     def m1(self):
#         print("this is m1 method from class A...")
#
# class B(A):             #B is child class of class A
#     def m2(self):
#         print("this is m2 method from class B...")
#
# b_obj=B()
# b_obj.m1()      # this is m1 method from class A...
# b_obj.m2()      # this is m2 method from class B...


# ex 2: Single Inheritance:

# class A:
#     x,y=10,20       #class variables
#     def m1(self):   # method
#         print(self.x+self.y)
#
# class B(A):
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
#
# b_obj=B()
# b_obj.m1()  #30
# b_obj.m2()  #100


# Ex 3: Multilevel Inheritance: parent>>child1>>child2>>child3
# class A:
#     a,b=200,100
#     def m1(self):
#         print(self.a+self.b)
# class B(A):       # B is child of class A
#     x,y=50,20
#     def m2(self):
#         print(self.x-self.y)
# class C(B):       # C is child of class B
#     p,q=15,5
#     def m3(self):
#         print(self.p*self.q)
#
# c_obj=C()
# c_obj.m1()  #300
# c_obj.m2()  #30
# c_obj.m3()  #75


# Ex 4: Hierarchy Inheritance: Single parent multiple childs.
# class A:
#     a,b=10,20
#     def m1(self):
#         print(self.a+self.b)
# class B(A):       # B is child of A class
#     x,y=20,30
#     def m2(self):
#         print(self.x-self.y)
# class C(A):       # C is child of A class
#     p,q=10,15
#     def m3(self):
#         print(self.p*self.q)
#
# b_obj=B()
# b_obj.m1()  #30
# b_obj.m2()  #-10
#
# c_obj=C()
# c_obj.m1()  #30
# c_obj.m3()  #150


# Ex 5: Multiple inheritance: Multiple parent single child:
# class A:
#     a,b=200,100
#     def m1(self):
#         print(self.a+self.b)
# class B:
#     x,y=20,10
#     def m2(self):
#         print(self.x-self.y)
#
# class C(A,B):       # C is child of class A and B
#     p,q=5,12
#     def m3(self):
#         print(self.p*self.q)
#
# c_obj=C()
# c_obj.m1()      # 300
# c_obj.m2()      # 10
# c_obj.m3()      # 60


# Ex 6: Overriding methods
# class A:
#     def m1(self):
#         print("This is m1 method from class A...")
# class B(A):
#     def m1(self):
#         print("This is m1 method from class B...")
#         super().m1()    # to invoke m1 method from class A(parent)
#
# b_obj=B()
# b_obj.m1()  #This is m1 method from class B...
# #After super().m1()     #This is m1 method from class A...



# Ex 7:
# class A:
#     a,b=10,20
#
# class B(A):
#     i,j=100,200     #Class variables
#     def m(self,x,y):        #local variable
#         print(x+y)
#         print(self.i+self.j)    #calling class variable by self.
#         print(self.a+self.b)    #calling class variables from class A
#
# b_obj=B()
# b_obj.m(1000,2000)
#
# # Output:
# # 3000
# # 300
# # 30


# Ex 8: Overriding variables.
# class Parent:
#     name="Scott"
#
# class Child(Parent):
#     name="John"     #overriding the variable name
#
# c_obj=Child()
# print(c_obj.name)       #John


# Ex 9: Overriding methods.
# class Bank:
#     def rateofinterest(self):
#         return 0
#
# class Xbank(Bank):
#     def rateofinterest(self):
#         return 10
#
# class Ybank(Bank):
#     def rateofinterest(self):
#         return 12
#
# xobj=Xbank()
# print(xobj.rateofinterest())     #10
#
# yobj=Ybank()
# print(yobj.rateofinterest())     #12


# Ex 10: Overloading(Polymorphism)
# class Human:
#     def sayhello(self,name=None):
#         if name is not None:
#             print("Hello"+ name)
#         else:
#             print("Hello Only")
#
# h=Human()
# h.sayhello("scott")     #Helloscott
# h.sayhello()            #Hello Only


# Ex 11: Overloading(Polymorphism)
class Calculation():
    def add(self,a=0,b=0,c=0):
        print(a+b+c)
calobj=Calculation()
calobj.add()                     # 0
calobj.add(10,20)               # 30
calobj.add(100,200,300)         # 600
