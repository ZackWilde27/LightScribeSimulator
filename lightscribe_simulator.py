# LightScribe Simulator

# LightScribe drives needed a tracking sensor to know the exact rotation the disc to properly draw the image
# but if it always spins at the same speed (which CDs apparently needed to do), why did they need that?
# The rotation of the disc can be figured out based on how much time has passed

# This simulation proves that theory, that there is no need for a tracking sensor and thus any off-the-shelf drive COULD
# have worked.

import pygame
from math import cos, sin
from time import perf_counter as time
from random import random as rand

PI = 3.14159
fullRotation = PI * 2

spindleSize = 0.25

# The faster the disc spins the faster the image is drawn
# but depending on how fast the code runs that might result in spread out dots instead of a continuous image
rotationsPerSecond = 2

spinRate = fullRotation * rotationsPerSecond
pullInRate = (1/256) * rotationsPerSecond

# Randomizes the disc's initial angle, to emulate inserting the disc at whatever angle
randomizeDiscOrientation = True

# Shows the disc spinning like it would in a real drive, instead of the laser travelling around the disc
# Enabling this will slow the code down, requiring a lower rotationsPerSecond
showDiscSpinning = False

# Shows the estimated sample point on the source image, at the cost of performance/rotationsPerSecond
showSamplePoint = False

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

srcImage = pygame.image.load("lightscribe.png")
debugImage = pygame.transform.rotate(srcImage, 0)

dstImage = pygame.transform.rotate(srcImage, 0)

dstImage.fill("black")
screen.fill("black")

def AngleToCoordinates(radians, width, height):
        x = sin(radians) * distance
        y = cos(radians) * distance
        # Convert from [-1, 1] to [0, 1]
        x *= 0.5
        y *= 0.5
        x += 0.5
        y += 0.5

        # Convert from [0, 1] to texture coordinates
        x *= width - 1
        y *= height - 1
        return (int(x), int(y))

screen.blit(srcImage, (1280-512, 0))

distance = 1
angle = 0
if randomizeDiscOrientation:
    angle = rand() * fullRotation

start = timer = time()
doneYet = False

while True:
    if pygame.QUIT in pygame.event.get():
        break

    # If you don't care about seeing it in action and want it to run as quickly as possible, change this if to a while, and the elif below into an if
    # That won't automatically make it run faster (it is based on time after all)
    # but it means you can increase the rotationsPerSecond by quite a bit and still get a continuous image
    if distance > spindleSize:
        now = time()
        elapsed = now - start
        delta = now - timer
        timer = now

        # These are the real coordinates, based on the angle of the disc
        (x, y) = AngleToCoordinates(angle, 512, 512)

        # These are the estimated coordinates based on time, used to sample the source image
        (x2, y2) = AngleToCoordinates(elapsed * spinRate, 512, 512)

        if showSamplePoint:
                debugImage.blit(srcImage, (0, 0))
                pygame.draw.circle(debugImage, (0, 255, 0, 255), (x2, y2), 5.0)
                screen.blit(debugImage, (1280-512, 0))

        if showDiscSpinning:
                dstImage.set_at((x, y), srcImage.get_at((x2, y2)))
                rotated = pygame.transform.rotate(dstImage, angle * -57.29578)
                screen.blit(rotated, rotated.get_rect(center=(256, 256)))
        else:
                screen.set_at((x, y), srcImage.get_at((x2, y2)))

        angle += spinRate * delta
        distance -= pullInRate * delta

    elif not doneYet:
        print("Done!")
        print("Completed in", time() - start, "seconds")
        doneYet = True

    pygame.display.flip()

pygame.quit()
