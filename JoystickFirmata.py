import serial
import time
import pygame, sys

from time import sleep

from pyfirmata import Arduino, util

board = Arduino('/dev/ttyACM0')

# Reads the values sent from the Arduino over USB using Firmata
it = util.Iterator(board)
it.start()
board.analog[0].enable_reporting()
time.sleep(1)
x_pos = board.analog[0].read()
board.analog[1].enable_reporting()
time.sleep(1)
y_pos = board.analog[1].read()
x_pos = float(x_pos)

# Sets the size of the GUI
x_border = 700
y_border = 700

pygame.init()

display = pygame.display.set_mode((x_border, y_border))
clock = pygame.time.Clock()

dotImg = pygame.image.load('download.png')

display.fill((255, 255, 255))


def dot(x, y):
    display.blit(dotImg, (x, y))


# User input for the sensitivity created by adjusting the magnitude of the coordinates
sens = raw_input("High, Medium, or Low Sensitivity?")
type(sens)

if (sens == "High"):
    mult = 1.5
elif (sens == "Medium"):
    mult = 1
elif (sens == "Low"):
    mult = .5
else:
    print("Please type either High, Medium, or Low with correct capitilization")

# Loop for updating the GUI with the position of joystick to adjust the dot
while True:
    display.fill((255, 255, 255))
    x_pos = board.analog[0].read() * 1000 * mult
    x_pos = float(x_pos)

    y_pos = board.analog[1].read() * 1000 * mult
    if (x_pos > 329 and x_pos < 336):
        x_pos = 330
    if (y_pos > 329 and y_pos < 336):
        y_pos = 330
    time.sleep(.05)

    dot(x_pos - 330 * mult, y_pos - 330 * mult)
    pygame.display.update()
    clock.tick(60)
    # Print the different coordinates
    print("Vx : {} Vy : {}".format(x_pos, y_pos))
