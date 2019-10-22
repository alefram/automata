int led = 7;
char userInput;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(led,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    userInput = Serial.read();

    if(userInput == 'a'){
       digitalWrite(led,HIGH);
       delay(500);
       digitalWrite(led,LOW); 
      }
    }
}
