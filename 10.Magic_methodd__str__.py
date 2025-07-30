class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return "Calculator have two inputs: "+ str(self.a)+ ' ,'+ str(self.b)

obj=Calculator(5,6)
print(obj)


