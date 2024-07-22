import argparse
import json

from config import config

LOG_FILE = 'app.log'


def log_info(message):
    with open(LOG_FILE, 'a') as f:
        f.write(f"INFO: {message}\n")


def log_error(message):
    with open(LOG_FILE, 'a') as f:
        f.write(f"ERROR: {message}\n")


def display_student(student):
    print(student)


def get_student_data():
    parser = argparse.ArgumentParser(description='Получение данных о студенте из командной строки.')
    parser.add_argument('--name', required=True, help='Имя студента')
    parser.add_argument('--subjects', required=True, help='Список предметов, разделенных запятыми')
    parser.add_argument('--grade', type=int, required=True, help='Оценка')
    args = parser.parse_args()

    subjects_list = args.subjects.split(',')
    student_data = {
        'name': args.name,
        'subjects': subjects_list,
        'grade': args.grade
    }
    log_info(f"Получены данные о студенте: {student_data}")
    return student_data


def save_student_data(student):
    try:
        with open(config['data_file'], 'w') as f:
            json.dump(student.__dict__, f, indent=4)
        log_info(f"Данные о студенте сохранены в файл: {config['data_file']}")
    except Exception as e:
        log_error(f"Ошибка сохранения данных о студенте: {e}")


def get_student_grades():
    parser = argparse.ArgumentParser(description='Получение оценки студента из командной строки.')
    parser.add_argument('--subject', required=True, help='Имя студента')
    parser.add_argument('--grade', type=int, required=True, help='Оценка')
    args = parser.parse_args()
    log_info(f"Получена оценка по предмету: {args.subject}, оценка: {args.grade}")
    return args.subject, args.grade
