#함수 정의
def fibonacci(a=1,b=1,n=None):
    print(a,end=' ')
    n-=1
    b,a=a+b,b
    if n==0:
        return
    fibonacci(a,b,n)

user_n=int(input('몇번째까지 계산할까요?'))
fibonacci(n=user_n)
