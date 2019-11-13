import tkinter as tk
from tkinter import ttk

import StudentApp


class StudentOperations(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.initComponents(controller)

    def initComponents(self, controller):

        buttonFrame= tk.Frame(self)


        b1 = tk.Button(buttonFrame, text="Lecture Files ",command=lambda: controller.show_frame(StudentApp.CheckFiles), borderwidth=4, width=24, height=3)
        b2 = tk.Button(buttonFrame, text="Assignments",command=lambda: controller.show_frame(StudentApp.StudentAssignment), borderwidth=4, width=24,height=3)
        b3 = tk.Button(buttonFrame, text="Grades", command=lambda: controller.show_frame(StudentApp.StudentGrades),borderwidth=4, width=24, height=3)
        b4 = tk.Button(buttonFrame, text="Announcements",command=lambda: controller.show_frame(StudentApp.StudentAnnouncements), borderwidth=4, width=24,height=3)
        b5 = tk.Button(buttonFrame, text="Log Out", command=lambda: controller.show_frame(StudentApp.LoginWindow),borderwidth=4, width=24, height=3)

        b1.grid(column=0, row=0)
        b2.grid(column=0, row=1)
        b3.grid(column=0, row=2)
        b4.grid(column=0, row=3)
        b5.grid(column=0, row=5)

        buttonFrame.grid(column=0, row=0)



# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Admin")
#     CourseOperations(root)
#     root.mainloop()
