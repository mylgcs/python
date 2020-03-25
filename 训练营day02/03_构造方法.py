class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("这只狗叫", self.name, "今年", self.age, "岁。")