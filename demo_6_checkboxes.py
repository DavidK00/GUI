import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk() #creates our dialogue box

        self.top_frame = tkinter.Frame(self.main_window) #frame method of the tkinter module
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        #set the intvar objects to 0
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        self.cb1 = tkinter.Checkbutton(self.top_frame, text = 'Option 1', 
                                            variable = self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame, text = 'Option 2', 
                                            variable = self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame, text = 'Option 3', 
                                            variable = self.cb_var3)

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

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
        self.message = 'You have selected: \n'
        if self.cb_var1.get() == 1:
            self.message += '1\n'
        if self.cb_var2.get() == 1:
            self.message += '2\n'
        if self.cb_var3.get() == 1:
            self.message += '3\n'
        tkinter.messagebox.showinfo('Response', self.message)

my_gui = MyGUI()

