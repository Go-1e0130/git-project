is_prime=True
num=int(input('숫자를 입력하세요: '))
if num>1000 or num<1:
    print('1~1000사이의 숫자를 입력하세요.')
elif num==1:
    is_prime=False
    print('소수가 아닙니다.')
else:
    for i in range(2,num):
        rest=num%i
        if rest==0:
            is_prime=False
            break
    if is_prime==True:
        print('소수입니다.')
    else:
        print('소수가 아닙니다.')
