class A:
    
    classvar1 = "I am a class variable in class A"

    def __init__(self):
        self.var1 = "I am Class A's constructors"
        self.classvar1 = "I am an Instance Variable"
        self.special = "I am a super special variable"

class B(A):
    
    classvar1 = "I am a variable in Class B"

    def __init__(self):
        super().__init__()
        print(super().classvar1)
        self.var1 = "I am Class B's constructors"
        self.classvar1 = "I am an Instance Variable in class B"     


a = A()
b = B()

print(a.var1)
print(b.classvar1)
print(b.special)