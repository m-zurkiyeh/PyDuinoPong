#include <Thread.h>
const int p1 = A0;
const int p2 = A1;
const int player1LED = 16;
const int player2LED = 17;
int pot1Val = 0;
int pot2Val = 0;
String data;
Thread p1LED = Thread();
Thread p2LED = Thread();


void flashP1LED();
void flashP2LED();
void signal();


void setup() {
  Serial.begin(9600);
  pinMode(player1LED, OUTPUT);
  pinMode(player2LED, OUTPUT);

  p1LED.onRun(flashP1LED);
  p1LED.setInterval(10);
  p1LED.enabled = false;

  p2LED.onRun(flashP2LED);
  p2LED.setInterval(10);
  p2LED.enabled = false;
}

void loop() {

  pot1Val = analogRead(p1);
  pot2Val = analogRead(p2);

  Serial.print(pot1Val);
  Serial.print(",");
  Serial.print(pot2Val);
  Serial.println();


  if (Serial.available() > 0) {
    data = Serial.readStringUntil('\n');
    Serial.println(data);
    if (data.equals("A"))
      p1LED.enabled = true;
    else if (data.equals("a"))
      p1LED.enabled = false;
    else if (data.equals("B"))
      p2LED.enabled = true;
    else if (data.equals("b"))
      p2LED.enabled = false;

    p1LED.run();
    p2LED.run();
    Serial.flush();
  }

  delay(50);
}

/**
 * Turns P1 LED ON/OFF based on the p1LED thread function being enabled or not
 * @return void
*/
void flashP1LED() {
  digitalWrite(player1LED, p1LED.enabled);
}

/**
 * Turns P2 LED ON/OFF based on the p2LED thread function being enabled or not
 * @return void
*/
void flashP2LED() {
  digitalWrite(player2LED, p2LED.enabled);
}