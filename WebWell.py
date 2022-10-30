import configparser
import logging
import RPi.GPIO as GPIO
import zlib
import schedule

configFile = "WebWell.ini"
myLogFile = "WebWell.log"
testInterval = "00:00:01"
windowOpen = "01:01:00"
windowClose = "01:00:00"
lvlBottom = 10.0
lvlTop = 7.0


def loadConfig (file = configFile):
    config = configparser.RawConfigParser()
    config.read(file)
    logging.debug("Loading configuration from %s", file)
    
    for e in config.sections():
        if e == "Global":
            global testInterval
            global windowOpen
            global windowClose
            global lvlBottom
            global lvlTop
        
            testInterval = config["Global"]["testInterval"]
            windowOpen = config["Global"]["windowOpen"]
            windowClose = config["Global"]["windowClose"]
            lvlBottom = config["Global"]["lvlBottom"]
            lvlTop = config["Global"]["lvlTop"]
        
            logging.debug("Loaded global settings")
      


def crc(fileName):
    prev = 0

    for eachLine in open(fileName,"rb"):
        prev = zlib.crc32(eachLine, prev)
    return "%X"%(prev & 0xFFFFFFFF)



def jobCheckConfig():
    global configCRC

    if configCRC == crc(configFile):
        logging.debug("Configuration unchaged")
    else:
        logging.debug("Configuration chaged! Reloading...")

        ReLoadConfig()
        configCRC = crc(configFile)



def setSchedule():
    schedule.every(1).minutes.do(jobCheckConfig)
 

      
if __name__ == '__main__':
    logging.basicConfig(filename=myLogFile, format='%(asctime)s - %(message)s', level=logging.INFO, datefmt='%y/%m/%d %H:%M:%S')
    logging.getLogger('schedule').setLevel(logging.DEBUG)
    
    loadConfig(configFile)
    configCRC = crc(configFile)

    setSchedule()

    GPIO.setmode(GPIO.BCM)

    def shutdown():
        logging.info("Normal shutdown...")
        GPIO.cleanup()
        exit(signal.SIGTERM)
