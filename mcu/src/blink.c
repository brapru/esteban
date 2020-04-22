#include "stm32f10x.h"

void delay(long cycles){
        while(cycles>0)
          cycles--;
}

void init(void){
        RCC->APB2ENR |= RCC_APB2ENR_IOPAEN | RCC_APB2ENR_IOPBEN | RCC_APB2ENR_IOPCEN;
        GPIOC->CRH = 0x44344444;
}

int main(void){
        init();

        while(1){
                GPIOC->BSRR = GPIO_BSRR_BS13;
                delay(50000);
                GPIOC->BSRR = GPIO_BSRR_BR13;
                delay(50000);
        }
}
