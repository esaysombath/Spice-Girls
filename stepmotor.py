import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib     # Use sudo pip3 install rpimotorlib
import time
from time import sleep

# First Iteration of code
direction = 22
step = 23
EN_pin = 24

# Pass GPIO pins numbers and the motor type
run_motor = RpiMotorLib.A4988Nema(direction, step(21, 21, 21), 'A4988')
GPIO.setup(EN_pin, GPIO.OUT)

# Pull enable to low to enable motor
GPIO.output(EN_pin, GPIO.LOW)

run_motor.motor_go(True,   # True = Clockwise, False = Counter
                   'Full',  # Step Type
                   200,     # Number of steps (200 for 360 deg)
                   .0005,   # Step delay (Sec)
                   Flase,   # True = print verbose output (Debugging)
                   .05)     # Initial delay (Sec)

# Clear GPIO allocations
GPIO.cleanup()

# Second Iteration of code
DIR = 20
STEP = 21
CW = 1      # Clockwise
CCW = 0     # Counter
Step_Rate = 200

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)

# Microstep aka full, half. Pins are to M1, m2, m3
MODE = (14, 15, 18)
GPIO.setup(MODE, GPIO.OUT)
Seq = {'Full': (0, 0, 0)}
GPIO.output(MODE, Seq['Full'])

step_count = Step_Rate
delay = 0.0208

for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)


# # Set Pin layout on Pi
# GPIO.setmode(GPIO.BOARD)
#
# # GPIO Pins A,B,C,D for full step
# control_pins = [5, 6, 13, 19]
#
# # Setting Pins as output
# for pin in control_pins:
#     GPIO.setup(pin, GPIO.OUT)
#     GPIO.output(pin, 0)
#
# Sequence = [[0, 1, 0, 1], [0, 1, 1, 0],
#             [1, 0, 1, 0], [1, 0, 0, 1]]
#
# global location
# location = 0
#
# rotation_needed = 0
# rotation_count = 0
#
#
# def pepper():
#     global location
#     location = 8        # Angle 45, 360/8
#     rotation_needed == 0
#
#     rotation_needed = location
#     rotation_count = 200 / rotation_needed
