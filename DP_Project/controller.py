import model
import view

class StrategyContext():
    def __init__(self, strategy):
        self._strategy = strategy
    
    def get_strategy(self):
        return self._strategy

    def set_strategy(self, strategy):
        print("view strategy changed!")
        self._strategy  = strategy
    
    def display_data(self):
        print("context: view selected")
        result = self._strategy.display(data)

    strategy = property(get_strategy, set_strategy)

class Controller(object):
    _instance = None
    def __init__(self, model, view):
        
        self._model = model
        self._view = view
        self._strategyContext = StrategyContext(view)
        self._strategyContext.strategy = self._view
        self._model.attach(self._view)

    #Student View Controller functions
    #one student details
    def show_student_details(self, usn):
        result = self._model.get_student_details(usn)
        if not(result):
            result = [("Enter correct usn!")]

        self._strategyContext.strategy = self._strategyContext.strategy.display_table(result)
        return 'student'

    def show_student_courses(self, usn):
        result = self._model.get_student_courses(usn)
        if not(result):
            result = [("No results found!")]

        
        self._strategyContext.strategy = self._strategyContext.strategy.display_table(result)
        return 'student'

    def show_student_grades(self, usn):
        result = self._model.get_student_grades(usn)
        if not(result):
            result = [("No results found!")]

        self._strategyContext.strategy = self._strategyContext.strategy.display_table(result)
        
        return 'student'
        
    #all students details
    def show_students_details(self):
        result = self._model.get_student_details()
        if not(result):
            result = [("No result found!")]

        self._strategyContext.strategy = self._strategyContext.strategy.display_table(result)
       
        return 'management'

    #add one new student
    def add_new_student(self, student_details):
        result = self._model.add_student_details(student_details)
        if not(result):
            result = [("Something went wrong!")]

        self._strategyContext.strategy = self._strategyContext.strategy.display_table(result)
        
        return 'management'

    #delete one student
    def delete_student(self, usn):
        result = self._model.delete_student_details(usn)
        self._strategyContext.strategy = self._strategyContext.strategy.display_table([("Query output!")])
        return 'management'   

    def show_top_students_details(self):
        result = self._model.get_top_students()
        students = []
        
        if result:
            for row in result:
                students.append(row)

        self._strategyContext.strategy = self._strategyContext.strategy.display_table(result)
        return 'student'

    def show_bottom_students_details(self, number = None, perc = 100):
        result = self._model.get_bottom_students()
        students = []
        if result:
            for row in result:
                students.append(row)
          
        self._strategyContext.strategy = self._strategyContext.strategy.display_table(result)
        return 'student'


    #teacher view related functions
    def show_course_top_students(self, course, number = None, perc = 100):
        result = self._model.get_course_top_students(course)

        students = []
        if result:
            for row in result:
                students.append(row)
        
        self._strategyContext.strategy = self._strategyContext.strategy.display_table(result)
        return 'teacher'

    def show_course_bottom_students(self, course, number = None, perc = 100):
        result = self._model.get_course_bottom_students(course)
        students = []
        if result:
            for row in result:
                students.append(row)
          
        self._strategyContext.strategy = self._strategyContext.strategy.display_table(result)
        return 'teacher'
        
    def show_course_grades(self, course):
        result = self._model.get_course_grades(course)
        if not(result):
            result = [("No student has enrolled !")]

        self._strategyContext.strategy = self._strategyContext.strategy.display_table(result)
        return 'teacher'

    def show_course_students(self, course):
        result = self._model.get_course_students(course)
        if not(result):
            result = [("No student has enrolled !")]

        self._strategyContext.strategy = self._strategyContext.strategy.display_table(result)
        return 'teacher'
    
    @staticmethod
    def createController(dbname, modelname, view):
        if not(Controller._instance) or (Controller._instance._view != view):
            if Controller._instance:
                Controller._instance._model.detach(Controller._instance._view)
            Controller._instance = Controller(model.StudentModel(dbname, modelname), view)
        return Controller._instance
        
