# Top level Makefile
#
# default all
#
.DEFAULT:
		cd mcu && $(MAKE) $@

install:
		cd mcu && $(MAKE) $@

.PHONY: install
