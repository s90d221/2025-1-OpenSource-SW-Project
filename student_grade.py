##################
# 프로그램명: Grade Calculation Program
# 작성자: 소프트웨어학부 / 윤수진
# 작성일: 2025-03-23
# 프로그램 설명: 이 프로그램은 학생들의 학번, 이름, 과목별 점수를 입력받고, 총점, 평균, 학점을 계산하여 
# 학생들의 등수를 매긴 후 결과를 출력하는 성적 계산 프로그램
# Copyright (C) 2025 Sujin Yoon
# Contact : sujin@gmail.com
##################

def get_student_info():  # 학생 정보 입력
    student_id = input("학번: ")
    name = input("학생 이름: ")
    scores = {
        "영어": int(input("영어 점수: ")),
        "C-언어": int(input("C-언어 점수: ")),
        "파이썬": int(input("파이썬 점수: ")),
    }
    return student_id, name, scores


def calculate_score(scores):  # 총점, 평균, 학점 계산
    total = sum(scores.values())  # .values()를 사용해 점수들만 가져와 sum()으로 총합
    average = total / len(scores)  # len()은 딕셔너리의 항목(과목 수)을 세는 함수
    grade = (
        "A"
        if average >= 90
        else "B+" if average >= 85
        else "B" if average >= 80
        else "C" if average >= 70
        else "D" if average >= 60
        else "F"
    )
    return total, average, grade


def calculate_ranks(students):  # 등수 계산
    scores = [student[2]["총점"] for student in students]  # 모든 학생의 총점을 리스트로 모은 것
    ranks = {score: sorted(scores, reverse=True).index(score) + 1 for score in scores} # 총점을 내림차순으로 정렬
    for student in students:
        student[2]["등수"] = ranks[student[2]["총점"]] # 학생 정보에 등수 추가


def print_results(students):  # 결과 출력
    print("\n                              성적관리 프로그램")
    print("=" * 100)
    print(
        f"{'학번':<13}{'이름':<10}{'영어':<8}{'C-언어':<8}{'파이썬':<8}{'총점':<8}{'평균':<8}{'학점':<8}{'등수':<6}"
    )
    print("=" * 100)
    students.sort(key=lambda x: x[2]["등수"])  # 등수 순으로 정렬
    for student_id, name, data in students:
        print(
            f"{student_id:<15}{name:<10}{data['영어']:<10}{data['C-언어']:<10}{data['파이썬']:<10}{data['총점']:<10}{data['평균']:<10.2f}{data['학점']:<10}{data['등수']:<6}"
        )


students = []
for _ in range(5):
    student_id, name, scores = get_student_info()
    total, average, grade = calculate_score(scores)
    scores.update({"총점": total, "평균": average, "학점": grade})
    students.append((student_id, name, scores))

calculate_ranks(students)
print_results(students)