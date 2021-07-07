import radio
from microbit import *

display.show(Image.YES)
radio.on()
radio.send("needID")

_id = None
image = None
is_turned = False


def draw_image_from_string(image_as_string):
    for i in range(5):
        for j in range(5):
            display.set_pixel(j, i, 9 * int(image_as_string[5 * i + j]))


while True:
    if _id is None or image is None:
        incoming = radio.receive()
        if incoming is not None:
            if len(incoming) < 10 and _id is None:
                _id = int(incoming)
                display.show(incoming)
            elif image is None:
                sleep(2500)
                image = incoming
                draw_image_from_string(incoming)
                radio.off()
    elif not is_turned:
        if accelerometer.is_gesture("face up"):
            is_turned = True
            radio.on()
            radio.send(str(_id))
            radio.off()
    else:
        if accelerometer.is_gesture("face down"):
            is_turned = False
            radio.on()
            radio.send(str(_id))
            radio.off()



