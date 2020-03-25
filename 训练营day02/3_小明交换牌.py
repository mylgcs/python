# 小明手里有两张牌，左手红桃A，右手黑桃K，问小明交换双手的牌
# 之后，左右手的牌各是什么？
# 先找对象 小明 两张牌  3个  小明 两只手 两张牌 5个
# 根据对象写类

# 牌的类，其对象是单张的牌
class Porke:
    def __init__(self):
        self.poker = None

    color = "" #牌的花色
    num = "" #牌的打小

# 手的类，用于创建一只手
class Hand:
    porke:Porke #手里可以有一张牌

#人类，用于创建小明
class Human:
    # 字段描述人的特征
    hand_left = Hand()
    hand_right = Hand()

    # 方法描述人的行为功能
    # 拿牌
    def catch_porke_cards(self,porke1:Porke,porke2:Porke):
        self.hand_left.porke = porke1
        self.hand_right.porke = porke2

    # 展示牌
    def show_cards(self):
        # print("左手:" + self.hand_left.poker.color + self.hand_left.poker.num)
        # print("右手:" + self.hand_right.porke.color + self.hand_right.porke.num)
        print("\n左手:%s_%s" % (self.hand_left.poker.color, self.hand_left.poker.num))
        print("右手:%s_%s\n" % (self.hand_right.poker.color, self.hand_right.poker.num))

    # 换牌

    def swap_cards(self):
        tmp = self.hand_right.porke
        self.hand_right.porke = self.hand_left.porke
        self.hand_left = tmp

porke1 = Porke()
porke1.color, porke1.num = "红桃","A"
porke2 = Porke()
porke2.color, porke2.num = "黑桃","K"

#创建小明
xiaoming = Human()



xiaoming.catch_porke_cards(porke1,porke2)
xiaoming.show_cards()
xiaoming.swap_cards()
xiaoming.show_cards()