# 변수 선언
def question():
    print('작업을 선택하세요.')
    print('  1. 입력')
    print('  2. 출력')
    print('  3. 계산')
    answer = int(input())
    return answer


convert = {'A+': 4.5, 'A': 4.0, 'B+': 3.5, 'B': 3.0, 'C+': 2.5, 'C': 2.0, 'D+': 1.5, 'D': 1.0, 'F': 0.0}
work = 1
code = 101
dictionary = {}
subject_list = []
subjects = []
n = 0
open_credit, open_gpa_sum, submit_credit, submit_gpa_sum = 0, 0, 0, 0
while work == 1 or work == 2:
    work = question()
    if work == 1:
        subject = input('과목명: ')
        user_credit = int(input('학점: '))
        user_grade = input('평점: ')
        user_gpa = convert[user_grade]
        if subject in subjects:    # 재수강 여부
            index = subjects.index(subject)
            saved_gpa = convert[subject_list[index][2]]
            if user_gpa > saved_gpa:    # 재수강 학점이 더 높으면?
                saved_data = subject_list.pop(index)
                saved_code, saved_credit = saved_data[0], saved_data[1]
                subject_list.insert(index, (saved_code, user_credit, user_grade))
            print('재수강 입력되었습니다.')
        else:
            dictionary[code] = subject
            subject_list.append((code, user_credit, user_grade))
            code += 1
            n += 1
            subjects = list(dictionary.values())
            print('입력되었습니다.')
    if work == 2:
        for i in range(101, 101+n):
            print('[{}] {}학점: {}'.format(dictionary[i], subject_list[i-101][1], subject_list[i-101][2]))
    if work == 3:
        for i in range(n):
            open_credit += subject_list[i][1]
            open_gpa_sum += convert[subject_list[i][2]] * subject_list[i][1]
            if subject_list[i][2] != 'F':
                submit_credit += subject_list[i][1]
                submit_gpa_sum += convert[subject_list[i][2]] * subject_list[i][1]
        print('열람용: {}학점(GPA:{})'.format(open_credit, round(open_gpa_sum/open_credit, 2)))
        print('제출용: {}학점(GPA:{})'.format(submit_credit, round(submit_gpa_sum/submit_credit, 2)))