import tkinter as tk
from tkinter import ttk

import shutil, os



import requests
from tqdm import tqdm


import StudentApp
from utils import database

class CheckFiles(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.CourseName = tk.StringVar()
        self.ChaptersFiles=tk.StringVar()

        self.operationsFrame = tk.Frame(self)
        self.initComponents(controller)

    def initComponents(self, controller):

        buttonFrame= tk.Frame(self)


        courseNames = database.select_courses()

        tk.Label(self.operationsFrame, text="Course  :").grid(column=0, row=0)
        tk.Spinbox(self.operationsFrame, fg="blue", font=12, textvariable=self.CourseName, values=courseNames).grid(
            column=1, row=0)

        tk.Button(self.operationsFrame, text="Confirm",command=self.next_step,
                  borderwidth=3, width=6,
                  height=1).grid(column=3, row=0, pady=10)




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
        self.operationsFrame.grid(column=1, row=0, padx=5)

    def next_step(self):

        cid=database.course_id(self.CourseName.get())
        result=database.select_course_file(cid)

        tk.Label(self.operationsFrame, text="Choose a file  :").grid(column=0, row=1)
        tk.Spinbox(self.operationsFrame, fg="blue", font=12, textvariable=self.ChaptersFiles, values=result).grid(
            column=1, row=1)
        tk.Button(self.operationsFrame, text="Download", command=self.download,
                  borderwidth=3, width=7,
                  height=1).grid(column=3, row=1, pady=10)

    def download(self):

        cid=database.course_id(self.CourseName.get())
        chname=self.ChaptersFiles.get()

        # path=database.file_course_path(cid, chname)

        # path ="C:\\Users\\salah\\Desktop\\bridgeport\\08138300024025.pdf"

        path="https://www.virginiawestern.edu/learning/elit/faculty/docs/bb/Coursefiles.pdf"

        r= requests.get(path, stream=True)

        chunk_size=1024

        total_size = int(r.headers['content-length'])

        with open(chname+".pdf",'wb') as f:
            for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size),total=total_size/chunk_size, unit='KB'):
                f.write(data)

        print("Download complete!")












# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Admin")
#     CheckFiles(root)
#     root.mainloop()
