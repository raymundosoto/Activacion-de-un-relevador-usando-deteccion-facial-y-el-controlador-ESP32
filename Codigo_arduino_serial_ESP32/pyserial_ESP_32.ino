// Enviar datos a Python

//void setup() {
//Serial.begin(9600);
//}
//
//void loop() {
//Serial.println("Hola mundo");
//delay(1000);
//}


// Recepción de señal de pyserial

char option = ' ';
int LED = 12;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(12, OUTPUT);
}
void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() != 0){
    option = Serial.read();
    if(option == 'a'){
      digitalWrite(LED_BUILTIN, HIGH);
      digitalWrite(12, HIGH);
    }
    else if(option == 'b'){
      digitalWrite(LED_BUILTIN, LOW);
      digitalWrite(12, LOW);
    }
  }
  
  delay(100);
}
