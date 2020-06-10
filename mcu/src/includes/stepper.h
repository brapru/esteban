#ifndef __STEPPER_H
#define __STEPPER_H

#include "stm32f10x_gpio.h"
#include "stm32f10x_tim.h"
#include "stm32f10x_rcc.h"

#define STEPPER_DIR     GPIO_Pin_5
#define STEPPER_STEP    GPIO_Pin_6
#define CLOCK           Bit_SET
#define COUNTER         Bit_RESET

#define MAX_RELOAD      0xFFFF

void initStepper(void);

void initStepperRCC(void);
void initStepperTimer(uint16_t frequency, uint16_t duty);
void initStepperPWMChannel(void);
void initStepperGPIO(void);

void stepTest(void);

#endif
