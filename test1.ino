#define SensorPin A1          // the pH meter Analog output is connected with the Arduino’s Analog
unsigned long int avgValue;  //Store the average value of the sensor feedback
float b;
int buf[10],temp;
#define turbidity_pin A0 
int read_ADC;
int ntu;

#define VREF    5000//VREF(mv)
#define ADC_RES 1024//ADC Resolution
 
uint32_t raw;
void setup(){// put your setup code here, to run once 
Serial.begin(115200);
pinMode(turbidity_pin, INPUT);
delay(2000);
}
 
void loop(){
  /////Turbidity Sensor
read_ADC = analogRead(turbidity_pin);
//if(read_ADC>208)read_ADC=208;

//ntu = map(read_ADC, 0, 208, 300, 0); 
Serial.print("Turbidity: "); 
Serial.println(read_ADC);

//Serial.println(ntu);

//
//if(ntu<10)            Serial.print("Water Very Clean");
//if(ntu>=10 && ntu<30) Serial.print("Water Norm Clean");
//if(ntu>=30)           Serial.print("Water Very Dirty");

delay(2000);


//////////////////pH VALUES CODE
for(int i=0;i<10;i++)       //Get 10 sample value from the sensor for smooth the value
  { 
    buf[i]=analogRead(SensorPin);
    delay(10);
  }
  for(int i=0;i<9;i++)        //sort the analog from small to large
  {
    for(int j=i+1;j<10;j++)
    {
      if(buf[i]>buf[j])
      {
        temp=buf[i];
        buf[i]=buf[j];
        buf[j]=temp;
      }
    }
  }
  avgValue=0;
  for(int i=2;i<8;i++)                      //take the average value of 6 center sample
    avgValue+=buf[i];
  float phValue=(float)avgValue*5.0/1024/6; //convert the analog into millivolt
  phValue=3.5*phValue;                      //convert the millivolt into pH value
  Serial.print("    pH:");  
  Serial.print(phValue,2);
  Serial.println(" ");
  digitalWrite(13, HIGH);       
  delay(800);
  digitalWrite(13, LOW); 

 /////////////////////Dissolven oxygen
    raw=analogRead(A2);
    Serial.println("raw:\t"+String(raw)+"\tVoltage(mv)"+String(raw*VREF/ADC_RES));
    delay(1000);
}
