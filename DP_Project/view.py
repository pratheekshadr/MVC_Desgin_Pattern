from abc import ABC, abstractmethod
import os

import requests
#interface
class View(ABC):
    @abstractmethod
    def update(self, subject):
        pass
    @abstractmethod
    def display_view(self):
        pass

class ConcreteView(View):
    def __init__(self, name):
        self._name = name    
        self._fp = "templates/" +name+ ".html"
        with open(self._fp, 'w+') as fo:
            fo.close()
        self._composite = Composite('html', self._fp)
      

    def update(self, subject):
        print("Update is called on Observer: " , self._name, "from subject: ", subject._name)
        child_list = []
        for child in self._body._children:
            child_list.append(child)

        for child in child_list:
            self._body.remove(child)
        
        js = ' var c = document.getElementById("result");c.innerHTML = "Query Output";' 
        alert =' alert("result has changed! Please query again to get updated information!");'

        result = Leaf('script ', self._fp,  js+alert )
        self._body.add(result)
        self.display_view()
        url = 'http://localhost:5000/display/'+self._name
        requests.get(url)
       

    def create_home_view(self):
        composite1 = Composite('body', self._fp)
        c1 = Composite('div', self._fp)

        l1 = Leaf('button', self._fp, 'Student View', "api_call('http://localhost:5000/studentView')")
        l2 = Leaf('button', self._fp, 'Professor View',"api_call('http://localhost:5000/teacherView')")
        l3 = Leaf('button', self._fp, 'Management View',"api_call('http://localhost:5000/managementView')")

        c1.add(l1)
        c1.add(l2)
        c1.add(l3)

        c2 = Leaf('h1', self._fp, 'WELCOME!!')

        composite1.add(c2)
        composite1.add(c1)

        api_call = "function api_call(api) { window.location = api; }"
        script = Leaf('script', self._fp, api_call)

        composite1.add(script)
       
        self._composite.add(composite1)
        self._body = composite1
        self.display_view()

    #creates html page for student view using compostie design pattern
    def create_student_view(self):
        composite1 = Composite('body style="margin-top:50px;margin-left:50px;"', self._fp)
        c1 = Leaf('h1 style="position: absolute;top:10;margin-left:500px;"', self._fp, 'Student View')
        
        c2 = Composite('div', self._fp)
        l1 = Leaf('button', self._fp, 'My Grades', "api_call('http://localhost:5000/studentView/getMyGrades')")
        l2 = Leaf('button', self._fp, 'My Profile',"api_call('http://localhost:5000/studentView/getMyProfile')")
        l3 = Leaf('button', self._fp,'My Courses',"api_call('http://localhost:5000/studentView/getMyCourses')")
        l4 = Leaf('input type="text" id="usn" placeholder="usn"', self._fp, 'Enter USN') 

        c2.add(l1)
        c2.add(l2)
        c2.add(l3)
        c2.add(l4)

        composite1.add(c1)
        composite1.add(c2)

        resultdiv = Composite('div id="result" style="background-color:grey;padding:50px;position:absolute;bottom:100;height:100px;overflow-y:scroll;"', self._fp)
        
        result = Leaf('script ', self._fp,  ' var c = document.getElementById("result");c.innerHTML = "Query Output";' )
        resultdiv.add(result)
        
        api_call = "function api_call(api){var c = document.getElementById('usn');var usn =c.value;var request = new XMLHttpRequest();request.open('GET', api+'?usn='+usn, true);request.send(); window.location ='/display/student'; }"
        script = Leaf('script', self._fp, api_call)

        composite1.add(script)
        composite1.add(resultdiv)

        self._composite.add(composite1)
        self._body = resultdiv
        self.display_view()

    #creates html page for teacher view using compostie design pattern
    def create_teacher_view(self):
        composite1 = Composite('body style="margin-top:50px;margin-left:50px;"', self._fp)
        c1 = Leaf('h1 style="position: absolute;top:10;margin-left:500px;"', self._fp, 'Teacher View')
        
        c2 = Composite('div', self._fp)
        l1 = Leaf('button', self._fp,'Bottom Students',"api_call('http://localhost:5000/teacherView/getCourseBottomStudents')")
        l2 = Leaf('button', self._fp,'Top Students',"api_call('http://localhost:5000/teacherView/getCourseTopStudents')")
        c2.add(l1)
        c2.add(l2)
        

        c3 = Composite('div', self._fp)
        l3 = Leaf('input type="text" id="courseId" placeholder="courseId"', self._fp, 'Enter CourseId')
        l4 = Leaf('button',  self._fp, 'Course Students', "api_call('http://localhost:5000/teacherView/getCourseStudents')")
        l5 = Leaf('button', self._fp, 'Course Grades',"api_call('http://localhost:5000/teacherView/getCourseGrades')")

        c3.add(l3)
        c3.add(l4)
        c3.add(l5)
        composite1.add(c1)
        composite1.add(c2)
        composite1.add(c3)
        
        resultdiv = Composite('div id="result" style="background-color:grey;padding:50px;position:absolute;bottom:100;height:100px;overflow-y:scroll;"', self._fp)
        
        result = Leaf('script ', self._fp,  ' var c = document.getElementById("result");c.innerHTML = "Query Output";' )
        resultdiv.add(result)

        api_call = "function api_call(api){var c = document.getElementById('courseId');var courseId =c.value;var request = new XMLHttpRequest();request.open('GET', api+'?courseId='+courseId, true);request.send(); window.location ='/display/teacher';}"
        script = Leaf('script', self._fp, api_call)

        composite1.add(script)
        composite1.add(resultdiv)
       
        self._composite.add(composite1)
        self._body = resultdiv
        self.display_view()
    
    #creates html page for management view using compostie design pattern
    def create_management_view(self):
        composite1 = Composite('body style="margin-top:50px;margin-left:50px;"', self._fp)
        c1 = Leaf('h1 style="position: absolute;top:10;margin-left:500px;"', self._fp, 'Management View')
        
        c2 = Composite('div', self._fp)
        l1 = Leaf('button',  self._fp, 'GetAllStudents', "api_call('http://localhost:5000/managementView/getAllStudents')")
        l2 = Leaf('button', self._fp, 'GetTopStudents',"api_call('http://localhost:5000/managementView/getTopStudents')")
        l3 = Leaf('button', self._fp,'GetBottomStudents',"api_call('http://localhost:5000/managementView/getBottomStudents')")

        c2.add(l1)
        c2.add(l2)
        c2.add(l3)

        c3 = Composite('div', self._fp)
        l4 = Leaf('button', self._fp,'AddStudent',"api_call('http://localhost:5000/managementView/addStudent')")
        l5 = Leaf('button', self._fp,'DeleteStudent',"api_call('http://localhost:5000/managementView/deleteStudent')")

        lusn = Leaf('input type="text" id="usn" placeholder="usn"', self._fp, 'Enter USN') 
        lname = Leaf('input type="text" id="name" placeholder="name"', self._fp, 'Enter NAME') 
        lsem = Leaf('input type="text" id="sem" placeholder="sem"', self._fp, 'Enter SEM') 
        lbranch = Leaf('input type="text" id="branch" placeholder="branch"', self._fp, 'Enter BRANCH') 
        lsec = Leaf('input type="text" id="sec" placeholder="sec"', self._fp, 'Enter SEC') 
        lgpa = Leaf('input type="text" id="gpa" placeholder="gpa"', self._fp, 'Enter GPS') 

        c3.add(l4)
        c3.add(l5)
        c3.add(lusn)
        c3.add(lname)
        c3.add(lsem)
        c3.add(lbranch)
        c3.add(lsec)
        c3.add(lgpa)

        composite1.add(c1)
        composite1.add(c2)
        composite1.add(c3)


        addusn = "var c = document.getElementById('usn'); usn = c.value;"
        addname = "var c = document.getElementById('name'); name = c.value;"
        addsem = "var c = document.getElementById('sem'); sem = c.value;"
        addbranch = "var c = document.getElementById('branch'); branch = c.value;"
        addsec = "var c = document.getElementById('sec'); sec = c.value;"
        addgpa = "var c = document.getElementById('gpa'); gpa = c.value;"
        
        api = "api+'?usn='+usn+'&name='+name+'&sem='+sem+'&branch='+branch+'&sec='+sec+'&gpa='+gpa"
        api_path = "var api_path="+api+";"
        getValues = addusn + addname + addsem+ addbranch + addsec + addgpa + api_path

        resultdiv = Composite('div id="result" style="background-color:grey;padding:50px;position:absolute;bottom:100;margin-left:500px;height:200px;overflow-y:scroll;"', self._fp)
        
        result = Leaf('script ', self._fp,  ' var c = document.getElementById("result");c.innerHTML = "Query Output";' )
        resultdiv.add(result)

        api_call = "function api_call(api){" + getValues + "var request = new XMLHttpRequest();request.open('GET', api_path, true);request.send(); window.location ='/display/management';}"
        script = Leaf('script', self._fp, api_call)
        composite1.add(script)
        composite1.add(resultdiv)
    
        self._composite.add(composite1)
        self._body = resultdiv
        self.display_view()
    
    def display_view(self):
        with open(self._fp, 'w') as fo:
            pass
        fo.close()
        self._composite.display()

    def display_table(self, result):
        child_list = []
        for child in self._body._children:
            child_list.append(child)

        for child in child_list:
            self._body.remove(child)
        
        values = result
        innerHTML = ''
        for row in result:
            innerHTML += str(row) + '<br>'
        result = Leaf('script ', self._fp,  ' var c = document.getElementById("result");c.innerHTML = "'+ innerHTML +'";' )
        self._body.add(result)
        self.display_view()
        return self

#interface
class Component(ABC):
    @abstractmethod
    def display(self):
        pass

class Composite(Component):
    def __init__(self, tag, fp, value = '', onclick = 'void(0)'):
        self._tag = tag
        self._children = set()
        self._value = value
        self._onclick = onclick
        self._fp = fp


    def display(self):
        str = '<' + self._tag + ' onclick = "' + self._onclick + ' "> ' 
        with open(self._fp, 'a') as fo:
            fo.writelines(str)
        fo.close()

        for child in self._children:
            child.display()
        str = '</' + self._tag + '>';  
        with open(self._fp, 'a') as fo:
            fo.writelines(str)
        fo.close()

    def add(self, component):
        self._children.add(component)
    
    def remove(self, component):
        self._children.discard(component)


class Leaf(Component):
    def __init__(self, tag, fp, value = '', onclick = 'void(0)'):
        self._tag = tag
        self._value = value
        self._onclick = onclick
        self._fp = fp

    def display(self):
        str = ' <' + self._tag + ' onclick = "' + self._onclick + ' "> ' + self._value + ' </' + self._tag + ' > <br><br>';  
        with open(self._fp, 'a') as fo:
            fo.writelines(str)
        fo.close()
       
