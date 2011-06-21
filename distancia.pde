/*

 Medidor de distancia com ultrasom

 Author: Gilson Giuriatti

 Email Address: gilson@gmail.com

 Created: 2010

 Modified: Maio 2011

 */

#define trig 8
#define echo 12

unsigned int duration;

void setup()
{
   Serial.begin(115200);
   pinMode(trig, OUTPUT);
   pinMode(echo, INPUT);
}


void loop()
{
  if (Serial.available())
  {
    switch (Serial.read())
    {
    case 'd':
      Serial.println(distcm(), 3);
      break;
    default:
      break;
    }
  }

}

float distcm()
{
  digitalWrite(trig, LOW);
  delayMicroseconds(10);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);
  
  duration = pulseIn(echo, HIGH);
  
  return duration / 29. / 2. ;
}

