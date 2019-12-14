import mydatabase as db

#CRUD operations on StudentGrades table
def get_student_grades(self, usn):
    query =  "SELECT * FROM {TBL_NAME} WHERE usn LIKE '{USN}';".format(TBL_NAME = db.STUDENTGRADES, USN = usn)
    resultProxy = self._connection.execute(query)
    row = resultProxy.fetchall()
    return row

def update_student_grades(self, usn, marks_details):
    self.notify()
    pass

def get_student_courses(self, usn):
    query =  "SELECT course FROM {TBL_NAME} WHERE usn LIKE '{USN}';".format(TBL_NAME = db.STUDENTGRADES, USN = usn)
    resultProxy = self._connection.execute(query)
    row = resultProxy.fetchall()
    return row