from bussiness.entity.Person import Person


class Form:

    id = 0
    creator: Person = None
    title = ""
    questions = []
    completed = False
    create_date = ""

    def __init__(self, id, creator: Person, title, questions, completed, create_date):
        self.id = id
        self.creator = creator
        self.title = title
        self.questions = questions
        self.completed = completed
        self.create_date = create_date


class AnsweredForm(Form):

    student: Person = None
    answers = []

    def __init__(self, id, creator: Person, student: Person, title, questions, answers, create_date):
        super().__init__(id, creator, title, questions, True, create_date)
        self.student = student
        self.answers = answers
