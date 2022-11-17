// Erster Test des Sensors VL53L0X 
// an einem Arduino Mega 
// E-Block EB22
// Anschluss (D8-D15 - D-Sub-Pin 7 und 8)
// D21 SCl Gelb
// D20 SDA Grün
// OJ 4.11.22
//---------------------------------------------------

#include "Adafruit_VL53L0X.h"

Adafruit_VL53L0X lox = Adafruit_VL53L0X();

void setup() {
  Serial.begin(115200);

  // wait until serial port opens for native USB devices
  while (! Serial) {
    delay(1);
  }

  Serial.println("Adafruit VL53L0X Change I2C-Adress ");
  if (!lox.begin(0x30)) {
    Serial.println(F("Failed to change Adress VL53L0X"));
    while(1);
  }
  // power
  Serial.println(F("VL53L0X Adress changed !\n\n"));
}

void loop() {
  if (lox.isRangeComplete()) {
    Serial.print("Distance in mm: ");
    Serial.println(lox.readRange());
  }
}
