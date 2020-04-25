#include "stepper.h"
#include "utils.h"

void initStepperTimer(void){
        RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM4, ENABLE);
        
        TIM_TimeBaseInitTypeDef timerInitStruct;
        timerInitStruct.TIM_Prescaler = 40000;
        timerInitStruct.TIM_CounterMode = TIM_CounterMode_Up;
        timerInitStruct.TIM_Period = 500;
        timerInitStruct.TIM_ClockDivision = TIM_CKD_DIV1;
        timerInitStruct.TIM_RepetitionCounter = 0;

        TIM_TimeBaseInit(TIM4, &timerInitStruct);
        TIM_Cmd(TIM4, ENABLE);
}

void initStepperPWMChannel(void){
	
	TIM_OCInitTypeDef timerOCInitStruct = {0,};
	
	timerOCInitStruct.TIM_OCMode = TIM_OCMode_PWM1;
	timerOCInitStruct.TIM_Pulse = 400;
	timerOCInitStruct.TIM_OutputState = TIM_OutputState_Enable;
	timerOCInitStruct.TIM_OCPolarity = TIM_OCPolarity_High;
	
	TIM_OC1Init(TIM4, &timerOCInitStruct);
	TIM_OC1PreloadConfig(TIM4, TIM_OCPreload_Enable);
    
}

void initStepperGPIO(void){
        
        RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOB, ENABLE);

        GPIO_InitTypeDef GPIO_InitStructure;
        
        GPIO_InitStructure.GPIO_Pin = STEPPER_STEP | STEPPER_DIR;
        GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
        GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP;
        
        GPIO_Init(GPIOB, &GPIO_InitStructure);
}

void stepTest(void){
        /* Start direction clock wise */
        GPIO_WriteBit(GPIOB, STEPPER_DIR, CLOCK);
        for(int i = 0;i <= 2000; i++){
                GPIO_WriteBit(GPIOB, STEPPER_STEP, Bit_SET);
                delay_ms(2000);
                GPIO_WriteBit(GPIOB, STEPPER_STEP, Bit_RESET);
                delay_ms(2000);
        }

        delay_ms(1000);

        /* Start direction counter clock wise */
        GPIO_WriteBit(GPIOB, STEPPER_DIR, COUNTER);
        for(int i = 0;i <= 2000*2; i++){
                GPIO_WriteBit(GPIOB, STEPPER_STEP, Bit_SET);
                delay_ms(1000);
                GPIO_WriteBit(GPIOB, STEPPER_STEP, Bit_RESET);
                delay_ms(1000);
        }

}
