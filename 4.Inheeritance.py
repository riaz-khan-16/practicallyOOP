class Calculator:
      def add(self, a,b):
               return a+b
      def sub(self, a,b):
               return a-b
      
class AdvancedCalculator(Calculator) :
        def   mult(self, a,b):
                  return a*b
        def dividee(selef, a,b):
                 return a/b
        
cal=AdvancedCalculator()
print(cal.add(5,6))
