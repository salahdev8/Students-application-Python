import tkinter as tk
from tkinter import ttk


# import Teacher.TeacherView as tv


class LoginWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.UserEmail = tk.StringVar()
        self.UserPassword = tk.StringVar()

        self.initComponents(controller)

    def initComponents(self, controller):
        self.pack()
        ttk.Label(self, text="Email :").grid(column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.UserEmail).grid(column=1, row=0)

        ttk.Label(self, text="Password :").grid(column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=25, show="*", textvariable=self.UserPassword).grid(column=1, row=1)

        self.makeButtons(controller)

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)




    def makeButtons(self,controller):
        buttonFrame = tk.Frame(self)
        buttonFrame.grid(column=0, row=3, columnspan=2, sticky=tk.E)

        tk.Button(buttonFrame, text="Connect", command=lambda: controller.login(self.UserEmail.get())).grid(column=0, row=0)
        tk.Button(buttonFrame, text="Cancel").grid(column=1, row=0)

    # def login(self, controller):
    #
    #     email=self.UserEmail.get()
    #     typeofaccount=str(database.login(email))
    #
    #     var=lambda x:controller.show_frame(so.StudentOperations)  if (x=="admin") \
    #         else controller.show_frame(so.StudentOperations)
    #
    #     return var(typeofaccount)



# lambda: controller.show_frame(self.login)




# lambda: controller.show_frame(so.StudentOperations)