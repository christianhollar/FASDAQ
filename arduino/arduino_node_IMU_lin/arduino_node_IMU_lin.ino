#include <Wire.h>;
#include <Adafruit_Sensor.h>;
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

Adafruit_BNO055 bno = Adafruit_BNO055(55);

void setup(void)
{
 Serial.begin(9600);
 Serial.println("Orientation Sensor Test"); Serial.println("");

 /* Initialise the sensor */
 if(!bno.begin())
 {
 /* There was a problem detecting the BNO055 ... check your connections */
 Serial.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
 while(1);
 }

 delay(1000);

 bno.setExtCrystalUse(true);
}
void loop(void)
{
 imu::Vector<3> lin = bno.getVector(Adafruit_BNO055::VECTOR_LINEARACCEL );
 Serial.print("X: ");
 Serial.print(lin.x());
 Serial.print(" Y: ");
 Serial.print(lin.y());
 Serial.print(" Z: ");
 Serial.print(lin.z());
 Serial.print("\t\t");
 Serial.println("");

 delay(100);
}
