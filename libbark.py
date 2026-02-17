import os
import time

version = "1.0.0"

def version():
    return version

def check():
    if not os.path.exists("logFile"):
        f = open("logFile","w")
        f.close()
def log(logLevel, logMessage):
    check()
    if logLevel == "0":
        logLevel = "I"
    if logLevel == "1":
        logLevel = "D"
    if logLevel == "2":
        logLevel = "W"
    if logLevel == "3":
        logLevel = "E"

    f = open("logFile","a")
    f.write(logLevel + " " + logMessage + " " + str(round(time.time(),2)) + "\n")
