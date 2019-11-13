import tkinter as tk
from tkinter import ttk
import locale
import StudentApp



class TeacherView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        result = locale.setlocale(locale.LC_ALL, '')

        if result == 'C':
            locale.setlocale(locale.LC_ALL, 'en_US')
        self.TeacherOperations(controller)

    def TeacherOperations(self, controller):

        buttonFrame= tk.Frame(self)


        # b1 = tk.Button(buttonFrame, text="Create Users", command=lambda: controller.show_frame(StudentApp), borderwidth=4, width=24, height=3)
        # b2 = tk.Button(buttonFrame, text="Create Courses", command=lambda: controller.show_frame(StudentApp), borderwidth=4, width=24,height=3)
        # b3 = tk.Button(buttonFrame, text="Assign Teacher", command=lambda: controller.show_frame(StudentApp), borderwidth=4, width=24, height=3)
        # b4 = tk.Button(buttonFrame, text="Add Student", command=lambda: controller.show_frame(StudentApp), borderwidth=4, width=24, height=3)
        # b5 = tk.Button(buttonFrame, text="Log Out", command=lambda: controller.show_frame(StudentApp.LoginWindow), borderwidth=4, width=24, height=3)
        #
        # b1.grid(column=0, row=0)
        # b2.grid(column=0, row=1)
        # b3.grid(column=0, row=3)
        # b4.grid(column=0, row=4)
        # b5.grid(column=0, row=5)




        buttonFrame.grid(column=0, row=0)



# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Admin")
#     TeacherView(root)
#     root.mainloop()
