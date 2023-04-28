#함수 정의
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

#변수 선언
subject_name={}
work=1
code=101
user_credit=0
user_grade=None
user_gpa_sum=0
open_credit=0
open_gpa_sum=0
submit_credit=0
submit_gpa_sum=0
n=0 #과목수 
subject_list=[]
only_subject_names=[]
reclass=None

#연산
while work==1 or work==2:
    print('작업을 선택하세요.')
    print('  1. 입력')
    print('  2. 출력')
    print('  3. 계산')
    work=int(input())
    if work==1:
        subject=input('과목명: ')
        reclass= subject in only_subject_names
        if reclass==True:
            
            original=subject_list.pop(only_subject_names.index(subject))
            code=original[0]
            open_gpa_sum -= convert_function(original[2]) * original[1]
            submit_gpa_sum -= convert_function(original[2]) * original[1]
            user_credit = int(input('학점: '))
            user_grade = input('평점: ')
            user_gpa_sum = convert_function(user_grade) * user_credit
            open_gpa_sum += user_gpa_sum
            if user_grade!='F':
                submit_gpa_sum += user_gpa_sum
            subject_list.insert(code-101,(code,original[1],user_grade))
        else:
            subject_name[code]=subject
            user_credit = int(input('학점: '))
            user_grade = input('평점: ')
            user_gpa_sum = convert_function(user_grade) * user_credit
            open_credit += user_credit
            open_gpa_sum += user_gpa_sum
            if user_grade!='F':
                submit_credit += user_credit
                submit_gpa_sum += user_gpa_sum
            subject_list.append((code,user_credit,user_grade))
            code+=1
            n+=1
        only_subject_names=list(subject_name.values())
        print('입력되었습니다.')
    if work==2:
        for i in range(101,101+n):
            print('[{}] {}학점: {}'.format(subject_name[i],subject_list[i-101][1],subject_list[i-101][2]))
    if work==3:
        print('열람용: {}학점(GPA:{})'.format(open_credit, round(open_gpa_sum/open_credit,2)))
        print('제출용: {}학점(GPA:{})'.format(submit_credit, round(submit_gpa_sum/submit_credit,2)))
        print(subject_list)
