#include "stepper.h"
#include "utils.h"

void initStepperRCC(void){
        
        RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM4, ENABLE);
        RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOB, ENABLE);

}

void initStepperTimer(uint16_t frequency, uint16_t duty){
        uint32_t Cycles = SystemCoreClock / frequency;
        uint16_t PSC_Value = (uint16_t)(Cycles / MAX_RELOAD + 1);
        uint16_t ARR_Value = (uint16_t)((Cycles + (PSC_Value / 2)) / PSC_Value);
        uint16_t Pulse = (uint16_t)(ARR_Value * duty)/100;

        TIM_TimeBaseInitTypeDef timerInitStruct;
        timerInitStruct.TIM_Prescaler = PSC_Value;
        timerInitStruct.TIM_CounterMode = TIM_CounterMode_Up;
        timerInitStruct.TIM_Period = ARR_Value;
        timerInitStruct.TIM_ClockDivision = 0;
        timerInitStruct.TIM_RepetitionCounter = 0;

        TIM_TimeBaseInit(TIM4, &timerInitStruct);
        TIM_Cmd(TIM4, ENABLE);
	
	TIM_OCInitTypeDef timerOCInitStruct;
	
	timerOCInitStruct.TIM_OCMode = TIM_OCMode_PWM1;
	timerOCInitStruct.TIM_Pulse = Pulse;
	timerOCInitStruct.TIM_OutputState = TIM_OutputState_Enable;
	timerOCInitStruct.TIM_OCPolarity = TIM_OCPolarity_High;

	TIM_OC1Init(TIM4, &timerOCInitStruct);
}

void initStepperGPIO(void){
        GPIO_InitTypeDef GPIO_InitStructure;
        
        GPIO_InitStructure.GPIO_Pin = STEPPER_STEP;
        GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
        GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF_PP;
        GPIO_Init(GPIOB, &GPIO_InitStructure);
        
        GPIO_InitStructure.GPIO_Pin = STEPPER_DIR;
        GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
        GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP;
        GPIO_Init(GPIOB, &GPIO_InitStructure);
}

void initStepper(void){
        initStepperRCC();
        initStepperGPIO();
        initStepperTimer(100, 50);

        GPIO_WriteBit(GPIOB, STEPPER_DIR, Bit_SET);
}
