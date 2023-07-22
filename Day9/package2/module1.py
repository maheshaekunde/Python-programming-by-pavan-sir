# class Employee:
#     def dispemp(self):
#         print("this is employee from module 1..")


#################### or ##########################
class Employee:     #class
    def __init__(self,eid,ename,sal):     #creating constructor.(local variables)
        self.eid=eid        ##assigning local variables as class variables.
        self.ename=ename
        self.sal=sal

    def display(self):      #method
        print(self.eid,self.ename,self.sal)

