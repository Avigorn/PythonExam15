import json


class Student:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects
        self.grades = {}
        print(f"Создан новый студент: {self.name}")

    def __str__(self):
        return f"Студент: {self.name}\nПредметы: {', '.join(self.subjects)}\nОценки: {self.grades}"

    def load_from_json(self, json_data):
        try:
            self.name = json_data['name']
            self.subjects = json_data['subjects']
            self.grades = json_data.get('grades', {})
            print(f"Студент {self.name} загружен из JSON.")
        except KeyError as e:
            print(f"Ошибка загрузки из JSON: {e}")

    def save_to_json(self, json_file):
        try:
            with open(json_file, 'w') as f:
                json.dump({'name': self.name, 'subjects': self.subjects, 'grades': self.grades}, f, indent=4)
            print(f"Студент {self.name} сохранен в JSON файл {json_file}.")
        except Exception as e:
            print(f"Ошибка сохранения в JSON файл: {e}")

    def add_grade(self, subject, grade):
        try:
            if subject not in self.subjects:
                raise ValueError(f"Предмет {subject} не найден")
            if not isinstance(grade, int) or grade < 2 or grade > 5:
                raise ValueError("Оценка должна быть целым числом от 2 до 5")
            self.grades[subject] = grade
            print(f"Оценка {grade} добавлена к предмету {subject} для студента {self.name}.")
        except ValueError as e:
            print(f"Ошибка добавления оценки: {e}")