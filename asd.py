def convert_function(grade):
    match grade:
        case 'A+':
            gpa=4.5
        case 'A':
            gpa=4.0
        case 'B+':
            gpa=3.5
        case 'B':
            gpa=3.0
        case 'C+':
            gpa=2.5
        case 'C':
            gpa=2.0
        case 'D+':
            gpa=1.5
        case 'D':
            gpa=1.0
        case 'F':
            gpa=0
    return gpa

user_credit=0
user_grade=0
user_gpa=0
submit_credit=0
submit_gpa=0
open_credit=0
open_gpa=0
work=1

while work==1:
    print('작업을 선택하세요')
    print('1. 입력')
    print('2. 계산')
    work=int(input())
    if work==1:
        user_credit = int(input('학점: '))
        user_grade = input('평점: ')
        user_gpa = convert_function(user_grade) * user_credit
        open_credit += user_credit
        open_gpa += user_gpa
        if user_grade!='F':
            submit_credit += user_credit
            submit_gpa += user_gpa
    if work==2:
        print('열람용: {}학점(GPA:{})'.format(open_credit, open_gpa/open_credit))
        print('제출용: {}학점(GPA:{})'.format(submit_credit, submit_gpa/submit_credit))
