#include "stm32f10x.h"
#include "stm32f10x_rcc.h"
#include "stm32f10x_gpio.h"
#include "stm32f10x_spi.h"

#include "spi.h"
#include "stepper.h"
#include "utils.h"

/* Initialization Fuction Declarations */
void ConfigureRCC(void);
void ConfigureGPIO(void);


void initSPI1Slave(void){
        
        ConfigureRCC();
        ConfigureGPIO();
        ConfigureSPI();

        GPIOC->CRH = 0x44344444;

}

int main(void){

        initDelay();
        
        initSPI1Slave();
        
        initStepperGPIO();
        initStepperTimer();
        initStepperPWMChannel(); 

        // Set direction bit for PWM to clockwise
        GPIO_WriteBit(GPIOB, STEPPER_DIR, CLOCK);

        while(1){
                GPIOC->BSRR = GPIO_BSRR_BS13;
                delay_ms(1000);
                GPIOC->BSRR = GPIO_BSRR_BR13;
                delay_ms(1000);
                //stepTest();
        }
}

void ConfigureRCC(void){
        
        /* SPI 1 clock enable */
        RCC_APB2PeriphClockCmd(RCC_APB2Periph_SPI1 | RCC_APB2Periph_AFIO | RCC_APB2Periph_GPIOC, ENABLE);

}

void ConfigureGPIO(void){

        RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA, ENABLE);

        GPIO_InitTypeDef GPIO_InitStructure;

        /* Initialize PA5 SCK1 with open-drain (50Mhz) */
        GPIO_InitStructure.GPIO_Pin = GPIO_Pin_5;
        GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF_OD; 
        GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
        GPIO_Init(GPIOA, &GPIO_InitStructure);

        /* Initialize PA6 MISO1 with push-pull (50MHz) */
        GPIO_InitStructure.GPIO_Pin = GPIO_Pin_6;
        GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF_PP;
        GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
        GPIO_Init(GPIOA, &GPIO_InitStructure);
       
        /* Initialize PA7 MOSI1 with open-drain (50MHz) */
        GPIO_InitStructure.GPIO_Pin = GPIO_Pin_7;
        GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF_OD;
        GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
        GPIO_Init(GPIOA, &GPIO_InitStructure);

}
