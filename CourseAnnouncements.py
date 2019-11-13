import tkinter as tk
import locale
from tkinter import ttk

import StudentApp
from utils import database


class CourseAnnouncements(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.CourseName = tk.StringVar()
        self.announcementTitle = tk.StringVar()
        self.announcementDescr = tk.StringVar()

        self.operationsFrame = tk.Frame(self)


        self.text=tk.Text(self.operationsFrame, height=5, width=50)


        self.announcementFrame = tk.Frame(self)


        self.initComponents(controller)

    def initComponents(self, controller):

        buttonFrame= tk.Frame(self)


        courseNames = database.select_courses()

        tk.Label(self.operationsFrame, text="Course  :").grid(column=0, row=0)
        tk.Spinbox(self.operationsFrame, fg="blue", font=12, textvariable=self.CourseName, values=courseNames).grid(
            column=1, row=0)
        tk.Label(self.operationsFrame, text="Title :").grid(column=0, row=1, pady=4)
        tk.Entry(self.operationsFrame, width=25, textvariable=self.announcementTitle).grid(column=1, row=1, pady=4)
        tk.Label(self.operationsFrame, text="Announcement :").grid(column=0, row=2, pady=4)
        self.text.grid(column=1, row=2, pady=4)




        tk.Button(self.operationsFrame, text="Add",command=lambda : self.method_annoc(),
                  borderwidth=3, width=6,
                  height=1).grid(column=0, row=3, pady=10)
        tk.Button(self.operationsFrame, text="cancel",
                  borderwidth=3, width=6,
                  height=1).grid(column=1, row=3, pady=10)



        b1 = tk.Button(buttonFrame, text="Lecture Files ", command=lambda: controller.show_frame(StudentApp.CourseFiles),borderwidth=4, width=24, height=3)
        b2 = tk.Button(buttonFrame, text="Assignments", command=lambda: controller.show_frame(StudentApp.CourseAssignments), borderwidth=4, width=24,height=3)
        b3 = tk.Button(buttonFrame, text="Add a student", command=lambda: controller.show_frame(StudentApp.CourseStudents), borderwidth=4, width=24, height=3)
        b4 = tk.Button(buttonFrame, text="Grades", command=lambda: controller.show_frame(StudentApp.CourseGrades), borderwidth=4, width=24, height=3)
        b5 = tk.Button(buttonFrame, text="Announcements", command=lambda: controller.show_frame(StudentApp.CourseAnnouncements), borderwidth=4, width=24, height=3)
        b6 = tk.Button(buttonFrame, text="Log Out", command=lambda: controller.show_frame(StudentApp.LoginWindow), borderwidth=4, width=24, height=3)

        b1.grid(column=0, row=0)
        b2.grid(column=0, row=1)
        b3.grid(column=0, row=3)
        b4.grid(column=0, row=4)
        b5.grid(column=0, row=5)
        b6.grid(column=0, row=6)

        buttonFrame.grid(column=0, row=0)
        self.operationsFrame.grid(column=1, row=0, padx=5)

    def method_annoc(self):
        data = self.text.get("1.0", "end-1c")
        result=""
        # self.announcementDescr.set(data)
        #
        # print(self.announcementDescr)
        for line in data.split():
            result+=" "+line
        print(result)

        self.announcementDescr.set(result)
        cid=database.course_id(self.CourseName.get())
        database.add_announce(cid,self.announcementTitle.get(),self.announcementDescr.get())

        result=database.show_announce(cid)
        i=4
        for announce in result:
            tk.Label(self.operationsFrame, text=announce).grid(column=0, row=i, pady=4)
            i=i+1




    # def add_annoucement(self):





# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Admin")
#     CourseAnnouncements(root)
#     root.mainloop()
