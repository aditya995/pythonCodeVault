import turtle

player = turtle.Turtle()
player.shape('circle')
player.shapesize(2, 2, 2)
player.speed(0)
player.penup()
player.left(90)
player.color('green')

counter = 0
distance = 75
speed = 20

while distance:
    if counter % 10 > 4:
        turtle.delay(speed)
        if counter % 10 == 5:
            distance //= 2
            player.right(180)
        player.forward(distance)
    else:
        if counter % 10 == 0:
            player.right(180)
        player.forward(distance)
    counter += 1

turtle.done()
