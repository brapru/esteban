#include "stm32f10x.h"
#include "stm32f10x_rcc.h"
#include "stm32f10x_gpio.h"
#include "stm32f10x_spi.h"

#include "spi.h"

/* Initialization Fuction Declarations */
void ConfigureRCC(void);
void ConfigureGPIO(void);

void initSPI1Slave(void){
        
        ConfigureRCC();
        ConfigureGPIO();
        ConfigureSPI();

}

int main(void){
        initSPI1Slave();

        while(1){
                __WFI();
        }
}

void ConfigureRCC(void){
        /* SPI 1 clock enable  */
        RCC_APB2PeriphClockCmd(RCC_APB2Periph_SPI1 | RCC_APB2Periph_AFIO | RCC_APB2Periph_GPIOA, ENABLE);
}

void ConfigureGPIO(void){
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
