TARGET = blink
MCU = cortex-m3

CC = arm-none-eabi-gcc
AS = arm-none-eabi-as
LD = arm-none-eabi-ld
BIN = arm-none-eabi-objcopy
STL = st-flash
CFLAGS = -mthumb -mcpu=$(MCU) -DSTM32F10X_MD -ggdb

INCDIR = -I./includes
LDDIR = ./ld
SRCDIR = ./src
BINDIR = ./bin

LDSCRIPT = ./ld/linker.ld
LFLAGS = -T$(LDSCRIPT)

C_SRC=$(SRCDIR)/blink.c
AS_SRC+=$(SRCDIR)/startup.s

INCLUDES = $(INCDIR)

OBJS  = $(AS_SRC:.s=.o)
OBJS += $(C_SRC:.c=.o)

.PHONY: all

all: $(TARGET).bin

%.o: %.s
	$(AS) $< -o $@

%.o: %.c
	$(CC) -c $(CFLAGS) $(INCLUDES) $< -o $@

$(TARGET).elf: $(OBJS)
	$(LD) $(LFLAGS) $^ -o $@ 

$(TARGET).bin: $(TARGET).elf
	$(BIN) -S -O binary $< $@

clean:
	rm -rf $(SRCDIR)/*.o $(SRCDIR)/*.elf
	rm -rf $(BINDIR)/*.elf $(BINDIR)/*.bin

flash:
	$(STL) write $(BINDIR)/$(TARGET).bin 0x8000000

erase:
	$(STL) erase
