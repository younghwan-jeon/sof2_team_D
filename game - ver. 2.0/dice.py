from PyQt5.QtGui import QMovie
import random


class Dice:
    def __init__(self):
        d1 = QMovie("Dice\diceroll1.gif")
        d2 = QMovie("Dice\diceroll2.gif")
        d3 = QMovie("Dice\diceroll3.gif")
        d4 = QMovie("Dice\diceroll4.gif")
        d5 = QMovie("Dice\diceroll5.gif")
        d6 = QMovie("Dice\diceroll6.gif")

        self.diceGif = [d1, d2, d3,
                        d4, d5, d6]

    def roll(self):
        r = random.randrange(0, 6)
        return r

    def diceImg(self, num):
        return self.diceGif[num]
