from unit import *

owner = [0 for _ in range(len(maps))]
buildinglv = [0 for _ in range(len(maps))]

def buy1pBd(lv):  #땅 주인, 빌딩 레벨을 바꾸고 돈 소모값 리턴
    num = player1_in_map.index(True)
    if owner[num] == 2 or buildinglv[num] != lv-1:  #땅 주인이 상대 것이거나 건물 레벨이 전 단계가 아닐 경우
        print("구매 불가")  #pyqt에서의 표시로 바꿔야함
        return 0  #구매하지 않았기 때문에 돈 소모값 0
    else:
        player1_turn[1] = False
        owner[num] = 1
        buildinglv[num] = lv
        return int(map_price[num])

def buy2pBd(lv):
    num = player2_in_map.index(True)
    if owner[num] == 1 or buildinglv[num] != lv-1:
        print("구매 불가")  #pyqt에서의 표시로 바꿔야함
        return 0
    else:
        player2_turn[1] = False
        owner[num] = 2
        buildinglv[num] = lv
        return int(map_price[num])

#자기 땅 아닐 시 땅값 리턴
def payment1p():
    num = player1_in_map.index(True)
    if owner[num] == 2:
        player1_turn[2] = False
        return int(map_price[num])*int(buildinglv[num])
    else:
        return 0

def payment2p():
    num = player2_in_map.index(True)
    if owner[num] == 1:
        player2_turn[2] = False
        return int(map_price[num])*int(buildinglv[num])
    else:
        return 0
