
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
#include <Arduino.h>
 
#define VREF    5000//VREF(mv)
#define ADC_RES 1024//ADC Resolution
 
uint32_t raw;
 
void setup()
{
    Serial.begin(115200);
}
 
void loop()
{
    raw=analogRead(A1);
    Serial.println("raw:\t"+String(raw)+"\tVoltage(mv)"+String(raw*VREF/ADC_RES));
    delay(1000);
}
