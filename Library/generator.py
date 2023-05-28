import random


class Generator:
    @staticmethod
    def generate_email(student, students, domen):
        dup_count = 0
        for stud in students:
            if student == stud:
                dup_count += 1
        message = (
            f"{student.name}.{student.surname}{dup_count}.y{domen}"
            if dup_count != 0
            else f"{student.name}.{student.surname}{domen}"
        )

        return message

    @staticmethod
    def generate_id():
        _id = ""
        for i in range(12):
            _id += str(random.randint(0, 1000))

        return _id[:12]
