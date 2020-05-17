#include "stm32f10x_spi.h"
#include "stm32f10x_gpio.h"
#include "stm32f10x_dma.h"
#include "stm32f10x_rcc.h"
#include "misc.h"

#include "spi.h"
#include "utils.h"

/* Private Variables  */
DMA_InitTypeDef DMA_InitStructure;
SPI_InitTypeDef SPI_InitStructure;
NVIC_InitTypeDef NVIC_InitStructure;

uint8_t SPI_SLAVE_Buffer_Rx[BUFFERSIZE];
uint8_t SPI_SLAVE_Buffer_Tx[BUFFERSIZE];

void initSpiRCC(void){
       
        /* PCLK2 = HCLK/2 */ 
        RCC_PCLK2Config(RCC_HCLK_Div2);
  
        /* Enable SPI_SLAVE DMA clock */
        RCC_AHBPeriphClockCmd(SPI_SLAVE_DMA_CLK, ENABLE);

        /* Enable clock and GPIO clock for SPI_SLAVE */
        RCC_APB2PeriphClockCmd(SPI_SLAVE_CLK | SPI_SLAVE_GPIO_CLK | RCC_APB2Periph_AFIO, ENABLE);
}

/* Configure SPI_SLAVE pins: NSS, SCK and MISO */
void initSpiGPIO(void){
        GPIO_InitTypeDef GPIO_InitStructure;

        GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;

        GPIO_InitStructure.GPIO_Pin = SPI_SLAVE_PIN_NSS | SPI_SLAVE_PIN_SCK | SPI_SLAVE_PIN_MOSI;
        GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IN_FLOATING;
        GPIO_Init(SPI_SLAVE_GPIO, &GPIO_InitStructure);

        GPIO_InitStructure.GPIO_Pin =  SPI_SLAVE_PIN_MISO;
        GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF_PP;
        GPIO_Init(SPI_SLAVE_GPIO, &GPIO_InitStructure);
}

void initSpiDMA(void){
        /* SPI_SLAVE_Rx_DMA_Channel configuration */
        DMA_DeInit(SPI_SLAVE_Rx_DMA_Channel);
        DMA_InitStructure.DMA_MemoryBaseAddr = (uint32_t)SPI_SLAVE_Buffer_Rx;
        DMA_InitStructure.DMA_BufferSize = BUFFERSIZE; 
        DMA_InitStructure.DMA_MemoryInc = DMA_MemoryInc_Enable;
        
        //DMA_InitStructure.DMA_PeripheralBaseAddr = (uint32_t)SPI_SLAVE_DR_Base;
        DMA_InitStructure.DMA_PeripheralBaseAddr = (uint32_t)&SPI1->DR;
        DMA_InitStructure.DMA_DIR = DMA_DIR_PeripheralSRC;
        DMA_InitStructure.DMA_PeripheralInc = DMA_PeripheralInc_Disable;
        DMA_InitStructure.DMA_PeripheralDataSize = DMA_PeripheralDataSize_Byte;
        DMA_InitStructure.DMA_MemoryDataSize = DMA_MemoryDataSize_Byte;
        DMA_InitStructure.DMA_Mode = DMA_Mode_Normal;
        DMA_InitStructure.DMA_Priority = DMA_Priority_VeryHigh;
        DMA_InitStructure.DMA_M2M = DMA_M2M_Disable; 

        DMA_Init(SPI_SLAVE_Rx_DMA_Channel, &DMA_InitStructure);

        /* SPI_SLAVE_Tx_DMA_Channel configuration */
        DMA_DeInit(SPI_SLAVE_Tx_DMA_Channel);
        DMA_InitStructure.DMA_MemoryBaseAddr = (uint32_t)SPI_SLAVE_Buffer_Tx; 
        DMA_InitStructure.DMA_BufferSize = BUFFERSIZE;
        DMA_InitStructure.DMA_MemoryInc = DMA_MemoryInc_Enable;

        //DMA_InitStructure.DMA_PeripheralBaseAddr = (uint32_t)SPI_SLAVE_DR_Base;
        DMA_InitStructure.DMA_PeripheralBaseAddr = (uint32_t)&SPI1->DR;
        DMA_InitStructure.DMA_DIR = DMA_DIR_PeripheralSRC;
        DMA_InitStructure.DMA_PeripheralInc = DMA_PeripheralInc_Disable;
        DMA_InitStructure.DMA_PeripheralDataSize = DMA_PeripheralDataSize_Byte;
        DMA_InitStructure.DMA_MemoryDataSize = DMA_MemoryDataSize_Byte;
        DMA_InitStructure.DMA_Mode = DMA_Mode_Normal;
        DMA_InitStructure.DMA_Priority = DMA_Priority_VeryHigh;
        DMA_InitStructure.DMA_M2M = DMA_M2M_Disable;
        
        DMA_Init(SPI_SLAVE_Tx_DMA_Channel, &DMA_InitStructure);

        DMA_ITConfig(SPI_SLAVE_Rx_DMA_Channel, DMA_IT_TC, ENABLE);
}

void initSpiInterrupt(void){

        NVIC_InitStructure.NVIC_IRQChannel = DMA1_Channel2_IRQn;
        NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 8;
        NVIC_InitStructure.NVIC_IRQChannelSubPriority = 0;
        NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;
        NVIC_Init(&NVIC_InitStructure); 

        NVIC_SetPriority(DMA1_Channel2_IRQn, 8);
}

void initSpiSlave(void){

        initSpiRCC();

        initSpiGPIO();

        initSpiDMA();

        initSpiInterrupt();

        SPI_I2S_DeInit(SPI_SLAVE);

        /* SPI SLAVE configuration */
        SPI_InitStructure.SPI_Direction = SPI_Direction_2Lines_FullDuplex;
        SPI_InitStructure.SPI_Mode = SPI_Mode_Slave;
        SPI_InitStructure.SPI_DataSize = SPI_DataSize_8b; // 8-bit transactions
        SPI_InitStructure.SPI_FirstBit = SPI_FirstBit_MSB; // MSB first
        SPI_InitStructure.SPI_CPOL = SPI_CPOL_Low; // CPOL = 0, clock idle low
        SPI_InitStructure.SPI_CPHA = SPI_CPHA_1Edge; // CPHA = 1
        SPI_InitStructure.SPI_NSS = SPI_NSS_Hard;
        SPI_InitStructure.SPI_BaudRatePrescaler = SPI_BaudRatePrescaler_2; 
        SPI_Init(SPI_SLAVE, &SPI_InitStructure);

        /* Enable SPI_SLAVE DMA Rx & Tx request */        
        SPI_I2S_DMACmd(SPI_SLAVE, SPI_I2S_DMAReq_Rx, ENABLE);
        SPI_I2S_DMACmd(SPI_SLAVE, SPI_I2S_DMAReq_Tx, ENABLE);

        /* Enable SPI_SLAVE  */
        SPI_Cmd(SPI_SLAVE, ENABLE);

        /* Enable the DMA channels */
        DMA_Cmd(SPI_SLAVE_Rx_DMA_Channel, ENABLE);
        DMA_Cmd(SPI_SLAVE_Tx_DMA_Channel, ENABLE);
}


/* Interrupt Handler Function */
void resetDMA(void){
        delay_us(1000000 / 50000);
        while ((SPI1->SR & SPI_I2S_FLAG_RXNE) != 0) {
                SPI_I2S_ReceiveData(SPI_SLAVE);
                delay_us(1000000 / 50000);
        }

        DMA_Cmd(SPI_SLAVE_Rx_DMA_Channel, DISABLE);
        SPI_SLAVE_Rx_DMA_Channel->CMAR = (uint32_t)&SPI_SLAVE_Buffer_Rx;
        SPI_SLAVE_Rx_DMA_Channel->CNDTR = BUFFERSIZE;
        SPI_SLAVE_Rx_DMA_Channel->CCR &= ~DMA_MemoryInc_Enable;
        SPI_SLAVE_Rx_DMA_Channel->CCR |= DMA_MemoryInc_Enable;
        DMA_Cmd(SPI_SLAVE_Rx_DMA_Channel, ENABLE);
}

volatile char state = 0;
void DMA1_Channel2_IRQHandler(void){
       
        DMA_ClearITPendingBit(DMA1_IT_GL2 | DMA1_IT_TC2 | DMA1_IT_HT2 | DMA1_IT_TE2);

        if (state == 0){
                GPIOC->BSRR = GPIO_BSRR_BR13; 
                state = 1;
        }
        else{
                GPIOC->BSRR |= GPIO_BSRR_BS13;
                state = 0;                
        }

        resetDMA();
}
