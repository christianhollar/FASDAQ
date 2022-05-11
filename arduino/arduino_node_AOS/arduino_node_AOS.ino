#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

Adafruit_BNO055 bno = Adafruit_BNO055(55);

void setup(void)
{
  Serial.begin(9600);
  Serial1.begin(9600);

  /* Initialise the sensor */
  if (!bno.begin())
  {
    /* There was a problem detecting the BNO055 ... check your connections */
    Serial.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
    while (1);
  }

  delay(1000);

  bno.setExtCrystalUse(true);
}

void loop(void)
{

  /* Vector Declaration:
     - Euler
     - Gyro
     - Accelerometer
     - Linear Accelerometer
  */

  imu::Vector<3> euler = bno.getVector(Adafruit_BNO055::VECTOR_EULER);
  imu::Vector<3> gyro = bno.getVector(Adafruit_BNO055::VECTOR_GYROSCOPE);
  imu::Vector<3> acc = bno.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);
  imu::Vector<3> linacc = bno.getVector(Adafruit_BNO055::VECTOR_LINEARACCEL);

  /* Euler:
     Roll Angle: Euler X
     Pitch Angle: Euler Y
     Yaw Angle: Euler Z
  */

  Serial.print("Euler,");
  Serial.print(euler.x());
  Serial.print(",");
  Serial.print(euler.y());
  Serial.print(",");
  Serial.print(euler.z());
  Serial.println(",");

  /* Gyro:
     Roll Velocity: Gyro X
     Pitch Velocity: Gyro Y
     Yaw Velocity: Gyro Z
  */

  Serial.print("Gyro,");
  Serial.print(gyro.x());
  Serial.print(",");
  Serial.print(gyro.y());
  Serial.print(",");
  Serial.print(gyro.z());
  Serial.println(",");

  /* Acceleration:
     Longitudinal Acceleration: Acceleration X
     Lateral Acceleration: Acceleration Y
     Vertical Acceleration: Acceleration Z
  */

  Serial.print("Acc,");
  Serial.print(acc.x());
  Serial.print(",");
  Serial.print(acc.y());
  Serial.print(",");
  Serial.print(acc.z());
  Serial.println(",");

  /* Linear Acceleration
      Linear Acceleration X
      Lienar Acceleration Y
      Linear Acceleration Z
  */

  Serial.print("LinAcc,");
  Serial.print(linacc.x());
  Serial.print(",");
  Serial.print(linacc.y());
  Serial.print(",");
  Serial.print(linacc.z());
  Serial.println(",");

  //GPS
//  while (Serial1.available()) {
//    Serial.write(Serial1.read());
//  }
}
