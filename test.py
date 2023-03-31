reading_credit = 0
submission_credit = 0
reading_grade = 0
submission_grade = 0

while True:
    print('작업을 선택하세요.')
    print('1. 입력')
    print('2. 계산')
    work = int(input())
    print("")
    if work == 1:
        print('학점을 입력하세요:')
        credit = int(input())
        print('평점을 입력하세요:')
        grade = str(input())
        print('입력되었습니다.\n')

        reading_credit = reading_credit + credit
        if grade == "F":
            submission_credit = submission_credit
        else:
            submission_credit = submission_credit + credit

        if grade == "A+":
            grade = 4.5
        elif grade == "A":
            grade = 4.0
        elif grade == "B+":
            grade = 3.5
        elif grade == "B":
            grade = 3.0
        elif grade == "C+":
            grade = 2.5
        elif grade == "C":
            grade = 2.0
        elif grade == "D+":
            grade = 1.5
        elif grade == "D":
            grade = 1.0
        else:
            grade = 0.0
        reading_grade = reading_grade + (grade * credit)
        if grade == 0.0:
            submission_grade = submission_grade
        else:
            submission_grade = submission_grade + (grade * credit)
    else:
        reading_grade = round(reading_grade / reading_credit, 2)
        submission_grade = round(submission_grade / submission_credit, 2)
        print(f"제출용: {submission_credit}학점 (GPA: {submission_grade})")
        print(f"열람용: {reading_credit}학점 (GPA: {reading_grade})\n")
        print("프로그램을 종료합니다.")
        break
