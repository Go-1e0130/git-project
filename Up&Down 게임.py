import random
answer=False
n=1
target=random.randint(0,100)
while answer==False:
    user=int(input('숫자를 입력하세요: '))
    if n>=10:
        break
    if user>target:
        print('DOWN')
        n+=1
    elif user<target:
        print('UP')
        n+=1
    else:
        answer=True
        break
match answer:
    case True:
        print('승리했습니다.')
    case False:
        print('실패했습니다.')
        print('정답은 {}입니다'.format(target))
