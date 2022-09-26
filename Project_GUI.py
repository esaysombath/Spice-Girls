from tkinter import *
from tkinter import font as tkFont


# Notes

# For the spice page, there will be a function that will sned a signal to the
# motor, to select the spice that was selected and have it run

# For the amount page there will be another function that will send a signal
# to the container motor to start dispensing the desired amount
# Will have to figure out the lambda function since that will be the route
# to be able to use multiple funtctions within one buttonB

# Idea: on the amount page, could direct to another page to see if user wants
# to select another spice, another measurement, and/or how many times you want
# spice

FONT = (('Times New Roman'), 20)


class SpiceApp(Tk):

    def __init__(self, *args, **kwargs):

        Tk.__init__(self, *args, **kwargs)

        # Creating a contanier
        container = Frame(self)
        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Initializing frames to an empty array
        self.frames = {}

        # Iterating through a tuple consisting of different page layouts
        for F in (SpicePage, AmountPage):

            frame = F(container, self)

            # Initializing frame of that object from pages with for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(SpicePage)

    # Display the current frame, passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class SpicePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # Frame Background color
        self['bg'] = 'black'

        # Label of frame for SpicePage
        Home_Label = Label(self, text='Please Select your Spice',
                           bg='black', fg='white', font=FONT)

        # putting it in place
        Home_Label.grid(row=0, column=2, padx=10, pady=10)

        # Make a button for the spices, and place them
        Spice1 = Button(self, text='Pepper',
                        command=lambda: controller.show_frame(AmountPage))
        Spice1.grid(row=1, column=0, padx=5, pady=5)

        Spice2 = Button(self, text='Paprika',
                        command=lambda: controller.show_frame(AmountPage))
        Spice2.grid(row=1, column=1, padx=5, pady=5)

        Spice3 = Button(self, text='Onion Powder',
                        command=lambda: controller.show_frame(AmountPage))
        Spice3.grid(row=1, column=2, padx=5, pady=5)

        Spice4 = Button(self, text='Garlic Powder',
                        command=lambda: controller.show_frame(AmountPage))
        Spice4.grid(row=1, column=3, padx=5, pady=5)

        Spice5 = Button(self, text='Salt',
                        command=lambda: controller.show_frame(AmountPage))
        Spice5.grid(row=1, column=4, padx=5, pady=5)

        Spice6 = Button(self, text='White Pepper',
                        command=lambda: controller.show_frame(AmountPage))
        Spice6.grid(row=2, column=1, padx=5, pady=5)

        Spice7 = Button(self, text='Cinnamon',
                        command=lambda: controller.show_frame(AmountPage))
        Spice7.grid(row=2, column=2, padx=5, pady=5)

        Spice8 = Button(self, text='Cayenne Pepper',
                        command=lambda: controller.show_frame(AmountPage))
        Spice8.grid(row=2, column=3, padx=5, pady=5)

        exit = Button(self, text='Exit', command=self.quit)
        exit.grid(row=3, column=0, padx=5, pady=5)


class AmountPage(Frame):
    def __init__(self, parent, controller):

        Frame.__init__(self, parent)

        self['bg'] = 'black'

        AmountP_Label = Label(self, text='Select the Amount you want',
                              bg='black', fg='white', font=FONT)
        AmountP_Label.grid(row=0, column=2, padx=10, pady=10)

        tsp_8th = Button(self, text='1/8 tsp')
        tsp_8th.grid(row=1, column=0, padx=5, pady=5)

        tsp_4th = Button(self, text='1/4 tsp')
        tsp_4th.grid(row=1, column=1, padx=5, pady=5)

        tsp_half = Button(self, text='1/2 tsp')
        tsp_half.grid(row=1, column=2, padx=5, pady=5)

        tsp_1 = Button(self, text='1 tsp')
        tsp_1.grid(row=1, column=3, padx=5, pady=5)

        Tbsp_half = Button(self, text='1/2 Tbsp')
        Tbsp_half.grid(row=2, column=1, padx=5, pady=5)

        Tbsp_1 = Button(self, text='1 Tbsp')
        Tbsp_1.grid(row=2, column=2, padx=5, pady=5)

        Back = Button(self, text='Back To Spices',
                      command=lambda: controller.show_frame(SpicePage))
        Back.grid(row=3, column=0, padx=10, pady=10)


gui = SpiceApp()
gui.geometry('800x480')
#gui.attributes('-fullscreen', True)
gui.mainloop()
