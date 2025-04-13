##################
# 프로그램명: student_grade_manager.py
# 작성자: 소프트웨어학부 / 윤수진
# 작성일: 2025-04-13
# 5명의 학생 정보를 입력받아, 총점, 평균, 학점, 등수를 계산하고
# 성적 출력, 삽입, 삭제, 탐색, 정렬, 통계를 수행하는 성적 관리 시스템.
# Copyright (C) 2025 Sujin Yoon
# Contact : sujin90d@gmail.com
##################

class Student:
    def __init__(self, student_id, name, eng, c_lang, python_score):
        self.student_id = student_id
        self.name = name
        self.scores = {
            "영어": eng,
            "C-언어": c_lang,
            "파이썬": python_score,
        }
        self.total = 0
        self.average = 0
        self.grade = ''
        self.rank = 0
        self.calculate_total_average_grade()

    def calculate_total_average_grade(self):
        self.total = sum(self.scores.values())
        self.average = self.total / len(self.scores)
        self.grade = self.get_grade()

    def get_grade(self):
        avg = self.average
        if avg >= 90:
            return "A"
        elif avg >= 85:
            return "B+"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def __str__(self):
        return (f"{self.student_id:<15}{self.name:<10}{self.scores['영어']:<10}"
                f"{self.scores['C-언어']:<10}{self.scores['파이썬']:<10}{self.total:<10}"
                f"{self.average:<10.2f}{self.grade:<10}{self.rank:<6}")


class GradeManager:
    def __init__(self):
        self.students = []

    def input_student(self):
        student_id = input("학번: ")
        name = input("이름: ")
        eng = int(input("영어 점수: "))
        c_lang = int(input("C-언어 점수: "))
        python_score = int(input("파이썬 점수: "))
        student = Student(student_id, name, eng, c_lang, python_score)
        self.students.append(student)
        self.calculate_ranks()

    def calculate_ranks(self):
        sorted_students = sorted(self.students, key=lambda s: s.total, reverse=True)
        for i, student in enumerate(sorted_students):
            student.rank = i + 1

    def print_students(self):
        print("\n                              성적관리 프로그램")
        print("=" * 100)
        print(f"{'학번':<13}{'이름':<10}{'영어':<8}{'C-언어':<8}{'파이썬':<8}{'총점':<8}{'평균':<8}{'학점':<8}{'등수':<6}")
        print("=" * 100)
        self.students.sort(key=lambda s: s.total, reverse=True)
        for student in self.students:
            print(student)

    def delete_student(self):
        student_id = input("삭제할 학생의 학번을 입력하세요: ")
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print(f"학번 {student_id}의 학생이 삭제되었습니다.")
                self.calculate_ranks()
                return
        print("해당 학번의 학생을 찾을 수 없습니다.")

    def search_by_id(self):
        student_id = input("검색할 학생의 학번을 입력하세요: ")
        for student in self.students:
            if student.student_id == student_id:
                print(student)
                return
        print("해당 학번의 학생을 찾을 수 없습니다.")

    def search_by_name(self):
        name = input("검색할 학생의 이름을 입력하세요: ")
        for student in self.students:
            if student.name == name:
                print(student)
                return
        print("해당 이름의 학생을 찾을 수 없습니다.")

    def count_students_above_80(self):
        count = sum(1 for student in self.students if student.average >= 80)
        print(f"80점 이상인 학생 수: {count}")


def main():
    manager = GradeManager()

    # 최초 5명 입력
    for _ in range(5):
        manager.input_student()

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
            manager.print_students()
        elif choice == '2':
            manager.input_student()
        elif choice == '3':
            manager.delete_student()
        elif choice == '4':
            manager.search_by_id()
        elif choice == '5':
            manager.search_by_name()
        elif choice == '6':
            manager.count_students_above_80()
        elif choice == '7':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")


if __name__ == "__main__":
    main()
