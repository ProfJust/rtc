#define ENABLE_LOX1 7  //Shutdown Pin , Shutdown - Active LOW => Enable


void setup() {
  // put your setup code here, to run once:
  pinMode(ENABLE_LOX1, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  // deactivating LOX1
  digitalWrite(ENABLE_LOX1, LOW);
  delay(2000);
  // activating LOX1
  digitalWrite(ENABLE_LOX1, HIGH);
  delay(2000);


}
