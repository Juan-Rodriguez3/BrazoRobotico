/*
 * USARTinit.h
 *
 * Created: 5/9/2025 10:12:23 AM
 *  Author: juana
 */ 


#ifndef USARTINIT_H_
#define USARTINIT_H_

#include <stdlib.h>  
#define F_CPU 16000000UL
#include <avr/io.h>
#include <avr/interrupt.h>
#include <stdio.h>	// Para sprintf
#include <string.h> // Para strcat

void writeString(char* texto);
void initUSART_9600(void);
uint8_t mapeo_DC(char* dato);
void write(char texto);
void FeedBackState(uint8_t modo);
uint8_t CtoI(const char *cadena);
uint16_t Map_rotor( uint8_t valor);
uint16_t Map_hombro (uint8_t valor);
uint8_t  Map_codo (uint8_t valor);
uint8_t Map_garra (uint8_t valor);
#endif /* USARTINIT_H_ */