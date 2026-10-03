#include <Servo.h>

// Create servo objects
Servo servo1; // thumb
Servo servo2; // index
Servo servo3; // middle
Servo servo4; // ring
Servo servo5; // pinky

void setup() {
  Serial.begin(9600);
  servo1.attach(11); 
  servo2.attach(10); 
  servo3.attach(9);  
  servo4.attach(6);  
  servo5.attach(5);  
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n'); // read till newline
    data.trim(); // remove spaces/newlines
    
    if (data.length() == 5) {
      // Map 0 -> closed (0°), 1 -> open (180°)
      servo1.write(data[0] == '1' ? 0 : 120); // thumb
      servo2.write(data[1] == '1' ? 0 : 180); // index
      servo3.write(data[2] == '1' ? 180 : 0); // middle
      servo4.write(data[3] == '1' ? 180 : 0); // ring
      servo5.write(data[4] == '1' ? 90 : 0); // pinky
    }
  }
}
