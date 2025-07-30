class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(B,A):  # Multiple inheritance
    pass

c = C()
c.show()  # Output?
