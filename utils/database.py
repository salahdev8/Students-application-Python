import sqlite3



def create_tables():

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS ADMIN(adminId integer primary key,accountType text,'
                   'adminName text, adminEmail text, adminPassword text)')

    cursor.execute('CREATE TABLE IF NOT EXISTS TEACHER(teacherId integer primary key,accountType text,'
                   'teacherFirstName text,teacherLastName text, teacherEmail text, teacherPassword text)')

    cursor.execute('CREATE TABLE IF NOT EXISTS STUDENT(studentId integer primary key,accountType text,'
                   'studentFirstName text,studentLastName text, studentEmail text, studentPassword text,'
                   ' firstcourse text, secondcourse text, thirdcourse text)')

    cursor.execute('CREATE TABLE IF NOT EXISTS COURSE(courseId integer primary key,courseLevel text,'
                   'courseName text, courseLocation text, courseTeacher integer,'
                   'FOREIGN KEY(courseTeacher) REFERENCES TEACHER(teacherId))')

    cursor.execute('CREATE TABLE IF NOT EXISTS ASSIGNMENT(assignmentId integer primary key,assignmentCourse integer,'
                   'assignmentName text, assignmentFilePath text,'
                   'FOREIGN KEY(assignmentCourse) REFERENCES COURSE(courseId))')

    cursor.execute('CREATE TABLE IF NOT EXISTS COURSEFILE(fileId integer primary key,fileCourse integer,'
                   'fileChapter text, filePath text,'
                   'FOREIGN KEY(fileCourse) REFERENCES COURSE(courseId))')

    cursor.execute('CREATE TABLE IF NOT EXISTS GRADES(gradeId integer primary key,gradeStudentId integer,'
                   'gradeAssignmentId integer,gradeValue integer, gradeComment text,'
                   'FOREIGN KEY(gradeStudentId) REFERENCES STUDENT(studentId),FOREIGN KEY(gradeAssignmentId) '
                   'REFERENCES ASSIGNMENT(assignmentId))')

    cursor.execute('CREATE TABLE IF NOT EXISTS ANNOUNCEMENT(announcementId integer primary key,announcementCourse '
                   'integer, announcementTitle text, announcementDescription text,'
                   'FOREIGN KEY(announcementCourse) REFERENCES COURSE(courseId))')

    connection.commit()
    connection.close()


def login_admin(word):

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute("Select accountType "
                   "from ADMIN where adminEmail=?", (word,))

    var=cursor.fetchone()

    cursor.close()

    if(var is None):
        return "doesnt exist"
    else:
        return var[0]



def login_teacher(word):

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute("Select accountType from TEACHER where teacherEmail=?", (word,))

    var=cursor.fetchone()

    cursor.close()

    if (var is None):
        return "doesnt exist"
    else:
        return var[0]

def login_student(word):

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute("Select accountType "
                   "from STUDENT where studentEmail=?", (word,))

    var=cursor.fetchone()

    cursor.close()

    if (var is None):
        return "doesnt exist"
    else:
        return var[0]



def create_user(type,fname,lname,email,password):

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    if (type == "teacher"):
        cursor.execute('INSERT INTO TEACHER(accountType,teacherFirstName,teacherLastName,'
                       'teacherEmail,teacherPassword) values(?,?,?,?,?)', (type, fname, lname, email, password))

    elif (type == "student"):
        cursor.execute('INSERT INTO STUDENT(accountType,studentFirstName,studentLastName,'
                       'studentEmail,studentPassword) values(?,?,?,?,?)', (type, fname, lname, email, password))

    else:
        print("error data not correct")

    connection.commit()
    connection.close()



def create_course(cname,clevel,clocation):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO COURSE(courseLevel,courseName,courseLocation'
                   ') values(?,?,?)', (clevel, cname, clocation))

    connection.commit()
    connection.close()


#select names of courses and put them in a tuple

def select_courses():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()


    cursor.execute('SELECT courseName from COURSE')

    result=cursor.fetchall()
    ourtuple=[]
    for ele in result:
        ourtuple.append(ele[0])

    connection.commit()
    connection.close()

    return tuple(ourtuple)

#select names of assignment from a specific course and put them in a tuple

def select_assignment(cid):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT assignmentName from ASSIGNMENT where assignmentCourse=?',(cid,))

    result=cursor.fetchall()
    ourtuple=[]
    for ele in result:
        ourtuple.append(ele[0])

    connection.commit()
    connection.close()

    return tuple(ourtuple)

#select names of assignment from a specific course and put them in a tuple

def select_student_from_course(cname):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT studentFirstName from STUDENT where firstcourse=? OR secondcourse=? OR thirdcourse=?',(cname,cname,cname))

    result=cursor.fetchall()
    ourtuple=[]
    for ele in result:
        ourtuple.append(ele[0])

    connection.commit()
    connection.close()

    return tuple(ourtuple)

#select names of teachers and put them in a tuple

def select_teachers():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()


    cursor.execute('SELECT teacherFirstName from TEACHER')

    result=cursor.fetchall()

    ourtuple = []
    for ele in result:
        ourtuple.append(ele[0])

    connection.commit()
    connection.close()

    return tuple(ourtuple)

#select names of students and put them in a tuple

def select_students():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()


    cursor.execute('SELECT studentFirstName from STUDENT')

    result=cursor.fetchall()

    ourtuple = []
    for ele in result:
        ourtuple.append(ele[0])

    connection.commit()
    connection.close()

    return tuple(ourtuple)


#return id of teacher

def teacher_id(tname):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT teacherId from TEACHER where teacherFirstName=?',(tname,))

    result = cursor.fetchall()

    connection.commit()
    connection.close()

    return result[0][0]

#return id of course

def course_id(cname):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT courseId from COURSE where courseName=?',(cname,))

    result = cursor.fetchall()

    connection.commit()
    connection.close()

    return result[0][0]

#return id of student

def student_id(sname):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT studentId from STUDENT where studentFirstName=?',(sname,))

    result = cursor.fetchall()

    connection.commit()
    connection.close()

    return result[0][0]

#return id of assignement

def assignment_id(assname):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT assignmentId from ASSIGNMENT where assignmentName=?',(assname,))

    result = cursor.fetchall()

    connection.commit()
    connection.close()

    return result[0][0]



#assign a teahcer to a course

def assign_Teacher(cname,tname):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    tid=teacher_id(tname)

    cursor.execute('update COURSE set courseTeacher=? where courseName=?', (tid,cname))

    connection.commit()
    connection.close()

#add 3 courses to a student

def add_courses_to_student(sname,fcourse,scourse,tcourse):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()


    cursor.execute('update STUDENT set firstcourse=?,secondcourse=?,thirdcourse=? where studentFirstName=?',
                   (fcourse,scourse,tcourse,sname))

    connection.commit()
    connection.close()


#insert course file

def inser_course_file(courseId, chapter, fpath):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO COURSEFILE(fileCourse, fileChapter, filePath'
                   ') values(?,?,?)', (courseId, chapter, fpath))

    connection.commit()
    connection.close()

#insert asssignement file

def inser_Assignment_file(courseId, assignemt, fpath):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO ASSIGNMENT(assignmentCourse, assignmentName, assignmentFilePath'
                   ') values(?,?,?)', (courseId, assignemt, fpath))

    connection.commit()
    connection.close()

#diplay assignment data

def display_assignments(cname):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * from ASSIGNMENT where assignmentCourse=?',(cname,))
    result=cursor.fetchall()

    connection.commit()
    connection.close()

    if(result):
        return result
    else:
        return None

#add grade for student
def add_grade(studId,assignId,value,comment):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO GRADES(gradeStudentId, gradeAssignmentId, gradeValue, gradeComment'
                   ') values(?,?,?,?)', (studId, assignId, value,comment))

    connection.commit()
    connection.close()

#add announcement

def add_announce(cid,title,descr):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO ANNOUNCEMENT(announcementCourse, announcementTitle, announcementDescription'
                   ') values(?,?,?)', (cid, title, descr))

    connection.commit()
    connection.close()

#return all announcements

def show_announce(cid):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * from ANNOUNCEMENT where announcementCourse=? ',(cid,))
    result = cursor.fetchall()

    connection.commit()
    connection.close()

    return result


#select names of courses and put them in a tuple

def select_course_file(cid):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()


    cursor.execute('SELECT fileChapter from COURSEFILE where fileCourse=?',(cid,))

    result=cursor.fetchall()
    ourtuple=[]
    for ele in result:
        ourtuple.append(ele[0])

    connection.commit()
    connection.close()

    return tuple(ourtuple)

#select names of assignments and put them in a tuple

def select_assignment(cid):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()


    cursor.execute('SELECT assignmentName from ASSIGNMENT where assignmentCourse=?',(cid,))

    result=cursor.fetchall()
    ourtuple=[]
    for ele in result:
        ourtuple.append(ele[0])

    connection.commit()
    connection.close()

    return tuple(ourtuple)


#return File Path

def file_course_path(cid,chname):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT filePath from COURSEFILE where fileCourse=? AND fileChapter=?',(cid, chname))

    result = cursor.fetchall()

    connection.commit()
    connection.close()

    return result[0][0]


#select courses taken by a student and put them in a tuple

def select_student_course(slname,spassword):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()


    cursor.execute('SELECT firstCourse, secondCourse,thirdCourse from STUDENT where studentLastName=? AND '
                   'studentPassword=?',(slname,spassword))

    result=cursor.fetchall()
    ourtuple=[]
    for ele in result:
        ourtuple.append(ele[0])
        ourtuple.append(ele[1])
        ourtuple.append(ele[2])

    connection.commit()
    connection.close()

    return tuple(ourtuple)



#select idss of assignments and put them in a tuple

def select_assignment_ids(cid):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()


    cursor.execute('SELECT assignmentId from ASSIGNMENT where assignmentCourse=?',(cid,))

    result=cursor.fetchall()
    ourtuple=[]
    for ele in result:
        ourtuple.append(ele[0])

    connection.commit()
    connection.close()

    return tuple(ourtuple)


#return a course homework's grades

def select_course_grades(assid):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    results=[]

    for id in assid:
        cursor.execute('SELECT  gradeValue, gradeComment from GRADES where gradeAssignmentId=?',(id,))
        result = cursor.fetchall()
        for ele in result:
            results.append(ele[0])
            results.append(ele[1])




    connection.commit()
    connection.close()

    return results

#return a homework's names from assignment names

def select_assignment_names(assid):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    results=[]

    i=0
    for id in list(assid):
        cursor.execute('SELECT  assignmentName from ASSIGNMENT where assignmentId=?',(id,))
        result = cursor.fetchall()

        for ele in result:
            results.append(ele[0])





    connection.commit()
    connection.close()

    return results

#return title and announcement of professor

def select_announcemnts(cid):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    results=[]

    cursor.execute('SELECT  announcementTitle, announcementDescription from ANNOUNCEMENT where announcementCourse=?',(cid,))
    result = cursor.fetchall()

    # for ele in result:
    #     results.append(ele[2])
    #     results.append(ele[3])


    connection.commit()
    connection.close()

    return result




#download course file https://www.youtube.com/watch?v=Xhw2l-hzoKk