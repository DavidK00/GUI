import tkinter
import tkinter.messagebox

class AvgGUI:
    def __init__(self):
        self.main_window = tkinter.Tk() #creates our dialogue box

        self.top_frame = tkinter.Frame(self.main_window) #frame method of the tkinter module
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.label_frame = tkinter.Frame(self.main_window)
        self.avg_frame = tkinter.Frame(self.main_window)

        self.main_window.configure(background = 'pink')

        self.prompt_label1 = tkinter.Label(self.top_frame, text = 'Enter the score for test 1: ') 
        self.prompt_label2 = tkinter.Label(self.mid_frame, text = 'Enter the score for test 2: ') 
        self.prompt_label3 = tkinter.Label(self.bottom_frame, text = 'Enter the score for test 3: ')
        self.avg_score_var = tkinter.StringVar()
        self.avg_label = tkinter.Label(self.label_frame, text = 'Average: ', textvariable = self.avg_score_var)


        self.score1 = tkinter.Entry(self.top_frame, width = 10)
        self.score2 = tkinter.Entry(self.mid_frame, width = 10)
        self.score3 = tkinter.Entry(self.bottom_frame, width = 10)


        self.prompt_label1.pack(side = 'left') 
        self.prompt_label2.pack(side = 'left') 
        self.prompt_label3.pack(side = 'left') 

        self.score1.pack(side = 'left') 
        self.score2.pack(side = 'left') 
        self.score3.pack(side = 'left') 
        
      
        #create button in main window, buttons says click me, button does what you tell it to do
        self.calc_button = tkinter.Button(self.label_frame,
                                        text = 'Average', 
                                        command = self.convert)
        
        self.quit_button = tkinter.Button(self.label_frame,
                                        text = 'Quit',
                                        command = self.main_window.destroy)
        
        #pack buttons
        self.calc_button.pack(side = 'left')
        self.quit_button.pack(side = 'right')

        self.top_frame.pack(side = 'top')
        self.mid_frame.pack(side = 'top')
        self.bottom_frame.pack(side = 'top')
        self.avg_frame.pack(side = 'top')
        self.label_frame.pack(side = 'top')
        

    

        tkinter.mainloop() #after you delete dialouge box code under executes

    def convert(self):
        score1 = float(self.score1.get())
        score2 = float(self.score2.get())
        score3 = float(self.score3.get())
        avg_score = (score1 + score2 + score3) / 3

        tkinter.messagebox.showinfo('Results', 
                                    avg_score)
        self.avg_score_var.set(avg_score)

my_gui = AvgGUI()

