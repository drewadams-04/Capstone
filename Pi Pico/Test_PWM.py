import machine
import utime
from machine import Pin, PWM

# set GP0 to PWM output
pwm = PWM(Pin(0))
# Set PWM frequency to 125 kHz
pwm.freq(125_000)

# Set duty cycle to 50%
# the range is 0-65535, 50% -> 32768
pwm.duty_u16(32768)

print("PWM running on GP0")
print("Frequency: 125 kHz")
print("Duty cycle: 50%")

# Blink LED to see if code is flashed

# Set up the onboard LED pin
led = machine.Pin("LED", machine.Pin.OUT)

# Loop forever, turning the LED on and off
while True:
    led.value(1)  # Turn LED on
    utime.sleep(1)  # Wait 1 second
    led.value(0)  # Turn LED off
    utime.sleep(1)  # Wait 1 second
