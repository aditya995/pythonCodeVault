import re
import turtle


def up():
    global scale
    global history
    player.setheading(90)
    player.forward(scale)
    history += '1'


def down():
    global scale
    global history
    player.setheading(270)
    player.forward(scale)
    history += '2'


def left():
    global scale
    global history
    player.setheading(180)
    player.forward(scale)
    history += '3'


def right():
    global scale
    global history
    player.setheading(0)
    player.forward(scale)
    history += '4'


def colorb():
    global history
    global penstat
    player.color('black', 'white')
    history += '5'
    print('Drawing 🎨 color ⬛' if penstat else 'Not Drawing ❌color ⬛')


def colorg():
    global history
    player.color('green', 'white')
    history += '6'
    print('Drawing 🎨 color 🟩' if penstat else 'Not Drawing ❌color 🟩')


def penUpDowntoggle():
    global history
    history += '7'
    global penstat
    if(penstat):
        player.penup()
        player.color('white')
        penstat = False
        print('Not Drawing ❌')
    else:
        player.pendown()
        player.color('red')
        penstat = True
        print('Drawing 🎨')


def clScr():
    player.clear()
    global history
    history = ''
    print('Screen Cleared!!')


def clHis():
    global history
    global scale
    global bufferScale
    global refreshed
    refreshed = True
    bufferScale = scale
    history = ''
    f = open("./Programs/graphics/saved.art", "w")  # TODO: set path correctly
    f.write(f'{scale}\n')
    f.close()
    print('Create new artwork!! 🌏\nChoose color b(for ⬛ ) or g(for 🟩 )')


def save():
    global scale
    global history
    global bufferScale
    global initialScale
    f = open("./Programs/graphics/saved.art", "w")  # TODO: set path correctly
    f.write(f'{bufferScale if refreshed else initialScale}\n{history}\n')
    print(f'Buffer Scale ******* {bufferScale}')
    f.close()
    print('Artwork saved!! ✔✔')


def printLoadedArt():
    global scale
    f = open("./Programs/graphics/saved.art", "r")  # TODO: set path correctly
    loaded = f.read()
    f.close()
    cacheList = loaded.split('\n')
    fileLineCount = len(cacheList)-1
    for k in range(0, fileLineCount):
        if k % 2 == 0:
            scale = int(cacheList[k])
            continue
        else:
            for i in cacheList[k]:
                funcBind[i]()
                # print(i, end='')
    print(f'Previous art printed 🌏\nCurrent scale: {scale}')


def scaleBrush():
    global scale
    global history
    try:
        scale = int(input('Input new scale\n'))
    except Exception as ex:
        print(f"🤐 {ex}")
    else:
        print(f'Current scale: {scale}')
        history += f'\n{scale}\n'


def makeGrid():
    global history
    global scale
    x = int(input('Grid- number of row\n'))
    y = int(input('Grid- number of column\n'))
    try:
        scale = int(input('scale\n'))
    except Exception as ex:
        print(f"🤐 {ex}")
    else:
        history += f'\n{scale}\n'
        print(f'Current scale: {scale}')
    for i in range(x+1):
        for j in range(y):
            if i % 2 == 1:
                left()
            else:
                right()
        down()

    # if x % 2 == 0:
    #     player.left(90)
    # else:
    #     player.right(90)
    colorb()
    up()
    colorg()

    for i in range(y+1):
        for j in range(x):
            if i % 2 == 1:
                down()
            else:
                up()
        if x % 2 == 0:
            left()
            print('left')
        else:
            right()
            print('right')


# main program

refreshed = False
bufferScale = 100
initialScale = 5
scale = initialScale
history = ''
player = turtle.Turtle()
player.shape('classic')
player.speed(0)
player.color('green', 'red')
turtle.bgcolor('black')
penstat = True
turtle.listen()

# player.begin_fill()
funcBind = {
    '1': up,
    '2': down,
    '3': left,
    '4': right,
    '5': colorb,
    '6': colorg,
    '7': penUpDowntoggle,
}
refreshed = False

turtle.onkey(colorb, 'b')
turtle.onkey(colorg, 'g')
turtle.onkey(penUpDowntoggle, 'p')
turtle.onkeypress(up, 'Up')
turtle.onkeypress(left, 'Left')
turtle.onkeypress(right, 'Right')
turtle.onkeypress(down, 'Down')
turtle.onkey(save, 's')
turtle.onkey(clScr, 'c')
turtle.onkey(scaleBrush, 'S')
turtle.onkey(printLoadedArt, 'l')
turtle.onkey(clHis, 'n')
turtle.onkey(makeGrid, 'G')
# player.end_fill()
turtle.mainloop()
