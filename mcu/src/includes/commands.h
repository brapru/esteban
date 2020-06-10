#ifndef __COMMANDS_H
#define __COMMANDS_H

#include "stm32f10x.h"
#include "devices.h"

#define DEVICE_ID_SIZE          3
#define BUFFERSIZE              11
#define RESPONSESIZE            8

#define NONE                    0
#define STATE                   1
#define SPEED                   2
#define DIRECTION               3

#define UPDATE_COMMAND_TYPE     '$' 
#define INFO_COMMAND_TYPE       '*' 
#define ERROR_COMMAND_TYPE      '-'

struct command;
struct device;

struct command {
        
        uint8_t type;

        uint8_t device_id; /* Numeric unique device identifier */
        uint8_t setting;
        uint8_t update;

        char *response;

};

void parseCommand(uint8_t *buffer, struct command *cmd);
void handleCommand(struct command *cmd);
void resetCommand(struct command *cmd);

#endif
