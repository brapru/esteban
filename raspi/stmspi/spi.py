#!/usr/bin/env python3

import stmspi as stm

class bcolors:
    OKRED = '\33[91m'
    OKGREEN = '\033[92m'
    OKYELL = '\33[93m'
    OKBLUE = '\033[94m'
    ENDC = '\033[0m'


on = [0x6F, 0x6E, 0xA]
off = [0x6F, 0x66, 0x66, 0xA]

CLOCK = 0
COUNTERCLOCK = 1

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
            rpi.setPumpState(1)
        
        elif ledstate == "off":
            print(f"{bcolors.OKRED}[{bcolors.OKYELL}*{bcolors.OKRED}]{bcolors.ENDC} LED: {bcolors.OKRED}OFF{bcolors.ENDC}")
            rpi.setPumpState(0)
        
        elif ledstate == "clock":
            rpi.setPumpDirection(CLOCK)
        
        elif ledstate == "counter":
            rpi.setPumpDirection(COUNTERCLOCK)
       
        elif ledstate == "speed":
            speed = input("\tset the speed: ")
            rpi.setPumpSpeed(int(speed))

        else:
            numb = 0

if __name__ == "__main__":
    main()
