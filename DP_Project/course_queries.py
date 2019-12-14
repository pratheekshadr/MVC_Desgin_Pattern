import mydatabase as db

#course relates queries
def get_course_students(self, course):
    query = " SELECT studentT.usn, studentT.name" \
            " FROM {TBL_NAME1} as gradeT LEFT JOIN {TBL_NAME2} as studentT " \
            " WHERE course LIKE '{COURSE}' AND gradeT.usn == studentT.usn; ".format(TBL_NAME1 = db.STUDENTGRADES, TBL_NAME2 = db.STUDENTDETAILS,  COURSE = course)
    
    try:
        resultProxy = self._connection.execute(query)
        row = resultProxy.fetchall()
        return row
    except:
        return 0

def get_course_grades(self, course):
    query = " SELECT studentT.usn, studentT.name, gradeT.grade " \
            " FROM {TBL_NAME1} as gradeT LEFT JOIN {TBL_NAME2} as studentT " \
            " WHERE course LIKE '{COURSE}' AND gradeT.usn == studentT.usn; ".format(TBL_NAME1 = db.STUDENTGRADES, TBL_NAME2 = db.STUDENTDETAILS,  COURSE = course)
    
    try:
        resultProxy = self._connection.execute(query)
        row = resultProxy.fetchall()
        return row
    except:
        return 0


def get_course_top_students(self, course):
    query = " SELECT studentT.usn, studentT.name, gradeT.grade" \
            " FROM {TBL_NAME1} as gradeT LEFT JOIN {TBL_NAME2} as studentT " \
            " WHERE course LIKE '{COURSE}' AND gradeT.usn == studentT.usn " \
            " ORDER BY gradeT.grade DESC, studentT.gpa DESC; ".format(TBL_NAME1 = db.STUDENTGRADES, TBL_NAME2 = db.STUDENTDETAILS,  COURSE = course)

    try:
        resultProxy = self._connection.execute(query)
        row = resultProxy.fetchall()
        return row
    except:
        return 0


def get_course_bottom_students(self, course):
    query = " SELECT studentT.usn, studentT.name, gradeT.grade" \
            " FROM {TBL_NAME1} as gradeT LEFT JOIN {TBL_NAME2} as studentT " \
            " WHERE course LIKE '{COURSE}' AND gradeT.usn == studentT.usn " \
            " ORDER BY gradeT.grade , studentT.gpa ; ".format(TBL_NAME1 = db.STUDENTGRADES, TBL_NAME2 = db.STUDENTDETAILS,  COURSE = course)
    try:
        resultProxy = self._connection.execute(query)
        row = resultProxy.fetchall()
        return row
    except:
        return 0
