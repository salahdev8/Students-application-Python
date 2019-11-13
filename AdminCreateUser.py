import tkinter as tk
from tkinter import ttk
import locale
import StudentApp

from utils import database




class AdminCreateUser(ttk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.UserAccountType = tk.StringVar()
        self.UserFirstName = tk.StringVar()
        self.UserLastName = tk.StringVar()

        self.UserEmail = tk.StringVar()
        self.UserPassword = tk.StringVar()


        self.adminOperations(controller)




    def adminOperations(self, controller):

        operationsFrame=tk.Frame(self)
        buttonFrame= tk.Frame(self)

        tk.Label(operationsFrame, text="Type of User :").grid(column=0, row=0, pady=4)
        tk.Entry(operationsFrame, width=25, textvariable=self.UserAccountType).grid(column=1, row=0, pady=4)
        tk.Label(operationsFrame, text="First name :").grid(column=0, row=1, pady=4)
        tk.Entry(operationsFrame, width=25, textvariable=self.UserFirstName).grid(column=1, row=1, pady=4)
        tk.Label(operationsFrame, text="Last Name :").grid(column=0, row=2, pady=4)
        tk.Entry(operationsFrame, width=25, textvariable=self.UserLastName).grid(column=1, row=2, pady=4)
        tk.Label(operationsFrame, text="Email of user :").grid(column=0, row=3, pady=4)
        tk.Entry(operationsFrame, width=25, textvariable=self.UserEmail).grid(column=1, row=3, pady=4)
        tk.Label(operationsFrame, text="Password :").grid(column=0, row=4, pady=4)
        tk.Entry(operationsFrame, width=25, textvariable=self.UserPassword).grid(column=1, row=4, pady=4)

        tk.Button(operationsFrame, text="submit", command=lambda: controller.create_user(str(self.UserAccountType.get()),self.UserFirstName.get(),self.UserLastName.get(),self.UserEmail.get(),self.UserPassword.get()), borderwidth=3, width=6, height=1).grid(column=1, row=6,pady=10)





        b1 = tk.Button(buttonFrame, text="Create Users", command=lambda: controller.show_frame(StudentApp.AdminCreateUser), borderwidth=4, width=24, height=3)
        b2 = tk.Button(buttonFrame, text="Create Courses",   command=lambda: controller.show_frame(StudentApp.AdminCreateCourse),borderwidth=4, width=24,height=3)
        b3 = tk.Button(buttonFrame, text="Assign Teacher", command=lambda: controller.show_frame(StudentApp.AdminAssignTeacher), borderwidth=4, width=24, height=3)
        b4 = tk.Button(buttonFrame, text="Add Student", command=lambda: controller.show_frame(StudentApp.AdminAddStudent), borderwidth=4, width=24, height=3)
        b5 = tk.Button(buttonFrame, text="Log Out", command=lambda: controller.show_frame(StudentApp.LoginWindow), borderwidth=4, width=24, height=3)

        b1.grid(column=0, row=0)
        b2.grid(column=0, row=1)
        b3.grid(column=0, row=3)
        b4.grid(column=0, row=4)
        b5.grid(column=0, row=5)

        operationsFrame.grid(column=1, row=0, padx=5)
        buttonFrame.grid(column=0, row=0)

    # def create_user(self,type,fname,lname,email,password):
    #
    #     database.create_user(type,fname,lname,email,password)

#
# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Admin")
#     AdminCreateUser(root)
#     root.mainloop()
