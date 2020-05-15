from bussiness.Type import UserType


class Person:

    id = 0
    name = ""
    user_type: UserType = None
    email = ""
    password = ""

    def __init__(self, id, name, user_type, email, password):
        self.id = id
        self.name = name
        self.user_type = user_type
        self.email = email
        self.password = password

    @classmethod
    def new_student(cls, id, name, email, password):
        return cls(id, name, UserType.STUDENT, email, password)

    @classmethod
    def new_teacher(cls, id, name, email, password):
        return cls(id, name, UserType.TEACHER, email, password)
