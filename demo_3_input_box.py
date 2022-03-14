import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk() #creates our dialogue box

        self.top_frame = tkinter.Frame(self.main_window) #frame method of the tkinter module
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, text = 'John') #create a label
        self.label2 = tkinter.Label(self.top_frame, text = 'Jill')
        self.label3 = tkinter.Label(self.top_frame, text = 'James')

        self.label1.pack(side = 'top') #top is default value, left does side by side
        self.label2.pack(side = 'top')
        self.label3.pack(side = 'top')

        self.label4 = tkinter.Label(self.bottom_frame, text = 'Jack') #create a label
        self.label5 = tkinter.Label(self.bottom_frame, text = 'Jim')
        self.label6 = tkinter.Label(self.bottom_frame, text = 'Jerry')

        self.label1.pack(side = 'top') #top is default value, left does side by side
        self.label2.pack(side = 'top')
        self.label3.pack(side = 'top')

        self.label4.pack(side = 'left') #top is default value, left does side by side
        self.label5.pack(side = 'left')
        self.label6.pack(side = 'left')

        #create button in main window, buttons says click me, button does what you tell it to do
        self.my_button = tkinter.Button(self.main_window,
                                        text = 'Click Me!', 
                                        command = self.do_something)
        
        self.quit_button = tkinter.Button(self.main_window,
                                        text = 'Quit',
                                        command = self.main_window.destroy)
        
        #pack buttons
        self.my_button.pack(side = 'left')
        self.quit_button.pack(side = 'right')

        self.top_frame.pack(side = 'top')
        self.bottom_frame.pack(side = 'top')

    

        tkinter.mainloop() #after you delete dialouge box code under executes

    def do_something(self):
        tkinter.messagebox.showinfo('Response', 'Thank you for clkicking the button')

my_gui = MyGUI()

print("Moving on.....")