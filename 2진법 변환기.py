num=1
repeat=1
user=int(input('숫자를 입력하세요: '))
if user>100:
    print('100이하의 숫자를 입력하세요.')
else:
    print('짜잔!!',end='  ')
    while num<user:
        num*=2
        repeat+=1
    divide_num=num
    if num!=user:
        divide_num/=2
        repeat-=1
    while repeat!=0:
        if user>=divide_num:
            user -= divide_num
            print('1',end=' ')
            divide_num /=2            
        else:
            print('0',end=' ')
            divide_num /=2
        repeat-=1
