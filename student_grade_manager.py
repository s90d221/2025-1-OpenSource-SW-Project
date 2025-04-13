# 성적 관리 프로그램
# Copyright (C) 2025 Sujin Yoon
# Licensed under the MIT License.
# Contact : sujin@gmail.com

# -*- coding: utf-8 -*-
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
    students.sort(key=lambda x: x[2]["총점"], reverse=True)  # 총점 순으로 내림차순 정렬
    for student_id, name, data in students:
        print(
            f"{student_id:<15}{name:<10}{data['영어']:<10}{data['C-언어']:<10}{data['파이썬']:<10}{data['총점']:<10}{data['평균']:<10.2f}{data['학점']:<10}{data['등수']:<6}"
        )


def insert_student(students):  # 학생 삽입 함수
    student_id, name, scores = get_student_info()
    total, average, grade = calculate_score(scores)
    scores.update({"총점": total, "평균": average, "학점": grade})
    students.append((student_id, name, scores))
    calculate_ranks(students)


def delete_student(students):  # 학생 삭제 함수
    student_id = input("삭제할 학생의 학번을 입력하세요: ")
    for student in students:
        if student[0] == student_id:
            students.remove(student)
            print(f"학번 {student_id}의 학생이 삭제되었습니다.")
            calculate_ranks(students)
            return
    print("해당 학번의 학생을 찾을 수 없습니다.")


def search_by_id(students):  # 학번으로 학생 검색
    student_id = input("검색할 학생의 학번을 입력하세요: ")
    for student in students:
        if student[0] == student_id:
            print(f"학번: {student[0]}, 이름: {student[1]}, 총점: {student[2]['총점']}, 학점: {student[2]['학점']}")
            return
    print("해당 학번의 학생을 찾을 수 없습니다.")


def search_by_name(students):  # 이름으로 학생 검색
    name = input("검색할 학생의 이름을 입력하세요: ")
    for student in students:
        if student[1] == name:
            print(f"학번: {student[0]}, 이름: {student[1]}, 총점: {student[2]['총점']}, 학점: {student[2]['학점']}")
            return
    print("해당 이름의 학생을 찾을 수 없습니다.")


def count_students_above_80(students):  # 80점 이상 학생 수 카운트
    count = 0
    for student in students:
        if student[2]['평균'] >= 80:
            count += 1
    print(f"80점 이상인 학생 수: {count}")


# 메인 함수
students = []
for _ in range(5):
    insert_student(students)  # 5명의 학생을 입력

while True:
    print("\n1. 성적 출력")
    print("2. 학생 추가")
    print("3. 학생 삭제")
    print("4. 학번으로 검색")
    print("5. 이름으로 검색")
    print("6. 80점 이상 학생 수 카운트")
    print("7. 종료")
    choice = input("원하는 작업을 선택하세요: ")

    if choice == '1':
        print_results(students)
    elif choice == '2':
        insert_student(students)
    elif choice == '3':
        delete_student(students)
    elif choice == '4':
        search_by_id(students)
    elif choice == '5':
        search_by_name(students)
    elif choice == '6':
        count_students_above_80(students)
    elif choice == '7':
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 선택입니다. 다시 시도하세요.")