"""
변경사항
맨 위의 display에 플레이어:  , 돈:   나오게 하기
unit.py 방향에 따른 이미지, 주사위 구현
맵의 경계 추가

할 것

건물 수정... 16x16 -> 64x64(우주선 크기, 주사위 크기)
주사위는 턴당 1번만
음악 넣기 : 방법 몰라서 보류
특별 맵 추가..?

"""

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QHBoxLayout, QComboBox
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtGui import QMovie, QPixmap
from purchase import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist
from unit import *
from PyQt5.QtCore import Qt
from dice import Dice


class BoradGame(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.player1 = unit()
        self.player2 = unit()
        self.dice = Dice()

        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setMaxLength(100)
        font = self.display.font()
        self.display.setAlignment(Qt.AlignCenter)
        font.setPointSize(font.pointSize() + 555)
        self.initUI()

    def initUI(self):
        self.player1location = [QLabel() for _ in range(len(maps))]
        self.player2location = [QLabel() for _ in range(len(maps))]
        self.player1location[0].setPixmap(self.player1.player1diection(0))
        self.player2location[0].setPixmap(self.player2.player2diection(0))
        self.building1 = [QLabel() for _ in range(len(maps))]
        self.building2 = [QLabel() for _ in range(len(maps))]
        self.building3 = [QLabel() for _ in range(len(maps))]
        self.turnpix = QLabel()
        mapsLayout = QGridLayout()
        mainLayout = QGridLayout()
        MapGroups = {'map': {'maps': maps, 'price': map_price, 'building': buildings}}

        mapin = MapGroups['map']
        self.name = [0 for i in range(len(maps))]
        self.price = [0 for i in range(len(maps))]
        self.map_priceWidget = [0 for i in range(len(maps))]

        for i in range(len(maps)):
            mapimg = QLabel()
            mapimg.setStyleSheet("border-style: solid;" "border-width: 1px;"
                                 "border-color: rgb(0,0,0);" "border-radius: 2px")
            mapLayout = QGridLayout()
            mappriceLayout = QHBoxLayout()
            buildingsLayout = QHBoxLayout()
            playerLayout = QHBoxLayout()
            # 6시
            if i < 7:
                mapsLayout.addLayout(mapLayout, 6, i)
                mapsLayout.addWidget(mapimg, 6, i)
            # 3시
            elif 7 <= i < 13:
                mapsLayout.addLayout(mapLayout, 12 - i, 6)
                mapsLayout.addWidget(mapimg, 12 - i, 6)

            # 9시
            elif 18 <= i < 24:
                mapsLayout.addLayout(mapLayout, i - 18, 0)
                mapsLayout.addWidget(mapimg, i - 18, 0)

            # 12시
            else:
                mapsLayout.addLayout(mapLayout, 0, 18 - i)
                mapsLayout.addWidget(mapimg, 0, 18 - i)

            # 이름, 가격 style 조정 (가격수정은 map.py)
            self.name[i] = QLabel(mapin['maps'][i])

            self.price[i] = QLabel(mapin['price'][i])

            self.map_priceWidget[i] = QLabel()
            self.map_priceWidget[i].setStyleSheet("color: black;""border-style: solid;""border-width: 1px;"
                                                  "border-color: rgb(0,0,0);""border-radius: 2px")
            # map, price layout 조정 (Widget -> mappriceLayout)
            mappriceLayout.addWidget(self.name[i])
            mappriceLayout.addWidget(self.price[i])

            # 건물 layout 조정 (Widget -> buildingsLayout)
            buildingsLayout.addWidget(self.building1[i])
            buildingsLayout.addWidget(self.building2[i])
            buildingsLayout.addWidget(self.building3[i])

            # (mapWidget -> mapLayout)
            mapLayout.addWidget(self.map_priceWidget[i], 0, 0)
            mapLayout.addLayout(mappriceLayout, 0, 0)
            mapLayout.addLayout(buildingsLayout, 1, 0)
            mapLayout.addLayout(playerLayout, 2, 0)
            playerLayout.addWidget(self.player1location[i])
            playerLayout.addWidget(self.player2location[i])

            # 창 움직임 조정
            self.player1location[i].setMinimumSize(16, 32)

        # 주사위 버튼
        self.roll1 = QToolButton()
        self.roll1.setMinimumSize(70, 70)
        self.roll1.setText('1p')
        self.roll1.clicked.connect(self.p1DiceButton)
        mapsLayout.addWidget(self.roll1, 1, 1)

        self.roll2 = QToolButton()
        self.roll2.setMinimumSize(70, 70)
        self.roll2.setText('2p')
        self.roll2.clicked.connect(self.p2DiceButton)
        mapsLayout.addWidget(self.roll2, 1, 2)

        self.turnover = QToolButton()
        self.turnover.setMinimumSize(70, 70)
        self.turnover.setText('턴 종료')
        self.turnover.clicked.connect(self.overClicked)
        mapsLayout.addWidget(self.turnover, 1, 3)

        self.turnpix.setPixmap(QPixmap("unit\p1turn.png"))
        mapsLayout.addWidget(self.turnpix, 3, 1)

        # 건물 구매 버튼 추가
        self.buy1pBuilding = QToolButton()
        self.buy1pBuilding.setMinimumSize(50, 50)
        self.buy1pBuilding.setText('1p 건물 구매')
        self.buy1pBuilding.clicked.connect(self.buy1pbuttonClicked)

        self.buildingLv = QComboBox()
        self.buildingLv.addItem("건물1")
        self.buildingLv.addItem("건물2")
        self.buildingLv.addItem("건물3")

        self.buy2pBuilding = QToolButton()
        self.buy2pBuilding.setMinimumSize(50, 50)
        self.buy2pBuilding.setText('2p 건물 구매')
        self.buy2pBuilding.clicked.connect(self.buy2pbuttonClicked)

        # BuildingButton -> mapsLayout

        mapsLayout.addWidget(self.buy1pBuilding, 2, 1)
        mapsLayout.addWidget(self.buy2pBuilding, 2, 2)
        mapsLayout.addWidget(self.buildingLv, 2, 3)

        self.dicelabel = QLabel()
        mapsLayout.addWidget(self.dicelabel, 4, 1)

        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        mainLayout.addLayout(mapsLayout, 1, 0)

        # 여러 화면에서
        self.setLayout(mainLayout)
        self.setWindowTitle("Board game")

    def p1DiceButton(self):
        if (player1_turn[0]):
            self.display.setText("p1         " + str(self.player1.money))
            # 주사위굴림 + 애니매이션
            num = self.dice.roll()
            img = self.dice.diceImg(num)
            img.start()
            self.dicelabel.setMovie(img)

            # p1의 위치를 찾고 이동
            a = self.player1.findPlayer1(num)

            # p1의 위치 표시
            for i in range(len(maps)):
                if player1_in_map[i] == True:
                    self.player1location[i].setPixmap(self.player1.player1diection(a))
                else:
                    self.player1location[i].setPixmap(QPixmap("unit\64x64"))

            #이동시 땅 소유 주인 확인 후 통행료 지불
            self.player1.money -= payment1p()
            self.player2.money += payment1p()
            player1_turn[0] = False
            self.turnpix.setPixmap(self.player1.p1turnover())

    def p2DiceButton(self):
        if (player2_turn[0]):
            self.display.setText("p2         " + str(self.player2.money))
            # 주사위굴림 + 애니매이션
            num = self.dice.roll()
            img = self.dice.diceImg(num)
            self.dicelabel.setMovie(img)
            img.start()

            # p2의 위치를 찾고 이동
            a = self.player2.findPlayer2(num)

            # p2의 위치 표시
            for i in range(len(maps)):
                if player2_in_map[i] == True:
                    self.player2location[i].setPixmap(self.player1.player2diection(a))
                else:
                    self.player2location[i].setPixmap(QPixmap("unit\64x64"))

            #이동시 땅 소유 주인 확인 후 통행료 지불
            self.player2.money -= payment2p()
            self.player1.money += payment2p()
            player2_turn[0] = False
            self.turnpix.setPixmap(self.player2.p2turnover())

    # 구매 버튼 클릭 함수들
    def buy1pbuttonClicked(self):
        if (player1_turn[1]):
            p = int(map_price[player1_in_map.index(True) - 1])
            if self.player1.money > p:
                self.player1.money -= buy1pBd(self.buildingLv.currentIndex()+1)
            for i in range(len(maps)):
                if owner[i] == 1:
                    self.map_priceWidget[i].setStyleSheet("color: black;" "background-color: #1E90FF;"
                                                          "border-style: solid;" "border-width: 1px;"
                                                          "border-color: rgb(0,0,0);" "border-radius: 2px")
                    if buildinglv[i] == 1:
                        self.building1[i].setText("")
                        self.building1[i].setPixmap(QPixmap("building\p1_small.png"))
                    elif buildinglv[i] == 2:
                        self.building2[i].setText("")
                        self.building2[i].setPixmap(QPixmap("building\p1_middle.png"))
                    elif buildinglv[i] == 3:
                        self.building3[i].setText("")
                        self.building3[i].setPixmap(QPixmap("building\p1_large.png"))
            self.display.setText("p1         " + str(self.player1.money))
            self.turnpix.setPixmap(self.player1.p1turnover())

    def buy2pbuttonClicked(self):
        if (player2_turn[1]):
            p = int(map_price[player2_in_map.index(True) - 1])
            if self.player2.money > p:
                self.player2.money -= buy2pBd(self.buildingLv.currentIndex()+1)
            for i in range(len(maps)):
                if owner[i] == 2:
                    self.map_priceWidget[i].setStyleSheet("color: black;" "background-color: #F78181;"
                                                          "border-style: solid;" "border-width: 1px;"
                                                          "border-color: rgb(0,0,0);" "border-radius: 2px")
                    if buildinglv[i] == 1:
                        self.building1[i].setText("")
                        self.building1[i].setPixmap(QPixmap("building\p2_small.png"))
                    elif buildinglv[i] == 2:
                        self.building2[i].setText("")
                        self.building2[i].setPixmap(QPixmap("building\p2_middle.png"))
                    elif buildinglv[i] == 3:
                        self.building3[i].setText("")
                        self.building3[i].setPixmap(QPixmap("building\p2_large.png"))
            self.display.setText("p2         " + str(self.player2.money))
            self.turnpix.setPixmap(self.player2.p2turnover())

    def overClicked(self):
        if (player1_turn[1] == True) and (player1_turn[2] == True):
            player1_turn[1] = False
            self.turnpix.setPixmap(self.player1.p1turnover())
        elif (player2_turn[1] == True) and (player2_turn[2] == True):
            player2_turn[1] = False
            self.turnpix.setPixmap(self.player2.p2turnover())



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    game = BoradGame()
    game.show()
    sys.exit(app.exec_())
