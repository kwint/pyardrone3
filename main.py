import libardrone
import time

dr = libardrone.ARDrone()
print("1")
dr.takeoff()
print("2")
time.sleep(5)
print("3")
dr.land()
print("4")
dr.halt()