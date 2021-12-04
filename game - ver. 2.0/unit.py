from map import *
from PyQt5.QtGui import QPixmap

player1_in_map = [False for _ in range(len(maps))]
player2_in_map = [False for _ in range(len(maps))]
player1_in_map[0] = True
player2_in_map[0] = True
player1_turn = [True, True, True] #주사위 굴림 여부, 건물 구매 여부, 통행료 지불 여부, 통합 턴 표시
player2_turn = [False, False, False]


class unit:
    def __init__(self):
        self.money = 100000
        self.life = True

    def Money(self):
        return self.money

    def findPlayer1(self, num):
        a = player1_in_map.index(True)
        player1_in_map[a] = False
        a += (num + 1)
        while a > 23:
            a -= 24

        player1_in_map[a] = True
        return a

    def findPlayer2(self, num):
        a = player2_in_map.index(True)
        player2_in_map[a] = False
        a += (num + 1)
        while a > 23:
            self.money += 10000
            a -= 24
        player2_in_map[a] = True
        return a

    def player1direction(self, loc):
        # 6시
        if loc < 7:
            return QPixmap("unit\p1-3")
            # 3시
        elif 7 <= loc < 13:
            return QPixmap("unit\p1-12")
            # 9시
        elif 18 <= loc < 24:
            return QPixmap("unit\p1-6")
            # 12시
        else:
            return QPixmap("unit\p1-9")

    def player2direction(self, loc):
        # 6시
        if loc < 7:
            return QPixmap("unit\p2-3")
            # 3시
        elif 7 <= loc < 13:
            return QPixmap("unit\p2-12")
            # 9시
        elif 18 <= loc < 24:
            return QPixmap("unit\p2-6")
            # 12시
        else:
            return QPixmap("unit\p2-9")

    def p1turnover(self):
        if(not player1_turn[0]) and ((not player1_turn[1]) or (not player1_turn[2])):  # 건물 구매 + 주사위 굴림 or 통행료 지불 + 주사위 굴림
            for i in range(3):
                player2_turn[i] = True
                player1_turn[i] = False
            return QPixmap("unit\p2turn.png")
        else:
            return QPixmap("unit\p1turn.png")

    def p2turnover(self):
        if(not player2_turn[0]) and ((not player2_turn[1]) or (not player2_turn[2])):
            for i in range(3):
                player1_turn[i] = True
                player2_turn[i] = False
            return QPixmap("unit\p1turn.png")
        else:
            return QPixmap("unit\p2turn.png")

    def lifeCheck(self):
        if self.money <= 0:
            self.life = False

        else:
            pass