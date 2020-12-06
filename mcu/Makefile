TARGET = esteban
MCU = cortex-m3

# Compiling and Flashing Tools
CC = arm-none-eabi-gcc
AS = arm-none-eabi-as
LD = arm-none-eabi-ld
BIN = arm-none-eabi-objcopy
STL = st-flash

# Directories
LIBDIR = lib
LDDIR = ld
SRCDIR = src
BINDIR = bin
OBJDIR = obj
CMSIS_DIR = lib/CMSIS
STDPERIPH_DIR = lib/STM32F10x_StdPeriph_Driver

# Gather all ASM Source Files
VPATH := $(SRCDIR):$(SRCDIR)/startups
ASOURCES = $(notdir $(wildcard $(SRCDIR)/startups/*.s))


# Gather CMSIS Source FIles
VPATH := $(VPATH):$(CMSIS_DIR)/CM3/CoreSupport:$(CMSIS_DIR)/CM3/DeviceSupport/ST/STM32F10x
CMSIS_SRC = $(notdir $(wildcard $(CMSIS_DIR)/CM3/CoreSupport/*.c \
				$(CMSIS_DIR)/CM3/DeviceSupport/ST/STM32F10x/*.c))	   		


# Gather Standard Peripheral Source FIles
VPATH := $(VPATH):$(STDPERIPH_DIR)/src
STDPERIPH_SRC = $(notdir $(wildcard $(STDPERIPH_DIR)/src/*.c))

# Gather all C Source Files
CSOURCES = $(notdir $(wildcard $(SRCDIR)/*.c)) \
	   $(CMSIS_SRC) \
	   $(STDPERIPH_SRC)

# Make sure compiler knows where to look
INCLUDE_DIRS = $(SRCDIR)/includes \
	       $(STDPERIPH_DIR)/inc \
	       $(CMSIS_DIR)/CM3/CoreSupport \
	       $(CMSIS_DIR)/CM3/DeviceSupport/ST/STM32F10x

# Object List
OBJECTS = $(addsuffix .o,$(addprefix $(OBJDIR)/,$(basename $(CSOURCES))))
OBJECTS += $(addsuffix .o,$(addprefix $(OBJDIR)/,$(basename $(ASOURCES))))

# Flags
MCFLAGS = -mthumb -mcpu=$(MCU) -mfloat-abi=soft 
DEFS = -DSTM32F10X_MD -DUSE_STDPERIPH_DRIVER
CFLAGS = $(MCFLAGS) $(addprefix -I,$(INCLUDE_DIRS)) $(DEFS) -gdwarf-4 -g3  --specs=rdimon.specs --specs=nosys.specs 

LDSCRIPT = ./ld/stm32f103c8tx.ld
LFLAGS = -T$(LDSCRIPT) $(MCFLAGS) --specs=rdimon.specs --specs=nosys.specs

# Most importantly, colorz 
RED=\033[0;31m
GREEN=\033[0;32m
ORANGE=\033[0;33m
LGREEN=\033[01;32m
NC=\033[0m

.PHONY: all clean flash erase

all: $(BINDIR)/$(TARGET).bin

$(BINDIR)/$(TARGET).bin: $(BINDIR)/$(TARGET).elf
	@$(BIN) -S -O binary $< $@
	@echo "[$(GREEN)*$(NC)] BIN $<"
	
	@echo "\n[${GREEN}*${NC}] $(TARGET) build success"
	@echo "[$(GREEN)*$(NC)] Run $(ORANGE)\"make flash\"$(NC) to flash to the MCU via ST-LINK."	
	@echo "[$(ORANGE)*$(NC)] $(ORANGE)Note:$(NC) You may need to run $(ORANGE)\"make erase\"$(NC) to clear the MCU before flashing."

$(BINDIR)/$(TARGET).elf: $(OBJECTS) 
	@mkdir -p $(BINDIR)
	@$(CC) $(LFLAGS) $^ -o $@ 
	@echo "[$(GREEN)*$(NC)] CC $<"

$(OBJDIR)/%.o: %.c
	@mkdir -p $(dir $@)
	@$(CC) -c $(CFLAGS) $(DEFS) $< -o $@
	@echo "[$(GREEN)*$(NC)] CC $<"

$(OBJDIR)/%.o: %.s
	@mkdir -p $(dir $@)
	@$(AS) $(MCFLAGS) $(addprefix -I,$(INCLUDE_DIRS)) $< -o $@
	@echo "[$(GREEN)*$(NC)] AS $<"

clean:
	@echo "[${GREEN}*${NC}] rm -rf $(BINDIR) $(OBJDIR)"
	@rm -rf $(BINDIR) $(OBJDIR)
	@echo "[${GREEN}*${NC}] rm -rf *.elf *.bin *.o"
	@echo "[${GREEN}*${NC}] Cleaned up esteban environment"

update:
	$(MAKE) erase && $(MAKE) clean && $(MAKE) && $(MAKE) flash

flash:
	$(STL) write $(BINDIR)/$(TARGET).bin 0x8000000

blink:
	$(STL) write examples/blink.bin 0x8000000

erase:
	$(STL) erase
