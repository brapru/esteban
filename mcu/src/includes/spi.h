#ifndef __SPI_H
#define __SPI_H

/*
                SPI PINOUT

   Master (RPI)         Slave (STM32)
  ====================================
  PA3 (SS)              PA4 (SPI1_NSS)
  ====================================
  PA5 (SPI1_SCK)        PA5 (SPI1_SCK)
  ====================================
  PA6 (SPI1_MISO)       PA6 (SPI1_MISO)
  ====================================
  PA7 (SPI1_MOSI)       PA7 (SPI1_MOSI)
  ====================================
  GND                   GND

*/

void ConfigureSPI(void);

#endif
