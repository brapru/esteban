/*

======A simple C run-time framework for the STM32 processor======

Check out
  [[arm_cortex-m3:stm32:minimal-c-program|Writing a minimal C program for the STM32]]

and

  [[gnu-tools:essential-ld|Essential GNU Linker Concepts for Embedded Systems Programmers]]

before continuing with this page.

=====A linker script for the STM32F103RBT6 processor=====

The STM32F103RBT6 processor has 128Kb flash (from address 0x08000000
which is also mapped to 0x0) and 20Kb of RAM (at 0x20000000).

The stack pointer will be initialized to 0x20005000. The Cortex-M3
core extracts the 4 byte value at address 0x0 and uses it to
initialize the stack pointer.

The interrupt vector table begins at location 0x4 (0x4 holds the reset
vector). We will fill up a few other entries in the table with address
of a function which executes an infinite loop.A group of these
function pointers are held in a global array which is in a section
called //isr_vector//.

The linker script directive //KEEP// is used to make sure that this
section is not //garbage-collected// even if the linker is invoked
with a command line argument which enables GC of unreferenced sections
(check out
[[http://blog.fosstronics.com/2008/07/02/gnu-toolchain-tips-of-the-week/|this
blog entry for more info about linker garbage collection]]).

Initialized global variables will be stored immediately after the
//text// section (in flash memory); upon reset, the //startup// code
will copy this data into RAM at location 0x20000000.

Uninitialized global variables will be placed immediately after the
block of initialized variables. The startup code will zero this block.

The symbol //_extext// is used by the startup code to identify end of
the //text// section and beginning of the section (in flash) which
holds initialized data.

The symbols //_sdata// (start data) and //_edata// (end data) are used
by the startup code to identify the bounds of the data section in RAM.

The symbols //_sbss// (start bss) and //_ebss// (end bss) are used by
the startup code to identify the bounds of the section in RAM which
holds uninitialized data.

Here is the actual linker script (the script is a cut-down version of
the one which comes with CircleOS).  */

/* Entry Point */
ENTRY(Reset_Handler)

/* The STM32F103VE memory map. */
MEMORY
{
    FLASH (rx) : ORIGIN = 0x08000000, LENGTH = 512K
    SRAM  (rw) : ORIGIN = 0x20000000, LENGTH = 64K
}

SECTIONS
{
    .text :
    {
        KEEP(*(.isr_vector))
        *(.text)
        *(.text.*)
        *(.note.*)      /* note sections otherwise appear (with gcc version 4.6.3)  
                           as the first section, thus moving .isr_vector to
                           higher addresses :-( */ 
        *(.glue_7t) 
        *(.glue_7)
        *(.rodata)                 /* read-only data (constants) */
        *(.rodata*)
    } > FLASH

    /* The following two sections appear if printf() is used. They are used for
       exception unwinding, but I don't know what printf() has to do with exceptions? */
    .ARM.extab : 
    {
        *(.ARM.extab* .gnu.linkonce.armextab.*)
    } > FLASH
    
    .ARM.exidx :
    {
        *(.ARM.exidx* .gnu.linkonce.armexidx.*)
        _etext = .;
        _sidata = .;
    } > FLASH
    
   /* .data : AT (ADDR(.text) + SIZEOF(.text)) */ /* without exceptions related section .ARM.ex* */
   
    .data : AT (ADDR(.ARM.exidx) + SIZEOF(.ARM.exidx)) 
    {
        _sdata = .;
        *(vtable)
        *(.data*)
        _edata = .;        
    } > SRAM

    .bss :
    {
        _sbss = .;
        *(.bss*)
        *(COMMON)
        _ebss = .;
        *(.stack)
    } > SRAM

    /* set initial stack value to end of RAM */
    _estack = 0x20010000;
}
