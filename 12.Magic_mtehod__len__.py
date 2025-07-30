class Calculator:
    
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def __len__(self):
        return 65

obj=Calculator(5,6)
print(len(obj))