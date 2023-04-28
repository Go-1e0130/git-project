import random

lotto=set()
while len(lotto) < 6:
    lotto.add(random.randint(1,45))
print(lotto)
user_value = input('1~45 사이의 숫자 6개를 입력하세요')
user_lotto = set(user_value)
intersection = lotto.intersection(user_lotto)
print('{}개 맞았습니다.'.format(len(intersection)))
