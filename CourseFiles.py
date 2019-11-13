import tkinter as tk
from tkinter import ttk

from tkinter import filedialog
import StudentApp
from utils import database


class CourseFiles(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.operationsFrame = tk.Frame(self)


        self.CourseName = tk.StringVar()
        self.Chapter = tk.StringVar()
        self.Path = tk.StringVar()

        self.teacherOperations(controller)

    def teacherOperations(self, controller):

        buttonFrame= tk.Frame(self)

        self.filename=self.fileDialog

        courseNames = database.select_courses()


        tk.Label(self.operationsFrame, text="Course  :").grid(column=0, row=0)
        tk.Spinbox(self.operationsFrame, fg="blue", font=12, textvariable=self.CourseName, values=courseNames).grid(
            column=1, row=0)
        tk.Label(self.operationsFrame, text="Chapter Name :").grid(column=0, row=1, pady=4)
        tk.Entry(self.operationsFrame, width=25, textvariable=self.Chapter).grid(column=1, row=1, pady=4)

        tk.Label(self.operationsFrame, text="Course File :").grid(column=0, row=2, pady=4)



        tk.Button(self.operationsFrame, text="upload",
                  command= self.filename,
                  borderwidth=3, width=6,
                  height=1).grid(column=1, row=2, pady=10)

        tk.Button(self.operationsFrame, text="Submit",
                  command=lambda: controller.add_course_file(database.course_id(self.CourseName.get()),
                                                             self.Chapter.get(), self.filename),
                  borderwidth=3, width=6,
                  height=1).grid(column=0, row=6,pady=10)

        tk.Button(self.operationsFrame, text="Cancel",
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
        self.operationsFrame.grid(column=1, row=0, padx=5)

    def fileDialog(self):

        self.filename= filedialog.askopenfilename(initialdir="/", title="Select File", filetype=(("PDF","*.pdf"),("All Files","*.*")))
        self.label=ttk.Label(self.operationsFrame, text="")
        self.label.grid(column=2, row=2)
        self.label.configure(text=self.filename)




# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Admin")
#     CourseOperations(root)
#     root.mainloop()
