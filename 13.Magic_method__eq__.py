class Calculator:
    def __init__(self,a):
        self.a=a
    
    def __eq__(self, other):
        if self.a==other.a:
            return True
        elif self.a==(other.a)**2:
            return True
        else:
            return False
        

#Here I have said that if the a of first objec is equal to a of another object they will be true
# or if it's square is equal, it will also be true

obj1=Calculator(25)
obj2=Calculator(5)
print(obj1==obj2)