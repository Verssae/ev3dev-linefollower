from ev3dev2.sensor import INPUT_1, INPUT_2
from ev3dev2.sensor.lego import TouchSensor, ColorSensor
from ev3dev2.sound import Sound
import sys, os, time

os.system('setfont Lat7-Terminus12x6')
#os.system('setfont Lat2-TerminusBold14')

cs = ColorSensor()
so = Sound()
so.beep()

csHSV = (0,0,0)
cs.rgb

print("Set Max Value : \n")

# print("Calibration White : \n")
# print("Set Max Value : \n")
# print("Press Touch Sensor : \n")

# ts.wait_for_pressed()
# time.sleep(0.01)
# cs.calibrate_white()

# so.beep()

 
while True:
    print(cs.rgb, cs.reflected_light_intensity, cs.color_name, cs.raw)
    print(cs.green, cs.green_max)
    print("----------")
    # csHSV = cs.hsv
    # col = round(csHSV[0], 2)
    # print(col, round(csHSV[1], 2), csHSV[2], sep=',' , end=' | ')
    # if csHSV[2]<20:
    #     print('color-nothing')
    # elif csHSV[1] < 0.4:
    #     print('color-white')
    # elif col < 1/12 or col > 11/12:
    #     print('color-Red')
    # elif col < 3/12:
    #     print('color-Yellow')
    # elif col < 6/13:
    #     print('color-Green')
    # else:
    #     print('color-Blue')

    # #print('Color - ', cs.color_name)
    # while ts.is_pressed:
    #     print(col, round(csHSV[1], 2), csHSV[2], sep=',' , end=' | ')
        
    
    time.sleep(0.5)
    # so.beep()

