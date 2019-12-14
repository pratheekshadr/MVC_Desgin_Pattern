import mydatabase as db
from random import randint
#CRUD operations on StudentDetails table
def get_student_details(self, usn = None):
    if usn == None:
        query =  "SELECT * FROM {TBL_NAME};".format(TBL_NAME = db.STUDENTDETAILS)
    else:
        query =  "SELECT * FROM {TBL_NAME} WHERE usn LIKE '{USN}';".format(TBL_NAME = db.STUDENTDETAILS, USN = usn)
    try:
        resultProxy = self._connection.execute(query)
        row = resultProxy.fetchall()
        return row
    except:
        return 0

def add_student_details(self, student_details):
    query1 = "INSERT INTO {TBL_NAME} values {ROW};".format(TBL_NAME = db.STUDENTDETAILS, ROW = student_details)
    course_code_prefix = str(student_details[3]) + '0' +str(student_details[2])
    marks = randint(0,100)
    try:
        resultProxy = self._connection.execute(query1)
        for i in range(5):
            course_code = course_code_prefix + '0' + str(i)
            resultProxy = self._connection.execute("INSERT INTO {TBL_NAME} values {ROW};".format(TBL_NAME = db.STUDENTGRADES, 
                                                            ROW = (student_details[0], course_code, marks)))
        self.notify()
        return 1 
    except:
        return 0

def delete_student_details(self, usn):
    query1 = "DELETE FROM {TBL_NAME} WHERE usn LIKE '{USN}';".format(TBL_NAME = db.STUDENTDETAILS, USN = usn)
    query2 = "DELETE FROM {TBL_NAME} WHERE usn LIKE '{USN}';".format(TBL_NAME = db.STUDENTGRADES, USN = usn)
    resultProxy = self._connection.execute(query1)
    resultProxy = self._connection.execute(query2)
    self.notify()
    return 1

def update_student_details(self, usn, student_details):
    self.notify()


#other queries
def get_top_students(self):
    query =  "SELECT * FROM {TBL_NAME} ORDER BY gpa DESC;".format(TBL_NAME = db.STUDENTDETAILS)
    try:
        resultProxy = self._connection.execute(query)
        row = resultProxy.fetchall()
        return row
    except:
        return 0

def get_bottom_students(self):
    query =  "SELECT * FROM {TBL_NAME} ORDER BY gpa ;".format(TBL_NAME = db.STUDENTDETAILS)
    try:
        resultProxy = self._connection.execute(query)
        row = resultProxy.fetchall()
        return row
    except:
        return 0
