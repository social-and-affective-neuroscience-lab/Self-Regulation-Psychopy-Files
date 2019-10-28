#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on October 21, 2019, at 15:29
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
expName = 'SlotMachTest'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\tul00635\\Documents\\GitHub\\Self-Regulation-Psychopy-Files\\Slot MachineTask\\SlotMachTest_lastrun.py',
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

# Initialize components for Routine "Instr"
InstrClock = core.Clock()
Instructions = visual.TextStim(win=win, name='Instructions',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=1.6, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
space = keyboard.Keyboard()
import numpy
from numpy import random

earnings = 0
earningsStr = "$" + str(earnings)
subID = int(expInfo['participant'])

FiftyGamble = [1,0]
SixtyGamble = [1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0]
ThirtyGamble = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0]

earning=0
chosenMoney = 0


#probability =[]
def gamProbability(gamProb):
    probs = int(gamProb)
    if probs == 65:
        probability = SixtyGamble
        print('65% gamble')
    if probs == 35:
        probability = ThirtyGamble
        print('35% gamble')
    if probs == 50:
        probability = FiftyGamble
        print('50% gamble')
def gambleFunc(gamProb):
    probs = int(gamProb)
    if probs == 65:
        probability = SixtyGamble
        #print('65% gamble')
    if probs == 35:
        probability = ThirtyGamble
        print('35% gamble')
    if probs == 50:
        probability = FiftyGamble
        print('50% gamble')
    result = random.choice(probability)
    print('gamble result:')
    print(result)

def loseFunc(chosenMoney, earning):
    earning -= chosenMoney
    print('Lost Money earnings:')
    print(earning)
def winFunc(chosenMoney, earning):
    earning += chosenMoney
    print('Won money earnings:')
    print(earning)

def earningsFunct(gamProb, chosenMoney, WinLossType, earning):
   if subID%2==0:   #gambles are on left side of screen
       if choice.keys == '1' and WinLossType== 1 : 
           print('gambled during win condition')
           #gamProbability(gamProb)
           probs = int(gamProb)
           if probs == 65:
               probability = SixtyGamble
               print('65% gamble')
           if probs == 35:
               probability = ThirtyGamble
               print('35% gamble')
           if probs == 50:
               probability = FiftyGamble
               print('50% gamble')
           result = random.choice(probability)
           print('gamble result:')
           print(result)
           if result == 1:   #win
               earning += chosenMoney
               print('Won money earnings:')
               print(earning)
       #    if result == 0: #lose
        #       earnings += 0
   
       if choice.keys == '1' and WinLossType==0:  
           print('gambled during lose condition')
           #gamProbability(gamProb)
           probs = int(gamProb)
           if probs == 65:
               probability = SixtyGamble
        #print('65% gamble')
           if probs == 35:
               probability = ThirtyGamble
               print('35% gamble')
           if probs == 50:
               probability = FiftyGamble
               print('50% gamble')
           result = random.choice(probability)
           print('gamble result:')
           print(result)           
           if result == 1: #lose
               earning -= chosenMoney
               print('Lost Money earnings:')
               print(earning)
     #      if result == 0: #win
     #          earnings += 0
                
       if choice.keys == '2'and WinLossType ==1:
           print('did not gamble for win')
           earning += chosenMoney
           print('Won money earnings:')
           print(earning)       
       if choice.keys == '2' and WinLossType == 0: 
           print('did not gamble for loss')
           earning -= chosenMoney
           print('Lost Money earnings:')
           print(earning)


   if subID%2==1:  #gambles are on right side of screen
       if choice.keys == '2' and WinLossType == 1: 
           print('gambled during win condition')
           #gamProbability(gamProb)
           probs = int(gamProb)
           if probs == 65:
               probability = SixtyGamble
               print('65% gamble')
           if probs == 35:
               probability = ThirtyGamble
               print('35% gamble')
           if probs == 50:
               probability = FiftyGamble
               print('50% gamble')
           result = random.choice(probability)
           print('gamble result:')
           print(result)           
           if result == 1: #win
               winFunc(chosenMoney, earning)
    #       if result == 0: #lost
    #           earnings += 0
        
        
       if choice.keys == '2' and WinLossType == 0: 
           print('gambled during lose condition')
           #gamProbability(gamProb)
           probs = int(gamProb)
           if probs == 65:
               probability = SixtyGamble
               print('65% gamble')
           if probs == 35:
               probability = ThirtyGamble
               print('35% gamble')
           if probs == 50:
               probability = FiftyGamble
               print('50% gamble')
           result = random.choice(probability)
           print('gamble result:')
           print(result)           
           if result == 1: #lose
               earning -= chosenMoney
               print('Lost Money earnings:')
               print(earning)
     #      if result == 0: #win
     #          earnings += 0
                
       if choice.keys == '1' and WinLossType == 1:
           print('did not gamble for win')
           earning += chosenMoney
           print('Won money earnings:')
           print(earning)
       if choice.keys == '1' and WinLossType == 0: 
           print('did not gamble for lose condition')
           earning -= chosenMoney
           print('Lost Money earnings:')
           print(earning)

# Initialize components for Routine "Inst2"
Inst2Clock = core.Clock()
instruct2 = visual.TextStim(win=win, name='instruct2',
    text='You will be given regulation intsructions prior to a block of trials. Please employ the strategy while making your decision. \n\nYou will have three seconds to make your choice upon seeing the options. \n\nTo choose the option on the left, press "1". To choose the option on the right, press "2".\n\nYou will first be playing some practice rounds. To begin the practice, press enter!',
    font='Arial',
    pos=(0, 0), height=0.065, wrapWidth=1.6, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
enter = keyboard.Keyboard()

# Initialize components for Routine "isi"
isiClock = core.Clock()
isi2 = visual.TextStim(win=win, name='isi2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "PracticeCue"
PracticeCueClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='REGULATE',
    font='Arial',
    pos=(0, 0), height=0.13, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "isi"
isiClock = core.Clock()
isi2 = visual.TextStim(win=win, name='isi2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Practice"
PracticeClock = core.Clock()
Line = visual.Line(
    win=win, name='Line',
    start=(-[1.0, 1.0][0]/2.0, 0), end=(+[1.0, 1.0][0]/2.0, 0),
    ori=90, pos=(0, 0),
    lineWidth=1.0, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
choice = keyboard.Keyboard()
GambleAmt = visual.TextStim(win=win, name='GambleAmt',
    text=None,
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
SureAmt = visual.TextStim(win=win, name='SureAmt',
    text=None,
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
GambleProb = visual.TextStim(win=win, name='GambleProb',
    text=None,
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
SureProb = visual.TextStim(win=win, name='SureProb',
    text=None,
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
moneyBank = visual.Rect(
    win=win, name='moneyBank',
    width=(0.46, 0.24)[0], height=(0.46, 0.24)[1],
    ori=0, pos=(0.68, -0.42),
    lineWidth=8, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
earningsText = visual.TextStim(win=win, name='earningsText',
    text='default text',
    font='Arial',
    pos=(0.67, -0.42), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "code_5"
code_5Clock = core.Clock()

# Initialize components for Routine "BeginInst"
BeginInstClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='You will now begin the full task.\n\nPress SPACE to start!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "isi"
isiClock = core.Clock()
isi2 = visual.TextStim(win=win, name='isi2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Cue"
CueClock = core.Clock()
cue = visual.TextStim(win=win, name='cue',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "isi"
isiClock = core.Clock()
isi2 = visual.TextStim(win=win, name='isi2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Practice"
PracticeClock = core.Clock()
Line = visual.Line(
    win=win, name='Line',
    start=(-[1.0, 1.0][0]/2.0, 0), end=(+[1.0, 1.0][0]/2.0, 0),
    ori=90, pos=(0, 0),
    lineWidth=1.0, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
choice = keyboard.Keyboard()
GambleAmt = visual.TextStim(win=win, name='GambleAmt',
    text=None,
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
SureAmt = visual.TextStim(win=win, name='SureAmt',
    text=None,
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
GambleProb = visual.TextStim(win=win, name='GambleProb',
    text=None,
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
SureProb = visual.TextStim(win=win, name='SureProb',
    text=None,
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
moneyBank = visual.Rect(
    win=win, name='moneyBank',
    width=(0.46, 0.24)[0], height=(0.46, 0.24)[1],
    ori=0, pos=(0.68, -0.42),
    lineWidth=8, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
earningsText = visual.TextStim(win=win, name='earningsText',
    text='default text',
    font='Arial',
    pos=(0.67, -0.42), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "ThankYou"
ThankYouClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='"Thank you for playing!"/n/n\n\n"Your total earnings are $" earnings',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instr"-------
# update component parameters for each repeat
Instructions.setColor('white', colorSpace='rgb')
Instructions.setPos((0, 0))
Instructions.setText('In this part of the study, you will be making a series of monetary decisions.\n\nYou will have the choice between taking a gamble or choosing a sure option. \n\nFor each gamble, you will have a chance of either winning money, losing money, or gaining nothing, while the sure option guarantees a win or loss. \n\nPress space to continue. ')
Instructions.setFont('Arial')
Instructions.setHeight(0.065)
space.keys = []
space.rt = []
# keep track of which components have finished
InstrComponents = [Instructions, space]
for thisComponent in InstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Instr"-------
while continueRoutine:
    # get current time
    t = InstrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions* updates
    if Instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions.frameNStart = frameN  # exact frame index
        Instructions.tStart = t  # local t and not account for scr refresh
        Instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions, 'tStartRefresh')  # time at next scr refresh
        Instructions.setAutoDraw(True)
    
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
    for thisComponent in InstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr"-------
for thisComponent in InstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instructions.started', Instructions.tStartRefresh)
thisExp.addData('Instructions.stopped', Instructions.tStopRefresh)
# check responses
if space.keys in ['', [], None]:  # No response was made
    space.keys = None
thisExp.addData('space.keys',space.keys)
if space.keys != None:  # we had a response
    thisExp.addData('space.rt', space.rt)
thisExp.addData('space.started', space.tStartRefresh)
thisExp.addData('space.stopped', space.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Inst2"-------
# update component parameters for each repeat
enter.keys = []
enter.rt = []
# keep track of which components have finished
Inst2Components = [instruct2, enter]
for thisComponent in Inst2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Inst2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Inst2"-------
while continueRoutine:
    # get current time
    t = Inst2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Inst2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruct2* updates
    if instruct2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct2.frameNStart = frameN  # exact frame index
        instruct2.tStart = t  # local t and not account for scr refresh
        instruct2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct2, 'tStartRefresh')  # time at next scr refresh
        instruct2.setAutoDraw(True)
    
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
    for thisComponent in Inst2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Inst2"-------
for thisComponent in Inst2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruct2.started', instruct2.tStartRefresh)
thisExp.addData('instruct2.stopped', instruct2.tStopRefresh)
# check responses
if enter.keys in ['', [], None]:  # No response was made
    enter.keys = None
thisExp.addData('enter.keys',enter.keys)
if enter.keys != None:  # we had a response
    thisExp.addData('enter.rt', enter.rt)
thisExp.addData('enter.started', enter.tStartRefresh)
thisExp.addData('enter.stopped', enter.tStopRefresh)
thisExp.nextEntry()
# the Routine "Inst2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "isi"-------
routineTimer.add(2.000000)
# update component parameters for each repeat
isi2.setText('+')
# keep track of which components have finished
isiComponents = [isi2]
for thisComponent in isiComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
isiClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "isi"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = isiClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=isiClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *isi2* updates
    if isi2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        isi2.frameNStart = frameN  # exact frame index
        isi2.tStart = t  # local t and not account for scr refresh
        isi2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(isi2, 'tStartRefresh')  # time at next scr refresh
        isi2.setAutoDraw(True)
    if isi2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > isi2.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            isi2.tStop = t  # not accounting for scr refresh
            isi2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(isi2, 'tStopRefresh')  # time at next scr refresh
            isi2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in isiComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "isi"-------
for thisComponent in isiComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('isi2.started', isi2.tStartRefresh)
thisExp.addData('isi2.stopped', isi2.tStopRefresh)

# ------Prepare to start Routine "PracticeCue"-------
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
PracticeCueComponents = [text]
for thisComponent in PracticeCueComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PracticeCueClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "PracticeCue"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = PracticeCueClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PracticeCueClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PracticeCueComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PracticeCue"-------
for thisComponent in PracticeCueComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

# set up handler to look after randomisation of conditions etc
reset = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='reset')
thisExp.addLoop(reset)  # add the loop to the experiment
thisReset = reset.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisReset.rgb)
if thisReset != None:
    for paramName in thisReset:
        exec('{} = thisReset[paramName]'.format(paramName))

for thisReset in reset:
    currentLoop = reset
    # abbreviate parameter names if possible (e.g. rgb = thisReset.rgb)
    if thisReset != None:
        for paramName in thisReset:
            exec('{} = thisReset[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    PracticeLoop = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('PracticeSlotMach.csv', selection='0:3'),
        seed=None, name='PracticeLoop')
    thisExp.addLoop(PracticeLoop)  # add the loop to the experiment
    thisPracticeLoop = PracticeLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop.rgb)
    if thisPracticeLoop != None:
        for paramName in thisPracticeLoop:
            exec('{} = thisPracticeLoop[paramName]'.format(paramName))
    
    for thisPracticeLoop in PracticeLoop:
        currentLoop = PracticeLoop
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop.rgb)
        if thisPracticeLoop != None:
            for paramName in thisPracticeLoop:
                exec('{} = thisPracticeLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "isi"-------
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        isi2.setText('+')
        # keep track of which components have finished
        isiComponents = [isi2]
        for thisComponent in isiComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        isiClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "isi"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = isiClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=isiClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *isi2* updates
            if isi2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                isi2.frameNStart = frameN  # exact frame index
                isi2.tStart = t  # local t and not account for scr refresh
                isi2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(isi2, 'tStartRefresh')  # time at next scr refresh
                isi2.setAutoDraw(True)
            if isi2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > isi2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    isi2.tStop = t  # not accounting for scr refresh
                    isi2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(isi2, 'tStopRefresh')  # time at next scr refresh
                    isi2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in isiComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "isi"-------
        for thisComponent in isiComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        PracticeLoop.addData('isi2.started', isi2.tStartRefresh)
        PracticeLoop.addData('isi2.stopped', isi2.tStopRefresh)
        
        # ------Prepare to start Routine "Practice"-------
        # update component parameters for each repeat
        Line.setSize((3, 0.5))
        Line.setFillColor([-1.000,-1.000,-1.000])
        Line.setLineColor([-1.000,-1.000,-1.000])
        Line.setLineWidth(7)
        choice.keys = []
        choice.rt = []
        GambleAmt.setColor('white', colorSpace='rgb')
        GambleAmt.setPos((-0.41, -0.1))
        GambleAmt.setText('')
        GambleAmt.setFont('Arial')
        GambleAmt.setHeight(0.11)
        SureAmt.setColor('white', colorSpace='rgb')
        SureAmt.setPos((0.41, -0.1))
        SureAmt.setText('')
        SureAmt.setFont('Arial')
        SureAmt.setHeight(0.11)
        GambleProb.setColor('white', colorSpace='rgb')
        GambleProb.setPos((-0.41, 0.3))
        GambleProb.setText('')
        GambleProb.setFont('Arial')
        GambleProb.setHeight(0.13)
        SureProb.setColor('white', colorSpace='rgb')
        SureProb.setPos((0.41, 0.3))
        SureProb.setText('')
        SureProb.setFont('Arial')
        SureProb.setHeight(0.13)
        
        leftVarText=[]
        leftVarMoney = []
        rightVarText = []
        rightVarMoney = []
        result = []
        
        if subID%2 == 1 :
            leftVarText = (gambleWinLoss)
            leftVarMoney = (gamble)
            rightVarText = (sureWinLoss)
            rightVarMoney = (sure)
        if subID%2 == 0:
            rightVarText= (gambleWinLoss)
            rightVarMoney= (gamble)
            leftVarText= (sureWinLoss)
            leftVarMoney= (sure)
        
        GambleAmt.setText(leftVarMoney)
        SureAmt.setText(rightVarMoney)
        GambleProb.setText(leftVarText)
        SureProb.setText(rightVarText)
        
        leftMoney = float(leftVarMoney[1:])
        
        rightMoney = float(rightVarMoney[1:])
        
        WinLossType = int(WinLossCode)
        
        
        blank.setText('')
        earningsText.setText(earningsStr)
        # keep track of which components have finished
        PracticeComponents = [Line, choice, GambleAmt, SureAmt, GambleProb, SureProb, blank, moneyBank, earningsText]
        for thisComponent in PracticeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "Practice"-------
        while continueRoutine:
            # get current time
            t = PracticeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PracticeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Line* updates
            if Line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Line.frameNStart = frameN  # exact frame index
                Line.tStart = t  # local t and not account for scr refresh
                Line.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Line, 'tStartRefresh')  # time at next scr refresh
                Line.setAutoDraw(True)
            if Line.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Line.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    Line.tStop = t  # not accounting for scr refresh
                    Line.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Line, 'tStopRefresh')  # time at next scr refresh
                    Line.setAutoDraw(False)
            
            # *choice* updates
            waitOnFlip = False
            if choice.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                choice.frameNStart = frameN  # exact frame index
                choice.tStart = t  # local t and not account for scr refresh
                choice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(choice, 'tStartRefresh')  # time at next scr refresh
                choice.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(choice.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(choice.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if choice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > choice.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    choice.tStop = t  # not accounting for scr refresh
                    choice.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(choice, 'tStopRefresh')  # time at next scr refresh
                    choice.status = FINISHED
            if choice.status == STARTED and not waitOnFlip:
                theseKeys = choice.getKeys(keyList=['1', '2'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    choice.keys = theseKeys.name  # just the last key pressed
                    choice.rt = theseKeys.rt
            
            # *GambleAmt* updates
            if GambleAmt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                GambleAmt.frameNStart = frameN  # exact frame index
                GambleAmt.tStart = t  # local t and not account for scr refresh
                GambleAmt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(GambleAmt, 'tStartRefresh')  # time at next scr refresh
                GambleAmt.setAutoDraw(True)
            if GambleAmt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > GambleAmt.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    GambleAmt.tStop = t  # not accounting for scr refresh
                    GambleAmt.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(GambleAmt, 'tStopRefresh')  # time at next scr refresh
                    GambleAmt.setAutoDraw(False)
            
            # *SureAmt* updates
            if SureAmt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                SureAmt.frameNStart = frameN  # exact frame index
                SureAmt.tStart = t  # local t and not account for scr refresh
                SureAmt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SureAmt, 'tStartRefresh')  # time at next scr refresh
                SureAmt.setAutoDraw(True)
            if SureAmt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > SureAmt.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    SureAmt.tStop = t  # not accounting for scr refresh
                    SureAmt.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(SureAmt, 'tStopRefresh')  # time at next scr refresh
                    SureAmt.setAutoDraw(False)
            
            # *GambleProb* updates
            if GambleProb.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                GambleProb.frameNStart = frameN  # exact frame index
                GambleProb.tStart = t  # local t and not account for scr refresh
                GambleProb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(GambleProb, 'tStartRefresh')  # time at next scr refresh
                GambleProb.setAutoDraw(True)
            if GambleProb.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > GambleProb.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    GambleProb.tStop = t  # not accounting for scr refresh
                    GambleProb.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(GambleProb, 'tStopRefresh')  # time at next scr refresh
                    GambleProb.setAutoDraw(False)
            
            # *SureProb* updates
            if SureProb.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                SureProb.frameNStart = frameN  # exact frame index
                SureProb.tStart = t  # local t and not account for scr refresh
                SureProb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SureProb, 'tStartRefresh')  # time at next scr refresh
                SureProb.setAutoDraw(True)
            if SureProb.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > SureProb.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    SureProb.tStop = t  # not accounting for scr refresh
                    SureProb.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(SureProb, 'tStopRefresh')  # time at next scr refresh
                    SureProb.setAutoDraw(False)
            
            if choice.keys == '1':
                GambleAmt.setColor('green')
                chosenMoney = leftMoney
            if choice.keys == '2':
                SureAmt.setColor('green')
                chosenMoney = rightMoney
                
            if (choice.keys == '1' or choice.keys == '2') and blank.status == NOT_STARTED:
                blank.tStart = t
                blank.frameNStart = frameN
                blank.setAutoDraw(True)
            #gamProbability(gambleProb)
            #gambleFunc(gambleProb)
            #earningsFunct(gambleProb, chosenMoney, WinLossCode, earnings)
            #print(earnings)
            
            
            
            #earningsText.setText(earningsStr)
            
            
            # *blank* updates
            if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
            
            # *moneyBank* updates
            if moneyBank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                moneyBank.frameNStart = frameN  # exact frame index
                moneyBank.tStart = t  # local t and not account for scr refresh
                moneyBank.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(moneyBank, 'tStartRefresh')  # time at next scr refresh
                moneyBank.setAutoDraw(True)
            if moneyBank.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > moneyBank.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    moneyBank.tStop = t  # not accounting for scr refresh
                    moneyBank.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(moneyBank, 'tStopRefresh')  # time at next scr refresh
                    moneyBank.setAutoDraw(False)
            
            # *earningsText* updates
            if earningsText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                earningsText.frameNStart = frameN  # exact frame index
                earningsText.tStart = t  # local t and not account for scr refresh
                earningsText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(earningsText, 'tStartRefresh')  # time at next scr refresh
                earningsText.setAutoDraw(True)
            if earningsText.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > earningsText.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    earningsText.tStop = t  # not accounting for scr refresh
                    earningsText.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(earningsText, 'tStopRefresh')  # time at next scr refresh
                    earningsText.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Practice"-------
        for thisComponent in PracticeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        PracticeLoop.addData('Line.started', Line.tStartRefresh)
        PracticeLoop.addData('Line.stopped', Line.tStopRefresh)
        # check responses
        if choice.keys in ['', [], None]:  # No response was made
            choice.keys = None
        PracticeLoop.addData('choice.keys',choice.keys)
        if choice.keys != None:  # we had a response
            PracticeLoop.addData('choice.rt', choice.rt)
        PracticeLoop.addData('choice.started', choice.tStartRefresh)
        PracticeLoop.addData('choice.stopped', choice.tStopRefresh)
        PracticeLoop.addData('GambleAmt.started', GambleAmt.tStartRefresh)
        PracticeLoop.addData('GambleAmt.stopped', GambleAmt.tStopRefresh)
        PracticeLoop.addData('SureAmt.started', SureAmt.tStartRefresh)
        PracticeLoop.addData('SureAmt.stopped', SureAmt.tStopRefresh)
        PracticeLoop.addData('GambleProb.started', GambleProb.tStartRefresh)
        PracticeLoop.addData('GambleProb.stopped', GambleProb.tStopRefresh)
        PracticeLoop.addData('SureProb.started', SureProb.tStartRefresh)
        PracticeLoop.addData('SureProb.stopped', SureProb.tStopRefresh)
        
        if choice.keys == '1':
            chosenMoney = leftMoney
        if choice.keys == '2':
            chosenMoney = rightMoney
        if choice.keys != None:
            if subID%2==1:   #gambles are on left side of screen
               if choice.keys == '1' and WinLossCode== 1 :  
                   print('gambled during win condition')
                   probs = int(gambleProb)
                   if probs == 65:
                       probability = SixtyGamble
                       print('65% gamble')
                   if probs == 35:
                       probability = ThirtyGamble
                       print('35% gamble')
                   if probs == 50:
                       probability = FiftyGamble
                       print('50% gamble')
                   result = random.choice(probability)
                   print('gamble result:')
                   print(result)
                   if result == 1:   #win
                       earnings = earnings + chosenMoney
                       print('Won money earnings:')
                       print(earnings)
                   #    if result == 0: #lose
                    #       earnings += 0
               
               if choice.keys == '1' and WinLossCode==0:  
                   print('gambled during lose condition')
                  #gamProbability(gamProb)
                   probs = int(gambleProb)
                   if probs == 65:
                       probability = SixtyGamble
                       print('65% gamble')
                   if probs == 35:
                       probability = ThirtyGamble
                       print('35% gamble')
                   if probs == 50:
                       probability = FiftyGamble
                       print('50% gamble')
                   result = random.choice(probability)
                   print('gamble result:')
                   print(result)           
                   if result == 1: #lose
                      earnings = earnings - chosenMoney
                      print('Lost Money earnings:')
                      print(earnings)
                 #      if result == 0: #win
                 #          earnings += 0
                            
               if choice.keys == '2'and WinLossCode ==1:  
                   print('did not gamble for win condition')
                   earnings = earnings + chosenMoney
                   print('Won sure money earnings:')
                   print(earnings)       
               if choice.keys == '2' and WinLossCode == 0: #did not gamble for lose condition
                   earnings = earnings - chosenMoney
                   print('Lost sure Money earnings:')
                   print(earnings)
        
        
            if subID%2==0:  #gambles are on right side of screen
               if choice.keys == '2' and WinLossCode == 1: 
                   print('gambled during win condition')
                   probs = int(gambleProb)
                   if probs == 65:
                       probability = SixtyGamble
                       print('65% gamble')
                   if probs == 35:
                       probability = ThirtyGamble
                       print('35% gamble')
                   if probs == 50:
                       probability = FiftyGamble
                       print('50% gamble')
                   result = random.choice(probability)
                   print('gamble result:')
                   print(result)           
                   if result == 1: #win
                       earnings = earnings + chosenMoney
                       print('won money earnings:')
                       print(earnings)
                #       if result == 0: #lost
                #           earnings += 0
                    
                    
               if choice.keys == '2' and WinLossCode == 0: 
                   print('gambled during lose condition')
                      #gamProbability(gamProb)
                   probs = int(gambleProb)
                   if probs == 65:
                       probability = SixtyGamble
                       print('65% gamble')
                   if probs == 35:
                       probability = ThirtyGamble
                       print('35% gamble')
                   if probs == 50:
                       probability = FiftyGamble
                       print('50% gamble')
                   result = random.choice(probability)
                   print('gamble result:')
                   print(result)           
                   if result == 1: #lose
                       earnings = earnings - chosenMoney
                       print('Lost Money earnings:')
                       print(earnings)
                 #      if result == 0: #win
                 #          earnings += 0
                            
               if choice.keys == '1' and WinLossCode == 1: 
                   print('did not gamble during win condition')
                   earnings = earnings + chosenMoney
                   print('Won sure money earnings:')
                   print(earnings)
               if choice.keys == '1' and WinLossCode == 0: 
                   print('did not gamble for loss condition')
                   earnings = earnings - chosenMoney
                   print('Lost sure Money earnings:')
                   print(earnings)
            earningsStr= str(earnings)
            earningsText.setText(earningsStr)
        GambleAmt.setColor('white')
        SureAmt.setColor('white')
        
        if (blank.status==FINISHED):
            GambleAmt.setAutoDraw(False)
            SureAmt.setAutoDraw(False)
            SureProb.setAutoDraw(False)
            GambleProb.setAutoDraw(False)
            Line.setAutoDraw(False)
            moneyBank.setAutoDraw(False)
        PracticeLoop.addData('blank.started', blank.tStartRefresh)
        PracticeLoop.addData('blank.stopped', blank.tStopRefresh)
        PracticeLoop.addData('moneyBank.started', moneyBank.tStartRefresh)
        PracticeLoop.addData('moneyBank.stopped', moneyBank.tStopRefresh)
        PracticeLoop.addData('earningsText.started', earningsText.tStartRefresh)
        PracticeLoop.addData('earningsText.stopped', earningsText.tStopRefresh)
        # the Routine "Practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'PracticeLoop'
    
    
    # ------Prepare to start Routine "code_5"-------
    # update component parameters for each repeat
    earning = 0
    earnings = 0
    # keep track of which components have finished
    code_5Components = []
    for thisComponent in code_5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    code_5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "code_5"-------
    while continueRoutine:
        # get current time
        t = code_5Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=code_5Clock)
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
        for thisComponent in code_5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "code_5"-------
    for thisComponent in code_5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    earning = 0
    earnings = 0
    # the Routine "code_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'reset'


# ------Prepare to start Routine "BeginInst"-------
# update component parameters for each repeat
earning = 0
earnings = 0
key_resp.keys = []
key_resp.rt = []
# keep track of which components have finished
BeginInstComponents = [text_2, key_resp]
for thisComponent in BeginInstComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BeginInstClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "BeginInst"-------
while continueRoutine:
    # get current time
    t = BeginInstClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BeginInstClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp.keys = theseKeys.name  # just the last key pressed
            key_resp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BeginInstComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "BeginInst"-------
for thisComponent in BeginInstComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
earnings = 0
earning = 0
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "BeginInst" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
mainLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PracticeSlotMach.csv'),
    seed=None, name='mainLoop')
thisExp.addLoop(mainLoop)  # add the loop to the experiment
thisMainLoop = mainLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMainLoop.rgb)
if thisMainLoop != None:
    for paramName in thisMainLoop:
        exec('{} = thisMainLoop[paramName]'.format(paramName))

for thisMainLoop in mainLoop:
    currentLoop = mainLoop
    # abbreviate parameter names if possible (e.g. rgb = thisMainLoop.rgb)
    if thisMainLoop != None:
        for paramName in thisMainLoop:
            exec('{} = thisMainLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "isi"-------
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    isi2.setText('+')
    # keep track of which components have finished
    isiComponents = [isi2]
    for thisComponent in isiComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    isiClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "isi"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = isiClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=isiClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *isi2* updates
        if isi2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            isi2.frameNStart = frameN  # exact frame index
            isi2.tStart = t  # local t and not account for scr refresh
            isi2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(isi2, 'tStartRefresh')  # time at next scr refresh
            isi2.setAutoDraw(True)
        if isi2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > isi2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                isi2.tStop = t  # not accounting for scr refresh
                isi2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(isi2, 'tStopRefresh')  # time at next scr refresh
                isi2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in isiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "isi"-------
    for thisComponent in isiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    mainLoop.addData('isi2.started', isi2.tStartRefresh)
    mainLoop.addData('isi2.stopped', isi2.tStopRefresh)
    
    # ------Prepare to start Routine "Cue"-------
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    cue.setText(CueType)
    # keep track of which components have finished
    CueComponents = [cue]
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
        
        # *cue* updates
        if cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cue.frameNStart = frameN  # exact frame index
            cue.tStart = t  # local t and not account for scr refresh
            cue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue, 'tStartRefresh')  # time at next scr refresh
            cue.setAutoDraw(True)
        if cue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                cue.tStop = t  # not accounting for scr refresh
                cue.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue, 'tStopRefresh')  # time at next scr refresh
                cue.setAutoDraw(False)
        
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
    mainLoop.addData('cue.started', cue.tStartRefresh)
    mainLoop.addData('cue.stopped', cue.tStopRefresh)
    earning = 0
    earnings = 0
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('SlotMachine.csv', selection=Rows),
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
        
        # ------Prepare to start Routine "isi"-------
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        isi2.setText('+')
        # keep track of which components have finished
        isiComponents = [isi2]
        for thisComponent in isiComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        isiClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "isi"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = isiClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=isiClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *isi2* updates
            if isi2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                isi2.frameNStart = frameN  # exact frame index
                isi2.tStart = t  # local t and not account for scr refresh
                isi2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(isi2, 'tStartRefresh')  # time at next scr refresh
                isi2.setAutoDraw(True)
            if isi2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > isi2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    isi2.tStop = t  # not accounting for scr refresh
                    isi2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(isi2, 'tStopRefresh')  # time at next scr refresh
                    isi2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in isiComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "isi"-------
        for thisComponent in isiComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('isi2.started', isi2.tStartRefresh)
        trials.addData('isi2.stopped', isi2.tStopRefresh)
        
        # ------Prepare to start Routine "Practice"-------
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        Line.setSize((3, 0.5))
        Line.setFillColor([-1.000,-1.000,-1.000])
        Line.setLineColor([-1.000,-1.000,-1.000])
        Line.setLineWidth(7)
        choice.keys = []
        choice.rt = []
        GambleAmt.setColor('white', colorSpace='rgb')
        GambleAmt.setPos((-0.41, -0.1))
        GambleAmt.setText('')
        GambleAmt.setFont('Arial')
        GambleAmt.setHeight(0.11)
        SureAmt.setColor('white', colorSpace='rgb')
        SureAmt.setPos((0.41, -0.1))
        SureAmt.setText('')
        SureAmt.setFont('Arial')
        SureAmt.setHeight(0.11)
        GambleProb.setColor('white', colorSpace='rgb')
        GambleProb.setPos((-0.41, 0.3))
        GambleProb.setText('')
        GambleProb.setFont('Arial')
        GambleProb.setHeight(0.13)
        SureProb.setColor('white', colorSpace='rgb')
        SureProb.setPos((0.41, 0.3))
        SureProb.setText('')
        SureProb.setFont('Arial')
        SureProb.setHeight(0.13)
        
        leftVarText=[]
        leftVarMoney = []
        rightVarText = []
        rightVarMoney = []
        result = []
        
        if subID%2 == 1 :
            leftVarText = (gambleWinLoss)
            leftVarMoney = (gamble)
            rightVarText = (sureWinLoss)
            rightVarMoney = (sure)
        if subID%2 == 0:
            rightVarText= (gambleWinLoss)
            rightVarMoney= (gamble)
            leftVarText= (sureWinLoss)
            leftVarMoney= (sure)
        
        GambleAmt.setText(leftVarMoney)
        SureAmt.setText(rightVarMoney)
        GambleProb.setText(leftVarText)
        SureProb.setText(rightVarText)
        
        leftMoney = float(leftVarMoney[1:])
        
        rightMoney = float(rightVarMoney[1:])
        
        WinLossType = int(WinLossCode)
        
        
        blank.setText('')
        earningsText.setText(earningsStr)
        # keep track of which components have finished
        PracticeComponents = [Line, choice, GambleAmt, SureAmt, GambleProb, SureProb, blank, moneyBank, earningsText]
        for thisComponent in PracticeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "Practice"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = PracticeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PracticeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Line* updates
            if Line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Line.frameNStart = frameN  # exact frame index
                Line.tStart = t  # local t and not account for scr refresh
                Line.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Line, 'tStartRefresh')  # time at next scr refresh
                Line.setAutoDraw(True)
            if Line.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Line.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    Line.tStop = t  # not accounting for scr refresh
                    Line.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Line, 'tStopRefresh')  # time at next scr refresh
                    Line.setAutoDraw(False)
            
            # *choice* updates
            waitOnFlip = False
            if choice.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                choice.frameNStart = frameN  # exact frame index
                choice.tStart = t  # local t and not account for scr refresh
                choice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(choice, 'tStartRefresh')  # time at next scr refresh
                choice.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(choice.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(choice.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if choice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > choice.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    choice.tStop = t  # not accounting for scr refresh
                    choice.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(choice, 'tStopRefresh')  # time at next scr refresh
                    choice.status = FINISHED
            if choice.status == STARTED and not waitOnFlip:
                theseKeys = choice.getKeys(keyList=['1', '2'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    choice.keys = theseKeys.name  # just the last key pressed
                    choice.rt = theseKeys.rt
            
            # *GambleAmt* updates
            if GambleAmt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                GambleAmt.frameNStart = frameN  # exact frame index
                GambleAmt.tStart = t  # local t and not account for scr refresh
                GambleAmt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(GambleAmt, 'tStartRefresh')  # time at next scr refresh
                GambleAmt.setAutoDraw(True)
            if GambleAmt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > GambleAmt.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    GambleAmt.tStop = t  # not accounting for scr refresh
                    GambleAmt.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(GambleAmt, 'tStopRefresh')  # time at next scr refresh
                    GambleAmt.setAutoDraw(False)
            
            # *SureAmt* updates
            if SureAmt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                SureAmt.frameNStart = frameN  # exact frame index
                SureAmt.tStart = t  # local t and not account for scr refresh
                SureAmt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SureAmt, 'tStartRefresh')  # time at next scr refresh
                SureAmt.setAutoDraw(True)
            if SureAmt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > SureAmt.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    SureAmt.tStop = t  # not accounting for scr refresh
                    SureAmt.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(SureAmt, 'tStopRefresh')  # time at next scr refresh
                    SureAmt.setAutoDraw(False)
            
            # *GambleProb* updates
            if GambleProb.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                GambleProb.frameNStart = frameN  # exact frame index
                GambleProb.tStart = t  # local t and not account for scr refresh
                GambleProb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(GambleProb, 'tStartRefresh')  # time at next scr refresh
                GambleProb.setAutoDraw(True)
            if GambleProb.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > GambleProb.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    GambleProb.tStop = t  # not accounting for scr refresh
                    GambleProb.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(GambleProb, 'tStopRefresh')  # time at next scr refresh
                    GambleProb.setAutoDraw(False)
            
            # *SureProb* updates
            if SureProb.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                SureProb.frameNStart = frameN  # exact frame index
                SureProb.tStart = t  # local t and not account for scr refresh
                SureProb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SureProb, 'tStartRefresh')  # time at next scr refresh
                SureProb.setAutoDraw(True)
            if SureProb.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > SureProb.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    SureProb.tStop = t  # not accounting for scr refresh
                    SureProb.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(SureProb, 'tStopRefresh')  # time at next scr refresh
                    SureProb.setAutoDraw(False)
            
            if choice.keys == '1':
                GambleAmt.setColor('green')
                chosenMoney = leftMoney
            if choice.keys == '2':
                SureAmt.setColor('green')
                chosenMoney = rightMoney
                
            if (choice.keys == '1' or choice.keys == '2') and blank.status == NOT_STARTED:
                blank.tStart = t
                blank.frameNStart = frameN
                blank.setAutoDraw(True)
            #gamProbability(gambleProb)
            #gambleFunc(gambleProb)
            #earningsFunct(gambleProb, chosenMoney, WinLossCode, earnings)
            #print(earnings)
            
            
            
            #earningsText.setText(earningsStr)
            
            
            # *blank* updates
            if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
            
            # *moneyBank* updates
            if moneyBank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                moneyBank.frameNStart = frameN  # exact frame index
                moneyBank.tStart = t  # local t and not account for scr refresh
                moneyBank.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(moneyBank, 'tStartRefresh')  # time at next scr refresh
                moneyBank.setAutoDraw(True)
            if moneyBank.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > moneyBank.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    moneyBank.tStop = t  # not accounting for scr refresh
                    moneyBank.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(moneyBank, 'tStopRefresh')  # time at next scr refresh
                    moneyBank.setAutoDraw(False)
            
            # *earningsText* updates
            if earningsText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                earningsText.frameNStart = frameN  # exact frame index
                earningsText.tStart = t  # local t and not account for scr refresh
                earningsText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(earningsText, 'tStartRefresh')  # time at next scr refresh
                earningsText.setAutoDraw(True)
            if earningsText.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > earningsText.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    earningsText.tStop = t  # not accounting for scr refresh
                    earningsText.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(earningsText, 'tStopRefresh')  # time at next scr refresh
                    earningsText.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Practice"-------
        for thisComponent in PracticeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('Line.started', Line.tStartRefresh)
        trials.addData('Line.stopped', Line.tStopRefresh)
        # check responses
        if choice.keys in ['', [], None]:  # No response was made
            choice.keys = None
        trials.addData('choice.keys',choice.keys)
        if choice.keys != None:  # we had a response
            trials.addData('choice.rt', choice.rt)
        trials.addData('choice.started', choice.tStartRefresh)
        trials.addData('choice.stopped', choice.tStopRefresh)
        trials.addData('GambleAmt.started', GambleAmt.tStartRefresh)
        trials.addData('GambleAmt.stopped', GambleAmt.tStopRefresh)
        trials.addData('SureAmt.started', SureAmt.tStartRefresh)
        trials.addData('SureAmt.stopped', SureAmt.tStopRefresh)
        trials.addData('GambleProb.started', GambleProb.tStartRefresh)
        trials.addData('GambleProb.stopped', GambleProb.tStopRefresh)
        trials.addData('SureProb.started', SureProb.tStartRefresh)
        trials.addData('SureProb.stopped', SureProb.tStopRefresh)
        
        if choice.keys == '1':
            chosenMoney = leftMoney
        if choice.keys == '2':
            chosenMoney = rightMoney
        if choice.keys != None:
            if subID%2==1:   #gambles are on left side of screen
               if choice.keys == '1' and WinLossCode== 1 :  
                   print('gambled during win condition')
                   probs = int(gambleProb)
                   if probs == 65:
                       probability = SixtyGamble
                       print('65% gamble')
                   if probs == 35:
                       probability = ThirtyGamble
                       print('35% gamble')
                   if probs == 50:
                       probability = FiftyGamble
                       print('50% gamble')
                   result = random.choice(probability)
                   print('gamble result:')
                   print(result)
                   if result == 1:   #win
                       earnings = earnings + chosenMoney
                       print('Won money earnings:')
                       print(earnings)
                   #    if result == 0: #lose
                    #       earnings += 0
               
               if choice.keys == '1' and WinLossCode==0:  
                   print('gambled during lose condition')
                  #gamProbability(gamProb)
                   probs = int(gambleProb)
                   if probs == 65:
                       probability = SixtyGamble
                       print('65% gamble')
                   if probs == 35:
                       probability = ThirtyGamble
                       print('35% gamble')
                   if probs == 50:
                       probability = FiftyGamble
                       print('50% gamble')
                   result = random.choice(probability)
                   print('gamble result:')
                   print(result)           
                   if result == 1: #lose
                      earnings = earnings - chosenMoney
                      print('Lost Money earnings:')
                      print(earnings)
                 #      if result == 0: #win
                 #          earnings += 0
                            
               if choice.keys == '2'and WinLossCode ==1:  
                   print('did not gamble for win condition')
                   earnings = earnings + chosenMoney
                   print('Won sure money earnings:')
                   print(earnings)       
               if choice.keys == '2' and WinLossCode == 0: #did not gamble for lose condition
                   earnings = earnings - chosenMoney
                   print('Lost sure Money earnings:')
                   print(earnings)
        
        
            if subID%2==0:  #gambles are on right side of screen
               if choice.keys == '2' and WinLossCode == 1: 
                   print('gambled during win condition')
                   probs = int(gambleProb)
                   if probs == 65:
                       probability = SixtyGamble
                       print('65% gamble')
                   if probs == 35:
                       probability = ThirtyGamble
                       print('35% gamble')
                   if probs == 50:
                       probability = FiftyGamble
                       print('50% gamble')
                   result = random.choice(probability)
                   print('gamble result:')
                   print(result)           
                   if result == 1: #win
                       earnings = earnings + chosenMoney
                       print('won money earnings:')
                       print(earnings)
                #       if result == 0: #lost
                #           earnings += 0
                    
                    
               if choice.keys == '2' and WinLossCode == 0: 
                   print('gambled during lose condition')
                      #gamProbability(gamProb)
                   probs = int(gambleProb)
                   if probs == 65:
                       probability = SixtyGamble
                       print('65% gamble')
                   if probs == 35:
                       probability = ThirtyGamble
                       print('35% gamble')
                   if probs == 50:
                       probability = FiftyGamble
                       print('50% gamble')
                   result = random.choice(probability)
                   print('gamble result:')
                   print(result)           
                   if result == 1: #lose
                       earnings = earnings - chosenMoney
                       print('Lost Money earnings:')
                       print(earnings)
                 #      if result == 0: #win
                 #          earnings += 0
                            
               if choice.keys == '1' and WinLossCode == 1: 
                   print('did not gamble during win condition')
                   earnings = earnings + chosenMoney
                   print('Won sure money earnings:')
                   print(earnings)
               if choice.keys == '1' and WinLossCode == 0: 
                   print('did not gamble for loss condition')
                   earnings = earnings - chosenMoney
                   print('Lost sure Money earnings:')
                   print(earnings)
            earningsStr= str(earnings)
            earningsText.setText(earningsStr)
        GambleAmt.setColor('white')
        SureAmt.setColor('white')
        
        if (blank.status==FINISHED):
            GambleAmt.setAutoDraw(False)
            SureAmt.setAutoDraw(False)
            SureProb.setAutoDraw(False)
            GambleProb.setAutoDraw(False)
            Line.setAutoDraw(False)
            moneyBank.setAutoDraw(False)
        trials.addData('blank.started', blank.tStartRefresh)
        trials.addData('blank.stopped', blank.tStopRefresh)
        trials.addData('moneyBank.started', moneyBank.tStartRefresh)
        trials.addData('moneyBank.stopped', moneyBank.tStopRefresh)
        trials.addData('earningsText.started', earningsText.tStartRefresh)
        trials.addData('earningsText.stopped', earningsText.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'mainLoop'


# ------Prepare to start Routine "ThankYou"-------
# update component parameters for each repeat
# keep track of which components have finished
ThankYouComponents = [text_3]
for thisComponent in ThankYouComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ThankYouClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "ThankYou"-------
while continueRoutine:
    # get current time
    t = ThankYouClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ThankYouClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ThankYouComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ThankYou"-------
for thisComponent in ThankYouComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# the Routine "ThankYou" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
