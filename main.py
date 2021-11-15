from flask import Flask, render_template, request, url_for, redirect
import datetime
from time import sleep
import RPi.GPIO as GPIO



class JunkTransporter:
   def __init__(self):
      self.weight = 0
      self.position = [0,0]
      self.battery = 100
      self.isOpen = True
      
   def move(self):
      pass
   def changeDirection(self):
      pass

   def backToStart(self):
      pass
   
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

junkTransporter = JunkTransporter()
trashSensor = Sensor(1, "detect_trash")
obstacleSensor = Sensor(2, "detect_obstancle")

# import RPi.GPIO as GPIO
# import os
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
   # pass in as json dictionary
   return render_template('index.html')

@app.route('/start_junk_transporter', methods=['GET', 'POST'])
def startRobot():
   print("Starting the Junk Transporter!")
   return "Starting junk transporter"

@app.route('/stop_junk_transporter', methods=['GET', 'POST'])
def stopRobot():
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


