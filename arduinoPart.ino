#define TRIG_PIN 9
#define ECHO_PIN 10
#define LED_PIN 13
#define THRESHOLD_DISTANCE 20 // in cm

void setup() {
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600); // Start serial communication
}

void loop() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  long duration = pulseIn(ECHO_PIN, HIGH);
  int distance = duration * 0.034 / 2; // Convert to cm

  Serial.println(distance); // Send distance to the computer

  if (distance < THRESHOLD_DISTANCE) {
    digitalWrite(LED_PIN, HIGH); // Turn LED ON
  } else {
    digitalWrite(LED_PIN, LOW); // Turn LED OFF
  }

  delay(100); // Delay to prevent spamming the serial monitor
}