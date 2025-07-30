class Calculator:

    def __init__(self):
        self.val="public"
        self.__val="private"  # define private variable by using doduble underscore
        self._val="protected"  # define protected by using single underscore


    def access(self):
        return self.__val

obj=Calculator()
print(obj.val)  #access public directly 
print(obj._val) ## access protected directly 
# print(obj.__val) # access private directly [will raise error]
print(obj.access()) # access via internal method


