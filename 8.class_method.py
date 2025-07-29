# Feature 1: by using cls we can access or modify class variable
class Calculator:
    a= 3  # class variable
    b=2
    c=0

    @classmethod
    def add(cls):
        return cls.a+cls.b
    
# x=Calculator()
# print(x.add())
# print(Calculator.c)


# Feature 2:  Create alternative cocnstructor:

class Calculator:
       #default constructor
       def __init__(self, val):
                self.val=val
       
       #alternative constructor
       @classmethod
       def alter(cls, val):
               return cls (val+100)
       
       def result(self):
             print(self.val)
       

       
x=Calculator(5).result()  # it will use default constructor and print 5
y=Calculator.alter(5).result()  # it will use alternative constructor and print 105
