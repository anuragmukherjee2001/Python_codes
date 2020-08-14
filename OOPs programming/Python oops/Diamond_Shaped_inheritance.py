class A:
    
    def met(self):
        print("This is a method from Class A")

class B(A):
    
    def met(self):
        print("This is a method from Class B")

class C(A):
    pass

class D(B, C):
    pass


a = A()
b = B()
c = C()
d = D()

d.met()
