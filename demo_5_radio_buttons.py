import tkinter
import tkinter.messagebox

class RadioButton:
    def __init__(self):
        self.main_window = tkinter.Tk() #creates our dialogue box

        self.top_frame = tkinter.Frame(self.main_window) #frame method of the tkinter module
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()

        #set the intvar object to 1
        self.radio_var.set(30)

        self.rb1 = tkinter.Radiobutton(self.top_frame, text = 'Option1',
                                        variable = self.radio_var,
                                        value = 10)
        
        self.rb2 = tkinter.Radiobutton(self.top_frame, text = 'Option2',
                                        variable = self.radio_var,
                                        value = 20)

        self.rb3 = tkinter.Radiobutton(self.top_frame, text = 'Option3',
                                        variable = self.radio_var,
                                        value = 30)

        self.rb2.select()
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

       

       
      
        #create button in main window, buttons says click me, button does what you tell it to do
        self.okbutton = tkinter.Button(self.bottom_frame,
                                        text = 'OK', 
                                        command = self.show_choice)
        
        self.resetbutton = tkinter.Button(self.bottom_frame,
                                        text = 'reset', 
                                        command = self.rb1.select)
        
        self.quit_button = tkinter.Button(self.bottom_frame,
                                        text = 'Quit',
                                        command = self.main_window.destroy)
        
        #pack buttons
        self.okbutton.pack(side = 'left')
        self.resetbutton.pack(side = 'left')
        self.quit_button.pack(side = 'left')

       
        

        self.top_frame.pack(side = 'top')
        self.bottom_frame.pack(side = 'top')

    

        tkinter.mainloop() #after you delete dialouge box code under executes

    def show_choice(self):
        tkinter.messagebox.showinfo('Selection', 'You have selected option ' + str(self.radio_var.get()))

my_gui = RadioButton()

