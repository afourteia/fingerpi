

import fingerpi as fp
import time




f = fp.FingerPi()

print("Connecting... ")

f.Open(extra_info = True, check_baudrate = True)

# print("Changing baudrate...")
# f.ChangeBaudrate(115200)
f.CmosLed(True)
time.sleep(1)
f.CmosLed(False)
print ("place on scanner")
f.CmosLed(True)
while True:

    response = f.IsPressFinger()
    if not response [0]['Parameter']:
        break

print("pressed")
print('Closing connection...')
f.Close()