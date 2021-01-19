// sonar.h
// edited 19.01.2021 by OJ
//--------------------------------------------
// Misst den Abstand mit dem SR04-Sonar-Sensor
//
// die Funktionsaufrufe sind im File turtlebot3_core.ino 
// auszuführen 
#include "turtlebot3_core_config.h"

float sonar_data_ ;//global
SONAR_PIN sonar_pin_; // Instanz 

// Funktion im setup() aufrufen
void initSonar(void)
{
  sonar_pin_.trig = BDPIN_GPIO_1;  //50
  sonar_pin_.echo = BDPIN_GPIO_2;  //51

  pinMode(sonar_pin_.trig, OUTPUT);
  pinMode(sonar_pin_.echo, INPUT);
  digitalWrite(sonar_pin_.trig, LOW);
}

// Funktion in der Loop aufrufen
void updateSonar(uint32_t now)
{
  //-- Abstands-Messung mit dem SR04-Sonar durchfuehren --
  //so KLAPPTS => rostopic hz /tf 30 Hz bei 35cm
  // Messung nur alle 100ms
  static uint32_t last_time = 0;
  const int UPDATE_INTERVALL=200; //ms

  // Schallgeschwindigkeit 343,2 m/s 
  // 58ms pro m hin und zurück
  // Sonar < 2m => Timeout 11600 us
  // Sonar < 3m => Timeout 17400 us
  const unsigned long int TIMEOUT=174000; 
  
  float distance, duration;  
    if(now - last_time > UPDATE_INTERVALL)
    { // update nur alle 200ms
        last_time = now; //aktuelle Zeit merken
        digitalWrite(sonar_pin_.trig, LOW);
        delayMicroseconds(2);
        digitalWrite(sonar_pin_.trig, HIGH);
        delayMicroseconds(10);
        digitalWrite(sonar_pin_.trig, LOW);

        //pulseIn mit Abbruch bei zu langer Wartezeit
        duration = pulseIn(sonar_pin_.echo, HIGH, TIMEOUT);
        distance = ((float)(340 * duration) / 10000) / 2;
        if (distance < 300.0) /*mm*/
            sonar_data_ = distance; //to global Var
        else 
            sonar_data_ = 0.0;
    }
}
 
// Funktion für die Konstruktion der Sensor-Msg des TurtleBots 
float getSonarData(void){
  return sonar_data_; //read global 
}
