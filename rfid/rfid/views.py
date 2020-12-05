from django.shortcuts import render
import serial,time

def index(request):
	ser = serial.Serial()
	ser.port = "/dev/ttyUSB0"
	ser.open()
	if ser.isOpen():
 		read_data = ser.read(12)
	return render(request,'home.html',{'name':read_data})