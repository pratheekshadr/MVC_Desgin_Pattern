from flask import Flask, render_template, request, redirect
app = Flask(__name__) 

from view import ConcreteView as view 
from controller import Controller

global ctrl
ctrl = None



@app.route('/') 
def home():
    global ctrl 
    ctrl = None
    home_view = view('firstPage')
    home_view.create_home_view()
    return render_template('firstPage.html')

@app.route('/studentView')
def studentView():
    global ctrl
    if ctrl == None:
        print("router: student view created")
        std_view = view('student')
        std_view.create_student_view()

        dbname = 'student.sqlite'
        modelname = 'teachermodel'
        ctrl = Controller.createController(dbname, modelname, std_view)
    return render_template('student.html')

@app.route('/studentView/getMyGrades', methods=['GET'])
def getMyGrades():
    global ctrl
    usn = request.args.get('usn', type = str)
    result = ctrl.show_student_grades(usn)
    return result

@app.route('/studentView/getMyProfile', methods=['GET'])
def getMyProfile():
    global ctrl
    usn = request.args.get('usn', type = str)
    result = ctrl.show_student_details(usn)
 
    return result

@app.route('/studentView/getMyCourses', methods=['GET'])
def getMyCourses():
    global ctrl
    usn = request.args.get('usn', type = str)
    result = ctrl.show_student_courses(usn)
    return result

@app.route('/display/student')
def student():
    return redirect('/studentView')

#teacher view methods
@app.route('/teacherView')
def teacherView():
    global ctrl
    if ctrl == None:
        print("router: teacher view created")
        teach_view = view('teacher')
        teach_view.create_teacher_view()

        dbname = 'student.sqlite'
        modelname = 'teachermodel'
        ctrl = Controller.createController(dbname, modelname, teach_view)
    
    return render_template('teacher.html')


@app.route('/teacherView/getCourseStudents')
def getCourseStudents():
    global ctrl
    course = request.args.get('courseId', type = str)
    result = ctrl.show_course_students(course)
    return result

@app.route('/teacherView/getCourseGrades', methods=['GET'])
def getCourseGrades():
    global ctrl
    course = request.args.get('courseId', type = str)
    result = ctrl.show_course_grades(course)
    return result

@app.route('/teacherView/getCourseTopStudents', methods=['GET'])
def getCourseTopStudents():
    global ctrl
    course = request.args.get('courseId', type = str)
    result = ctrl.show_course_top_students(course) 
    return result

@app.route('/teacherView/getCourseBottomStudents', methods=['GET'])
def getCourseBottomStudents():
    global ctrl
    course = request.args.get('courseId', type = str)
    result = ctrl.show_course_bottom_students(course)
    return result

@app.route('/display/teacher')
def teacher():
    return redirect('/teacherView')

#management view methods
@app.route('/managementView')
def managementView():
    global ctrl
    if ctrl == None:
        print("router: management view created")
        mng_view = view('management')
        mng_view.create_management_view()

        dbname = 'student.sqlite'
        modelname = 'managementModel'
        ctrl = Controller.createController(dbname, modelname, mng_view)

    return render_template('management.html')

@app.route('/managementView/getAllStudents', methods=['GET'])
def getAllStudents():
    global ctrl
    result = ctrl.show_students_details()
    return result

@app.route('/managementView/getTopStudents', methods=['GET'])
def getTopStudents():
    global ctrl
    result = ctrl.show_top_students_details()
    return result

@app.route('/managementView/getBottomStudents', methods=['GET'])
def getBottomStudents():
    global ctrl
    result = ctrl.show_bottom_students_details()
    return result

@app.route('/managementView/addStudent', methods=['GET'])
def addStudent():
    global ctrl
    usn = request.args.get('usn')
    name = request.args.get('name')
    sem = request.args.get('sem')
    branch = request.args.get('branch')
    sec = request.args.get('sec')
    gpa = request.args.get('gpa')


    student_details = (usn, name, sem, branch, sec, gpa)
    result = ctrl.add_new_student(student_details)

    return result

@app.route('/managementView/deleteStudent', methods=['GET'])
def deleteStudent():
    global ctrl
    usn = request.args.get('usn', type = str)
    result = ctrl.delete_student(usn)
    #display in proper format on the webpage
    return result

@app.route('/display/management')
def management():
    return redirect('/managementView')

if __name__ == '__main__': 
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True  
    app.run(debug=True)

