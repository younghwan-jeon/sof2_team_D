maps = ['월급', '타이베이', '베이징', '마닐라', '싱가포르', '특', '아테네', '코펜하겐', '스톡홀름', '스위스', '베른린', '특', '리스본'
        , '상파울루', '시드니', '부산', '특', '마드리드', '도쿄', '파리', '특', '로마', '런던', '서울']

buildings = ['건물1', '건물2', '건물3']

special_map = [5, 11, 16, 20]

map_price = [str(1000 * i) for i in range(len(maps))]

for i in range(len(maps)):
    if i in special_map:
        map_price[i] = str(0)
