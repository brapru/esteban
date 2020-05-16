#ifndef __STEPPER_H
#define __STEPPER_H

#include "stm32f10x_gpio.h"
#include "stm32f10x_tim.h"
#include "stm32f10x_rcc.h"

#define STEPPER_DIR GPIO_Pin_8
#define STEPPER_STEP GPIO_Pin_9
#define CLOCK Bit_SET
#define COUNTER Bit_RESET

void initStepperTimer(void);
void initStepperPWMChannel(void);
void initStepperGPIO(void);

void stepTest(void);

#endif
