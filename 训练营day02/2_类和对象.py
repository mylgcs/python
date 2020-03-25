class Dog:
    name = ""
    age = 0
    def bark(self):
        print(self.name,'叫：','won won won')
d = Dog()
d.name = '楼SB'
d.age = 26
d.bark()

class Dog1:
    def __init__(self,name,age):
        self.name = "楼SB"
        self.age = 20
    def show(self):
        print("这只狗叫", self.name ,"今年", self.age)