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

def instructions():
    print(f"{bcolors.OKRED}[{bcolors.OKYELL}***{bcolors.OKRED}] SPI Communications Test[{bcolors.OKYELL}***{bcolors.OKRED}]\nEnter 1 to turn ON or 0 for OFF{bcolors.ENDC}")

def main():

    instructions()

    rpi = stm.RpiController(0)

    while True:
        ledstate = input("brapru> ")
     
        if ledstate == "exit":
            quit()
        elif ledstate == "0":
            print(f"{bcolors.OKRED}[{bcolors.OKYELL}*{bcolors.OKRED}]{bcolors.ENDC} LED: {bcolors.OKGREEN}ON{bcolors.ENDC}")
            #spi.writebytes([0])
            #spi.xfer2([0x6F]) # switch it on
            rpi.setLed(0)
        elif ledstate == "1":
            print(f"{bcolors.OKRED}[{bcolors.OKYELL}*{bcolors.OKRED}]{bcolors.ENDC} LED: {bcolors.OKRED}OFF{bcolors.ENDC}")
            #spi.xfer2([0x66]) # switch it on
            #spi.writebytes([1])
            rpi.setLed(1)
        elif ledstate == "get led":
            rpi.getState("led")
        
        else:
            numb = 0

if __name__ == "__main__":
    main()
