# class and methods demo in python

class DemoClass:  # class declaration

    num = 100  # variable in a class. this is known as class variable

    def print_message(self):  # method declaration in a class
        print("hello world {}".format(self.num))  # All variable has to be accessed using self keyword
        # or class name - classname.variableName

    def __init__(self, a, b):  # constructor is defined using __init__ . Here a and b are instance variable
        self.a = a
        self.b = b

    def summation(self):
        print("Sum of numbers {} and {} is {}".format(self.a, self.b, self.a + self.b))
        return self.a + self.b


# classObj = DemoClass()  # creating an object of the class

# classObj.print_message()
# print("class variable is {}".format(classObj.num))

classObj2 = DemoClass(4, 5)
classObj2.summation()
