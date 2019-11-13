import tkinter as tk
from tkinter import ttk
import locale

import StudentApp
from utils import database



class AdminAddStudent(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        self.fCourseName = tk.StringVar()
        self.sCourseName = tk.StringVar()
        self.tCourseName = tk.StringVar()
        self.StudentName = tk.StringVar()


        self.adminOperations(controller)




    def adminOperations(self, controller):

        operationsFrame=tk.Frame(self)
        buttonFrame= tk.Frame(self)

        courseNames=database.select_courses()
        studentNames=database.select_students()

        tk.Label(operationsFrame, text="Course 1 :").grid(column=0, row=0)
        tk.Spinbox(operationsFrame, fg="blue", font=12, textvariable=self.fCourseName, values=courseNames).grid(column=1, row=0)

        tk.Label(operationsFrame, text="Course 2 :").grid(column=0, row=1)
        tk.Spinbox(operationsFrame, fg="blue", font=12, textvariable=self.sCourseName, values=courseNames).grid(column=1,row=1)

        tk.Label(operationsFrame, text="Course 3 :").grid(column=0, row=2)
        tk.Spinbox(operationsFrame, fg="blue", font=12, textvariable=self.tCourseName, values=courseNames).grid(column=1,row=2)

        tk.Label(operationsFrame, text="Student Name :").grid(column=0, row=3)
        tk.Spinbox(operationsFrame, fg="blue", font=12, textvariable=self.StudentName, values=studentNames).grid(column=1, row=3)

        tk.Button(operationsFrame, text="submit",
                  command=lambda: controller.add_course_student(self.StudentName.get(), self.fCourseName.get(),
                                                                self.sCourseName.get(), self.tCourseName.get()),
                  borderwidth=3, width=6,
                  height=1).grid(column=1, row=6, pady=10)





        b1 = tk.Button(buttonFrame, text="Create Users", command=lambda: controller.show_frame(StudentApp.AdminCreateUser),borderwidth=4, width=24, height=3)
        b2 = tk.Button(buttonFrame, text="Create Courses",   command=lambda: controller.show_frame(StudentApp.AdminCreateCourse),borderwidth=4, width=24,height=3)
        b3 = tk.Button(buttonFrame, text="Assign Teacher", command=lambda: controller.show_frame(StudentApp.AdminAssignTeacher),borderwidth=4, width=24, height=3)
        b4 = tk.Button(buttonFrame, text="Add Student",  command=lambda: controller.show_frame(StudentApp.AdminAddStudent), borderwidth=4, width=24, height=3)
        b5 = tk.Button(buttonFrame, text="Log Out", command=lambda: controller.show_frame(StudentApp.LoginWindow), borderwidth=4, width=24, height=3)

        b1.grid(column=0, row=0)
        b2.grid(column=0, row=1)
        b3.grid(column=0, row=3)
        b4.grid(column=0, row=4)
        b5.grid(column=0, row=5)

        operationsFrame.grid(column=1, row=0, padx=5)
        buttonFrame.grid(column=0, row=0)

#
# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Admin")
#     AdminAddStudent(root)
#     root.mainloop()
