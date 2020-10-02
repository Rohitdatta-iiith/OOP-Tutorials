#to get friendlier output rather than getting objects direct location
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Object dog is created with name: {self.name} and age: {self.age}"
a = Dog("lilly",2)
b = Dog("laika",4)
print(a)
print(b)
#this is code 4 of the tutorial and __init__ and __str__ are called dunder methods becaues of trailing and ending underscores


