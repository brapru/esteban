#ifndef __SPI_H
#define __SPI_H

/*
                SPI PINOUT

   Master (RPI)         Slave (STM32)
  ====================================
  GPIO8 (CE0)           PA4 (SPI1_NSS)
  ====================================
  GPIO11 (SCLK)         PA5 (SPI1_SCK)
  ====================================
  GPIO9 (MISO)          PA6 (SPI1_MISO)
  ====================================
  GPIO10 (MOSI)         PA7 (SPI1_MOSI)
  ====================================
  GND                   GND

*/

#define SPI_SLAVE                       SPI1
#define SPI_SLAVE_CLK                   RCC_APB2Periph_SPI1
#define SPI_SLAVE_GPIO                  GPIOA
#define SPI_SLAVE_GPIO_CLK              RCC_APB2Periph_GPIOA
#define SPI_SLAVE_PIN_NSS               GPIO_Pin_4
#define SPI_SLAVE_PIN_SCK               GPIO_Pin_5
#define SPI_SLAVE_PIN_MISO              GPIO_Pin_6
#define SPI_SLAVE_PIN_MOSI              GPIO_Pin_7
#define SPI_SLAVE_DMA_CLK               RCC_AHBPeriph_DMA1
#define SPI_SLAVE_Rx_DMA_Channel        DMA1_Channel2
#define SPI_SLAVE_Tx_DMA_Channel        DMA1_Channel3
#define SPI_SLAVE_DR_Base               0x4001300C
#define SPI_SLAVE_IRQn                  SPI1_IRQn

#define BUFFERSIZE                      7

void initSpiRCC(void);
void initSpiGPIO(void);
void initSpiDMA(void);
void initSpiInterrupt(void);
void initSpiSlave(void);

void resetDMA(void);
void DMA1_Channel2_IRQHandler(void);

#endif
