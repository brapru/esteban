# Top level Makefile

# Most importantly, colorz 
RED=\033[0;31m
GREEN=\033[0;32m
ORANGE=\033[0;33m
NC=\033[0m

default: all


.DEFAULT:
		@cd mcu && $(MAKE) $@


install:
		cd mcu && $(MAKE) $@

.PHONY: install
