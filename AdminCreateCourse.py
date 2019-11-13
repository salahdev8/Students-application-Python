import tkinter as tk
from tkinter import ttk
import locale

import StudentApp

class AdminCreateCourse(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        self.CourseLevel = tk.StringVar()
        self.CourseName = tk.StringVar()
        self.CourseLocation = tk.StringVar()

        self.adminOperations(controller)




    def adminOperations(self, controller):

        operationsFrame=tk.Frame(self)
        buttonFrame= tk.Frame(self)

        tk.Label(operationsFrame, text="Course Level :").grid(column=0, row=0, pady=4)
        tk.Entry(operationsFrame, width=25, textvariable=self.CourseLevel).grid(column=1, row=0, pady=4)
        tk.Label(operationsFrame, text="Course Name :").grid(column=0, row=1, pady=4)
        tk.Entry(operationsFrame, width=25, textvariable=self.CourseName).grid(column=1, row=1, pady=4)
        tk.Label(operationsFrame, text="Course Location:").grid(column=0, row=2, pady=4)
        tk.Entry(operationsFrame, width=25, textvariable=self.CourseLocation).grid(column=1, row=2, pady=4)

        tk.Button(operationsFrame, text="submit",command=lambda: controller.create_course(self.CourseLevel.get(),
         self.CourseName.get(),self.CourseLocation.get()),
        borderwidth=3, width=6, height=1).grid(column=1, row=6, pady=10)

        b1 = tk.Button(buttonFrame, text="Create Users", command=lambda: controller.show_frame(StudentApp.AdminCreateUser),borderwidth=4, width=24, height=3)
        b2 = tk.Button(buttonFrame, text="Create Courses", command=lambda: controller.show_frame(StudentApp.AdminCreateCourse), borderwidth=4, width=24,height=3)
        b3 = tk.Button(buttonFrame, text="Assign Teacher",command=lambda: controller.show_frame(StudentApp.AdminAssignTeacher), borderwidth=4, width=24, height=3)
        b4 = tk.Button(buttonFrame, text="Add Student",command=lambda: controller.show_frame(StudentApp.AdminAddStudent), borderwidth=4, width=24, height=3)
        b5 = tk.Button(buttonFrame, text="Log Out",  command=lambda: controller.show_frame(StudentApp.LoginWindow), borderwidth=4, width=24, height=3)

        b1.grid(column=0, row=0)
        b2.grid(column=0, row=1)
        b3.grid(column=0, row=3)
        b4.grid(column=0, row=4)
        b5.grid(column=0, row=5)

        operationsFrame.grid(column=1, row=0, padx=5)
        buttonFrame.grid(column=0, row=0)


# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Admin")
#     AdminCreateCourse(root)
#     root.mainloop()
