#Classes are user defined blueprint or prototype
#sum,mul,add,constants#methods, class variables, instance variable, constructors etc
#self keywordd is mandatory for calling varibale name into method
#instances and class variables have whole different purpose
#constructor name should be __init__
#new keyword is not required when you create object
class Calculator:
    num =100
    def __init__(self,a,b):
        self.first=a
        self.second=b
        print("RPal")

    def getData(self):
        print("Rohan")
    def summation(self):
        return self.first +self.second+ Calculator.num

obj= Calculator(2,3)
obj.getData()
print(obj.summation())
obj1= Calculator(5,8)
obj.getData()
print(obj1.summation())