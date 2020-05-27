#include "commands.h"
#include "string.h"

void parseCommand(uint8_t *buffer, struct command *cmd){

        cmd->type = buffer[0];
        
        // Check if cmd->type is of valid type before setting to variable
        if ((cmd->type != UPDATE_COMMAND_TYPE) && (cmd->type != INFO_COMMAND_TYPE))
                // set_error("Incorrect command type");         
                return;
                
        memcpy(&cmd->deviceID, &buffer[1], DEVICE_ID_SIZE);

        if (cmd->type == INFO_COMMAND_TYPE){
                cmd->setting = NONE;
                cmd->update = NONE;
                return;         
        }

        cmd->setting = buffer[5];
        cmd->update = buffer[7];

}
