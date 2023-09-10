#include <Arduino.h>

#define joyX A0
#define joyY A1
#define joyButton 13
#define X_BUTTON 4
#define TRIANGLE_BUTTON 3
#define SQUARE_BUTTON 5
#define CIRCLE_BUTTON 2

void setup()
{
  Serial.begin(9600);
  pinMode(X_BUTTON, INPUT_PULLUP);
  pinMode(TRIANGLE_BUTTON, INPUT_PULLUP);
  pinMode(SQUARE_BUTTON, INPUT_PULLUP);
  pinMode(CIRCLE_BUTTON, INPUT_PULLUP);
}

void loop()
{
  float xValue = analogRead(joyX);
  float yValue = analogRead(joyY);

  float xValueMapped = map(xValue, 0, 1023, 800, 0);
  float yValueMapped = map(yValue, 0, 1023, 0, 600);

  int buttonValue = digitalRead(joyButton);

  // Print the values
  Serial.print("xValueMapped: ");
  Serial.println(xValueMapped);

  Serial.print("yValueMapped: ");
  Serial.println(yValueMapped);

  Serial.print("buttonValue: ");
  Serial.println(buttonValue);

  // Print button values
  int x_button = digitalRead(X_BUTTON);
  int triangle_button = digitalRead(TRIANGLE_BUTTON);
  int square_button = digitalRead(SQUARE_BUTTON);
  int circle_button = digitalRead(CIRCLE_BUTTON);
  Serial.print("X_BUTTON: ");
  Serial.println(x_button);

  Serial.print("TRIANGLE_BUTTON: ");
  Serial.println(triangle_button);

  Serial.print("SQUARE_BUTTON: ");
  Serial.println(square_button);

  Serial.print("CIRCLE_BUTTON: ");
  Serial.println(circle_button);

  Serial.flush();
}
