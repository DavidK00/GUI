import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk() #creates our dialogue box

        #configure the maijn window
        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        self.label1 = tkinter.Label(self.main_window, text = 'Hello World') #create a label

        self.label2 = tkinter.Label(self.main_window, text = 'This is my GUI program')

        self.label1.pack(side = 'top') #top is default value, left does side by side
        self.label2.pack(side = 'bottom')

        tkinter.mainloop() #after you delete dialouge box code under executes


my_gui = MyGUI()

print("Moving on.....")