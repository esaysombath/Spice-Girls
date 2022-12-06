Individual Report Week 9 (10/23)
Summary of the week: 
 The Spice Girls team met with Dr.Peng to discuss our project.  Talk about parts to acquire and start thinking of coding/system development. Research the hardware works and the steps and research I will need to learn to implement the functions as a whole code.
 For individual work, I did more research on the functions needed to control the motor and worked on GUI with Jacob, played around testing functions on example codes I found that are related to the project.
Goal of the week: 
Understand more about what the works and steps are for the hardware of our project,  start coding and testing. Work on GUI to be prettier and modern.
Problem of the week: 
	Thinking of starting with a whole new design, easier for code and hardware works. 
Why that is a problem: 
	This is a problem because if we start a whole new design, I would have to possibly chancing a lot of the work I have done already. 
How are you planning on solving?: 
	Seeing if there are ways we can work around our current design so I do not have to start from scratch, and trying to find more simple outlooks.
General Notes: 
Control a Relay with Arduino and Hall Effect Sensor
The circuit diagram for controlling a 5V Relay Module with Hall Effect Sensor and Arduino is shown below.

Code
const int ledPin = 10;
const int hallPin = 2;
volatile bool ledState = LOW;

void setup() 
{
  pinMode(ledPin,OUTPUT);
  pinMode(hallPin,INPUT);
  attachInterrupt(digitalPinToInterrupt(hallPin), hall_ISR, CHANGE);
}

void loop() 
{
digitalWrite(ledPin, ledState);
}

void hall_ISR() 
{
ledState = !ledState;
}


How To Control a DC Motor with an Arduino 
const int pwm = 2 ;	//initializing pin 2 as pwm
const int in_1 = 8 ;
const int in_2 = 9 ;

//For providing logic to L298 IC to choose the direction of the DC motor 

void setup()
{
pinMode(pwm,OUTPUT) ;  	//we have to set PWM pin as output
pinMode(in_1,OUTPUT) ; 	//Logic pins are also set as output
pinMode(in_2,OUTPUT) ;
}

void loop()
{
//For Clock wise motion , in_1 = High , in_2 = Low

digitalWrite(in_1,HIGH) ;
digitalWrite(in_2,LOW) ;
analogWrite(pwm,255) ;

/*setting pwm of the motor to 255
we can change the speed of rotaion
by chaning pwm input but we are only
using arduino so we are using higest
value to driver the motor  */

//Clockwise for 3 secs
delay(3000) ; 		

//For brake
digitalWrite(in_1,HIGH) ;
digitalWrite(in_2,HIGH) ;
delay(1000) ;

//For Anti Clock-wise motion - IN_1 = LOW , IN_2 = HIGH
digitalWrite(in_1,LOW) ;
digitalWrite(in_2,HIGH) ;
delay(3000) ;

//For brake
digitalWrite(in_1,HIGH) ;
digitalWrite(in_2,HIGH) ;
delay(1000) ;
 }

How to get stepper motor to run for x time
I have this code which I found on Google, which runs based on number of steps, but want to not use steps as a method of running. I want to get the stepper motor to stop after x amount of time that I set it to.
void loop() 
{
  spin(150000,100);
  exit(0); 
}
void spin(unsigned long steps, int sspeed)
{
  while(steps>0)
  {
digitalWrite(3, HIGH);
delayMicroseconds(40);
digitalWrite(3, LOW);
delayMicroseconds(40);
//delayMicroseconds(sspeed);
Steps--;
  }
}
Snip of python code for GUI interface 
FONT = (('Times New Roman'), 20)
class SpiceApp(Tk)
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

   #SERVO MOTOR CODE
# will be turning the augerl to dispense spice
#not very intuitive. This just allows me to run the code and the servo spins until the time it has been told to stop. In this case 10 seconds. 
#this code will need to be modified to work with the the Force Sensitive Resistor of the tray in order to stop the motor when enough pressure in weight has been put in the trayl. 

import RPI.GPIO as GPIO
import time
import sys              #library to use command line args

pin = 18     			#on pin 18
n = sys.argv[1]         #sets n to whatever the value is after calling the python code
n = int(n)              #sets n to an interger since the command line arg is taken as a string

GPIO.setmode(GPIO.BCM)
GPIO.setup(18.GPIO.OUT)		#send signal out to the servo
p= GPIO.PWM(pin,60)		#pwm is for pulse width modulation, the signal sent out to this servo is supposed to be 60Hz frequency 
time.sleep(n)              #change the offset to n so that the servo will run for n seconds
p.stop()
GPIO.cleanup()

Conclusion:
The Spice Girls team met regularly for our team meetings on most Fridays, sometimes on weekends. I performed a further study on the functions required to operate the motor and worked on the GUI with Jacob, testing functions on sample codes I discovered relevant to the project. Learn more about how the hardware in our project works and what the stages are, narrow down the huge range of options to implement the motor controls, and begin coding or getting a concept of what will be done. There are so many possibilities for how we'll run the gadget that it's difficult to keep track of them all. 
