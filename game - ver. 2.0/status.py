import random


class status:
    def __init__(self):
        self.list = ["뒤로 3칸 이동", "뒤로 2칸 이동", "뒤로 1칸 이동", "인센티브! 10000원 지급!",
                "앞으로 1칸 이동", "앞으로 2칸 이동", "앞으로 3칸 이동"]
        self.listlist = [-4, -3, -2, 0, 0, 1, 2]
        self.value = random.randrange(0, 7)

    def statValue(self):
        return self.value

    def statTxt(self, num):
        print(self.list[1])
        return self.list[num]

    def statMove(self, num):
        return self.listlist[num]
