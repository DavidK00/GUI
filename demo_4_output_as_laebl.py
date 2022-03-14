import tkinter
import tkinter.messagebox

class KiloConverterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk() #creates our dialogue box

        self.top_frame = tkinter.Frame(self.main_window) #frame method of the tkinter module
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(self.top_frame, text = 'Enter a distance in Kilometers: ') 
        self.kilo_entry = tkinter.Entry(self.top_frame, width = 10)

        self.descr_label = tkinter.Label(self.mid_frame, text = 'Converted to miles.')
        
        self.miles_var = tkinter.StringVar()

        self.miles_lable = tkinter.Label(self.mid_frame, 
                                        textvariable = self.miles_var)

        self.prompt_label.pack(side = 'left') 
        self.kilo_entry.pack(side = 'left') 
        
      
        #create button in main window, buttons says click me, button does what you tell it to do
        self.calc_button = tkinter.Button(self.main_window,
                                        text = 'Convert', 
                                        command = self.convert)
        
        self.quit_button = tkinter.Button(self.main_window,
                                        text = 'Quit',
                                        command = self.main_window.destroy)
        
        #pack buttons
        self.calc_button.pack(side = 'left')
        self.quit_button.pack(side = 'right')

        self.descr_label.pack(side = 'left')
        

        self.top_frame.pack(side = 'top')
        self.mid_frame.pack(side = 'top')
        self.bottom_frame.pack(side = 'top')

    

        tkinter.mainloop() #after you delete dialouge box code under executes

    def convert(self):
        kilo = float(self.kilo_entry.get())

        miles = round((kilo * 0.6214), 2)

        self.miles_var.set(miles)

my_gui = KiloConverterGUI()

