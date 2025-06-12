##################
# 프로그램명: Student Grade Manager
# 작성자: 소프트웨어학부 / 윤수진
# 작성일: 2025-04-13
# 5명의 학생 정보를 입력받아, 총점, 평균, 학점, 등수를 계산하고
# 성적 출력, 삽입, 삭제, 탐색, 정렬, 통계를 수행하는 성적 관리 프로그램
# Copyright (C) 2025 Sujin Yoon
# Contact : sujin90d@gmail.com
##################

import mysql.connector

class GradeManager:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="student_db"
        )
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id VARCHAR(20) PRIMARY KEY,
            name VARCHAR(20),
            eng INT,
            c_lang INT,
            python_score INT,
            total INT,
            average FLOAT,
            grade VARCHAR(2),
            rank INT
        )
        """)

    def input_student(self):
        student_id = input("학번: ")
        name = input("이름: ")
        eng = int(input("영어 점수: "))
        c_lang = int(input("C-언어 점수: "))
        python_score = int(input("파이썬 점수: "))
        total = eng + c_lang + python_score
        average = total / 3
        grade = self.get_grade(average)

        sql = """
        INSERT INTO students (student_id, name, eng, c_lang, python_score, total, average, grade)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(sql, (student_id, name, eng, c_lang, python_score, total, average, grade))
        self.conn.commit()
        self.update_ranks()
        print("학생 정보가 성공적으로 저장되었습니다.")

    def get_grade(self, avg):
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

    def update_ranks(self):
        self.cursor.execute("SELECT student_id, total FROM students ORDER BY total DESC")
        students = self.cursor.fetchall()
        for i, (student_id, _) in enumerate(students, start=1):
            self.cursor.execute("UPDATE students SET rank = %s WHERE student_id = %s", (i, student_id))
        self.conn.commit()

    def print_students(self):
        self.cursor.execute("SELECT student_id, name, eng, c_lang, python_score, total, average, grade, rank FROM students ORDER BY total DESC")
        students = self.cursor.fetchall()
        print("\n                              성적관리 프로그램")
        print("=" * 100)
        print(f"{'학번':<13}{'이름':<10}{'영어':<8}{'C-언어':<8}{'파이썬':<8}{'총점':<8}{'평균':<8}{'학점':<8}{'등수':<8}")
        print("=" * 100)
        for row in students:
            print(f"{row[0]:<13}{row[1]:<10}{row[2]:<8}{row[3]:<8}{row[4]:<8}{row[5]:<8}{row[6]:<8.2f}{row[7]:<8}{row[8]:<8}")

    def delete_student(self):
        student_id = input("삭제할 학생의 학번을 입력하세요: ")
        self.cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
        self.conn.commit()
        if self.cursor.rowcount > 0:
            self.update_ranks()
            print(f"학번 {student_id}의 학생이 삭제되었습니다.")
        else:
            print("해당 학번의 학생을 찾을 수 없습니다.")

    def search_by_id(self):
        student_id = input("검색할 학생의 학번을 입력하세요: ")
        self.cursor.execute("""
            SELECT student_id, name, eng, c_lang, python_score, total, average, grade, rank 
            FROM students WHERE student_id = %s
        """, (student_id,))
        student = self.cursor.fetchone()
        if student:
            print(student)
        else:
            print("해당 학번의 학생을 찾을 수 없습니다.")

    def search_by_name(self):
        name = input("검색할 학생의 이름을 입력하세요: ")
        self.cursor.execute("""
            SELECT student_id, name, eng, c_lang, python_score, total, average, grade, rank 
            FROM students WHERE name = %s
        """, (name,))
        students = self.cursor.fetchall()
        if students:
            for student in students:
                print(student)
        else:
            print("해당 이름의 학생을 찾을 수 없습니다.")

    def count_students_above_80(self):
        self.cursor.execute("SELECT COUNT(*) FROM students WHERE average >= 80")
        count = self.cursor.fetchone()[0]
        print(f"80점 이상인 학생 수: {count}")

    def close(self):
        self.cursor.close()
        self.conn.close()


def main():
    manager = GradeManager()

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
            manager.close()
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")


if __name__ == "__main__":
    main()