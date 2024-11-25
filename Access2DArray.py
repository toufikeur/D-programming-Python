
1.NO
#ifndef F_CPU
#define F_CPU 8000000UL
#endif

#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
	DDRB = 0xFF;
	PORTB = 0xFF;
}





Lab.2

#ifndef F_CPU
#define  F_CPU 8000000UL
#endif
#include <avr/io.h>
#include <util/delay.h>
int main(void)
{
	DDRC =0xFF;
	while(1)
	{
	PORTC = 0xFF;
	_delay_ms(1000);
	PORTC =0x00;
	_delay_ms(1000);
	}
}




Lab3.
#include <avr/io.h>
#include <util/delay.h>
void main() {
	DDRC = 0xFF;
	while (1) {
		PORTC = 0b00111111; // 0
		_delay_ms(1000);
		PORTC = 0b00000110; // 1
		_delay_ms(1000);
		PORTC = 0b01011011; // 2
		_delay_ms(1000);
		PORTC = 0b01001111; // 3
		_delay_ms(1000);
		PORTC = 0b01100110; // 4
		_delay_ms(1000);
		PORTC = 0b01101101; // 5
		_delay_ms(1000);
		PORTC = 0b11111101; // 6
		_delay_ms(1000);
		PORTC = 0b00000111; // 7
		_delay_ms(1000);
		PORTC = 0b01111111; // 8
		_delay_ms(1000);
		PORTC = 0b11101111; // 9
		_delay_ms(1000);
	}
}





4.No

#include <avr/io.h>
#include <util/delay.h>

uint8_t sm2[10] = {
	0b00111111,
	0b00000110,
	0b01011011,
	0b01001111,
	0b01100110,
	0b01101101,
	0b01111101,
	0b00000111,
	0b01111111,
	0b01101111
};

int main(void) {
	DDRB = 0xFF;
	DDRC = 0xFF;

	while (1) {
		for (int i = 0; i < 10; i++) {
			PORTB = sm2[i];
			for (int j = 0; j < 10; j++) {
				PORTC = sm2[j];
				_delay_ms(50);
			}
		}
	}

	return 0;
}



Lab5;

#include<LiquidCrystal.h>
LiquidCrystal lcd(12,10,3,2,1,0);
void setup()
{
  lcd.begin(16,2);
}

int main(void)
{
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Welcome TO");
  lcd.setCursor(0,1);
  lcd.print("Bangladesh V2.0");
  delay(500);
  lcd.clear();
  delay(500);
}





























from numpy import*

a=array([[1,2,3,4],[5,6,7,8],[11,12,13,14]])

# for r in a:
#     for x in r:
#         print(x)
#     print()

n=len(a)
# for i in range(n):
#     for j in range(len(a[i])):
#         print(a[i][j])
#     print()
i=0
while (i<n):
    j=0
    while j<len(a[i]):
        print(a[i][j])
        j+=1
    print()
    i+=1
print("End of the code")
