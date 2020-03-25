# 小明手里有两张牌，左手红桃A，右手黑桃K，问小明交换双手的牌
# 之后，左右手的牌各是什么？
# 先找对象 小明 两张牌  3个  小明 两只手 两张牌 5个
# 根据对象写类

# 牌的类，其对象是单张的牌
class Poker:
    # 字段描述对象的属性/特性
    color = ""      # 花色
    num = ""        # 大小



# 手的类，用于创建一只手
class Hand:
    poker: Poker    # 手里面可以有一张牌


# 人类，用于创建小明
class Human:
    # 字段描述人的特征
    hand_left = Hand()
    hand_right = Hand()

    # 方法描述人的行为功能
    # 拿牌
    def catch_poker_cards(self, poker1: Poker, poker2: Poker):
        self.hand_left.poker = poker1
        self.hand_right.poker = poker2

    # 展示牌
    def show_cards(self):
        print("\n左手:%s_%s" % (self.hand_left.poker.color, self.hand_left.poker.num))
        print("右手:%s_%s\n" % (self.hand_right.poker.color, self.hand_right.poker.num))

    # 换牌
    def swap_cards(self):
        tmp = self.hand_right.poker
        self.hand_right.poker = self.hand_left.poker
        self.hand_left.poker = tmp



# 创建两张牌
poker1 = Poker()
poker1.color, poker1.num = "红桃", "A"
poker2 = Poker()
poker2.color, poker2.num = "黑桃", "K"

# 创建小明
xiaoming = Human()


# 演示流程
xiaoming.catch_poker_cards(poker1,poker2)
xiaoming.show_cards()
xiaoming.swap_cards()
xiaoming.show_cards()



