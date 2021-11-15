from flask import Flask, render_template, request, url_for, redirect
import datetime
from time import sleep
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

r_in1 = 27
r_in2 = 22
r_en = 4

l_in1 = 5
l_in2 = 6
l_en = 13

class JunkTransporter:
   def __init__(self):
      self.weight = 0
      self.position = [0,0]
      self.battery = 100
      self.isOpen = True
   
   def openTrash(self):
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(25, GPIO.OUT)
      pwm = GPIO.PWM(25, 50)
      pwm.start(5)
      pwm.ChangeDutyCycle(5)
      sleep(3)
      pwm.ChangeDutyCycle(7.5)
      sleep(1)
      pwm.ChangeDutyCycle(50)
      pwm.stop()
      GPIO.cleanup()

class Response:
   def __init__(self):
      self.direction = 0.0 
      self.numberOfUnits = 0

   def printResponse(self):
      print("Direction", )

class Sensor:
   def __init__(self, modelNumber, sensorType):
      self.modelNumber = modelNumber
      self.sensorType = sensorType
      
   def detectObject(self):
      pass

   def distance(self):
      GPIO.setmode(GPIO.BCM)
 
      #set GPIO Pins
      GPIO_TRIGGER = 18
      GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
      GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
      GPIO.setup(GPIO_ECHO, GPIO.IN)
      # set Trigger to HIGH
      GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
      time.sleep(0.00001)
      GPIO.output(GPIO_TRIGGER, False)
 
      StartTime = time.time()
      StopTime = time.time()
 
    # save StartTime
      while GPIO.input(GPIO_ECHO) == 0:
         StartTime = time.time()
 
    # save time of arrival
      while GPIO.input(GPIO_ECHO) == 1:
         StopTime = time.time()
 
    # time difference between start and arrival
      TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
      distance = (TimeElapsed * 34300) / 2
      GPIO.cleanup()
      return distance
   
junkTransporter = JunkTransporter()
obstacleSensor = Sensor(2, "detect_obstacle")

# import RPi.GPIO as GPIO
# import os
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
   return render_template('index.html')

@app.route('/start_junk_transporter', methods=['GET', 'POST'])
def startRobot():
   
   print("Starting the Junk Transporter!")
   counter = 0
   while(True):
      if counter == 10:
         break
      distance = obstacleSensor.distance()
      print(distance)
      if (distance <= 10):
         junkTransporter.openTrash()
      counter = counter + 1
      sleep(1)
   #set GPIO Pins
      
   return "Starting junk transporter"

@app.route('/stop_junk_transporter', methods=['GET', 'POST'])
def stopRobot():
   GPIO.cleanup()
   print("Stopping the Junk Transporter!")
   return "Stopping junk transporter"

@app.route('/open_junk_transporter', methods=['GET', 'POST'])
def openRobot():
   print("Opening the Junk Transporter!")
   junkTransporter.openTrash()
   return "Opening junk transporter"

def start():
   pass

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)




