#include "stm32f10x.h"
#include "stm32f10x_rcc.h"
#include "stm32f10x_gpio.h"

#include "spi.h"
#include "stepper.h"
#include "utils.h"

/* Initialization Fuction Declarations */

int main(void){

        RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOC, ENABLE);
        GPIOC->CRH = 0x44344444;
        GPIOC->BSRR = GPIO_BSRR_BS13;

        initDelay();
        
        initSpiSlave();

        initStepper();

        while(1){
                //GPIOC->BSRR = GPIO_BSRR_BS13;
                //delay_ms(100);
                //GPIOC->BSRR = GPIO_BSRR_BR13;
                //delay_ms(100);
        }
}
