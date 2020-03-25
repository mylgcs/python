# 类是一个自定义的类型，对象是这个类型创建的变量。

# 类由成员变量，和成员方法组成。

class Dog:
    name = ""
    age = 0

    def bark(self):
        print(self.name, "叫：", "Won, Won!")


d = Dog()
d.name = "小白"
d.age = 5
d.bark()