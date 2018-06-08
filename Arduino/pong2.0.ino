const int p1upInput = 31; //Boton P1_UP
const int p1downInput = 30; //Boton P1_DOWN
const int p2upInput = 5; //Boton P2_UP
const int p2downInput = 4; //Boton P2_DOWN

const int volumeInput = 2;
const int colorInput = 3;

const int a2 = 7;
const int b2 = 11;
const int c2 = 10;
const int d2 = 9;
const int e2 = 8;
const int f2 = 6;
const int g2 = 45;

const int a = 39;
const int b = 38;
const int c = 34;
const int d = 36;
const int e = 37;
const int f = 40;
const int g = 41;
 
int data;

int p1upInputState = 0; //Variable para leer estado de switch
int p1downInputState = 0; //Variable para leer estado de switch 
int p2upInputState = 0;
int p2downInputState = 0;
int volumeState = 0;
int colorState = 0;

void setup()
{
    pinMode(p1upInput, INPUT_PULLUP); //Switch PIN is Input
    pinMode(p1downInput, INPUT_PULLUP); //Switch PIN is Input
    pinMode(p2upInput, INPUT_PULLUP);
    pinMode(p2downInput, INPUT_PULLUP);
    pinMode(volumeInput, INPUT_PULLUP);
    pinMode(colorInput, INPUT_PULLUP);
    pinMode(a, OUTPUT);
    pinMode(b, OUTPUT);
    pinMode(c, OUTPUT);
    pinMode(d, OUTPUT);
    pinMode(e, OUTPUT);
    pinMode(f, OUTPUT);
    pinMode(g, OUTPUT);
    pinMode(a2, OUTPUT);
    pinMode(b2, OUTPUT);
    pinMode(c2, OUTPUT);
    pinMode(d2, OUTPUT);
    pinMode(e2, OUTPUT);
    pinMode(f2, OUTPUT);
    pinMode(g2, OUTPUT);
    Serial.begin(9600);
}
void botones()
{
    p1upInputState = digitalRead(p1upInput); //Read the status of the Switch
    if (p1upInputState == LOW) //If the switch is pressed
    {
        Serial.println("P1_UP%");
    }
    p1downInputState = digitalRead(p1downInput); //Read the status of the Switch
    if (p1downInputState == LOW) //If the switch is pressed
    {
        Serial.println("P1_DOWN%");
    }
    p2upInputState = digitalRead(p2upInput); //Read the status of the Switch
    if (p2upInputState == LOW) //If the switch is pressed
    {
        Serial.println("P2_UP%");
    }
    p2downInputState = digitalRead(p2downInput); //Read the status of the Switch
    if (p2downInputState == LOW) //If the switch is pressed
    {
        Serial.println("P2_DOWN%");
    }
    volumeState = digitalRead(volumeInput);
    if (volumeState == LOW)
    {
        Serial.println("MUTE%");
    }
    colorState = digitalRead(colorInput);
    if (colorState == LOW)
    {
        Serial.println("COLOR%");
    }
    delay(65);
}
void displays()
{
  data = Serial.read();
  //data = 54;
  switch(data)
  {
    case 48:
    digitalWrite(a, HIGH);
    digitalWrite(b, HIGH);
    digitalWrite(c, HIGH);
    digitalWrite(d, HIGH);
    digitalWrite(e, HIGH);
    digitalWrite(f, HIGH);
    digitalWrite(g, LOW);
    break;

    case 49:
    digitalWrite(a, LOW);
    digitalWrite(b, HIGH);
    digitalWrite(c, HIGH);
    digitalWrite(d, LOW);
    digitalWrite(e, LOW);
    digitalWrite(f, LOW);
    digitalWrite(g, LOW);
    break;

    case 50:
    digitalWrite(a, HIGH);
    digitalWrite(b, HIGH);
    digitalWrite(c, LOW);
    digitalWrite(d, HIGH);
    digitalWrite(e, HIGH);
    digitalWrite(f, LOW);
    digitalWrite(g, HIGH);
    break;

    case 51:
    digitalWrite(a, HIGH);
    digitalWrite(b, HIGH);
    digitalWrite(c, HIGH);
    digitalWrite(d, HIGH);
    digitalWrite(e, LOW);
    digitalWrite(f, LOW);
    digitalWrite(g, HIGH);
    break;

    case 52:
    digitalWrite(a, LOW);
    digitalWrite(b, HIGH);
    digitalWrite(c, HIGH);
    digitalWrite(d, LOW);
    digitalWrite(e, LOW);
    digitalWrite(f, HIGH);
    digitalWrite(g, HIGH);
    break;

    case 53:
    digitalWrite(a, HIGH);
    digitalWrite(b, LOW);
    digitalWrite(c, HIGH);
    digitalWrite(d, HIGH);
    digitalWrite(e, LOW);
    digitalWrite(f, HIGH);
    digitalWrite(g, HIGH);
    break;
  }
  switch(data)
  {
    case 54:
    Serial.println(data);
    digitalWrite(a2, HIGH);
    digitalWrite(b2, HIGH);
    digitalWrite(c2, HIGH);
    digitalWrite(d2, HIGH);
    digitalWrite(e2, HIGH);
    digitalWrite(f2, HIGH);
    digitalWrite(g2, LOW);
    break;

    case 55:
    digitalWrite(a2, LOW);
    digitalWrite(b2, HIGH);
    digitalWrite(c2, HIGH);
    digitalWrite(d2, LOW);
    digitalWrite(e2, LOW);
    digitalWrite(f2, LOW);
    digitalWrite(g2, LOW);
    break;

    case 56:
    digitalWrite(a2, HIGH);
    digitalWrite(b2, HIGH);
    digitalWrite(c2, LOW);
    digitalWrite(d2, HIGH);
    digitalWrite(e2, HIGH);
    digitalWrite(f2, LOW);
    digitalWrite(g2, HIGH);
    break;

    case 57:
    digitalWrite(a2, HIGH);
    digitalWrite(b2, HIGH);
    digitalWrite(c2, HIGH);
    digitalWrite(d2, HIGH);
    digitalWrite(e2, LOW);
    digitalWrite(f2, LOW);
    digitalWrite(g2, HIGH);
    break;

    case 58:
    digitalWrite(a2, LOW);
    digitalWrite(b2, HIGH);
    digitalWrite(c2, HIGH);
    digitalWrite(d2, LOW);
    digitalWrite(e2, LOW);
    digitalWrite(f2, HIGH);
    digitalWrite(g2, HIGH);
    break;

    case 59:
    digitalWrite(a2, HIGH);
    digitalWrite(b2, LOW);
    digitalWrite(c2, HIGH);
    digitalWrite(d2, HIGH);
    digitalWrite(e2, LOW);
    digitalWrite(f2, HIGH);
    digitalWrite(g2, HIGH);
    break;
  }
}
void loop()
{
  displays();
  botones();
}

