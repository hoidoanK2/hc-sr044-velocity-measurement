const int trig = 8;     // chân trig của HC-SR04
const int echo = 7;     // chân echo của HC-SR04
float data_distance[2] = {0.0, 0.0};

void setup()
{
    Serial.begin(9600);     // giao tiếp Serial với baudrate 9600
    pinMode(trig,OUTPUT);   // chân trig sẽ phát tín hiệu
    pinMode(echo,INPUT);    // chân echo sẽ nhận tín hiệu

}

void loop()
{
    unsigned long duration; // biến đo thời gian
    float distance;           // biến lưu khoảng cách

    /* Phát xung từ chân trig */
    digitalWrite(trig,0);   // tắt chân trig
    delayMicroseconds(2);
    digitalWrite(trig,1);   // phát xung từ chân trig
    delayMicroseconds(5);   // xung có độ dài 5 microSeconds
    digitalWrite(trig,0);   // tắt chân trig
    
    /* Tính toán thời gian */
    // Đo độ rộng xung HIGH ở chân echo. 
    duration = pulseIn(echo,HIGH);  
    // Tính khoảng cách đến vật.
    distance = float(duration/2/29.412);
    
    // Lưu biến khoảng cách
    data_distance[0] = data_distance[1];
    data_distance[1] = distance;
    // Tính toán vận tốc
    float dis_2 = data_distance[1];
    float dis_1 = data_distance[0];
    float velocity = (dis_1 - dis_2) / 0.2;

    /* In kết quả ra Serial Monitor */
    
    Serial.print(velocity);
    Serial.println("cm/s");
    delay(200);
}
