import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk() 

        self.main_window.geometry('500x200')
        self.main_window.title("David's Pizza")

        self.title_frame = tkinter.Frame(self.main_window)
        self.name_frame = tkinter.Frame(self.main_window)
        self.crust_frame = tkinter.Frame(self.main_window)

        self.title = tkinter.Label(self.title_frame, text = 'Pizza Configurator') 

        self.name_label = tkinter.Label(self.name_frame, text = 'Name: ')
        self.name_entry = tkinter.Entry(self.name_frame, width = 20)

        self.title.pack(side = 'top')
        self.name_label.pack(side = 'top') 
        self.name_entry.pack(side = 'top')

        self.title_frame.pack(side = 'top')
        self.name_frame.pack(side = 'top')


my_gui = MyGUI()