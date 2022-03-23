

import tkinter
import tkinter.messagebox

class Pizza:
    def __init__(self):
        self.main_window = tkinter.Tk() 

        #window attributes
        self.main_window.geometry('700x900')
        self.main_window.title("David's Pizza")
        self.main_window.configure(bg='Linen')
        self.main_window.option_add("*Font", "Batang")

        #frame definition
        self.name_frame = tkinter.Frame(self.main_window)
        self.size_frame = tkinter.Frame(self.main_window)
        self.sauce_frame = tkinter.Frame(self.main_window)
        self.crust_frame = tkinter.Frame(self.main_window)
        self.cheese_frame = tkinter.Frame(self.main_window)
        self.toppings_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.empty_Frame1 = tkinter.Frame(self.main_window, bg = 'linen', width=700, height=25)
        self.empty_Frame2 = tkinter.Frame(self.main_window, bg = 'linen', width=700, height=25)
        self.empty_Frame3 = tkinter.Frame(self.main_window, bg = 'linen', width=700, height=25)
        self.empty_Frame4 = tkinter.Frame(self.main_window, bg = 'linen', width=700, height=25)
        self.empty_Frame5 = tkinter.Frame(self.main_window, bg = 'linen', width=700, height=25)
        
        #size
        
        self.size_radio = tkinter.IntVar()
        if self.size_radio == 9:
            self.size_radio
        elif self.size_radio == 12:
            self.size_radio
        else:
            self.size_radio

        self.size_label = tkinter.Label(self.size_frame,bg = 'red', text = "Pick A Size Option: ")  
        self.size_label.pack()  

        self.small = tkinter.Radiobutton(self.size_frame, text="Small (+$.900)", variable= self.size_radio, value=9)  
        self.medium = tkinter.Radiobutton(self.size_frame, text="Medium (+$12.00)", variable= self.size_radio, value=12)    
        self.large = tkinter.Radiobutton(self.size_frame, text="Large (+$15.00)", variable= self.size_radio, value=15) 
    
        #sauce
        self.sauce_radio = tkinter.IntVar()
        if self.sauce_radio == 0:
            self.sauce_radio
        elif self.sauce_radio == 1.0:
            self.sauce_radio
        else:
            self.sauce_radio

        self.sauce_label = tkinter.Label(self.sauce_frame,bg = 'red', text = "Pick A Sauce Option: ")  
        self.sauce_label.pack()  

        self.marinara = tkinter.Radiobutton(self.sauce_frame, text="Marinara (+$1.00)", variable= self.sauce_radio, value=0)  
        self.ranch = tkinter.Radiobutton(self.sauce_frame, text="Ranch (+$1.00)", variable= self.sauce_radio, value=1.0)    
        self.bbq = tkinter.Radiobutton(self.sauce_frame, text="BBQ (+$1.50)", variable= self.sauce_radio, value=1.5)  
         

        #name entry
        self.prompt_label = tkinter.Label(self.name_frame, bg = 'red' , text = 'Enter your Name ') 
        self.name_entry = tkinter.Entry(self.name_frame, width = 10)

        #sauce entry

        #crust options
        self.crust_radio = tkinter.IntVar()
        if self.crust_radio == 1:
            self.crust_radio
        elif self.crust_radio == 2:
            self.crust_radio
        else:
            self.crust_radio
        
        self.crust_label = tkinter.Label(self.crust_frame, bg = 'red', text = "Pick A Crust Option: ")  
        self.crust_label.pack()  

        self.regular = tkinter.Radiobutton(self.crust_frame, text="Regular (+$0.00)", variable=self.crust_radio, value=0)  
        self.stuffed = tkinter.Radiobutton(self.crust_frame, text="Stuffed (+$2.00)", variable=self.crust_radio, value=2)    
        self.thin = tkinter.Radiobutton(self.crust_frame, text="Thin (+$0.00)", variable=self.crust_radio, value= 0.00)  

        #cheese options
        self.cheese_radio = tkinter.IntVar()
        
        if self.cheese_radio == 1:
            self.cheese_radio
        elif self.cheese_radio == 1.0:
            self.cheese_radio
        elif self.cheese_radio == 1.5:
            self.cheese_radio
        else:
            self.crust_radio

        self.cheese_label = tkinter.Label(self.cheese_frame,bg = 'red', text = "Pick A Cheese Option: ")  
        self.cheese_label.pack()  

        self.mozz = tkinter.Radiobutton(self.cheese_frame, text="Mozzarella (+$1.00)", variable= self.cheese_radio, value=1)  
        self.american = tkinter.Radiobutton(self.cheese_frame, text="American (+$1.00)", variable= self.cheese_radio, value=1.0)    
        self.cheddar = tkinter.Radiobutton(self.cheese_frame, text="Cheddar (+$1.50)", variable= self.cheese_radio, value=1.5)  
        self.gouda = tkinter.Radiobutton(self.cheese_frame, text="Gouda (+$2.00)", variable= self.cheese_radio, value=2)  
         
        #topping options
        self.toppings = tkinter.Label(self.toppings_frame, bg = 'red', text = 'Pick Your Toppings (All Toppings + $1.00)')
        self.toppings.pack(side = 'top') 

        
        self.var1 = tkinter.IntVar()
        self.var2 = tkinter.IntVar()
        self.var3 = tkinter.IntVar()
        self.var4 = tkinter.IntVar()
        self.var5 = tkinter.IntVar()
        self.var6 = tkinter.IntVar()
    
        self.pepperoni = tkinter.Checkbutton(self.toppings_frame, text='Pepperoni',variable=self.var1, onvalue=1, offvalue=0)
        self.pineapple = tkinter.Checkbutton(self.toppings_frame, text='Pineapple',variable=self.var2, onvalue=1, offvalue=0)
        self.peppers = tkinter.Checkbutton(self.toppings_frame, text='Bell Peppers',variable=self.var3, onvalue=1, offvalue=0)
        self.onions = tkinter.Checkbutton(self.toppings_frame, text='Red Onions',variable=self.var4, onvalue=1, offvalue=0)
        self.sausage = tkinter.Checkbutton(self.toppings_frame, text='Sausage',variable=self.var5, onvalue=1, offvalue=0)
        self.mushrooms = tkinter.Checkbutton(self.toppings_frame, text='Mushrooms',variable=self.var6, onvalue=1, offvalue=0)
      
        
        self.calc_button = tkinter.Button(self.bottom_frame,
                                        text = 'Calculate Total', 
                                        command = self.convert)
        
        self.quit_button = tkinter.Button(self.bottom_frame,
                                        text = 'Quit',
                                        command = self.main_window.destroy)
        
        #pack buttons
        self.calc_button.pack(side = 'left')
        self.quit_button.pack(side = 'right')

        #pack name 
        self.prompt_label.pack(side = 'left') 
        self.name_entry.pack(side = 'left') 
        
        #pack size
        self.small.pack()
        self.medium.pack()
        self.large.pack()

        #pack sauce
        self.marinara.pack()
        self.bbq.pack()
        self.ranch.pack()

        #pack crust
        self.regular.pack() 
        self.stuffed.pack()
        self.thin.pack()
        
        #pack cheese
        self.mozz.pack(side = 'left')
        self.american.pack(side = 'left')
        self.cheddar.pack(side = 'right')
        self.gouda.pack(side = 'right')

        #pack toppings
        self.pepperoni.pack(side = 'left')
        self.pineapple.pack(side = 'left')
        self.peppers.pack(side = 'left')
        self.onions.pack(side = 'right')
        self.sausage.pack(side = 'right')
        self.mushrooms.pack(side = 'right')

         
        #pack frames
        self.name_frame.pack(side = 'top')
        self.empty_Frame1.pack(side = 'top')
        self.size_frame.pack(side = 'top')
        self.empty_Frame5.pack(side = 'top')
        self.sauce_frame.pack(side = 'top')
        self.empty_Frame4.pack(side = 'top')
        self.crust_frame.pack(side = 'top')
        self.empty_Frame2.pack(side = 'top')
        self.cheese_frame.pack(side = 'top')
        self.empty_Frame3.pack(side = 'top')
        self.toppings_frame.pack(side = 'top')
        self.bottom_frame.pack(side = 'bottom')

    

        tkinter.mainloop() 

    def convert(self):
        size = float(self.size_radio.get())
        sauce = float(self.sauce_radio.get())
        crust = float(self.crust_radio.get())
        cheese = float(self.cheese_radio.get())
        toppings = round((float(self.var1.get()) + float(self.var2.get()) + float(+ self.var3.get())
         + float(self.var4.get()) + float(self.var5.get() + float(self.var6.get()))),2)
        name = self.name_entry.get()

        total = crust + cheese + toppings + sauce +size
        total_format = "{:.2f}".format(total)

        tkinter.messagebox.showinfo('Recepit', 'Name: ' + name + '\n' + 'Total: ' + '$' + str(total_format))
                                    

my_gui = Pizza()
