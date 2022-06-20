import pyttsx3
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
    try:
        x = int(input('Grid- number of row\n'))
        y = int(input('Grid- number of column\n'))
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


def drawString():
    global stringStream
    global charDict
    global scale
    global history
    global charCounter
    global penstat
    history += f'\n{scale}\n'
    stringStream = stringStream.lower()
    if not penstat:
        penUpDowntoggle()
    for i in stringStream:
        print('charCounter ', charCounter)
        if i == '\n':
            charDict[i] = '5'+10*'2'+'3'*(charCounter*7)+'34'
            charCounter = 0
        else:
            charCounter += 1
        for j in charDict[i]:
            funcBind[j]()
        if i == '\n':
            charDict[i] = ''
    charCounter = 0


def drawText():
    global stringStream
    content = 'something to be replaced'
    stringStream = ''
    print(
        'Regex for input [A-Za-z-0-9+,() \\n]\nPress enter twice to exit multiline input')
    while content != '':
        content = input()
        stringStream += content+'\n'
    # stringStream = 'abc defghij\nklmnopqrst\nuvwxyz\n0123456789\n,(+ -)'
    drawString()
    speaker = pyttsx3.init()
    speaker.say(stringStream)
    speaker.runAndWait()


def drawInstruction():
    global stringStream
    global scHeight
    global scWidth
    global penstat
    global scale
    if penstat:
        penUpDowntoggle()
    pos = ((-scWidth/2)+100*scale, (scHeight/2)-100*scale)
    # stringStream = 'p, toggle penup-down\n(b, g) colors\narrows, move\nn, create pattern\ns, save pattern\nl, draw saved-pattern\nshift s, change scale\nq, create grid, give console-input\nc, clear screen\nshift i, info\nw, draw text'
    stringStream = 'press p,b,g,arrows,s,c,l,n,w\nshift+s,g,i'
    player.setpos(pos)
    speaker = pyttsx3.init()
    speaker.say('Instructions are written below')
    speaker.runAndWait()
    drawString()
    speaker = pyttsx3.init()
    speaker.say(stringStream)
    speaker.runAndWait()


charDict = {
    '\n': '',
    'a': '61111444441131133322322444442222544',
    'b': '61111111142222222234444141131333444141131333222222224445444',
    'c': '54644414511111631423113332322222242444145244',
    'd': '61111111144424422222233233344454444',
    'e': '644444134432333331111444441221333331111444442344522222224',
    'f': '64334111144122133111144444224334522222244',
    'g': '5464441411133215144163413133323222222424445444',
    'h': '611111111222244444111122222222544',
    'i': '544644333411111111344432222222245444',
    'j': '51611344322424441411111113333312214444422222225244',
    'k': '61111111122224141414143232323224242424544',
    'l': '6111111112222222244444544',
    'm': '6111111112424241414122222222544',
    'n': '61111111122422422424241111111122222222544',
    'o': '546131111114144424222222323334445444',
    'p': '61111111144442422323333444452222444',
    'q': '546131111114144424222222323334441131242424254134',
    'r': '61111111144442422323333424242424544',
    's': '546131242444141131333131141444245222242224',
    't': '544611111111334444433222222223454444',
    'u': '54613111111122222224244414111111122222225244',
    'v': '544643113111311122242224224114111411122252222244',
    'w': '611111111222222224114111422242241111111122222222544',
    'x': '6141141431311312422424141141232232242242544',
    'y': '544644333411114222211113131131242242414114125222222244',
    'z': '64444433333141411411414133333522222226244444544',
    '0': '54613111111414442422222232333114141411142222225244',
    '1': '54644431111111132324222222445444',
    '2': '6444441331414111313133232224413141242423232323244444544',
    '3': '54644414111341113133323224141424232342423231332424445444',
    '4': '544464111413211111322322411222222111133442333114114144542224222224',
    '5': '546444141113133311444413333322224442423231332424445444',
    '6': '546444141113133321114442411333332222222424516131414242323526445444',
    '7': '546411414114111333332444423223232224544444',
    '8': '5464441411134111313332322243222424516414131141313232424323242526445444',
    '9': '54644414111111313332322244445161313232444526223231332424445444',
    '(': '54444641131311414113232323224242424544',
    ')': '6414141411313131322424223232245444444',
    ' ': '4'*7,
    '-': '541116311444442233334444522244',
    '+': '544641114411331113222332244222454444',
    '*': '',
    '/': '',
    '#': '',
    '\\': '',
    ',': '5446413242154444',

}

funcBind = {
    '1': up,
    '2': down,
    '3': left,
    '4': right,
    '5': colorb,
    '6': colorg,
    '7': penUpDowntoggle,
}
# main program
stringStream = ''
refreshed = False
bufferScale = 100
initialScale = 2
scale = initialScale
history = ''
penstat = True
charCounter = 0
scHeight = 800
scWidth = 600

# Player creation
player = turtle.Turtle()
sc = turtle.Screen()
sc.setup(scWidth, scHeight)
player.shape('classic')
player.speed(0)
player.color('green', 'red')
turtle.bgcolor('black')
turtle.listen()

# main loop
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
turtle.onkey(drawInstruction, 'I')
turtle.onkey(drawText, 'w')
turtle.mainloop()
