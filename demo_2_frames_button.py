import tkinter
import tkinter.messagebox

class KiloConverterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk() #creates our dialogue box

        self.top_frame = tkinter.Frame(self.main_window) #frame method of the tkinter module
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(self.top_frame, text = 'Enter a distance in Kilometers: ') 
        self.kilo_entry = tkinter.Entry(self.top_frame, width = 10)

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

        self.top_frame.pack(side = 'top')
        self.bottom_frame.pack(side = 'top')

    

        tkinter.mainloop() #after you delete dialouge box code under executes

    def convert(self):
        kilo = float(self.kilo_entry.get())

        miles = round((kilo * 0.6214), 2)

        tkinter.messagebox.showinfo('Results', 
                                    str(kilo) + ' Kilometers is equal to '+ 
                                    str(miles) + ' miles.')

my_gui = KiloConverterGUI()
