#ifndef __ESTEBAN_H
#define __ESTEBAN_H

#include "devices.h"
#include "commands.h"
#include "spi.h"
#include "stepper.h"
#include "utils.h"
#include "boiler.h"

struct controller {
        
        struct device led;
        struct device pump;
        struct device boiler;
};

/* === Externs === */
extern struct controller esteban;

#endif
