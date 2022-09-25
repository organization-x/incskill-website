import copy

class Course:
    courseName = ""
    complete = 0.0
    units = []
    all_courses = []

    def __init__(self, courseName, units):
        self.courseName = courseName
        self.units = units
        Course.all_courses.append(self)
    
    def __init__(self, courseName):
        self.courseName = courseName
        Course.all_courses.append(self)

    def chg_name(self, courseName):
        self.courseName = courseName
    
    def print(self):
        print(self.courseName)

    def add_unit(self, unit):
        if type(unit) is Unit:
            self.units.append(copy.copy(unit))

    def find_course(courseName):
        for course in Course.all_courses:
            if course.courseName == courseName:
                return course



class Unit:
    complete = 0.0
    unitName = ""
    modules = []
    all_units = []

    def __init__(self, unitName, modules):
        self.unitName = unitName
        self.modules = modules
        Unit.all_units.append(self)

    def __init__(self, unitName):
        self.unitName = unitName
        Unit.all_units.append(self)

    def add_module(self, module):
        if type(module) is Module:
            self.modules.append(copy.copy(module))   

    def find_unit(unitName):
        for unit in Unit.all_units:
            if unit.unitName == unitName:
                return unit

class Module:
    complete = False
    modName = ""
    mod_type = ""
    all_modules = []

    def __init__(self, modName, mod_type):
        self.modName = modName
        self.mod_type = mod_type
        Module.all_modules.append(self)

    def find_module(modName):
        for module in Module.all_modules:
            if module.modName == modName:
                return module

    def complete(self):
        self.complete = True


class Quiz(Module):
    questions = []
    def __init__(self, modName, mod_type):
        super().__init__(modName, "quiz")

    def add_question(self, question):
        if type(question) is Question:
            self.questions.append(question)




class Question:
    qName = ""
    ques = ""
    ans = ""
    a = ""
    b = ""
    c = ""
    d = ""
    all_questions = []
    def __init__(self, name, ques, ans, a, b, c, d):
        self.qName = name
        self.ques = ques
        self.ans = ans
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        Question.all_questions.append(self)
    
    def find_ques(qName):
        for q in Question.all_questions:
            if q.qName == qName:
                return q
