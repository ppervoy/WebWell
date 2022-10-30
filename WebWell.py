import configparser
import logging
import RPi.GPIO as GPIO

configFile = "WebWell.ini"
testInterval = "00:00:01"
windowOpen = "01:01:00"
windowClose = "01:00:00"


def loadConfig (file = configFile):
    config = configparser.RawConfigParser()
    config.read(file)
    logging.debug("Loading configuration from %s", file)
    
    for e in config.sections():
        if e == "Global":
            global testInterval
            global windowOpen
            global windowClose
        
            testInterval = config["Global"]["testInterval"]
            windowOpen = config["Global"]["windowOpen"]
            windowClose = config["Global"]["windowClose"]
        
            logging.debug("Loaded global settings")
      
      
      
GPIO.setmode(GPIO.BCM)
loadConfig(configFile)
