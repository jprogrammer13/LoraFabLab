# main.py -- put your code here!
from network import LoRa
import socket
import machine
import pycom
import time

# TRIMMER - INVIO

lora = LoRa(mode=LoRa.LORA, frequency=868000000) # 868 MHz
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)


pycom.heartbeat(False)
pycom.rgbled(0x000000)


adc = machine.ADC()
apin = adc.channel(pin='P16') # Pin fisico G3 (vedi pinout su slack)


def map_voltage(voltage):
	return ((voltage // 64) * 0x111111)

while True:
	time.sleep(0.5) # Attesa per evitare errore EAGAIN -> Velocità di trasmissione troppo elevata
	rgb_value = map_voltage(apin())
	pycom.rgbled(rgb_value)
	s.send(str(rgb_value))
	print(apin())
