#!/usr/bin/env python3

import stmspi as stm

class bcolors:
    OKRED = '\33[91m'
    OKGREEN = '\033[92m'
    OKYELL = '\33[93m'
    OKBLUE = '\033[94m'
    ENDC = '\033[0m'


ON = 1
OFF = 0
CLOCK = 0
COUNTER = 1

def instructions():
    print(f"{bcolors.OKRED}[{bcolors.OKYELL}***{bcolors.OKRED}] SPI Communications Test[{bcolors.OKYELL}***{bcolors.OKRED}]\nEnter 0 to turn ON or 1 for OFF{bcolors.ENDC}")

def main():

    instructions()

    rpi = stm.RpiController(0)
    
    while True:
        ledstate = input("brapru> ")
     
        if ledstate == "exit":
            quit()
        
        elif ledstate == "on":
            print(f"{bcolors.OKRED}[{bcolors.OKYELL}*{bcolors.OKRED}]{bcolors.ENDC} LED: {bcolors.OKGREEN}ON{bcolors.ENDC}")
            rpi.setDeviceState(rpi.led, ON)
<<<<<<< HEAD

        elif ledstate == "off":
            print(f"{bcolors.OKRED}[{bcolors.OKYELL}*{bcolors.OKRED}]{bcolors.ENDC} LED: {bcolors.OKRED}OFF{bcolors.ENDC}")
            rpi.setDeviceState(rpi.led, OFF)

        elif ledstate == "clock":
            rpi.setDeviceDirection(rpi.peristaltic, CLOCK)

        elif ledstate == "counter":
            print(COUNTER)
            rpi.setDeviceDirection(rpi.peristaltic, COUNTER)

        elif ledstate == "speed":
            speed = input("\tset the speed: ")
            rpi.setDeviceSpeed(rpi.peristaltic, int(speed))

        elif ledstate == "status":
            print(rpi.getDeviceStatus(rpi.led))
=======
        
        elif ledstate == "off":
            print(f"{bcolors.OKRED}[{bcolors.OKYELL}*{bcolors.OKRED}]{bcolors.ENDC} LED: {bcolors.OKRED}OFF{bcolors.ENDC}")
            rpi.setDeviceState(rpi.led, OFF)
        
        elif ledstate == "clock":
            rpi.setDeviceDirection(rpi.peristaltic, CLOCK)
        
        elif ledstate == "counter":
            rpi.setDeviceDirection(rpi.peristaltic, COUNTER)
       
        elif ledstate == "speed":
            speed = input("\tset the speed: ")
            print(type(speed))
            #rpi.setDeviceSpeed(rpi.peristaltic, int(speed))
>>>>>>> development

        else:
            numb = 0

if __name__ == "__main__":
    main()
