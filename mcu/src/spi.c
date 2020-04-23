#include "stm32f10x_spi.h"

#include "spi.h"

void ConfigureSPI(void){

        /* SPI SLAVE configuration */
        SPI_InitTypeDef SPI_InitDef;
        
        SPI_StructInit(&SPI_InitDef);
        SPI_InitDef.SPI_Direction = SPI_Direction_2Lines_FullDuplex;
        SPI_InitDef.SPI_Mode = SPI_Mode_Slave;
        SPI_InitDef.SPI_DataSize = SPI_DataSize_8b; // 8-bit transactions
        SPI_InitDef.SPI_FirstBit = SPI_FirstBit_MSB; // MSB first
        SPI_InitDef.SPI_CPOL = SPI_CPOL_Low; // CPOL = 0, clock idle low
        SPI_InitDef.SPI_CPHA = SPI_CPHA_2Edge; // CPHA = 1
        SPI_InitDef.SPI_BaudRatePrescaler = SPI_BaudRatePrescaler_64; // APB2 72/64 = 1.125 MHz
        SPI_InitDef.SPI_CRCPolynomial = 7;
        SPI_Init(SPI1, &SPI_InitDef);

        SPI_Cmd(SPI1, ENABLE);
}
