import pygame
import random
import math


final_cost1 = 0
final_cost2 = 0
final_index = -1

def creatingEnvironment():
    screen.blit(blueKicker, (blueKickerX, blueKickerY))
    screen.blit(blue1, (blue1X, blue1Y))
    screen.blit(blue2, (blue2X, blue2Y))
    screen.blit(blue3, (blue3X, blue3Y))
    screen.blit(red1, (red1X, red1Y))
    screen.blit(red2, (red2X, red2Y))
    screen.blit(red3, (red3X, red3Y))


def checkRedBetween(x_src, y_src, x_dest, y_dest):
    if y_src < y_dest:
        temp=y_src
        y_src=y_dest
        y_dest=temp
        temp = x_src
        x_src = x_dest
        x_dest = temp
    try:
        m_test = (y_dest-y_src)/(x_dest-x_src)
        c_test = y_dest - m_test * x_dest
        while(y_src >= y_dest):
            #print(0)
            y_src -= 0.1
            x_src = (y_src - c_test) / m_test
            if y_src < red1Y + 32 and y_src > red1Y-32 and x_src < red1X+32 and x_src > red1X-32:
                return True
            if y_src < red2Y + 32 and y_src > red2Y-32 and x_src < red2X+32 and x_src > red2X-32:
                return True
            if y_src < red3Y + 32 and y_src > red3Y-32 and x_src < red3X+32 and x_src > red3X-32:
                return True
        return False
    except:
        while (y_src >= y_dest):
            # print(0)
            y_src -= 0.1
            if y_src < red1Y + 32 and y_src > red1Y - 32 and x_src < red1X + 32 and x_src > red1X - 32:
                return True
            if y_src < red2Y + 32 and y_src > red2Y - 32 and x_src < red2X + 32 and x_src > red2X - 32:
                return True
            if y_src < red3Y + 32 and y_src > red3Y - 32 and x_src < red3X + 32 and x_src > red3X - 32:
                return True
        return False

def move_ball(ballx, bally, m_ball, c_ball):
    if m_ball==10000:
        bally-=1
        return ballx,bally
    bally -= 1
    ballx = (bally-c_ball)/m_ball
    return ballx, bally



# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((576,768))
background = pygame.image.load('Field.png')

# Title and Icon
pygame.display.set_caption("Football_M20CS017")
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)


# Setting the ball
ball = pygame.image.load('ball.png')
ballx = 9*32-16
bally = 12*32-16

# Setting Environment Location
blueKicker = pygame.image.load('blue_player.png')
blueKickerX = 9*32
blueKickerY = 12*32

blue1 = pygame.image.load('blue_player.png')
blue1X = random.randint(3,14)*32
blue1Y = random.randint(1,5)*32

red1 = pygame.image.load('red_player.png')
red1X = random.randint(3,14)*32
red1Y = random.randint(1,5)*32

blue2 = pygame.image.load('blue_player.png')
blue2X = random.randint(1,16)*32
blue2Y = random.randint(6,10)*32

blue3 = pygame.image.load('blue_player.png')
blue3X = random.randint(1,16)*32
blue3Y = random.randint(6,10)*32

red2 = pygame.image.load('red_player.png')
red2X = random.randint(1,16)*32
red2Y = random.randint(6,10)*32

red3 = pygame.image.load('red_player.png')
red3X = random.randint(1,16)*32
red3Y = random.randint(6,10)*32

cost1 = math.sqrt((blue1X-blueKickerX) * (blue1X-blueKickerX) + (blue1Y-blueKickerY) * (blue1Y-blueKickerY)) + math.sqrt((blue1X-9*32) * (blue1X-9*32) + (blue1Y-0) * (blue1Y-0))
cost2 = math.sqrt((blue2X-blueKickerX) * (blue2X-blueKickerX) + (blue2Y-blueKickerY) * (blue2Y-blueKickerY)) + math.sqrt((blue2X-9*32) * (blue2X-9*32) + (blue2Y-0) * (blue2Y-0))
cost3 = math.sqrt((blue3X-blueKickerX) * (blue3X-blueKickerX) + (blue3Y-blueKickerY) * (blue3Y-blueKickerY)) + math.sqrt((blue3X-9*32) * (blue3X-9*32) + (blue3Y-0) * (blue3Y-0))

cost4 = math.sqrt((blue1X-blueKickerX) * (blue1X-blueKickerX) + (blue1Y-blueKickerY) * (blue1Y-blueKickerY)) + math.sqrt((blue1X-blue2X) * (blue1X-blue2X) + (blue1Y-blue2Y) * (blue1Y-blue2Y)) + math.sqrt((blue2X-9*32) * (blue2X-9*32) + (blue2Y-0) * (blue2Y-0))
cost5 = math.sqrt((blue1X-blueKickerX) * (blue1X-blueKickerX) + (blue1Y-blueKickerY) * (blue1Y-blueKickerY)) + math.sqrt((blue1X-blue3X) * (blue1X-blue3X) + (blue1Y-blue3Y) * (blue1Y-blue3Y)) + math.sqrt((blue3X-9*32) * (blue3X-9*32) + (blue3Y-0) * (blue3Y-0))
cost6 = math.sqrt((blue2X-blueKickerX) * (blue2X-blueKickerX) + (blue2Y-blueKickerY) * (blue2Y-blueKickerY)) + math.sqrt((blue3X-blue2X) * (blue3X-blue2X) + (blue3Y-blue2Y) * (blue3Y-blue2Y)) + math.sqrt((blue3X-9*32) * (blue3X-9*32) + (blue3Y-0) * (blue3Y-0))
cost7 = math.sqrt((blue2X-blueKickerX) * (blue2X-blueKickerX) + (blue2Y-blueKickerY) * (blue2Y-blueKickerY)) + math.sqrt((blue1X-blue2X) * (blue1X-blue2X) + (blue1Y-blue2Y) * (blue1Y-blue2Y)) + math.sqrt((blue1X-9*32) * (blue1X-9*32) + (blue1Y-0) * (blue1Y-0))
cost8 = math.sqrt((blue3X-blueKickerX) * (blue3X-blueKickerX) + (blue3Y-blueKickerY) * (blue3Y-blueKickerY)) + math.sqrt((blue3X-blue2X) * (blue3X-blue2X) + (blue3Y-blue2Y) * (blue3Y-blue2Y)) + math.sqrt((blue2X-9*32) * (blue2X-9*32) + (blue2Y-0) * (blue2Y-0))
cost9 = math.sqrt((blue3X-blueKickerX) * (blue3X-blueKickerX) + (blue3Y-blueKickerY) * (blue3Y-blueKickerY)) + math.sqrt((blue1X-blue3X) * (blue1X-blue3X) + (blue1Y-blue3Y) * (blue1Y-blue3Y)) + math.sqrt((blue1X-9*32) * (blue1X-9*32) + (blue1Y-0) * (blue1Y-0))

cost10 = math.sqrt((blue1X-blueKickerX) * (blue1X-blueKickerX) + (blue1Y-blueKickerY) * (blue1Y-blueKickerY)) + math.sqrt((blue1X-blue2X) * (blue1X-blue2X) + (blue1Y-blue2Y) * (blue1Y-blue2Y)) + math.sqrt((blue3X-blue2X) * (blue3X-blue2X) + (blue3Y-blue2Y) * (blue3Y-blue2Y)) + math.sqrt((blue3X-9*32) * (blue3X-9*32) + (blue3Y-0) * (blue3Y-0))
cost11 = math.sqrt((blue1X-blueKickerX) * (blue1X-blueKickerX) + (blue1Y-blueKickerY) * (blue1Y-blueKickerY)) + math.sqrt((blue1X-blue3X) * (blue1X-blue3X) + (blue1Y-blue3Y) * (blue1Y-blue3Y)) + math.sqrt((blue3X-blue2X) * (blue3X-blue2X) + (blue3Y-blue2Y) * (blue3Y-blue2Y)) + math.sqrt((blue2X-9*32) * (blue2X-9*32) + (blue2Y-0) * (blue2Y-0))
cost12 = math.sqrt((blue2X-blueKickerX) * (blue2X-blueKickerX) + (blue2Y-blueKickerY) * (blue2Y-blueKickerY)) + math.sqrt((blue3X-blue2X) * (blue3X-blue2X) + (blue3Y-blue2Y) * (blue3Y-blue2Y)) + math.sqrt((blue1X-blue3X) * (blue1X-blue3X) + (blue1Y-blue3Y) * (blue1Y-blue3Y)) + math.sqrt((blue1X-9*32) * (blue1X-9*32) + (blue1Y-0) * (blue1Y-0))
cost13 = math.sqrt((blue2X-blueKickerX) * (blue2X-blueKickerX) + (blue2Y-blueKickerY) * (blue2Y-blueKickerY)) + math.sqrt((blue1X-blue2X) * (blue1X-blue2X) + (blue1Y-blue2Y) * (blue1Y-blue2Y)) + math.sqrt((blue1X-blue3X) * (blue1X-blue3X) + (blue1Y-blue3Y) * (blue1Y-blue3Y)) + math.sqrt((blue3X-9*32) * (blue3X-9*32) + (blue3Y-0) * (blue3Y-0))
cost14 = math.sqrt((blue3X-blueKickerX) * (blue3X-blueKickerX) + (blue3Y-blueKickerY) * (blue3Y-blueKickerY)) + math.sqrt((blue3X-blue2X) * (blue3X-blue2X) + (blue3Y-blue2Y) * (blue3Y-blue2Y)) + math.sqrt((blue1X-blue2X) * (blue1X-blue2X) + (blue1Y-blue2Y) * (blue1Y-blue2Y)) + math.sqrt((blue1X-9*32) * (blue1X-9*32) + (blue1Y-0) * (blue1Y-0))
cost15 = math.sqrt((blue3X-blueKickerX) * (blue3X-blueKickerX) + (blue3Y-blueKickerY) * (blue3Y-blueKickerY)) + math.sqrt((blue1X-blue3X) * (blue1X-blue3X) + (blue1Y-blue3Y) * (blue1Y-blue3Y)) + math.sqrt((blue1X-blue2X) * (blue1X-blue2X) + (blue1Y-blue2Y) * (blue1Y-blue2Y)) + math.sqrt((blue2X-9*32) * (blue2X-9*32) + (blue2Y-0) * (blue2Y-0))

# checking red in between for cost 1
if(checkRedBetween(blueKickerX, blueKickerY, blue1X, blue1Y) or checkRedBetween(9*32, 0, blue1X, blue1Y)):
    cost1 = 100000
# checking red in between for cost 2
if(checkRedBetween(blueKickerX, blueKickerY, blue2X, blue2Y) or checkRedBetween(9*32, 0, blue2X, blue2Y)):
    cost2 = 100000
# checking red in between for cost 3
if(checkRedBetween(blueKickerX, blueKickerY, blue3X, blue3Y) or checkRedBetween(9*32, 0, blue3X, blue3Y)):
    cost3 = 100000
# checking red in between for cost 4
if(checkRedBetween(blueKickerX, blueKickerY, blue1X, blue1Y) or checkRedBetween(blue1X, blue1Y, blue2X, blue2Y) or checkRedBetween(9*32, 0, blue2X, blue2Y)):
    cost4 = 100000
# checking red in between for cost 5
if(checkRedBetween(blueKickerX, blueKickerY, blue1X, blue1Y) or checkRedBetween(blue1X, blue1Y, blue3X, blue3Y) or checkRedBetween(9*32, 0, blue3X, blue3Y)):
    cost5 = 100000
# checking red in between for cost 6
if(checkRedBetween(blueKickerX, blueKickerY, blue2X, blue2Y) or checkRedBetween(blue2X, blue2Y, blue3X, blue3Y) or checkRedBetween(9*32, 0, blue3X, blue3Y)):
    cost6 = 100000
# checking red in between for cost 7
if(checkRedBetween(blueKickerX, blueKickerY, blue2X, blue2Y) or checkRedBetween(blue1X, blue1Y, blue2X, blue2Y) or checkRedBetween(9*32, 0, blue1X, blue1Y)):
    cost7 = 100000
# checking red in between for cost 8
if(checkRedBetween(blueKickerX, blueKickerY, blue3X, blue3Y) or checkRedBetween(blue2X, blue2Y, blue3X, blue3Y) or checkRedBetween(9*32, 0, blue2X, blue2Y)):
    cost8 = 100000
# checking red in between for cost 9
if(checkRedBetween(blueKickerX, blueKickerY, blue3X, blue3Y) or checkRedBetween(blue1X, blue1Y, blue3X, blue3Y) or checkRedBetween(9*32, 0, blue1X, blue1Y)):
    cost9 = 100000
# checking red in between for cost 10
if(checkRedBetween(blueKickerX, blueKickerY, blue1X, blue1Y) or checkRedBetween(blue1X, blue1Y, blue2X, blue2Y) or checkRedBetween(blue2X, blue2Y, blue3X, blue3Y) or checkRedBetween(9*32, 0, blue3X, blue3Y)):
    cost10 = 100000
# checking red in between for cost 11
if(checkRedBetween(blueKickerX, blueKickerY, blue1X, blue1Y) or checkRedBetween(blue1X, blue1Y, blue3X, blue3Y) or checkRedBetween(blue2X, blue2Y, blue3X, blue3Y) or checkRedBetween(9*32, 0, blue2X, blue2Y)):
    cost11 = 100000
# checking red in between for cost 12
if(checkRedBetween(blueKickerX, blueKickerY, blue2X, blue2Y) or checkRedBetween(blue2X, blue2Y, blue3X, blue3Y) or checkRedBetween(blue1X, blue1Y, blue3X, blue3Y) or checkRedBetween(9*32, 0, blue1X, blue1Y)):
    cost12 = 100000
# checking red in between for cost 13
if(checkRedBetween(blueKickerX, blueKickerY, blue2X, blue2Y) or checkRedBetween(blue1X, blue1Y, blue2X, blue2Y) or checkRedBetween(blue1X, blue1Y, blue3X, blue3Y) or checkRedBetween(9*32, 0, blue3X, blue3Y)):
    cost13 = 100000
# checking red in between for cost 14
if(checkRedBetween(blueKickerX, blueKickerY, blue3X, blue3Y) or checkRedBetween(blue2X, blue2Y, blue3X, blue3Y) or checkRedBetween(blue1X, blue1Y, blue2X, blue2Y) or checkRedBetween(9*32, 0, blue1X, blue1Y)):
    cost14 = 100000
# checking red in between for cost 15
if(checkRedBetween(blueKickerX, blueKickerY, blue3X, blue3Y) or checkRedBetween(blue1X, blue1Y, blue3X, blue3Y) or checkRedBetween(blue1X, blue1Y, blue2X, blue2Y) or checkRedBetween(9*32, 0, blue2X, blue2Y)):
    cost15 = 100000

costList = [cost1, cost2, cost3, cost4, cost5, cost6, cost7, cost8, cost9, cost10, cost11, cost12, cost13, cost14, cost15]
costListIndex = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


# sorting based on the cost


for i in range(len(costList)-1):
    for j in range(0, len(costList) - i - 1):

        if costList[j] > costList[j + 1]:
            costList[j], costList[j + 1] = costList[j + 1], costList[j]
            costListIndex[j], costListIndex[j + 1] = costListIndex[j + 1], costListIndex[j]

print(costList)
print(costListIndex)
final_cost1 = costList[0]
final_cost2 = costList[1]
final_index = costListIndex[0]

#calculating the slope
try:
    mk1 = (blueKickerY-blue1Y)/(blueKickerX-blue1X)
except:
    mk1 = 10000
try:
    mk2 = (blueKickerY-blue2Y)/(blueKickerX-blue2X)
except:
    mk2 = 10000
try:
    mk3 = (blueKickerY-blue3Y)/(blueKickerX-blue3X)
except:
    mk3 = 10000
try:
    m1g = (blue1Y-0)/(blue1X-9*32)
except:
    m1g = 10000
try:
    m2g = (blue2Y-0)/(blue2X-9*32)
except:
    m2g = 10000
try:
    m3g = (blue3Y-0)/(blue3X-9*32)
except:
    m3g = 10000
try:
    m12 = (blue1Y-blue2Y)/(blue1X-blue2X)
except:
    m12 = 10000
try:
    m13 = (blue1Y-blue3Y)/(blue1X-blue3X)
except:
    m13 = 10000
try:
    m23 = (blue2Y-blue3Y)/(blue2X-blue3X)
except:
    m23 = 10000


#calculating the intercept

ck1 = blueKickerY-mk1*blueKickerX
ck2 = blueKickerY-mk2*blueKickerX
ck3 = blueKickerY-mk3*blueKickerX

c1g = 0-m1g*9*32
c2g = 0-m2g*9*32
c3g = 0-m3g*9*32

c12 = blue1Y-m12*blue1X
c13 = blue1Y-m13*blue1X
c23 = blue2Y-m23*blue2X


#Setting the Cost
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
font = pygame.font.Font('freesansbold.ttf', 32)
outputstring = "Cost1: "+str(round(final_cost1,2))+"  Cost2: "+str(round(final_cost2,2))
text = font.render(outputstring, True, green, blue)
textRect = text.get_rect()
textRect.center = (9*32,18*32)


# GameOver Text
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
font = pygame.font.Font('freesansbold.ttf', 32)
outputstring = "Can't Score, Game Over"
text2 = font.render(outputstring, True, white, blue)
textRect2 = text.get_rect()
textRect2.center = (340, 768/2)

# GameOver Text
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
font = pygame.font.Font('freesansbold.ttf', 32)
outputstring = "Goal!! You Won"
text3 = font.render(outputstring, True, white, blue)
textRect3 = text.get_rect()
textRect3.center = (380, 768/2)

#game loop
running = True
while running:
    # RGB background
    screen.fill((0, 128, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    creatingEnvironment()
    screen.blit(text, textRect)


    # #MOVING THE BALL
    screen.blit(ball, (ballx, bally))

    if final_cost1 == 100000:
        screen.blit(text2, textRect2)
    else:
        if final_index == 1:
            if bally > blue1Y:
                ballx, bally = move_ball(ballx, bally, mk1, ck1)
            elif bally > 0:
                ballx, bally = move_ball(ballx, bally, m1g, c1g)

        if final_index == 2:
            if bally > blue2Y:
                ballx, bally = move_ball(ballx, bally, mk2, ck2)
            elif bally > 0:
                ballx, bally = move_ball(ballx, bally, m2g, c2g)

        if final_index == 3:
            if bally > blue3Y:
                ballx, bally = move_ball(ballx, bally, mk3, ck3)
            elif bally > 0:
                ballx, bally = move_ball(ballx, bally, m3g, c3g)

        if final_index == 4:
            if bally > blue1Y:
                ballx, bally = move_ball(ballx, bally, mk1, ck1)
            elif bally > blue2Y:
                ballx, bally = move_ball(ballx, bally, m12, c12)
            elif bally > 0:
                ballx, bally = move_ball(ballx, bally, m2g, c2g)

        if final_index == 5:
            if bally > blue1Y:
                ballx, bally = move_ball(ballx, bally, mk1, ck1)
            elif bally > blue3Y:
                ballx, bally = move_ball(ballx, bally, m13, c13)
            elif bally > 0:
                ballx, bally = move_ball(ballx, bally, m3g, c3g)

        if final_index == 6:
            if bally > blue2Y:
                ballx, bally = move_ball(ballx, bally, mk2, ck2)
            elif bally > blue3Y:
                ballx, bally = move_ball(ballx, bally, m23, c23)
            elif bally > 0:
                ballx, bally = move_ball(ballx, bally, m3g, c3g)

        if final_index == 7:
            if bally > blue2Y:
                ballx, bally = move_ball(ballx, bally, mk2, ck2)
            elif bally > blue1Y:
                ballx, bally = move_ball(ballx, bally, m12, c12)
            elif bally > 0:
                ballx, bally = move_ball(ballx, bally, m1g, c1g)

        if final_index == 8:
            if bally > blue3Y:
                ballx, bally = move_ball(ballx, bally, mk3, ck3)
            elif bally > blue2Y:
                ballx, bally = move_ball(ballx, bally, m23, c23)
            elif bally > 0:
                ballx, bally = move_ball(ballx, bally, m2g, c2g)

        if final_index == 9:
            if bally > blue3Y:
                ballx, bally = move_ball(ballx, bally, mk3, ck3)
            elif bally > blue1Y:
                ballx, bally = move_ball(ballx, bally, m13, c13)
            elif bally > 0:
                ballx, bally = move_ball(ballx, bally, m1g, c1g)

        if final_index == 10:
            if bally > blue1Y:
                ballx, bally = move_ball(ballx, bally, mk1, ck1)
            elif bally > blue2Y:
                ballx, bally = move_ball(ballx, bally, m12, c12)
            elif bally > blue3Y:
                ballx, bally = move_ball(ballx, bally, m23, c23)
            elif bally > 0:
                ballx, bally = move_ball(ballx, bally, m3g, c3g)

        if final_index == 11:
            if bally > blue1Y:
                ballx, bally = move_ball(ballx, bally, mk1, ck1)
            elif bally > blue3Y:
                ballx, bally = move_ball(ballx, bally, m13, c13)
            elif bally > blue2Y:
                ballx, bally = move_ball(ballx, bally, m23, c23)
            elif bally > 0:
                ballx, bally = move_ball(ballx, bally, m2g, c2g)

        if final_index == 12:
            if bally > blue2Y:
                ballx, bally = move_ball(ballx, bally, mk2, ck2)
            elif bally > blue3Y:
                ballx, bally = move_ball(ballx, bally, m23, c23)
            elif bally > blue1Y:
                ballx, bally = move_ball(ballx, bally, m13, c13)
            elif bally > 0:
                ballx, bally = move_ball(ballx, bally, m1g, c1g)

        if final_index == 13:
            if bally > blue2Y:
                ballx, bally = move_ball(ballx, bally, mk2, ck2)
            elif bally > blue1Y:
                ballx, bally = move_ball(ballx, bally, m12, c12)
            elif bally > blue3Y:
                ballx, bally = move_ball(ballx, bally, m13, c13)
            elif bally > 0:
                ballx, bally = move_ball(ballx, bally, m3g, c3g)

        if final_index == 14:
            if bally > blue3Y:
                ballx, bally = move_ball(ballx, bally, mk3, ck3)
            elif bally > blue2Y:
                ballx, bally = move_ball(ballx, bally, m23, c23)
            elif bally > blue1Y:
                ballx, bally = move_ball(ballx, bally, m12, c12)
            elif bally > 0:
                ballx, bally = move_ball(ballx, bally, m1g, c1g)

        if final_index == 15:
            if bally > blue3Y:
                ballx, bally = move_ball(ballx, bally, mk3, ck3)
            elif bally > blue1Y:
                ballx, bally = move_ball(ballx, bally, m13, c13)
            elif bally > blue2Y:
                ballx, bally = move_ball(ballx, bally, m12, c12)
            elif bally > 0:
                ballx, bally = move_ball(ballx, bally, m2g, c2g)

        if bally<32:
            screen.blit(text3, textRect3)


    pygame.display.update()