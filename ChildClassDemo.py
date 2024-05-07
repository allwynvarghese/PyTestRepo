from class_demo import DemoClass

class ChildClass(DemoClass):  # child class is declared with parent class in round brackets

    num2 = 200

    def __init__(self):
        DemoClass.__init__(self, 2, 10)

    def total(self):
        return self.num2 + self.num + self.summation()


obj = ChildClass()
print(obj.total())