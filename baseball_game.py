import random

#임의의 숫자 설정
def select_number():
    a=random.randint(0,9)
    b=random.randint(0,9)
    c=random.randint(0,9)
    while a==b:
        b=random.randint(0,9)
    while a==c or b==c:
        c=random.randint(0,9)
    return a, b, c

#변수 선언
answer=False
n=0

#입력값과 비교
a, b, c= select_number()
while answer==False:
    strike=0
    ball=0
    if n>=10:
        break
    user_a=int(input('숫자를 입력하세요: '))
    user_b=int(input('숫자를 입력하세요: '))
    user_c=int(input('숫자를 입력하세요: '))
    if user_a==a:
        strike += 1
    if user_b==b:
        strike += 1
    if user_c==c:
        strike += 1
    if user_a==b or user_a==c:
        ball += 1
    if user_b==a or user_b==c:
        ball += 1
    if user_c==a or user_c==b:
        ball += 1
    if strike==3:
        answer=True
        break
    else:
        print('{}스트라이크 {}볼입니다.'.format(strike,ball))
    n+=1
match answer:
    case True:
        print('정답입니다!')
    case False:
        print('실패입니다!')
        print('정답은 {} {} {}입니다.'.format(a,b,c))
