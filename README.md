# Automated Pourover Coffee Machine

An embedded systems project to automatically pour a great cup of coffee.

## Raspberry Pi Zero W: 
Runs a Flask API server to handle mobile app API calls. Stores pour profiles,
user preferences, and more in the local database. Interfaces with the MCU over
the SPI protocol to send commands from the STMSPI library.

## STM32F103C8T6 Microcontroller
SPI Slave to the Raspberry Pi. Waits for commands, and executes them to control
speed and direction of DC pumps.
