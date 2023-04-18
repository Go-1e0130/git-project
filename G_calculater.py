coordinates = []
work = 1
sum_x = 0
sum_y = 0
while work == 1 or work == 2:
    print('작업을 선택하세요.')
    print('1. 좌표 입력')
    print('2. 좌표 출력')
    print('3. 계산')
    work = int(input())
    if work == 1:
        user_x = int(input('x값: '))
        user_y = int(input('y값: '))
        coordinates.append((user_x,user_y))
    elif work == 2:
        print(coordinates)
    elif work == 3:
        for i in range(len(coordinates)):
            sum_x += coordinates[i][0]
            sum_y += coordinates[i][1]
            mean = (sum_x/len(coordinates),sum_y/len(coordinates))
        print(mean)
