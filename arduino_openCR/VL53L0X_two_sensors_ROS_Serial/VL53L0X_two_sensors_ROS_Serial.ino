#include "Adafruit_VL53L0X.h"

//--- includes for serial communication as with ROS-Serial-Node  --
// OJ 17.11.22
//
// start Node on Remote PC with 
// $ rosrun rosserial_python serial_node.py _port:=/dev/ttyACM0 _baud:=115200

#include <ros.h>
#include <std_msgs/Float32.h>
ros::NodeHandle nh;

std_msgs::Float32 dist1_msg;
std_msgs::Float32 dist2_msg;
ros::Publisher pub_distance1("distance1", &dist1_msg);
ros::Publisher pub_distance2("distance2", &dist2_msg);

// address we will assign if dual sensor is present
#define LOX1_ADDRESS 0x30
#define LOX2_ADDRESS 0x31

// set the pins to shutdown
#define SHT_LOX1 7
#define SHT_LOX2 6

// objects for the vl53l0x
Adafruit_VL53L0X lox1 = Adafruit_VL53L0X();
Adafruit_VL53L0X lox2 = Adafruit_VL53L0X();

// this holds the measurement
VL53L0X_RangingMeasurementData_t measure1;
VL53L0X_RangingMeasurementData_t measure2;


void setID() {
  /*
    Reset all sensors by setting all of their XSHUT pins low for delay(10), then set all XSHUT high to bring out of reset
    Keep sensor #1 awake by keeping XSHUT pin high
    Put all other sensors into shutdown by pulling XSHUT pins low
    Initialize sensor #1 with lox.begin(new_i2c_address) Pick any number but 0x29 and it must be under 0x7F. Going with 0x30 to 0x3F is probably OK.
    Keep sensor #1 awake, and now bring sensor #2 out of reset by setting its XSHUT pin high.
    Initialize sensor #2 with lox.begin(new_i2c_address) Pick any number but 0x29 and whatever you set the first sensor to
 */
  // all reset
  digitalWrite(SHT_LOX1, LOW);    
  digitalWrite(SHT_LOX2, LOW);
  delay(10);
  // all unreset
  digitalWrite(SHT_LOX1, HIGH);
  digitalWrite(SHT_LOX2, HIGH);
  delay(10);

  // activating LOX1 and resetting LOX2
  digitalWrite(SHT_LOX1, HIGH);
  digitalWrite(SHT_LOX2, LOW);

  // initing LOX1
  if(!lox1.begin(LOX1_ADDRESS)) {
    //Serial.println(F("Failed to boot first VL53L0X"));
    while(1);
  }
  delay(10);

  // activating LOX2
  digitalWrite(SHT_LOX2, HIGH);
  delay(10);

  //initing LOX2
  if(!lox2.begin(LOX2_ADDRESS)) {
    //Serial.println(F("Failed to boot second VL53L0X"));
    while(1);
  }
}

void read_dual_sensors() {
  
  lox1.rangingTest(&measure1, false); // pass in 'true' to get debug data printout!
  lox2.rangingTest(&measure2, false); // pass in 'true' to get debug data printout!

}

void setup() {
  pinMode(SHT_LOX1, OUTPUT);
  pinMode(SHT_LOX2, OUTPUT);
  digitalWrite(SHT_LOX1, LOW);
  digitalWrite(SHT_LOX2, LOW);
  setID(); //I2C-IDs setzen

  nh.initNode();
  nh.advertise(pub_distance1); 
  nh.advertise(pub_distance2); 
}

void loop() {
  
  read_dual_sensors();
  dist1_msg.data = measure1.RangeMilliMeter;
  dist2_msg.data = measure2.RangeMilliMeter;
  pub_distance1.publish(&dist1_msg);
  pub_distance2.publish(&dist2_msg);
  
  nh.spinOnce();  
}
