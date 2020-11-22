#include "stm32f10x.h"
#include "stm32f10x_rcc.h"
#include "stm32f10x_gpio.h"

#include <stddef.h>

#include "esteban.h"

/* === Globals === */
struct controller esteban;

/* === Initialization Fuction Declarations === */
void initController(void){
        createNewDevice(&esteban.pump, PUMPID, OFF, 0, 0, changePumpState, changePumpDirection, changePumpSpeed); 
        createNewDevice(&esteban.led, LEDID, OFF, 0, 0, changeLedState, NULL, NULL);
        createNewDevice(&esteban.boiler, BOILERID, OFF, 0, 0, changeBoilerState, NULL, NULL);
}


int main(void){
        /* Debug for on board led */
        RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOC, ENABLE);
        GPIOC->CRH = 0x44344444;
        GPIOC->BSRR = GPIO_BSRR_BS13;

        initDelay();
        initSpiSlave();
        initStepper();
        initBoiler();
        initController();

        while(1){
        }
}
