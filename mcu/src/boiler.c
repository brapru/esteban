#include "boiler.h"

/* 
 * The boiler is simply controlled by the Sunfounder DC 5V Relay Module. 
 * The MCU provides 5V to power the relay switch, and the data signal is sent to the IN2 line of the relay switch.
 *
 * The RPI is keeping track of the temperature of the water. When a brew is started, the RPI will send a command
 * to start the boiler. When the target temperature is reached, the RPI will send a command to the MCU to turn off the boiler.
 * 
 * We can simply control the state of the boiler by writing a low/high bit to IN2 line.
 * */

void initBoilerRCC(void){
        RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOB, ENABLE);
}

void initBoilerGPIO(void){
        GPIO_InitTypeDef GPIO_InitStructure;

        GPIO_InitStructure.GPIO_Pin = BOILER_GPIO;
        GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
        GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP;
        GPIO_Init(GPIOB, &GPIO_InitStructure);
}

void initBoiler(void){
        initBoilerRCC();
        initBoilerGPIO();

        /* Boiler should be off on initialization */
        GPIO_WriteBit(GPIOB, BOILER_GPIO, Bit_SET);
};

/* Callback Functions  */

/* 
 * This callback function is a part of the boiler device struct. It's called within the SPI interrupt context. 
 * If the MCU receives a command to turn on, it will set the line to high. To turn off, set the line to low.
 * BOILER_GPIO here is configured for B13 of the MCU, see includes/boiler.h
 * */
void changeBoilerState(uint8_t state){
        GPIO_WriteBit(GPIOB, BOILER_GPIO, state);
}
