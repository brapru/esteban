#include "devices.h"
#include "esteban.h"

void createNewDevice(struct device *device, uint8_t id, uint8_t state, uint8_t direction, uint8_t speed, deviceFunc *state_handler, deviceFunc *direction_handler, deviceFunc *speed_handler){
        /* === Initalize the Device === */ 
        device->id = id;
        device->state = state;
        device->direction = direction;
        device->speed = speed;
        
        /* === Callback Handler Function ===  */
        device->state_handler = state_handler;
        device->direction_handler = direction_handler;
        device->speed_handler = speed_handler;
}

struct device *getDeviceFromID(uint8_t id){
        switch(id){
                case LEDID:     return &esteban.led;    break;
                case PUMPID:    return &esteban.pump;   break;
                case BOILERID:  return &esteban.boiler; break;
        }
}

void changeLedState(uint8_t state){
        GPIO_WriteBit(GPIOC, GPIO_Pin_13, state);
}

void changePumpState(uint8_t state){
        TIM_Cmd(TIM4, state);
}

void changePumpDirection(uint8_t direction){
        if (esteban.pump.state & OFF){
                TIM_Cmd(TIM4, DISABLE);
                delay_ms(10);
                GPIO_WriteBit(GPIOB, STEPPER_DIR, direction);
                TIM_Cmd(TIM4, ENABLE);
        }else{
                GPIO_WriteBit(GPIOB, STEPPER_DIR, direction);
        }
}

void changePumpSpeed(uint8_t speed){
        TIM4->ARR = speed;
}

void getDeviceInfo(struct command *cmd){
        cmd->response = "TEST"; 
}
