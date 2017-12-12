#!/usr/bin/env python
# coding: Latin-1

#############################################################
# This is the module which holds all the global values      #
#############################################################

# General values
badFrameCount = 0
frameCounter = 0
frameAnnounce = 0
running = True
frameTimes = []
lastFrameStamp = 0
trackFound = False
lastLines = []
lapCount = 0
lapTravelled = 0.0
frontRobot = True
skipLights = False

# Defaults for values set from the Race Code Functions
userSpeed = 100.0
userTargetLane = 0.0

# States
startLights = 0
imageMode = 0
lastImageMode = 0
seenStart = False
startWaitCount = 0
pollDelay = 0.01
processingWriteLogLevel = 3
processingPrintLogLevel = 2

# Images
displayFrame = None
displayPredator = None
lastRawFrame = None

# Threads and locks
processorPool = []
controller = None
frameLock = None

# Functions
MonsterLed = None
MonsterMotors = None

# Other resources
capture = None
userLogFile = None
processingLogFile = None

# These are the values transmitted to the other robot
dataToSend = {
		'front':'true',
		'lap-count':'0',
		'mode':'0',
		'lights':'0',
}

# These are the values received from the other robot
dataReceived = {}
