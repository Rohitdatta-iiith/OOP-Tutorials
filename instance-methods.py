#Code3 of the tutorial
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def description(self):
        print(f"The Dog {self.name} age is {self.age} ")
    def speak(self,sound):
        print(f"The Dog {self.name} shouts {sound}")

a = Dog("lilly",2)
b = Dog("RashKonda",3)
a.description()
a.speak("Bow Bow")
#instance methods are the ones where functions are defined inside classes & can only be called from instance of that class
