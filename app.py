# 小明手里有两张牌，左手红桃A，右手黑桃K，问小明交换双手的牌
# 之后，左右手的牌各是什么？
# 先找对象 小明 两张牌  3个  小明 两只手 两张牌 5个
# 根据对象写类

# 牌的类，其对象是单张的牌
class pai:
    # 字段描述对象的属性/特性
    yanse = ''
    shuz = ''
# 手的类，用于创建一只手
class Hand:
    shou:pai  # 手里面可以有一张牌
# 人类，用于创建小明
class Human:
    # 字段描述人的特征
    hand_left = Hand()
    hand_right = Hand()

    # 方法描述人的行为功能
    # 拿牌
    def catch_poker_cards(self,pai1:pai,pai2:pai):
        self.hand_left.shou = pai1
        self.hand_right.shou = pai2
    # 展示牌
    def show_cards(self):
        print("\n左手:%s_%s" % (self.hand_left.shou.yanse,self.hand_left.shou.shuz))
        print("右手:%s_%s\n" % (self.hand_right.shou.yanse,self.hand_right.shou.shuz))

    # 换牌
    def swap_cards(self):
        temp = self.hand_right.shou
        self.hand_right.shou = self.hand_left.shou
        self.hand_left.shou = temp

# 创建两张牌

pai1 = pai()
pai1.yanse,pai1.shuz = "红桃","A"
pai2 = pai()
pai2.yanse,pai2.shuz = "黑桃","K"

#创建小余
xiaoyu = Human()

#演示流程
xiaoyu.catch_poker_cards(pai1,pai2)
xiaoyu.show_cards()
xiaoyu.swap_cards()
xiaoyu.show_cards()