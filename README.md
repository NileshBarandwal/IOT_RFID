# IOT_RFID
```
Before running server install following module in virtual environment
pip install pyserial
or
pip install --upgrade pyserial
```

```
Connect RFID reader to USB port of Raspberri Pi and open terminal, run
 dmesg | grep tty
note down USB port number, say USB0 is allotted
open views.py and edit it as follows
from django.shortcuts import render
import serial,time
def index(request):
ser = serial.Serial()
ser.port = "/dev/ttyUSB0"
ser.open()
if ser.isOpen():
 read_data = ser.read(12)
return render(request,'home.html',{'name':read_data})
```
