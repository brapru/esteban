#ifndef __DEVICES_H
#define __DEVICES_H

#include "commands.h"

#define ON              0
#define OFF             1

#define LEDID           1
#define PUMPID          2

#define SPEEDLOW        1       
#define SPEEDMID        2
#define SPEEDHIGH       3
#define SPEEDVHIGH      4

#define STATE           1
#define SPEED           2
#define DIRECTION       3

struct device;
struct command;

/* === Callback function for handling commands  === */
typedef void deviceFunc(uint8_t update);

struct device {
        
        uint8_t id; /* 3 letter unique device identifier */
        uint8_t state;
        uint8_t direction;
        uint8_t speed;
        
        deviceFunc *state_handler;
        deviceFunc *direction_handler;
        deviceFunc *speed_handler;

};

void createNewDevice(struct device *device, uint8_t id, uint8_t state, uint8_t direction, uint8_t speed, deviceFunc *state_handler, deviceFunc *direction_handler, deviceFunc *speed_handler);

struct device *getDeviceFromID(uint8_t id);
void getDeviceInfo(struct command *cmd);

/* === Device Handlers === */
void changeLedState(uint8_t state);
void changePumpState(uint8_t state);
void changePumpDirection(uint8_t direction);
void changePumpSpeed(uint8_t speed);

#endif
