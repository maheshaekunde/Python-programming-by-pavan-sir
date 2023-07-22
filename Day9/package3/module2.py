# class Student:
#     def dispstu(self):
#         print("this is student from module2..")



######### or ############
class Student:      #creating class
    def __init__(self,sid,sname,grad):      # creating constructor and local variables.
        self.sid=sid        # converting local variables into class variables.
        self.sname=sname
        self.grad=grad
    def display(self):
        print(self.sid,self.sname,self.grad)


