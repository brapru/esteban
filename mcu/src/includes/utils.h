#ifndef __UTILS_H
#define __UTILS_H

#include "stm32f10x.h"

__IO uint32_t time_us, time_ms;

void initDelay(void);
void delay_ms(uint32_t ms_delay);
void delay_us(uint32_t us_delay);

void SysTick_Handler(void);

#endif
