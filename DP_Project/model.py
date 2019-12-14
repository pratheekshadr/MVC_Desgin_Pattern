import mydatabase as db

from abc import ABC, abstractmethod

import student_table_queries as stdq
import grades_table_queries as gradeq
import course_queries as courseq

#interface
class Model(ABC):

    #attach observer to the model
    @abstractmethod
    def attach(self, observer):
        pass

    #detach observer from the model
    @abstractmethod
    def detach(self, observer):
        pass
    
    #notify all observers about the update
    @abstractmethod
    def notify(self):
        pass

#StudentModel
class StudentModel(Model):
    def __init__(self, dbname, model_name):
        self._dbms = db.MyDatabase(dbname)
        self._connection = self._dbms.get_db_connection()
        self._name = model_name
        self._observers = []

    #observer pattern related methods
    def attach(self, observer):
        print("Observer: ", observer._name, "attached")
        self._observers.append(observer)
    
    def detach(self, observer):
        print("Observer: ", observer._name, "detached")
        self._observers.remove(observer)

    def notify(self):
        print("Notifying observers")
        for observer in self._observers:
            observer.update(self)

    #CRUD operations on StudentDetails table
    def get_student_details(self, usn = None):
        return stdq.get_student_details(self, usn)

    def add_student_details(self, student_details):
        return stdq.add_student_details(self, student_details)

    def delete_student_details(self, usn):
        return stdq.delete_student_details(self, usn)

    def update_student_details(self, usn, student_details):
        stdq.update_student_details(self, usn, student_details)


    #other queries on StudentDetails table
    def get_top_students(self):
        return stdq.get_top_students(self)

    def get_bottom_students(self):
        return stdq.get_bottom_students(self)


    #CRUD operations on StudentGrades table
    def get_student_grades(self, usn):
        return gradeq.get_student_grades(self, usn)

    def get_student_courses(self, usn):
        return gradeq.get_student_courses(self, usn)

    #course relates queries
    def get_course_students(self, course):
        return courseq.get_course_students(self, course)

    def get_course_grades(self, course):
        return courseq.get_course_grades(self, course)

    def get_course_top_students(self, course):
        return courseq.get_course_top_students(self, course)  
       
    def get_course_bottom_students(self, course):
        return courseq.get_course_bottom_students(self, course)



