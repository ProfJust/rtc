// sonar.h
// edited 27.01.2021 by OJ
//--------------------------------------------
// Misst den Abstand mit dem SR04-Sonar-Sensor
// Version mit 2x Sonar
//
// die Funktionsaufrufe sind im File turtlebot3_core.ino 
// auszuführen 
#include "turtlebot3_core_config.h"

<<<<<<< HEAD
const int UPDATE_INTERVALL= 500; //ms
=======
const int UPDATE_INTERVALL= 750; //ms
>>>>>>> 2fc28e6d2c56207cf3e9cc6638f5369b89fe4f09
// Schallgeschwindigkeit 343,2 m/s 
  // 58ms pro m hin und zurück
  // Sonar < 2m => Timeout 11600 us
  // Sonar < 3m => Timeout 17400 us
<<<<<<< HEAD
const uint32_t TIMEOUT=17500; //us
// ...dazu passend der maximale Weg
const uint16_t  MAX_DIST=3000; //mm
=======
const unsigned long int TIMEOUT=50000;
>>>>>>> 2fc28e6d2c56207cf3e9cc6638f5369b89fe4f09

  //-- Abstands-Messung mit 2x SR04-Sonar durchfuehren --
  //so KLAPPTS => rostopic hz /tf ~28 Hz bei 35cm
  // uint-Version in ganzen cm => float vermeiden


float sonar_data_ ;//global
SONAR_PIN sonar_pin_; // Instanz 
float sonar_data2_ ;//global
SONAR_PIN sonar_pin2_; // Instanz 

// Funktion im setup() aufrufen
void initSonar(void)
{
  sonar_pin_.trig = BDPIN_GPIO_1;  //50
  sonar_pin_.echo = BDPIN_GPIO_2;  //51

  pinMode(sonar_pin_.trig, OUTPUT);
  pinMode(sonar_pin_.echo, INPUT);
  digitalWrite(sonar_pin_.trig, LOW);
}

void initSonar2(void)
{
   //diese Pins sind anscheined bislang NC 
   //$grep -r BDPIN_GPIO
  sonar_pin2_.trig = BDPIN_GPIO_3;  //52
  sonar_pin2_.echo = BDPIN_GPIO_4;  //53

  pinMode(sonar_pin2_.trig, OUTPUT);
  pinMode(sonar_pin2_.echo, INPUT);
  digitalWrite(sonar_pin2_.trig, LOW);
}

// Funktion in der Loop aufrufen
void updateSonar(uint32_t now)
{
  static uint32_t last_time = 0;     
  uint16_t duration_uint,distance_uint;
    if(now - last_time > UPDATE_INTERVALL)
    { // update nur alle xxx ms
        last_time = now; //aktuelle Zeit merken
        digitalWrite(sonar_pin_.trig, LOW);
        delayMicroseconds(2);
        digitalWrite(sonar_pin_.trig, HIGH);
        delayMicroseconds(10);
        digitalWrite(sonar_pin_.trig, LOW);

        //pulseIn mit Abbruch bei zu langer Wartezeit
        duration_uint = pulseIn(sonar_pin_.echo, HIGH, TIMEOUT);
        distance_uint = ((340 * duration_uint) / 10000) / 2;
<<<<<<< HEAD
        if (distance_uint <= MAX_DIST) /*mm*/
=======
        if (distance_uint < 300) /*mm*/
>>>>>>> 2fc28e6d2c56207cf3e9cc6638f5369b89fe4f09
            sonar_data_ = (float) distance_uint; //to global float Var
        else 
            sonar_data_ = 0.0;
    }
}

// Funktion in der Loop aufrufen
void updateSonar2(uint32_t now)
{
  static uint32_t last_time = 0;
  uint16_t duration_uint,distance_uint;
  
  // Messung nur alle xxx ms
  if(now - last_time > UPDATE_INTERVALL) { 
        last_time = now; //aktuelle Zeit merken
        digitalWrite(sonar_pin2_.trig, LOW);
        delayMicroseconds(2);
        digitalWrite(sonar_pin2_.trig, HIGH);
        delayMicroseconds(10);
        digitalWrite(sonar_pin2_.trig, LOW);

        //pulseIn mit Abbruch bei zu langer Wartezeit
        duration_uint = pulseIn(sonar_pin2_.echo, HIGH, TIMEOUT);
<<<<<<< HEAD
        distance_uint = ((340 * duration_uint) / 10000) / 2;
        if (distance_uint <= MAX_DIST) /*mm*/
=======
        distance_uint = ((float)(340 * duration_uint) / 10000) / 2;
        if (distance_uint < 300) /*mm*/
>>>>>>> 2fc28e6d2c56207cf3e9cc6638f5369b89fe4f09
            sonar_data2_ = (float) distance_uint; //to global float Var
        else 
            sonar_data2_ = 0.0;
    }
}
 
// Funktion für die Konstruktion der Sensor-Msg des TurtleBots 
float getSonarData(void){
  return sonar_data_; //read global 
}

// Funktion für die Konstruktion der Sensor-Msg des TurtleBots 
float getSonarData2(void){
  return sonar_data2_; //read global 
}
