#ifndef __COMMANDS_H
#define __COMMANDS_H

#include "stm32f10x.h"


#define DEVICE_ID_SIZE          3
#define BUFFERSIZE              11

#define NONE                    0
#define STATE                   1
#define SPEED                   2
#define DIRECTION               3

#define UPDATE_COMMAND_TYPE     '$' 
#define INFO_COMMAND_TYPE       '*' 
#define ERROR_COMMAND_TYPE      '-'

struct command {
        uint8_t type;

        char deviceID[4]; /* 3 letter unique device identifier */
        uint8_t setting;
        uint8_t update;

        //bool responseRequired;
        //char *response;
};

void parseCommand(uint8_t *buffer, struct command *cmd);

#endif
