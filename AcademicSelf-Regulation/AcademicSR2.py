#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on October 28, 2019, at 12:14
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'AcademicSR'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\tul00635\\Documents\\GitHub\\Self-Regulation-Psychopy-Files\\AcademicSelf-Regulation\\AcademicSR.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
instruct = visual.TextStim(win=win, name='instruct',
    text='In this part of the study, you will be choosing between answering practice questions for standardized tests, or playing a videogame. \n\nYou will be completing 5 rounds of the chosen option, and will then be given a chance to choose again.\n\nPrior to choosing, you will be given a regulation strategy to use. Please employ this strategy while making your decision.  \n\nPress SPACE to begin!',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.4, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
space = keyboard.Keyboard()

# Initialize components for Routine "ISI"
ISIClock = core.Clock()

# Initialize components for Routine "Cue"
CueClock = core.Clock()
regCue = visual.TextStim(win=win, name='regCue',
    text='REGULATE',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()

# Initialize components for Routine "Choice"
ChoiceClock = core.Clock()
choiceQ = visual.TextStim(win=win, name='choiceQ',
    text="Please indicate which option you would like to complete by pressing '1' for the choice on the left, or '2' for the choice on the right. ",
    font='Arial',
    pos=(0, 0.35), height=0.05, wrapWidth=1.4, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
choiceResp = keyboard.Keyboard()
testChoice = visual.TextStim(win=win, name='testChoice',
    text='Practice Standardized Test Questions',
    font='Arial',
    pos=(-0.41, 0.15), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
videogameChoice = visual.TextStim(win=win, name='videogameChoice',
    text='Play a Videogame',
    font='Arial',
    pos=(0.41, 0.15), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
gre = visual.ImageStim(
    win=win,
    name='gre', 
    image='gre.png', mask=None,
    ori=0, pos=(-.41, 0.02), size=(0.3, 0.105),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
gmat = visual.ImageStim(
    win=win,
    name='gmat', 
    image='gmat.png', mask=None,
    ori=0, pos=(-0.41, -0.13), size=(0.3, 0.11),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
lsat = visual.ImageStim(
    win=win,
    name='lsat', 
    image='lsat.png', mask=None,
    ori=0, pos=(-0.41, -0.27), size=(0.3, 0.11),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
game = visual.ImageStim(
    win=win,
    name='game', 
    image='game.png', mask=None,
    ori=0, pos=(0.41, -0.19), size=(0.4, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
doTestPractice = []
doGame = []
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "testQuestionsChoice"
testQuestionsChoiceClock = core.Clock()
testQChoice = visual.TextStim(win=win, name='testQChoice',
    text='What test would you like to practice questions for? Use the arrow keys to move up and down, then press ENTER to select.',
    font='Arial',
    pos=(0, 0.35), height=0.055, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='gre.png', mask=None,
    ori=0, pos=(0, 0.105), size=(0.3, 0.11),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='gmat.png', mask=None,
    ori=0, pos=(0, -0.05), size=(0.3, 0.11),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='lsat.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.3, 0.11),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
upDown = keyboard.Keyboard()
polygon = visual.Rect(
    win=win, name='polygon',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1.0, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1.0, depth=-5.0, interpolate=True)
enter = keyboard.Keyboard()

# Initialize components for Routine "testQs"
testQsClock = core.Clock()
TextQuestion = visual.TextStim(win=win, name='TextQuestion',
    text='default text',
    font='Arial',
    pos=(0, 0.35), height=0.028, wrapWidth=1.45, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
letterKey = keyboard.Keyboard()
enterKey = keyboard.Keyboard()
choiceA = visual.TextStim(win=win, name='choiceA',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.026, wrapWidth=1.4, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
choiceB = visual.TextStim(win=win, name='choiceB',
    text='default text',
    font='Arial',
    pos=(0, -0.1), height=0.026, wrapWidth=1.4, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
choiceC = visual.TextStim(win=win, name='choiceC',
    text='default text',
    font='Arial',
    pos=(0, -0.2), height=0.026, wrapWidth=1.4, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
choiceD = visual.TextStim(win=win, name='choiceD',
    text='default text',
    font='Arial',
    pos=(0, -0.3), height=0.026, wrapWidth=1.4, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
choiceE = visual.TextStim(win=win, name='choiceE',
    text='default text',
    font='Arial',
    pos=(0, -0.4), height=0.026, wrapWidth=1.4, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
conBlank = visual.TextStim(win=win, name='conBlank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "Game"
GameClock = core.Clock()
gameInstructions = visual.TextStim(win=win, name='gameInstructions',
    text='You will be playing a version of Pacman. You will be playing as the yellow dot. Your goal is to gather as many points while avoiding the red dots. \n\nWhen you are ready, press SPACE!',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
spaceKey = keyboard.Keyboard()
pacmanClock = core.Clock()
# Initialize components for Routine "pacman"
class vector(collections.Sequence):
    PRECISION = 6

    __slots__ = ('_x', '_y', '_hash')

    def __init__(self, x, y):
        self._hash = None
        self._x = round(x, self.PRECISION)
        self._y = round(y, self.PRECISION)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if self._hash is not None:
            raise ValueError('cannot set x after hashing')
        self._x = round(value, self.PRECISION)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if self._hash is not None:
            raise ValueError('cannot set y after hashing')
        self._y = round(value, self.PRECISION)

    def __hash__(self):
        if self._hash is None:
            pair = (self.x, self.y)
            self._hash = hash(pair)
        return self._hash

    def __len__(self):

        return 2

    def __getitem__(self, index):
        if index == 0:
            return self.x
        if index == 1:
            return self.y
        raise IndexError

    def copy(self):
        type_self = type(self)
        return type_self(self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, vector):
            return self.x != other.x or self.y != other.y
        return NotImplemented

    def __iadd__(self, other):
        if self._hash is not None:
            raise ValueError('cannot add vector after hashing')
        elif isinstance(other, vector):
            self.x += other.x
            self.y += other.y
        else:
            self.x += other
            self.y += other
        return self

    def __add__(self, other):
        copy = self.copy()
        return copy.__iadd__(other)

    __radd__ = __add__

    def move(self, other):
        self.__iadd__(other)

    def __isub__(self, other):
        if self._hash is not None:
            raise ValueError('cannot subtract vector after hashing')
        elif isinstance(other, vector):
            self.x -= other.x
            self.y -= other.y
        else:
            self.x -= other
            self.y -= other
        return self

    def __sub__(self, other):
        copy = self.copy()
        return copy.__isub__(other)

    def __imul__(self, other):
        if self._hash is not None:
            raise ValueError('cannot multiply vector after hashing')
        elif isinstance(other, vector):
            self.x *= other.x
            self.y *= other.y
        else:
            self.x *= other
            self.y *= other
        return self

    def __mul__(self, other):
        copy = self.copy()
        return copy.__imul__(other)

    __rmul__ = __mul__

    def scale(self, other):
        self.__imul__(other)

    def __itruediv__(self, other):
        if self._hash is not None:
            raise ValueError('cannot divide vector after hashing')
        elif isinstance(other, vector):
            self.x /= other.x
            self.y /= other.y
        else:
            self.x /= other
            self.y /= other
        return self

    def __truediv__(self, other):
        copy = self.copy()
        return copy.__itruediv__(other)

    def __neg__(self):
        copy = self.copy()
        copy.x = -copy.x
        copy.y = -copy.y
        return copy

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def rotate(self, angle):
        if self._hash is not None:
            raise ValueError('cannot rotate vector after hashing')
        radians = angle * math.pi / 180.0
        cosine = math.cos(radians)
        sine = math.sin(radians)
        x = self.x
        y = self.y
        self.x = x * cosine - y * sine
        self.y = y * cosine + x * sine

    def __repr__(self):
        type_self = type(self)
        name = type_self.__name__
        return '{}({!r}, {!r})'.format(name, self.x, self.y)

def floor(value, size, offset=200):
    return float(((value + offset) // size) * size - offset)


state = {'score': 0}
path = Turtle(visible=False)
writer = Turtle(visible=False)
aim = vector(5, 0)
pacman = vector(-40, -80)
ghosts = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]
defaultKeyboard = keyboard.Keyboard()
spaceKey = keyboard.Keyboard()
def displayEnd(textVar):
    display = visual.TextStim(win=win, text = textVar, font='Arial', pos=(-0.41, 0.15), color='white', height=0.06)
    display.setAutoDraw(True)
    if spaceKey.keys == 'space':
        continueRoutine = False


def square(x, y):
    "Draw square using path at (x, y)."
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()

def offset(point):
    "Return offset of point in tiles."
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

def valid(point):
    "Return True if point is valid in tiles."
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0

def world():
    "Draw world using path."
    bgcolor('black')
    path.color('blue')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')

def move():
    "Move pacman and all ghosts."
    writer.undo()
    writer.write(state['score'])

    clear()

    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')

    for point, course in ghosts:
        if valid(point + course):
            point.move(course)
        else:
            options = [
                vector(5, 0),
                vector(-5, 0),
                vector(0, 5),
                vector(0, -5),
            ]
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')

    update()

    for point, course in ghosts:
        if abs(pacman - point) < 20:
            print("You Died :(")
            displayEnd("Oh no! The game will restart soon")
            return

    ontimer(move, 100)

def change(x, y):
    "Change pacman aim if valid."
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y


def pacmanGame():

    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    writer.goto(160, 160)
    writer.color('white')
    writer.write(state['score'])
    listen()
    onkey(lambda: change(5, 0), 'Right')
    onkey(lambda: change(-5, 0), 'Left')
    onkey(lambda: change(0, 5), 'Up')
    onkey(lambda: change(0, -5), 'Down')
    world()
    move()
    done()
#End pacman vars & functs 



# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
# update component parameters for each repeat
space.keys = []
space.rt = []
# keep track of which components have finished
InstructionsComponents = [instruct, space]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruct* updates
    if instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct.frameNStart = frameN  # exact frame index
        instruct.tStart = t  # local t and not account for scr refresh
        instruct.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct, 'tStartRefresh')  # time at next scr refresh
        instruct.setAutoDraw(True)
    
    # *space* updates
    waitOnFlip = False
    if space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space.frameNStart = frameN  # exact frame index
        space.tStart = t  # local t and not account for scr refresh
        space.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space, 'tStartRefresh')  # time at next scr refresh
        space.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space.status == STARTED and not waitOnFlip:
        theseKeys = space.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            space.keys = theseKeys.name  # just the last key pressed
            space.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruct.started', instruct.tStartRefresh)
thisExp.addData('instruct.stopped', instruct.tStopRefresh)
# check responses
if space.keys in ['', [], None]:  # No response was made
    space.keys = None
thisExp.addData('space.keys',space.keys)
if space.keys != None:  # we had a response
    thisExp.addData('space.rt', space.rt)
thisExp.addData('space.started', space.tStartRefresh)
thisExp.addData('space.stopped', space.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
AllTrials = data.TrialHandler(nReps=5, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='AllTrials')
thisExp.addLoop(AllTrials)  # add the loop to the experiment
thisAllTrial = AllTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisAllTrial.rgb)
if thisAllTrial != None:
    for paramName in thisAllTrial:
        exec('{} = thisAllTrial[paramName]'.format(paramName))

for thisAllTrial in AllTrials:
    currentLoop = AllTrials
    # abbreviate parameter names if possible (e.g. rgb = thisAllTrial.rgb)
    if thisAllTrial != None:
        for paramName in thisAllTrial:
            exec('{} = thisAllTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ISI"-------
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = []
    for thisComponent in ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "ISI"-------
    while continueRoutine:
        # get current time
        t = ISIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ISIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ISI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Cue"-------
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    CueComponents = [regCue]
    for thisComponent in CueComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    CueClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Cue"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = CueClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=CueClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *regCue* updates
        if regCue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            regCue.frameNStart = frameN  # exact frame index
            regCue.tStart = t  # local t and not account for scr refresh
            regCue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(regCue, 'tStartRefresh')  # time at next scr refresh
            regCue.setAutoDraw(True)
        if regCue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > regCue.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                regCue.tStop = t  # not accounting for scr refresh
                regCue.frameNStop = frameN  # exact frame index
                win.timeOnFlip(regCue, 'tStopRefresh')  # time at next scr refresh
                regCue.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Cue"-------
    for thisComponent in CueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    AllTrials.addData('regCue.started', regCue.tStartRefresh)
    AllTrials.addData('regCue.stopped', regCue.tStopRefresh)
    
    # ------Prepare to start Routine "ISI"-------
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = []
    for thisComponent in ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "ISI"-------
    while continueRoutine:
        # get current time
        t = ISIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ISIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ISI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Choice"-------
    # update component parameters for each repeat
    choiceResp.keys = []
    choiceResp.rt = []
    blank.setText('')
    # keep track of which components have finished
    ChoiceComponents = [choiceQ, choiceResp, testChoice, videogameChoice, gre, gmat, lsat, game, blank]
    for thisComponent in ChoiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ChoiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Choice"-------
    while continueRoutine:
        # get current time
        t = ChoiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ChoiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *choiceQ* updates
        if choiceQ.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choiceQ.frameNStart = frameN  # exact frame index
            choiceQ.tStart = t  # local t and not account for scr refresh
            choiceQ.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choiceQ, 'tStartRefresh')  # time at next scr refresh
            choiceQ.setAutoDraw(True)
        if choiceQ.status == STARTED:
            if bool(blank.status == FINISHED):
                # keep track of stop time/frame for later
                choiceQ.tStop = t  # not accounting for scr refresh
                choiceQ.frameNStop = frameN  # exact frame index
                win.timeOnFlip(choiceQ, 'tStopRefresh')  # time at next scr refresh
                choiceQ.setAutoDraw(False)
        
        # *choiceResp* updates
        waitOnFlip = False
        if choiceResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choiceResp.frameNStart = frameN  # exact frame index
            choiceResp.tStart = t  # local t and not account for scr refresh
            choiceResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choiceResp, 'tStartRefresh')  # time at next scr refresh
            choiceResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(choiceResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(choiceResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if choiceResp.status == STARTED:
            if bool(choiceQ.status == FINISHED):
                # keep track of stop time/frame for later
                choiceResp.tStop = t  # not accounting for scr refresh
                choiceResp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(choiceResp, 'tStopRefresh')  # time at next scr refresh
                choiceResp.status = FINISHED
        if choiceResp.status == STARTED and not waitOnFlip:
            theseKeys = choiceResp.getKeys(keyList=['1', '2'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                choiceResp.keys = theseKeys.name  # just the last key pressed
                choiceResp.rt = theseKeys.rt
        
        # *testChoice* updates
        if testChoice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            testChoice.frameNStart = frameN  # exact frame index
            testChoice.tStart = t  # local t and not account for scr refresh
            testChoice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testChoice, 'tStartRefresh')  # time at next scr refresh
            testChoice.setAutoDraw(True)
        if testChoice.status == STARTED:
            if bool(blank.status == FINISHED):
                # keep track of stop time/frame for later
                testChoice.tStop = t  # not accounting for scr refresh
                testChoice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(testChoice, 'tStopRefresh')  # time at next scr refresh
                testChoice.setAutoDraw(False)
        
        # *videogameChoice* updates
        if videogameChoice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            videogameChoice.frameNStart = frameN  # exact frame index
            videogameChoice.tStart = t  # local t and not account for scr refresh
            videogameChoice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(videogameChoice, 'tStartRefresh')  # time at next scr refresh
            videogameChoice.setAutoDraw(True)
        if videogameChoice.status == STARTED:
            if bool(blank.status == FINISHED):
                # keep track of stop time/frame for later
                videogameChoice.tStop = t  # not accounting for scr refresh
                videogameChoice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(videogameChoice, 'tStopRefresh')  # time at next scr refresh
                videogameChoice.setAutoDraw(False)
        
        # *gre* updates
        if gre.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            gre.frameNStart = frameN  # exact frame index
            gre.tStart = t  # local t and not account for scr refresh
            gre.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(gre, 'tStartRefresh')  # time at next scr refresh
            gre.setAutoDraw(True)
        if gre.status == STARTED:
            if bool(blank.status == FINISHED):
                # keep track of stop time/frame for later
                gre.tStop = t  # not accounting for scr refresh
                gre.frameNStop = frameN  # exact frame index
                win.timeOnFlip(gre, 'tStopRefresh')  # time at next scr refresh
                gre.setAutoDraw(False)
        
        # *gmat* updates
        if gmat.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            gmat.frameNStart = frameN  # exact frame index
            gmat.tStart = t  # local t and not account for scr refresh
            gmat.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(gmat, 'tStartRefresh')  # time at next scr refresh
            gmat.setAutoDraw(True)
        if gmat.status == STARTED:
            if bool(blank.status == FINISHED):
                # keep track of stop time/frame for later
                gmat.tStop = t  # not accounting for scr refresh
                gmat.frameNStop = frameN  # exact frame index
                win.timeOnFlip(gmat, 'tStopRefresh')  # time at next scr refresh
                gmat.setAutoDraw(False)
        
        # *lsat* updates
        if lsat.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lsat.frameNStart = frameN  # exact frame index
            lsat.tStart = t  # local t and not account for scr refresh
            lsat.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lsat, 'tStartRefresh')  # time at next scr refresh
            lsat.setAutoDraw(True)
        if lsat.status == STARTED:
            if bool(blank.status == FINISHED):
                # keep track of stop time/frame for later
                lsat.tStop = t  # not accounting for scr refresh
                lsat.frameNStop = frameN  # exact frame index
                win.timeOnFlip(lsat, 'tStopRefresh')  # time at next scr refresh
                lsat.setAutoDraw(False)
        
        # *game* updates
        if game.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            game.frameNStart = frameN  # exact frame index
            game.tStart = t  # local t and not account for scr refresh
            game.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(game, 'tStartRefresh')  # time at next scr refresh
            game.setAutoDraw(True)
        if game.status == STARTED:
            if bool(blank.status == FINISHED):
                # keep track of stop time/frame for later
                game.tStop = t  # not accounting for scr refresh
                game.frameNStop = frameN  # exact frame index
                win.timeOnFlip(game, 'tStopRefresh')  # time at next scr refresh
                game.setAutoDraw(False)
        if choiceResp.keys == '1':
            testChoice.setColor('green')
        if choiceResp.keys == '2':
            videogameChoice.setColor('green')
        
        if choiceResp.keys == '2' or choiceResp.keys == '1':
            choiceResp.status = FINISHED
        
        # *blank* updates
        if blank.status == NOT_STARTED and len(choiceResp.keys) > 0:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ChoiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Choice"-------
    for thisComponent in ChoiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # check responses
    if choiceResp.keys in ['', [], None]:  # No response was made
        choiceResp.keys = None
    AllTrials.addData('choiceResp.keys',choiceResp.keys)
    if choiceResp.keys != None:  # we had a response
        AllTrials.addData('choiceResp.rt', choiceResp.rt)

    videogameChoice.setColor('white')
    testChoice.setColor('white')
    
    if blank.status == FINISHED:
        choiceQ.setAutoDraw(False)
        testChoice.setAutoDraw(False)
        videogameChoice.setAutoDraw(False)
        gre.setAutoDraw(False)
        gmat.setAutoDraw(False)
        lsat.setAutoDraw(False)
        continueRoutine = False 
        
    if choiceResp.keys == '1':
        doTestPractice = 1
        doGame = 0
    if choiceResp.keys == '2':
        doTestPractice = 0
        doGame = 1
    AllTrials.addData('blank.started', blank.tStartRefresh)
    AllTrials.addData('blank.stopped', blank.tStopRefresh)
    # the Routine "Choice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    QuestionTrials = data.TrialHandler(nReps=doTestPractice, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('RowsExcel.xlsx'),
        seed=None, name='QuestionTrials')
    thisExp.addLoop(QuestionTrials)  # add the loop to the experiment
    thisQuestionTrial = QuestionTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisQuestionTrial.rgb)
    if thisQuestionTrial != None:
        for paramName in thisQuestionTrial:
            exec('{} = thisQuestionTrial[paramName]'.format(paramName))
    
    for thisQuestionTrial in QuestionTrials:
        currentLoop = QuestionTrials
        # abbreviate parameter names if possible (e.g. rgb = thisQuestionTrial.rgb)
        if thisQuestionTrial != None:
            for paramName in thisQuestionTrial:
                exec('{} = thisQuestionTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "testQuestionsChoice"-------
        # update component parameters for each repeat
        upDown.keys = []
        upDown.rt = []
        polygon.setOpacity(1)
        polygon.setSize((0.32, 0.13))
        polygon.setOri(0)
        polygon.setLineWidth(8)
        y = 0
        q = []

        if upDown.keys == '1':
            y = 0.105
        elif upDown.keys == '2':
            y = -0.05
        elif upDown.keys == '3':
            y = -0.2
            
        
        
        enter.keys = []
        enter.rt = []
        # keep track of which components have finished
        testQuestionsChoiceComponents = [testQChoice, image, image_2, image_3, upDown, polygon, enter]
        for thisComponent in testQuestionsChoiceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        testQuestionsChoiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "testQuestionsChoice"-------
        while continueRoutine:
            # get current time
            t = testQuestionsChoiceClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=testQuestionsChoiceClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *testQChoice* updates
            if testQChoice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                testQChoice.frameNStart = frameN  # exact frame index
                testQChoice.tStart = t  # local t and not account for scr refresh
                testQChoice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(testQChoice, 'tStartRefresh')  # time at next scr refresh
                testQChoice.setAutoDraw(True)
            
            # *image* updates
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                image.setAutoDraw(True)
            
            # *image_2* updates
            if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_2.frameNStart = frameN  # exact frame index
                image_2.tStart = t  # local t and not account for scr refresh
                image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                image_2.setAutoDraw(True)
            
            # *image_3* updates
            if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_3.frameNStart = frameN  # exact frame index
                image_3.tStart = t  # local t and not account for scr refresh
                image_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                image_3.setAutoDraw(True)
            
            # *upDown* updates
            waitOnFlip = False
            if upDown.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                upDown.frameNStart = frameN  # exact frame index
                upDown.tStart = t  # local t and not account for scr refresh
                upDown.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(upDown, 'tStartRefresh')  # time at next scr refresh
                upDown.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(upDown.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(upDown.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if upDown.status == STARTED and not waitOnFlip:
                theseKeys = upDown.getKeys(keyList=['1', '2', '3'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    upDown.keys = theseKeys.name  # just the last key pressed
                    upDown.rt = theseKeys.rt
            
            # *polygon* updates
            if polygon.status == NOT_STARTED and upDown.keys == '1' or upDown.keys == '2' or upDown.keys == '3' or upDown.keys == '4':
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                polygon.setAutoDraw(True)
            if polygon.status == STARTED:  # only update if drawing
                polygon.setPos([0,y], log=False)

            if upDown.keys == '1':
                y = 0.105
            elif upDown.keys == '2':
                y = -0.05
            elif upDown.keys == '3':
                y = -0.2
                
            
            # *enter* updates
            waitOnFlip = False
            if enter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                enter.frameNStart = frameN  # exact frame index
                enter.tStart = t  # local t and not account for scr refresh
                enter.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(enter, 'tStartRefresh')  # time at next scr refresh
                enter.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(enter.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(enter.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if enter.status == STARTED and not waitOnFlip:
                theseKeys = enter.getKeys(keyList=['return'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    enter.keys = theseKeys.name  # just the last key pressed
                    enter.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in testQuestionsChoiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "testQuestionsChoice"-------
        for thisComponent in testQuestionsChoiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        # check responses
        if upDown.keys in ['', [], None]:  # No response was made
            upDown.keys = None
        QuestionTrials.addData('upDown.keys',upDown.keys)
        if upDown.keys != None:  # we had a response
            QuestionTrials.addData('upDown.rt', upDown.rt)

        if upDown.keys == '1' and enter.keys != 0:
            q = 1
        elif upDown.keys == '2' and enter.keys != 0:
            q = 2
        elif upDown.keys == '3' and enter.keys != 0:
            q = 3
        # check responses
        if enter.keys in ['', [], None]:  # No response was made
            enter.keys = None
        QuestionTrials.addData('enter.keys',enter.keys)
        if enter.keys != None:  # we had a response
            QuestionTrials.addData('enter.rt', enter.rt)

        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        Questions5 = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('QuestionsText.xlsx', selection=Rows),
            seed=None, name='Questions5')
        thisExp.addLoop(Questions5)  # add the loop to the experiment
        thisQuestions5 = Questions5.trialList[0]
        if thisQuestions5 != None:
            for paramName in thisQuestions5:
                exec('{} = thisQuestions5[paramName]'.format(paramName))
        
        for thisQuestions5 in Questions5:
            currentLoop = Questions5
            # abbreviate parameter names if possible (e.g. rgb = thisQuestions5.rgb)
            if thisQuestions5 != None:
                for paramName in thisQuestions5:
                    exec('{} = thisQuestions5[paramName]'.format(paramName))
            

            TextQuestion.setText('PLACEHOLDER')
            letterKey.keys = []
            letterKey.rt = []
            enterKey.keys = []
            enterKey.rt = []
            choiceA.setText('QA')
            choiceB.setText('QB')
            choiceC.setText('QC')
            choiceD.setText('QD')
            choiceE.setText('QE')
            answerKey = []
            
            if q == 3:
                TextQuestion.setText(LSAT)
                choiceA.setText(LSATQA)
                choiceB.setText(LSATQB)
                choiceC.setText(LSATQC)
                choiceD.setText(LSATQD)
                choiceE.setText(LSATQE)
                answerKey = (LSATAs)
                
            if q == 2:
                TextQuestion.setText(GMAT)
                choiceA.setText(GMATQA)
                choiceB.setText(GMATQB)
                choiceC.setText(GMATQC)
                choiceD.setText(GMATQD)
                choiceE.setText(GMATQE)
                answerKey = (GMATAs)
                
            if q == 1:
                TextQuestion.setText(GRE)
                choiceA.setText(GREQA)
                choiceB.setText(GREQB)
                choiceC.setText(GREQC)
                choiceD.setText(GREQD)
                choiceE.setText(GREQE)
                answerKey = (GREA)
                
            # keep track of which components have finished
            testQsComponents = [TextQuestion, letterKey, enterKey, choiceA, choiceB, choiceC, choiceD, choiceE, conBlank]
            for thisComponent in testQsComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            testQsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            continueRoutine = True
            
            # -------Run Routine "testQs"-------
            while continueRoutine:
                # get current time
                t = testQsClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=testQsClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *TextQuestion* updates
                if TextQuestion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    TextQuestion.frameNStart = frameN  # exact frame index
                    TextQuestion.tStart = t  # local t and not account for scr refresh
                    TextQuestion.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(TextQuestion, 'tStartRefresh')  # time at next scr refresh
                    TextQuestion.setAutoDraw(True)
                if TextQuestion.status == STARTED:
                    if bool(conBlank.status == FINISHED or t>=180):
                        # keep track of stop time/frame for later
                        TextQuestion.tStop = t  # not accounting for scr refresh
                        TextQuestion.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(TextQuestion, 'tStopRefresh')  # time at next scr refresh
                        TextQuestion.setAutoDraw(False)
                
                # *letterKey* updates
                waitOnFlip = False
                if letterKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    letterKey.frameNStart = frameN  # exact frame index
                    letterKey.tStart = t  # local t and not account for scr refresh
                    letterKey.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(letterKey, 'tStartRefresh')  # time at next scr refresh
                    letterKey.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(letterKey.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(letterKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if letterKey.status == STARTED:
                    if bool(conBlank.status == STARTED):
                        # keep track of stop time/frame for later
                        letterKey.tStop = t  # not accounting for scr refresh
                        letterKey.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(letterKey, 'tStopRefresh')  # time at next scr refresh
                        letterKey.status = FINISHED
                if letterKey.status == STARTED and not waitOnFlip:
                    theseKeys = letterKey.getKeys(keyList=['a', 'b', 'c', 'd', 'e'], waitRelease=False)
                    if len(theseKeys):
                        theseKeys = theseKeys[0]  # at least one key was pressed
                        
                        # check for quit:
                        if "escape" == theseKeys:
                            endExpNow = True
                        letterKey.keys = theseKeys.name  # just the last key pressed
                        letterKey.rt = theseKeys.rt
                
                # *enterKey* updates
                waitOnFlip = False
                if enterKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    enterKey.frameNStart = frameN  # exact frame index
                    enterKey.tStart = t  # local t and not account for scr refresh
                    enterKey.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(enterKey, 'tStartRefresh')  # time at next scr refresh
                    enterKey.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(enterKey.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(enterKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if enterKey.status == STARTED:
                    if bool(conBlank.status == STARTED):
                        # keep track of stop time/frame for later
                        enterKey.tStop = t  # not accounting for scr refresh
                        enterKey.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(enterKey, 'tStopRefresh')  # time at next scr refresh
                        enterKey.status = FINISHED
                if enterKey.status == STARTED and not waitOnFlip:
                    theseKeys = enterKey.getKeys(keyList=['return'], waitRelease=False)
                    if len(theseKeys):
                        theseKeys = theseKeys[0]  # at least one key was pressed
                        
                        # check for quit:
                        if "escape" == theseKeys:
                            endExpNow = True
                        enterKey.keys = theseKeys.name  # just the last key pressed
                        enterKey.rt = theseKeys.rt
                
                # *choiceA* updates
                if choiceA.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    choiceA.frameNStart = frameN  # exact frame index
                    choiceA.tStart = t  # local t and not account for scr refresh
                    choiceA.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(choiceA, 'tStartRefresh')  # time at next scr refresh
                    choiceA.setAutoDraw(True)
                if choiceA.status == STARTED:
                    if bool(conBlank.status == FINISHED or t>=180):
                        # keep track of stop time/frame for later
                        choiceA.tStop = t  # not accounting for scr refresh
                        choiceA.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(choiceA, 'tStopRefresh')  # time at next scr refresh
                        choiceA.setAutoDraw(False)
                
                # *choiceB* updates
                if choiceB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    choiceB.frameNStart = frameN  # exact frame index
                    choiceB.tStart = t  # local t and not account for scr refresh
                    choiceB.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(choiceB, 'tStartRefresh')  # time at next scr refresh
                    choiceB.setAutoDraw(True)
                if choiceB.status == STARTED:
                    if bool(conBlank.status == FINISHED or t>=180):
                        # keep track of stop time/frame for later
                        choiceB.tStop = t  # not accounting for scr refresh
                        choiceB.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(choiceB, 'tStopRefresh')  # time at next scr refresh
                        choiceB.setAutoDraw(False)
                
                # *choiceC* updates
                if choiceC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    choiceC.frameNStart = frameN  # exact frame index
                    choiceC.tStart = t  # local t and not account for scr refresh
                    choiceC.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(choiceC, 'tStartRefresh')  # time at next scr refresh
                    choiceC.setAutoDraw(True)
                if choiceC.status == STARTED:
                    if bool(conBlank.status == FINISHED or t>=180):
                        # keep track of stop time/frame for later
                        choiceC.tStop = t  # not accounting for scr refresh
                        choiceC.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(choiceC, 'tStopRefresh')  # time at next scr refresh
                        choiceC.setAutoDraw(False)
                
                # *choiceD* updates
                if choiceD.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    choiceD.frameNStart = frameN  # exact frame index
                    choiceD.tStart = t  # local t and not account for scr refresh
                    choiceD.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(choiceD, 'tStartRefresh')  # time at next scr refresh
                    choiceD.setAutoDraw(True)
                if choiceD.status == STARTED:
                    if bool(conBlank.status == FINISHED or t>=180):
                        # keep track of stop time/frame for later
                        choiceD.tStop = t  # not accounting for scr refresh
                        choiceD.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(choiceD, 'tStopRefresh')  # time at next scr refresh
                        choiceD.setAutoDraw(False)
                
                # *choiceE* updates
                if choiceE.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    choiceE.frameNStart = frameN  # exact frame index
                    choiceE.tStart = t  # local t and not account for scr refresh
                    choiceE.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(choiceE, 'tStartRefresh')  # time at next scr refresh
                    choiceE.setAutoDraw(True)
                if choiceE.status == STARTED:
                    if bool(conBlank.status == FINISHED or t>=180):
                        # keep track of stop time/frame for later
                        choiceE.tStop = t  # not accounting for scr refresh
                        choiceE.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(choiceE, 'tStopRefresh')  # time at next scr refresh
                        choiceE.setAutoDraw(False)
                if (letterKey.keys == 'a' and enterKey.keys == 'return') and answerKey == 'a':
                    choiceA.setColor('green')
                if (letterKey.keys == 'b' and enterKey.keys == 'return') and answerKey == 'b':
                    choiceB.setColor('green')
                if (letterKey.keys == 'c' and enterKey.keys == 'return') and answerKey == 'c':
                    choiceC.setColor('green')
                if (letterKey.keys == 'd' and enterKey.keys == 'return') and answerKey == 'd':
                    choiceD.setColor('green')
                if (letterKey.keys == 'e' and enterKey.keys == 'return') and answerKey == 'e':
                    choiceE.setColor('green')
                    
                if (letterKey.keys == 'a' and enterKey.keys == 'return') and answerKey != 'a':
                    choiceA.setColor('red')
                if (letterKey.keys == 'b' and enterKey.keys == 'return') and answerKey != 'b':
                    choiceB.setColor('red')
                if (letterKey.keys == 'c' and enterKey.keys == 'return') and answerKey != 'c':
                    choiceC.setColor('red')
                if (letterKey.keys == 'd' and enterKey.keys == 'return') and answerKey != 'd':
                    choiceD.setColor('red')
                if (letterKey.keys == 'e' and enterKey.keys == 'return') and answerKey != 'e':
                    choiceE.setColor('red')
                
                if (enterKey.keys == 'return' and letterKey.keys != 'a') and answerKey == 'a':
                    choiceA.setColor('green')
                if (enterKey.keys == 'return' and letterKey.keys != 'b') and answerKey == 'b':
                    choiceB.setColor('green')
                if (enterKey.keys == 'return' and letterKey.keys != 'c') and answerKey == 'c':
                    choiceC.setColor('green')
                if (enterKey.keys == 'return' and letterKey.keys != 'd') and answerKey == 'd':
                    choiceD.setColor('green')
                if (enterKey.keys == 'return' and letterKey.keys != 'e') and answerKey == 'e':
                    choiceE.setColor('green')
                
                
                # *conBlank* updates
                if conBlank.status == NOT_STARTED and enterKey.keys == 'return':
                    # keep track of start time/frame for later
                    conBlank.frameNStart = frameN  # exact frame index
                    conBlank.tStart = t  # local t and not account for scr refresh
                    conBlank.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(conBlank, 'tStartRefresh')  # time at next scr refresh
                    conBlank.setAutoDraw(True)
                if conBlank.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > conBlank.tStartRefresh + 2.5-frameTolerance:
                        # keep track of stop time/frame for later
                        conBlank.tStop = t  # not accounting for scr refresh
                        conBlank.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(conBlank, 'tStopRefresh')  # time at next scr refresh
                        conBlank.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in testQsComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "testQs"-------
            for thisComponent in testQsComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            Questions5.addData('TextQuestion.started', TextQuestion.tStartRefresh)
            Questions5.addData('TextQuestion.stopped', TextQuestion.tStopRefresh)
            # check responses
            if letterKey.keys in ['', [], None]:  # No response was made
                letterKey.keys = None
            Questions5.addData('letterKey.keys',letterKey.keys)
            if letterKey.keys != None:  # we had a response
                Questions5.addData('letterKey.rt', letterKey.rt)
            Questions5.addData('letterKey.started', letterKey.tStartRefresh)
            Questions5.addData('letterKey.stopped', letterKey.tStopRefresh)
            # check responses
            if enterKey.keys in ['', [], None]:  # No response was made
                enterKey.keys = None
            Questions5.addData('enterKey.keys',enterKey.keys)
            if enterKey.keys != None:  # we had a response
                Questions5.addData('enterKey.rt', enterKey.rt)
            Questions5.addData('enterKey.started', enterKey.tStartRefresh)
            Questions5.addData('enterKey.stopped', enterKey.tStopRefresh)
            Questions5.addData('choiceA.started', choiceA.tStartRefresh)
            Questions5.addData('choiceA.stopped', choiceA.tStopRefresh)
            Questions5.addData('choiceB.started', choiceB.tStartRefresh)
            Questions5.addData('choiceB.stopped', choiceB.tStopRefresh)
            Questions5.addData('choiceC.started', choiceC.tStartRefresh)
            Questions5.addData('choiceC.stopped', choiceC.tStopRefresh)
            Questions5.addData('choiceD.started', choiceD.tStartRefresh)
            Questions5.addData('choiceD.stopped', choiceD.tStopRefresh)
            Questions5.addData('choiceE.started', choiceE.tStartRefresh)
            Questions5.addData('choiceE.stopped', choiceE.tStopRefresh)
            
            if conBlank.status == FINISHED:
                choiceA.setAutoDraw(False)
                choiceB.setAutoDraw(False)
                choiceC.setAutoDraw(False)
                choiceD.setAutoDraw(False)
                choiceE.setAutoDraw(False)
                continueRoutine = False
            
            
            
            choiceA.setColor('white')
            choiceB.setColor('white')
            choiceC.setColor('white')
            choiceD.setColor('white')
            choiceE.setColor('white')
            Questions5.addData('conBlank.started', conBlank.tStartRefresh)
            Questions5.addData('conBlank.stopped', conBlank.tStopRefresh)
            # the Routine "testQs" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'Questions5'
        
        thisExp.nextEntry()
        
    # completed doTestPractice repeats of 'QuestionTrials'
    
    
    # set up handler to look after randomisation of conditions etc
    GameTrials = data.TrialHandler(nReps=doGame, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='GameTrials')
    thisExp.addLoop(GameTrials)  # add the loop to the experiment
    thisGameTrial = GameTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisGameTrial.rgb)
    if thisGameTrial != None:
        for paramName in thisGameTrial:
            exec('{} = thisGameTrial[paramName]'.format(paramName))
    
    for thisGameTrial in GameTrials:
        currentLoop = GameTrials
        # abbreviate parameter names if possible (e.g. rgb = thisGameTrial.rgb)
        if thisGameTrial != None:
            for paramName in thisGameTrial:
                exec('{} = thisGameTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Game"-------
        # update component parameters for each repeat
        spaceKey.keys = []
        spaceKey.rt = []
        # keep track of which components have finished
        GameComponents = [gameInstructions, spaceKey]
        for thisComponent in GameComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        GameClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "Game"-------
        while continueRoutine:
            # get current time
            t = GameClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=GameClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *gameInstructions* updates
            if gameInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                gameInstructions.frameNStart = frameN  # exact frame index
                gameInstructions.tStart = t  # local t and not account for scr refresh
                gameInstructions.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(gameInstructions, 'tStartRefresh')  # time at next scr refresh
                gameInstructions.setAutoDraw(True)
            
            # *spaceKey* updates
            waitOnFlip = False
            if spaceKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                spaceKey.frameNStart = frameN  # exact frame index
                spaceKey.tStart = t  # local t and not account for scr refresh
                spaceKey.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(spaceKey, 'tStartRefresh')  # time at next scr refresh
                spaceKey.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(spaceKey.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(spaceKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if spaceKey.status == STARTED and not waitOnFlip:
                theseKeys = spaceKey.getKeys(keyList=['space'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    spaceKey.keys = theseKeys.name  # just the last key pressed
                    spaceKey.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in GameComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Game"-------
        for thisComponent in GameComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        # check responses
        if spaceKey.keys in ['', [], None]:  # No response was made
            spaceKey.keys = None
        GameTrials.addData('spaceKey.keys',spaceKey.keys)
        if spaceKey.keys != None:  # we had a response
            GameTrials.addData('spaceKey.rt', spaceKey.rt)

        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials = data.TrialHandler(nReps=5, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials')
        thisExp.addLoop(trials)  # add the loop to the experiment
        thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        for thisTrial in trials:
            currentLoop = trials
            # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
            if thisTrial != None:
                for paramName in thisTrial:
                    exec('{} = thisTrial[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "pacman"-------
            # update component parameters for each repeat
            setup(420, 420, 370, 0)
            #hideturtle()
            #tracer(False)
            #writer.goto(160, 160)
            #writer.color('white')
            #writer.write(state['score'])
            #listen()
            #onkey(lambda: change(5, 0), 'Right')
            #onkey(lambda: change(-5, 0), 'Left')
            #onkey(lambda: change(0, 5), 'Up')
            #onkey(lambda: change(0, -5), 'Down')
            #world()
            #move()
            #
            # keep track of which components have finished
            pacmanComponents = []
            for thisComponent in pacmanComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            pacmanClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            continueRoutine = True
            
            # -------Run Routine "pacman"-------
            while continueRoutine:
                # get current time
                t = pacmanClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=pacmanClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                setup(420, 420, 370, 0)
                hideturtle()
                tracer(False)
                writer.goto(160, 160)
                writer.color('white')
                writer.write(state['score'])
                listen()
                onkey(lambda: change(5, 0), 'Right')
                onkey(lambda: change(-5, 0), 'Left')
                onkey(lambda: change(0, 5), 'Up')
                onkey(lambda: change(0, -5), 'Down')
                world()
                move()
                done()
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in pacmanComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "pacman"-------
            for thisComponent in pacmanComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            done()
            # the Routine "pacman" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 5 repeats of 'trials'
        
        thisExp.nextEntry()
        
    # completed doGame repeats of 'GameTrials'
    
    thisExp.nextEntry()
    

win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
