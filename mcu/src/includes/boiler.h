#ifndef __BOILER_H
#define __STEPPER_H

#include "stm32f10x_gpio.h"
#include "stm32f10x_rcc.h"

#define BOILER_GPIO     GPIO_Pin_13
#define BOILER_ON       Bit_SET
#define BOILER_OFF      Bit_RESET

void initBoilerRCC(void);
void initBoilerGPIO(void);
void initBoiler(void);

void changeBoilerState(uint8_t state);

#endif
