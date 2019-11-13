from AdminView import *
from LoginWindow import *
from AdminAssignTeacher import *
from AdminCreateUser import *
from AdminAddStudent import *
from AdminCreateCourse import *

from CourseOperations import *
from CourseFiles import *
from CourseAssignments import *
from CourseStudents import *
from CourseGrades import *
from CourseAnnouncements import *

from StudentOperations import *
from CheckFiles import *
from StudentAssignment import *
from StudentGrades import *
from StudentAnnouncements import *



import tkinter as tk
from utils import database




class StudentApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        self.frames = {}

        for F in (LoginWindow, AdminView, AdminCreateUser, AdminAssignTeacher, AdminAddStudent, AdminCreateCourse,
                  CourseOperations, CourseFiles, CourseAssignments, CourseStudents, CourseGrades, CourseAnnouncements,
                  StudentOperations, CheckFiles, StudentAssignment, StudentGrades, StudentAnnouncements):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginWindow)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()



    def login(self,email):

        if(database.login_admin(email)=="admin"):
            self.show_frame(AdminView)
        elif(database.login_teacher(email)=="teacher"):
            self.show_frame(CourseOperations)
        elif (database.login_student(email)=="student"):
            self.show_frame(StudentOperations)



    def create_user(self, type, fname, lname, email, password):
        database.create_user(type, fname, lname, email, password)



    def create_course(self,clevel,cname,clocation):
        database.create_course(cname,clevel,clocation)

    def assign_teacher(self,cname,tname):
        database.assign_Teacher(cname,tname)

    def add_course_student(self,sname,fcourse,scourse,tcourse):
        database.add_courses_to_student(sname,fcourse,scourse,tcourse)

    def add_course_file(self,fid,fchapter,fpath):
        database.inser_course_file(fid,fchapter,fpath)

    def add_assignemnt_file(self,fid,assignment,fpath):

        database.inser_Assignment_file(fid,assignment,fpath)

    # def add_grade(self,assname,stdname,grade,remark):
    #
    #     sid=database.student_id(stdname)
    #     assid=database.assignment_id(assname)
    #
    #     database.add_grade(sid,assid,grade,remark)



        # if(typeofaccount=="admin"):
        #     self.show_frame(AdminView)
        #
        # elif(typeofaccount=="teacher"):
        #     self.show_frame(TeacherView)
        #
        # elif(typeofaccount=="student"):
        #     self.show_frame(StudentView)


# class LoginWindow(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#
#         self.UserEmail = tk.StringVar()
#         self.UserPassword = tk.StringVar()
#
#         self.initComponents(controller)
#
#     def initComponents(self, controller):
#         self.pack()
#         ttk.Label(self, text="Email :").grid(column=0, row=0, sticky=tk.E)
#         ttk.Entry(self, width=25, textvariable=self.UserEmail).grid(column=1, row=0)
#
#         ttk.Label(self, text="Password :").grid(column=0, row=1, sticky=tk.E)
#         ttk.Entry(self, width=25, textvariable=self.UserPassword).grid(column=1, row=1)
#
#         self.makeButtons(controller)
#
#         for child in self.winfo_children():
#             child.grid_configure(padx=5, pady=3)
#
#     def makeButtons(self,controller):
#         buttonFrame = tk.Frame(self)
#         buttonFrame.grid(column=0, row=3, columnspan=2, sticky=tk.E)
#
#         tk.Button(buttonFrame, text="Connect", command=lambda: controller.show_frame(AdminView)).grid(column=0, row=0)
#         tk.Button(buttonFrame, text="Cancel").grid(column=1, row=0)



if __name__ == "__main__":

    database.create_tables()

    result=database.show_announce(1)
    print(result)




    root = StudentApp()
    root.title("Student App")
    root.mainloop()