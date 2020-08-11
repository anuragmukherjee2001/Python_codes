class p:
    def __init__(self,name,alias):
        self.name = name
        self.__alias = alias
    def who(self):
        print('name',self.name)
        print('alias',self.__alias)
    def __foo(self):
        print("this is private method")
    def foo(self):
        print("this is a public method")
        self.__foo()

obj = p("ankit","rick")
obj.who()
obj.foo()
