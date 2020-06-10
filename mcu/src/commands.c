#include "commands.h"

void parseCommand(uint8_t *buffer, struct command *cmd){

        cmd->type = buffer[0];
        
        // Check if cmd->type is of valid type before setting to variable
        if ((cmd->type != UPDATE_COMMAND_TYPE) && (cmd->type != INFO_COMMAND_TYPE))
                // TODO: set_error();
                return;
        
        cmd->device_id = buffer[1];

        if (cmd->type == INFO_COMMAND_TYPE){
                cmd->setting = NONE;
                cmd->update = NONE;
                return;         
        }

        cmd->setting = buffer[3];
        cmd->update = buffer[5];

}

void handleCommand(struct command *cmd){
        
        struct device *device = getDeviceFromID(cmd->device_id);

        switch(cmd->setting){
                case STATE:
                        device->state = cmd->update;
                        device->state_handler(device->state);
                        break;
                
                case SPEED:     
                        device->speed = cmd->update;     
                        device->speed_handler(device->speed);
                        break;

                case DIRECTION: 
                        device->direction = cmd->update;
                        device->direction_handler(device->direction);
                        break;
        }
}

void resetCommand(struct command *cmd){
        
        cmd->type = NONE;
        cmd->device_id = NONE;
        cmd->setting = NONE;
        cmd->update= NONE;
        cmd->response = "";

}
