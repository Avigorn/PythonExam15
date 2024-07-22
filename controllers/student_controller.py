from models.student import Student
from views.student_view import display_student, get_student_data, save_student_data

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_student():
    try:
        student_data = get_student_data()
        logging.info(f"Получены данные о студенте: {student_data}")

        student = Student(student_data['name'], student_data['subjects'])
        logging.info(f"Создан объект студента: {student}")

        student.add_grade(student_data['subjects'], student_data['grade'])
        logging.info(f"Добавлена оценка к студенту: {student}")

        save_student_data(student)
        logging.info(f"Данные о студенте сохранены: {student}")

        display_student(student)
        logging.info(f"Информация о студенте отображена: {student}")

    except Exception as e:
        logging.error(f"Произошла ошибка во время создания студента: {e}")

if __name__ == "__main__":
    create_student()