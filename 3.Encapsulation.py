class calculator:
       def __init__(self):
               self.__result=0   #protecteed
       def add(self, val):
                self.__result+=val
       def sub(self, val):
                self.__result-=val
       def get_result(self):  
                print(self.__result)
                return self.__result

##Here we can not see the value of __result by using print(calcuclator.__result). we need to call the method calculator.get_result()

cal=calculator()
cal.add(5)
cal.sub(6)
# cal.__result # will give error
cal.get_result()  # will give the result