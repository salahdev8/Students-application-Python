import tkinter as tk
from tkinter import ttk

import StudentApp
from utils import database


class CourseGrades(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.CourseName = tk.StringVar()
        self.AssignmentName=tk.StringVar()
        self.StudentName=tk.StringVar()
        self.GradeValue=tk.StringVar()
        self.Remark=tk.StringVar()

        self.operationsFrame = tk.Frame(self)

        self.initComponents(controller)

    def initComponents(self, controller):

        buttonFrame= tk.Frame(self)
        courseNames = database.select_courses()

        tk.Label(self.operationsFrame, text="Course  :").grid(column=0, row=0)
        tk.Spinbox(self.operationsFrame, fg="blue", font=12, textvariable=self.CourseName, values=courseNames).grid(
            column=1, row=0)
        tk.Button(self.operationsFrame, text="Confirm",command=self.nextstep,
                  borderwidth=3, width=6,
                  height=1).grid(column=3, row=0, pady=10)




        b1 = tk.Button(buttonFrame, text="Lecture Files ",command=lambda: controller.show_frame(StudentApp.CourseFiles), borderwidth=4, width=24, height=3)
        b2 = tk.Button(buttonFrame, text="Assignments",command=lambda: controller.show_frame(StudentApp.CourseAssignments), borderwidth=4, width=24,height=3)
        b3 = tk.Button(buttonFrame, text="Add a student",command=lambda: controller.show_frame(StudentApp.CourseStudents), borderwidth=4, width=24,height=3)
        b4 = tk.Button(buttonFrame, text="Grades", command=lambda: controller.show_frame(StudentApp.CourseGrades),borderwidth=4, width=24, height=3)
        b5 = tk.Button(buttonFrame, text="Announcements",command=lambda: controller.show_frame(StudentApp.CourseAnnouncements), borderwidth=4, width=24,height=3)
        b6 = tk.Button(buttonFrame, text="Log Out", command=lambda: controller.show_frame(StudentApp.LoginWindow),borderwidth=4, width=24, height=3)

        b1.grid(column=0, row=0)
        b2.grid(column=0, row=1)
        b3.grid(column=0, row=3)
        b4.grid(column=0, row=4)
        b5.grid(column=0, row=5)
        b6.grid(column=0, row=6)

        buttonFrame.grid(column=0, row=0)
        self.operationsFrame.grid(column=1, row=0, padx=5)

    def nextstep(self):
        cid=database.course_id(self.CourseName.get())
        self.assignementlist=database.select_assignment(cid)
        self.studentlist=database.select_student_from_course(self.CourseName.get())

        if(self.assignementlist==()):
            self.assignementlist=("None")

        if(self.studentlist==()):
            self.studentlist=("None")


        tk.Label(self.operationsFrame, text="Assignments  :").grid(column=0, row=1)
        tk.Spinbox(self.operationsFrame, fg="blue", font=12, textvariable=self.AssignmentName, values=self.assignementlist).grid(
            column=1, row=1)
        tk.Label(self.operationsFrame, text="students  :").grid(column=0, row=2)
        tk.Spinbox(self.operationsFrame, fg="blue", font=12, textvariable=self.StudentName,
                   values=self.studentlist).grid(
            column=1, row=2)
        tk.Label(self.operationsFrame, text="Grade ( /100) :").grid(column=0, row=3, pady=4)
        tk.Entry(self.operationsFrame, width=25, textvariable=self.GradeValue).grid(column=1, row=3, pady=4)

        tk.Label(self.operationsFrame, text="Comment :").grid(column=0, row=4, pady=4)
        tk.Entry(self.operationsFrame, width=25, textvariable=self.Remark).grid(column=1, row=4, pady=4)

        tk.Button(self.operationsFrame, text="Confirm", command=self.add_grade,
                  borderwidth=3, width=6,
                  height=1).grid(column=0, row=5, pady=10)
        tk.Button(self.operationsFrame, text="cancel",
                  borderwidth=3, width=6,
                  height=1).grid(column=1, row=5, pady=10)

    def add_grade(self):
        assname=self.AssignmentName.get()
        stdname=self.StudentName.get()
        grade=self.GradeValue.get()
        remark=self.Remark.get()

        if (assname == "None" or stdname == "None"):
            print("No student or assignment selected ")



        else:
            sid = database.student_id(stdname)
            assid = database.assignment_id(assname)
            database.add_grade(sid,assid,grade,remark)





# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Admin")
#     CourseOperations(root)
#     root.mainloop()
