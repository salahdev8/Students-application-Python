import tkinter as tk
from tkinter import ttk

import StudentApp
from utils import database


class CourseStudents(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.fCourseName = tk.StringVar()
        self.sCourseName = tk.StringVar()
        self.tCourseName = tk.StringVar()
        self.StudentName = tk.StringVar()

        self.initComponents(controller)

    def initComponents(self, controller):

        buttonFrame= tk.Frame(self)
        operationsFrame = tk.Frame(self)

        courseNames = database.select_courses()
        studentNames = database.select_students()

        tk.Label(operationsFrame, text="Course 1 :").grid(column=0, row=0)
        tk.Spinbox(operationsFrame, fg="blue", font=12, textvariable=self.fCourseName, values=courseNames).grid(
            column=1, row=0)

        tk.Label(operationsFrame, text="Course 2 :").grid(column=0, row=1)
        tk.Spinbox(operationsFrame, fg="blue", font=12, textvariable=self.sCourseName, values=courseNames).grid(
            column=1, row=1)

        tk.Label(operationsFrame, text="Course 3 :").grid(column=0, row=2)
        tk.Spinbox(operationsFrame, fg="blue", font=12, textvariable=self.tCourseName, values=courseNames).grid(
            column=1, row=2)

        tk.Label(operationsFrame, text="Student Name :").grid(column=0, row=3)
        tk.Spinbox(operationsFrame, fg="blue", font=12, textvariable=self.StudentName, values=studentNames).grid(
            column=1, row=3)

        tk.Button(operationsFrame, text="submit",
                  command=lambda: controller.add_course_student(self.StudentName.get(), self.fCourseName.get(),
                                                                self.sCourseName.get(), self.tCourseName.get()),
                  borderwidth=3, width=6,
                  height=1).grid(column=1, row=6, pady=10)


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
        operationsFrame.grid(column=1, row=0, padx=5)



# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Admin")
#     CourseOperations(root)
#     root.mainloop()
