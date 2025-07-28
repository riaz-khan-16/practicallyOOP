
class Add:

    def calculate(self, a, b):

           return a+b

class Subtract:

    def calculate(self, a,b):

          return a-b
    
A=Add()

B=Subtract()



print(A.calculate(5,3) )  

print(B.calculate(5,3))

## Same name but different task for different object: This is called Polymorphism

