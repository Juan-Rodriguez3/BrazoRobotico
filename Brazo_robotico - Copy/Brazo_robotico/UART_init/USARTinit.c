/*
 * USARTinit.c
 *
 * Created: 5/9/2025 10:12:12 AM
 *  Author: juana
 */ 
#include "USARTinit.h"

void write(char texto){
	while ((UCSR0A & (1<<UDRIE0))==0);	//Esperamos a que el registro de datos de USART este vac?o
	UDR0= texto;
}

void writeString(char* texto){
	for(uint8_t i = 0; *(texto+i) !='\0'; i++)
		write(*(texto+i));
	}
	
	
uint8_t ascii_to_int(char*i)	// Funci�n para convertir de ascii a int
{
	int resultado = 0;	// Se declara e inicializa una variable para guardar el resultado de la conversi�n
	while (*i >= '0' && *i <= '9')	// Se mantiene en el while siempre que el d�gito al que apunte sea un n�mero (termina si detecta \n o \0 por ejemplo)
	{
		resultado = resultado * 10 + (*i - '0');	// Toma el ascii, lo convierte en d�gito y lo ordena en sistema decimal
		i++;	// suma al caracter a convertir
	}
	return resultado;	// Se retorna el valor del resultado de la conversi�n
}



uint8_t mapeo_DC(char* dato) {
	uint8_t grados = 0;
	grados = (uint8_t)atoi(dato); // atoi convierte cadena a int
	return grados;
}

void initUSART_9600(){
	//Configurar los pines PD1 Tx y PD0 Rx
	DDRD |= (1<<PORTD1);
	DDRD &= ~(1<<PORTD0);
	UCSR0A = 0;		//No se utiliza doble speed.
	UCSR0B = 0;
	UCSR0B |= (1<<RXCIE0)|(1<<RXEN0)|(1<<TXEN0);  //Habilitamos interrupciones al recibir, habilitar recepci?n y transmisi?n
	UCSR0C = 0;
	UCSR0C |= (1<<UCSZ00)|(1<<UCSZ01);	//Asincrono, deshabilitado el bit de paridad, un stop bit, 8 bits de datos.
	UBRR0=103;	//UBBRR0=103; -> 9600 con frecuencia de 16MHz
}

void FeedBackState(uint8_t modo) 
{
	char buffer[20]; // Suficiente espacio para el texto y el n�mero
	char numStr[10]; // Para almacenar el n�mero como cadena
	
	// Convertir el n�mero a cadena
	sprintf(numStr, "%d", modo);

	// Construir el mensaje completo
	strcpy(buffer, "Modo actual: ");
	strcat(buffer, numStr);
	strcat(buffer, "\n");

	// Enviar el mensaje
	writeString(buffer);
}

uint8_t CtoI(const char *cadena) {
	int valor = 0;
	uint8_t empezar = 0; // Bandera para iniciar conversi�n

	for (int i = 0; cadena[i] != '\0'; i++) {
		// Buscar ':' para empezar
		if (cadena[i] == ':') {
			empezar = 1;
			continue;
		}

		// Si ya encontramos ':', procesar d�gitos
		if (empezar) {
			// Ignorar espacios o saltos de l�nea
			if (cadena[i] == ' ' || cadena[i] == '\n') continue;

			// Verificar si es un d�gito ASCII (0-9)
			if (cadena[i] >= '0' && cadena[i] <= '9') {
				valor = valor * 10 + (cadena[i] - '0'); // Conversi�n ASCII a entero
				} else {
				break; // Car�cter no num�rico, terminar
			}
		}
	}

	return valor; // -1 si no se encontr� ':'
}

uint16_t Map_rotor(uint8_t valor){
	return (1010UL + valor * (3970UL/180));		//Reglita de tres para calcular OCRA1 
}

uint8_t Map_codo(uint8_t valor){
	return (12UL+(valor*5UL)/60);		//Reglita de tres para calcular OCRA2
}	

uint16_t Map_hombro(uint8_t valor){
	return (1010UL + valor * (1000UL/73));		//Reglita de tres para calcular OCRB1
	
}

uint8_t Map_garra(uint8_t valor){
	return (6UL+(valor*5UL)/54);		//Reglita de tres para calcular OCRB2
}