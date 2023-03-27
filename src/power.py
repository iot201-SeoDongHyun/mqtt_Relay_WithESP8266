import sys
import paho.mqtt.client as mqtt
server = "18.209.210.51"     # EC2의 IP주소로 변경

client = mqtt.Client()
client.connect(server, 1883, 60)

if len(sys.argv) <= 1:
    print("Usage : "+sys.argv[0]+" on/off")
    exit()
else:
    client.publish("id/DongHyun/switch/evt", str(sys.argv[1]))
