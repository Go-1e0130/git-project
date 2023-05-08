class CourseHistory:
    # 평점 변환
    convert = {'A+': 4.5, 'A': 4.0, 'B+': 3.5, 'B': 3.0, 'C+': 2.5, 'C': 2.0, 'D+': 1.5, 'D': 1.0, 'F': 0.0}

    # 인스턴스 변수 선언
    def __init__(self):
        self.subject = {}  # { name : code }
        self.credit = {}   # { code : credit }
        self.grade = {}    # { code : grade }
        self.subject_list = []
        self.code = 1001

    # 1. 입력
    def input(self):
        user_subject = input("과목명: ")
        user_credit = int(input("학점: "))
        user_grade = input("평점: ")
        user_gpa = CourseHistory.convert[user_grade]

        # 재수강 = True
        if user_subject in self.subject_list:
            subject_code = self.subject[user_subject]
            if CourseHistory.convert[self.grade[subject_code]] < user_gpa:
                self.credit[subject_code] = user_credit
                self.grade[subject_code] = user_grade
            print("재수강 입력되었습니다.")

        # 재수강 = False
        else:
            self.subject_list.append(user_subject)
            self.subject[user_subject] = self.code
            self.credit[self.code] = user_credit
            self.grade[self.code] = user_grade
            self.code += 1
            print("입력되었습니다.")

    # 2. 출력
    def output(self):
        for subject_name in self.subject_list:
            subject_code = self.subject[subject_name]
            print("[{}] {}학점: {}".format(subject_name, self.credit[subject_code], self.grade[subject_code]))

    # 3. 조회
    def check(self):
        subject_name = input("과목명: ")
        if subject_name in self.subject_list:
            subject_code = self.subject[subject_name]
            print("[{}] {}학점: {}".format(subject_name, self.credit[subject_code], self.grade[subject_code]))
        else:
            print("해당하는 과목이 없습니다.")

    # 4. 계산
    def calculate(self):
        archive_credit, submit_credit, archive_gpa_sum, submit_gpa_sum = 0, 0, 0.0, 0.0
        for subject_name in self.subject_list:
            subject_code = self.subject[subject_name]
            archive_credit += self.credit[subject_code]
            archive_gpa_sum += CourseHistory.convert[self.grade[subject_code]] * self.credit[subject_code]
            if self.grade[subject_code] != 'F':
                submit_credit += self.credit[subject_code]
                submit_gpa_sum += CourseHistory.convert[self.grade[subject_code]] * self.credit[subject_code]
        archive_gpa = round(archive_gpa_sum / archive_credit, 2)
        submit_gpa = round(submit_gpa_sum / submit_credit, 2)
        print("제출용: {}학점 (GPA: {})".format(submit_credit, submit_gpa))
        print("열람용: {}학점 (GPA: {})".format(archive_credit, archive_gpa))

    # 반복 질문
    def question(self):
        print('작업을 선택하세요.')
        print('  1. 입력')
        print('  2. 출력')
        print('  3. 조회')
        print('  4. 계산')
        print('  5. 종료')
        answer = int(input())
        return answer


# Code start
course = CourseHistory()
while True:
    work = course.question()
    if work == 1:
        course.input()
    if work == 2:
        course.output()
    if work == 3:
        course.check()
    if work == 4:
        course.calculate()
    if work == 5:
        break
print("종료")
