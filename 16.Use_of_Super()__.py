class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        super().show()   # Call Parent's show()
        print("Child method")

c = Child()
c.show()   
