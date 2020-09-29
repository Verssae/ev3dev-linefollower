from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sound import Sound
from ev3dev2.display import Display
from ev3dev2.button import Button
from time import sleep, time

speeker = Sound()
tank = MoveTank(OUTPUT_A, OUTPUT_B)
cs = ColorSensor()
screen = Display()
button = Button()

def drive(black, white, speed, endtime):
    th = (black + white) / 2
    start_time = time()
    triggerd = False
    while True:
        # print(cs.color_name, cs.rgb, cs.hsv)
        if cs.color == 5:
            print("RED")
            speeker.beep()
            tank.stop()
            sleep(1)
            exit()

        elif cs.reflected_light_intensity < th:
            tank.on(0, speed)
        else:
            tank.on(speed, 0)

        if time() - start_time >= endtime and not triggerd:
            tank.stop()
            speeker.beep()
            sleep(1)
            triggerd = True
        sleep(0.01)

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


    BLACK = 5
    WHITE = 55
    SPEED = 30
    speeker.beep()
    t = getInput()
    try:
        drive(BLACK, WHITE, SPEED, t)
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
