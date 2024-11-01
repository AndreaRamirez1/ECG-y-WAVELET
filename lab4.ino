const int ecgPin = A0;  // Pin conectado al AD8232
const int baudRate = 9600;  // Tasa de baudios para la comunicación serial

void setup() {
  Serial.begin(baudRate);
}

void loop() {
  int ecgValue = analogRead(ecgPin);  // Leer la señal analógica del AD8232
  Serial.println(ecgValue);           // Enviar el valor leído al puerto serial
  delay(1);                           // Ajusta el delay para controlar la tasa de muestreo
}
