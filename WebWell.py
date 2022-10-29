import configparser
import logging
import RPi.GPIO as GPIO

configFile = "WebWell.ini"

def loadConfig (file = configFile):
    config = configparser.RawConfigParser()
    config.read(file)
    logging.debug("Loading configuration from %s ***", file)
    
    for e in config.selections():
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