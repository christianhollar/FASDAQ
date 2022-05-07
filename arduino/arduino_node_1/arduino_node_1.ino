void setup() {
  // put your setup code here, to run once:
Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  int myrand = random(100);
  Serial.println(myrand);
  delay(1);
}
