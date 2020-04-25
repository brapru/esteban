#include "utils.h"

void initDelay(void){
        SystemCoreClockUpdate();
        SysTick_Config(SystemCoreClock/1000000);
}

void delay_us(uint32_t us_delay){
        time_us = us_delay;
        while (time_us);
}
        
void delay_ms(uint32_t ms_delay){
        time_ms = ms_delay;
        while (time_ms--)
                delay_us(1000);
}

void SysTick_Handler(void) {
        if(time_us)
                time_us--;
}
