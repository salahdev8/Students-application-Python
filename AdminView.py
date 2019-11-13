import tkinter as tk
from tkinter import ttk


import StudentApp

class AdminView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.adminOperations(controller)



    def adminOperations(self, controller):

        buttonFrame= tk.Frame(self)

        b1 = tk.Button(buttonFrame, text="Create Users", command=lambda: controller.show_frame(StudentApp.AdminCreateUser), borderwidth=4, width=24, height=3)
        b2 = tk.Button(buttonFrame, text="Create Courses",  command=lambda: controller.show_frame(StudentApp.AdminCreateCourse), borderwidth=4, width=24,height=3)
        b3 = tk.Button(buttonFrame, text="Assign Teacher", command=lambda: controller.show_frame(StudentApp.AdminAssignTeacher), borderwidth=4, width=24, height=3)
        b4 = tk.Button(buttonFrame, text="Add Student", command=lambda: controller.show_frame(StudentApp.AdminAddStudent), borderwidth=4, width=24, height=3)
        b5 = tk.Button(buttonFrame, text="Log Out", command=lambda: controller.show_frame(StudentApp.LoginWindow), borderwidth=4, width=24, height=3)

        b1.grid(column=0, row=0)
        b2.grid(column=0, row=1)
        b3.grid(column=0, row=3)
        b4.grid(column=0, row=4)
        b5.grid(column=0, row=5)




        buttonFrame.grid(column=0, row=0)



# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Admin")
#     AdminView(root)
#     root.mainloop()
