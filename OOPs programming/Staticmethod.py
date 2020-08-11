class TestApp:
    count = 0
    def __init__(self):
        TestApp.count = TestApp.count + 1
    @staticmethod
    def showcount():
        print("total object count",TestApp.count)
ob = TestApp()
ob2 = TestApp()
ob2.showcount()            