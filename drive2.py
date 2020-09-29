from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank, SpeedPercent, follow_for_ms, follow_for_forever
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sound import Sound
from ev3dev2.display import Display
from ev3dev2.button import Button
from time import sleep, time
import threading
import os

speeker = Sound()
tank = MoveTank(OUTPUT_A, OUTPUT_B)
cs = ColorSensor()
tank.cs = cs
screen = Display()
button = Button()

# os.system('setfont CyrAsia-Terminus12x6')

def color_find(endtime):
    start_time = time()
    triggerd = False
    while True:
        if cs.color == 5:
            speeker.beep()
            tank.stop()
            sleep(1)
            exit()
        if time() - start_time >= endtime and not triggerd:
            tank.stop()
            speeker.beep()
            sleep(1)
            triggerd = True
        
def getInput():
    t = 0
    text = str(t)
    screen.text_pixels(text, x=89, y=64)
    screen.update()
    while not button.enter:
        if button.up:
            t = t + 0.1
        elif button.down and t > 0:
            t = t - 0.1
        text = str(t)
        screen.text_pixels(text, x=89, y=64)
        screen.update()
        sleep(0.1)
    screen.text_pixels("GO!", x=89, y=64)
    screen.update()
    return t

if __name__ == "__main__":


    speeker.beep()
    t = getInput()
    thread = threading.Thread(target=color_find,args=[t], daemon=False)
    
    try:
        thread.start()
        tank.follow_line(
            kp=11.3, ki=0.05, kd=3.2,
            speed=SpeedPercent(30),
            follow_for=follow_for_forever
        )
       

    except:
        tank.stop()
        exit()













# tank = MoveTank(OUTPUT_A, OUTPUT_B)
# tank.cs = ColorSensor()

# initial_intensity = tank.cs.reflected_light_intensity
# th = 57
# outside_cnt_max = 20

# outside_cnt = 0

# while True:
#     cur_intensity = tank.cs.reflected_light_intensity
#     diff = initial_intensity - cur_intensity

#     if cur_intensity >= th:
#         outside_cnt += 1
#         if outside_cnt >= outside_cnt_max:
#             tank.stop()
#     sleep(0.1)
