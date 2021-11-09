from flask import Flask, render_template, request, url_for, redirect
import datetime


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
      pass
   
   def closeTrash(self):
      pass

   def getCurrentWeight(self):
      return self.weight
   
   def updateWeight(self, modifier):
      self.weight = self.weight - modifier
      return self.weight
      

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
   return "Opening junk transporter"

@app.route('/close_junk_transporter', methods=['GET', 'POST'])
def closeRobot():
   print("Closing the Junk Transporter!")
   return "Closing junk transporter"

def start():
   pass

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)


