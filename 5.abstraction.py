from abc import ABC, abstractmethod
class Calculator:
    def calculate(self, a,b):
            pass
    
class  Adder(Calculator):
             def calculate(self, a,b):
                    return a-b
class Divider(Calculator):
            def calculate(self, a,b):
                    return a//b

calc=Divider()
ans=calc.calculate(25,5)
print(ans)